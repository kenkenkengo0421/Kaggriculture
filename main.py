
import random


def get_market_price(obs, product):
    """現在価格を取得する。"""
    return obs["market"]["prices"][product]


def score(input):
    """max_depth=3 のDecisionTreeモデル。"""

    if input[3] <= 10096.5:
        if input[0] <= 257.5:
            if input[2] <= 265.0:
                var0 = 262.30210213139543
            else:
                var0 = 269.14311998948614
        else:
            if input[2] <= 180.0:
                var0 = 169.52286374133948
            else:
                var0 = 192.71375464684016
    else:
        if input[0] <= 497.5:
            if input[3] <= 10127.5:
                var0 = 95.84500378501136
            else:
                var0 = 82.26066931619805
        else:
            if input[3] <= 10154.5:
                var0 = 19.437829958238122
            else:
                var0 = 6.73007806147341

    return var0


def should_sell_melon(
    melon_price,
    melon_stock,
    melon_in_shed,
    day,
    step,
):
    """MELONをSELLするかHOLDするか判断する。"""

    # 終盤は価格に関係なく売却
    if step >= 710:
        return True

    # 12ターン以内の最高価格を予測
    pred_price = score([
        step,
        melon_in_shed,
        melon_price,
        melon_stock,
        0,
        0,
        0,
    ])

    # 現在価格の方が予測最高価格以上なら売却
    if melon_price >= pred_price:
        return True

    return False


def get_harvest_age(crop_name):
    """現在の戦略で使う収穫開始日を返す。"""
    if crop_name == "MELON":
        return 10
    return 2


def get_tile_action(tile, day):
    """足元のタイルで今すぐ行う作業を返す。"""
    if not isinstance(tile, dict):
        return None

    if tile.get("kind") == "WEED":
        return ["DIG"]

    if tile.get("animal"):
        if not tile.get("fed_today", False):
            return ["FEED"]

        if not tile.get("cared_today", False):
            return ["CARE"]

        if tile.get("yield_units", 0) > 0:
            return ["HARVEST"]

        if tile.get("fertilizer_available", 0) > 0:
            return ["COLLECT_FERTILIZER"]

        return None

    if tile.get("kind") != "PLANT":
        return None

    crop_name = tile.get("crop", "WHEAT")
    crop_age = day - tile.get("planted_day", day)
    harvest_age = get_harvest_age(crop_name)

    if not tile.get("watered_today", True):
        return ["WATER"]

    if crop_age >= harvest_age:
        return ["HARVEST"]

    return None


def step_toward(fx, fy, tx, ty, tiles):
    """
    目的地に近づく方向へ1マス移動する。
    目的地へ直接進めない場合は、移動可能な方向を選ぶ。
    """
    max_y = len(tiles) - 1
    max_x = len(tiles[0]) - 1

    candidates = []

    if fx < tx and fx < max_x and tiles[fy][fx + 1] != "LOCKED":
        candidates.append("EAST")
    elif fx > tx and fx > 0 and tiles[fy][fx - 1] != "LOCKED":
        candidates.append("WEST")

    if fy < ty and fy < max_y and tiles[fy + 1][fx] != "LOCKED":
        candidates.append("SOUTH")
    elif fy > ty and fy > 0 and tiles[fy - 1][fx] != "LOCKED":
        candidates.append("NORTH")

    if candidates:
        return random.choice(candidates)

    valid_dirs = []

    if fy > 0 and tiles[fy - 1][fx] != "LOCKED":
        valid_dirs.append("NORTH")

    if fy < max_y and tiles[fy + 1][fx] != "LOCKED":
        valid_dirs.append("SOUTH")

    if fx < max_x and tiles[fy][fx + 1] != "LOCKED":
        valid_dirs.append("EAST")

    if fx > 0 and tiles[fy][fx - 1] != "LOCKED":
        valid_dirs.append("WEST")

    if valid_dirs:
        return random.choice(valid_dirs)

    return "PASS"

def find_empty_pasture(
    tiles,
    fx,
    fy,
):
    """現在位置から最も近い空のpastureを返す"""
    best_target = None
    best_distance = 9999

    for y in range(len(tiles)):
        for x in range(len(tiles[0])):

            tile = tiles[y][x]

            if (
                isinstance(tile, dict)
                and tile.get("kind") == "PASTURE"
                and not tile.get("animal")
            ):
                distance = (abs(x - fx) + abs(y - fy))

                if distance < best_distance:
                    best_distance = distance
                    best_target = (x, y)

    return best_target

def find_fertilize_target(
    tiles,
    fx,
    fy,
    day,
):
    """現在位置から最も近い肥料対象の植物を返す"""

    best_target = None
    best_distance = 9999

    for y in range(len(tiles)):
        for x in range(len(tiles[0])):

            tile = tiles[y][x]

            if(
                isinstance(tile, dict)
                and tile.get("kind") == "PLANT"
                and tile.get("fertilized_until_day", -1) < day
            ):
                distance = abs(x - fx) + abs(y - fy)

                if distance < best_distance:
                    best_distance = distance
                    best_target = (x, y)

    return best_target

def find_cow_target(tiles, fx, fy, day):
    """現在位置から最も近い作業対象のCOWを返す"""

    best_target = None
    best_distance = 9999

    for y in range(len(tiles)):
        for x in range(len(tiles[0])):

            tile = tiles[y][x]

            if(
                isinstance(tile, dict)
                and tile.get("animal") == "COW"
                and get_tile_action(tile, day)is not None
            ):
                distance = abs(x - fx) + abs(y - fy)

                if distance < best_distance:
                    best_distance = distance
                    best_target = (x, y)

    return best_target

def find_target_tile(
    tiles,
    fx,
    fy,
    has_seeds,
    day,
    excluded_coords=None,
):
    """
    現在位置から各作業候補を評価し、
    最もスコアの高いタイルの座標を返す。
    """
    if excluded_coords is None:
        excluded_coords = set()

    best_target = None
    best_score = -9999

    for y in range(len(tiles)):
        for x in range(len(tiles[0])):
            if (x, y) in excluded_coords:
                continue

            tile = tiles[y][x]
            if tile == "LOCKED":
                continue

            base_score = None

            # 雑草
            if isinstance(tile, dict) and tile.get("kind") == "WEED":
                if day >= 27:
                    continue

                base_score = 0

            #動物
            elif isinstance(tile, dict) and tile.get("animal"):
                if not tile.get("fed_today", False):
                    base_score = 100

                elif not tile.get("cared_today", False):
                    base_score = 75

                elif tile.get("yield_units", 0) > 0:
                    base_score = 60

                elif tile.get("fertilizer_available", 0) > 0:
                    base_score = 55


            # 植物
            elif isinstance(tile, dict) and tile.get("kind") == "PLANT":
                crop_name = tile.get("crop", "WHEAT")
                crop_age = day - tile.get("planted_day", day)
                harvest_age = get_harvest_age(crop_name)

                if crop_age >= harvest_age:
                    if crop_name == "MELON":
                        base_score = 250
                    else:
                        base_score = 25

                elif not tile.get("watered_today", True):
                    base_score = 50

            # 空き地
            elif tile is None and has_seeds:
                if day >= 27:
                    continue

                base_score = 50

            if base_score is None:
                continue

            movement_cost = abs(x - fx) + abs(y - fy)
            task_score = base_score - movement_cost

            if task_score > best_score:
                best_score = task_score
                best_target = (x, y)

    return best_target


def build_market_actions(
    me,
    seeds,
    shed,
    day,
    step,
    melon_price,
    melon_stock,
    cow_count,
):
    """現在の市場売買・雇用・土地購入ルールから注文一覧を作る。"""

    market = []

    money = me.get("money", 0)
    current_hands = me.get("hands", [])
    unlocked_quads = me.get(
        "unlocked_quadrants",
        ["NW"],
    )

    wheat_seeds = seeds.get("WHEAT", 0)
    melon_seeds = seeds.get("MELON", 0)

    wheat_in_shed = shed.get("WHEAT", 0)
    melon_in_shed = shed.get("MELON", 0)

    milk_in_shed = shed.get("MILK", 0)

    # 種を購入
    if day < 8 and money >= 500:
        if melon_seeds == 0:
            market.append(["BUY_SEED", "MELON", 10])

    if wheat_seeds == 0 and money >= 10:
        market.append(["BUY_SEED", "WHEAT", 6])


    # WHEAT売却
    if cow_count > 0:
        if wheat_in_shed < 2:
            market.append(["BUY_PRODUCT", "WHEAT", 2 - wheat_in_shed,])

        wheat_to_sell = max(wheat_in_shed - 2, 0,)

        if wheat_to_sell > 0:
            market.append(["SELL", "WHEAT", wheat_to_sell,])

    elif wheat_in_shed > 0:
        market.append(["SELL", "WHEAT", wheat_in_shed])

    #MILK売却
    if milk_in_shed > 0:
        market.append(["SELL", "MILK", milk_in_shed])



    # MELON売却
    if melon_in_shed > 0:
        if should_sell_melon(
            melon_price,
            melon_stock,
            melon_in_shed,
            day,
            step,
        ):
            market.append(["SELL", "MELON", melon_in_shed])

    # 雇用
    total_people = 1 + len(current_hands)

    if total_people < 7:
        market.append(["HIRE"])


    # 土地購入
    if len(unlocked_quads) < 3 and money >= 5000:
        market.insert(0,["BUY_LAND"],)


    #cowを飼う
    cow_in_shed = shed.get("COW", 0)

    if(
        len(unlocked_quads) >= 1
        and cow_count < 4
        and money >= 400
    ):
        market.append(["BUY_ANIMAL", "COW", 1])


    return market


def agent(obs, config):

    # 状態取得

    player = obs["player"]

    me = obs["farms"][player]
    private = obs["private"]

    tiles = me["tiles"]

    fx, fy = me["farmer"]
    farmer_tile = tiles[fy][fx]

    seeds = private.get("seeds", {})
    shed = private.get("shed", {})

    day = obs.get("day", 0)
    step = obs.get("step", 0)
    hour = obs.get("hour", 0)

    current_hands = me.get("hands", [])

    melon_price = get_market_price(obs, "MELON",)
    melon_stock = obs["market"]["inventory"]["MELON"]

    wheat_seeds = seeds.get("WHEAT", 0)
    melon_seeds = seeds.get("MELON", 0)

    remaining_wheat_seeds = wheat_seeds
    remaining_melon_seeds = melon_seeds

    melon_plant_allowed = day < 8

    wheat_in_shed = shed.get("WHEAT", 0)

    has_seeds = (wheat_seeds > 0 or melon_seeds > 0)

    inventories = private.get("inventories", [])

    famer_inventory = (
        inventories[0]
        if len(inventories) > 0
        else {}
    )
    farmer_cow = famer_inventory.get("COW", 0)

    farmer_wheat = famer_inventory.get("WHEAT", 0)
    farmer_fertilizer = famer_inventory.get("FERTILIZER", 0)

    farmer_milk = famer_inventory.get("MILK", 0)

    pasture_count = 0

    for row in tiles:
        for tile in row:
            if isinstance(tile, dict) and tile.get("kind") == "PASTURE":
                pasture_count += 1

    cow_count = 0

    for row in tiles:
        for tile in row:
            if (
                isinstance(tile, dict) and tile.get("animal") == "COW"
            ):
                cow_count += 1
    cow_count += shed.get("COW", 0)
    cow_count += farmer_cow



    # 市場

    market = build_market_actions(
        me,
        seeds,
        shed,
        day,
        step,
        melon_price,
        melon_stock,
        cow_count,
    )

    # メイン農家

    farmer_action = None
    cow_in_shed = shed.get("COW", 0)

    if step >= 710 and farmer_milk > 0:
        if (fx, fy) == (4, 4):
            farmer_action = ["PLACE", "MILK", farmer_milk,]

        else:
            move_dir = step_toward(fx, fy, 4, 4, tiles)
            farmer_action = [move_dir]



    elif farmer_cow > 0:
        if (
            isinstance(farmer_tile, dict)
            and farmer_tile.get("kind") == "PASTURE"
            and not farmer_tile.get("animal")
        ):
            farmer_action = ["PLACE","COW"]

        else:
            pasture_target = find_empty_pasture(tiles, fx, fy)

            if pasture_target is not None:
                move_dir = step_toward(
                    fx,
                    fy,
                    pasture_target[0],
                    pasture_target[1],
                    tiles,
                )

                farmer_action = [move_dir]

    elif(
        cow_in_shed > 0
        and find_empty_pasture(tiles, fx, fy) is not None
        and hour == 0
    ):
        farmer_action = ["PICKUP", "COW", 1,]

    elif(
        cow_count > 0
        and farmer_wheat == 0
        and wheat_in_shed > 0
        and hour == 0
    ):
        farmer_action = ["PICKUP", "WHEAT", 1,]


    elif farmer_tile is None:
        if cow_in_shed > 0 and pasture_count < 4:
            farmer_action = ["BUILD_PASTURE",]

        elif melon_plant_allowed and remaining_melon_seeds > 0:
            farmer_action = ["PLANT", "MELON",]
            remaining_melon_seeds -= 1

        elif remaining_wheat_seeds > 0:
            farmer_action = ["PLANT", "WHEAT",]
            remaining_wheat_seeds -= 1

    else:
        farmer_action = get_tile_action(farmer_tile, day,)

    # メイン農家の移動

    claimed_targets = set()

    if(farmer_action is None and farmer_fertilizer > 0):
        if(
            isinstance(farmer_tile, dict)
            and farmer_tile.get("kind") == "PLANT"
            and farmer_tile.get("fertilized_until_day", -1,) < day
        ):
            farmer_action = ["FERTILIZE"]

        else:
            fertilizer_target = find_fertilize_target(tiles, fx, fy, day)

            if fertilizer_target is not None:
                move_dir = step_toward(
                    fx, fy,
                    fertilizer_target[0],
                    fertilizer_target[1],
                    tiles,
                )

                farmer_action = [move_dir]

    if farmer_action is None:

        remaining_has_seeds = (
            remaining_wheat_seeds > 0 or (melon_plant_allowed and remaining_melon_seeds > 0)
        )

        target = find_target_tile(
            tiles,
            fx,
            fy,
            remaining_has_seeds,
            day,
            claimed_targets,
        )
        if target is not None:
            claimed_targets.add(target)
            move_dir = step_toward(
                fx,
                fy,
                target[0],
                target[1],
                tiles,
            )
            farmer_action = [move_dir]
        else:
            farmer_action = ["PASS"]
    else:
        claimed_targets.add(
            (fx, fy)
        )


    # 作業員

    hands_actions = []

    for hand_index, hand in enumerate(current_hands):
        hx, hy = hand

        hand_inventory = (
            inventories[hand_index + 1]
            if len(inventories) > hand_index + 1
            else {}
        )

        hand_wheat = hand_inventory.get("WHEAT", 0)

        hand_tile = tiles[hy][hx]

        if hand_index == 0:

            if(
                cow_count > 0
                and hand_wheat == 0
                and wheat_in_shed > 0
            ):
                if (hx, hy) == (4, 4):
                    hand_action = ["PICKUP", "WHEAT", 1,]

                else:
                    move_dir = step_toward(
                        hx,
                        hy,
                        4,
                        4,
                        tiles,
                    )
                    hand_action = [move_dir]

            elif(
                isinstance(hand_tile, dict)
                and hand_tile.get("animal") == "COW"
            ):
                hand_action = get_tile_action(
                    hand_tile,
                    day,
                )

                if hand_action is None:
                    cow_target = find_cow_target(
                        tiles,
                        hx,
                        hy,
                        day,
                    )

                    if cow_target is not None:
                        move_dir = step_toward(
                            hx,
                            hy,
                            cow_target[0],
                            cow_target[1],
                            tiles,
                        )
                        hand_action = [move_dir]

                    else:
                        hand_action = None


            else:
                cow_target = find_cow_target(
                    tiles,
                    hx,
                    hy,
                    day,
                )

                if cow_target is not None:
                    move_dir = step_toward(
                        hx,
                        hy,
                        cow_target[0],
                        cow_target[1],
                        tiles,
                    )
                    hand_action = [move_dir]

                else:
                    hand_action = None

            if hand_action is None:
                cow_coords = set()

            if hand_action is None:
                if hand_tile is None:
                    if melon_plant_allowed and remaining_melon_seeds > 0:
                        hand_action = ["PLANT", "MELON",]
                        remaining_melon_seeds -= 1

                    elif remaining_wheat_seeds > 0:
                        hand_action = ["PLANT", "WHEAT",]
                        remaining_wheat_seeds -= 1

                elif not(
                    isinstance(hand_tile, dict)
                    and hand_tile.get("animal")
                ):
                    hand_action = get_tile_action(hand_tile, day,)

            if hand_action is None:
                cow_coords = set()

                for y in range(len(tiles)):
                    for x in range(len(tiles[0])):
                        tile = tiles[y][x]

                        if(
                            isinstance(tile, dict)
                            and tile.get("animal") == "COW"
                        ):
                            cow_coords.add((x, y))

                remaining_has_seeds = (
                    remaining_wheat_seeds > 0
                    or (
                        melon_plant_allowed
                        and remaining_melon_seeds > 0
                    )
                )

                target = find_target_tile(
                    tiles,
                    hx,
                    hy,
                    remaining_has_seeds,
                    day,
                    claimed_targets | cow_coords,
                )

                if target is not None:
                    claimed_targets.add(target)

                    move_dir = step_toward(
                        hx,
                        hy,
                        target[0],
                        target[1],
                        tiles,
                    )

                    hand_action = [move_dir]

                else:
                    hand_action = ["PASS"]


        else:

            if hand_tile is None:
                if melon_plant_allowed and remaining_melon_seeds > 0:
                    hand_action = ["PLANT", "MELON",]
                    remaining_melon_seeds -= 1

                elif remaining_wheat_seeds > 0:
                    hand_action = ["PLANT", "WHEAT",]
                    remaining_wheat_seeds -= 1

                else:
                    hand_action = None

            elif(
                isinstance(hand_tile, dict)
                and hand_tile.get("animal")
            ):
                hand_action = None

            else:
                hand_action = get_tile_action(
                    hand_tile,
                    day,
                )

            if hand_action is None:
                cow_coords = set()

                for y in range(len(tiles)):
                    for x in range(len(tiles[0])):
                        tile = tiles[y][x]

                        if(
                            isinstance(tile, dict)
                            and tile.get("animal") == "COW"
                        ):
                            cow_coords.add((x, y))

                remaining_has_seeds = (
                    remaining_wheat_seeds > 0
                    or (
                        melon_plant_allowed
                        and remaining_melon_seeds > 0
                    )
                )

                target = find_target_tile(
                    tiles,
                    hx,
                    hy,
                    remaining_has_seeds,
                    day,
                    claimed_targets | cow_coords,
                )

                if target is not None:
                    claimed_targets.add(target)

                    move_dir = step_toward(
                        hx,
                        hy,
                        target[0],
                        target[1],
                        tiles,
                    )

                    hand_action = [move_dir]

                else:
                    hand_action = ["PASS"]


        if hand_action is not None:
            claimed_targets.add(
                (hx, hy)
            )

        hands_actions.append(
            hand_action
        )


    # 出力

    return {
        "farmer": farmer_action,
        "hands": hands_actions,
        "market": market,
    }
