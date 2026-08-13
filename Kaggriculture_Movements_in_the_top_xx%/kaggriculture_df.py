


import json
import pandas as pd



class Kaggriculture_df:
    def __init__(self, json_file, player_num):
        """
        <in>:
        json_file,
        player_num,

        <out>:
        df,
        from kaggriculture_df import Kaggriculture_df

        df = (Kaggriculture_df("/content/90295581.json", 0)).df
        df2 = (Kaggriculture_df("/content/90295581.json", 1)).df

        df.to_csv("test0.csv", index=False, encoding="utf-8")
        df2.to_csv("test1.csv", index=False, encoding="utf-8")

        """

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        summary = []

        for i, step_list in enumerate(data["steps"]):
            p = step_list[player_num]["observation"]

            hands_n = len(step_list[player_num]["observation"]["farms"][player_num]["hands"])
            hands_x_y = step_list[player_num]["observation"]["farms"][player_num]["hands"]

            hands_action = step_list[player_num]["action"]["hands"]

            hands_list = []
            hands_action_list = []

            for j in range(20):
                if j < hands_n:
                    hands_list.append(hands_x_y[j])
                    if j < len(hands_action):
                        hands_action_list.append(hands_action[j])
                    else:
                        hands_action_list.append(["PASS"])
                else:
                    hands_list.append([None, None])
                    hands_action_list.append([None])

            turn_data = {

                    "step": i,
                    "day": p.get("day"),
                    "money": p["farms"][player_num]["money"],  # プレイヤー0の所持金
                    "tiles": p["farms"][player_num]["tiles"],  # 10x10のマス目の状態
                    "farmer_x_y": p["farms"][player_num]["farmer"], #自分の座標
                    "hands_n": len(p['farms'][player_num]["hands"]), #労働者の人数
                    "hires_today": p["farms"][player_num]["hires_today"],#本日採用した人数
                    "unlocked_quadrants": p["farms"][player_num]["unlocked_quadrants"],#アンロックした土地サブセット
                    "private_shed": p["private"]["shed"],#小屋の収穫物在庫
                    "private_seeds": p["private"]["seeds"],#所持している種の数
                    "market_inv": p["market"]["inventory"],#市場の在庫数
                    "market_prices": p["market"]["prices"],#現在の価格


                    "farmer_action": step_list[player_num]["action"]["farmer"],#メイン農家の行動
                    "hands_action": step_list[player_num]["action"]["hands"],#労働者の行動
                    "market_action": step_list[player_num]["action"]["market"],#市場での売買・雇用アクション


                    "hands_list_1": hands_list[0],#労働者1座標
                    "hands_list_2": hands_list[1],#労働者2座標
                    "hands_list_3": hands_list[2],#労働者3座標
                    "hands_list_4": hands_list[3],#労働者4座標
                    "hands_list_5": hands_list[4],#労働者5座標
                    "hands_list_6": hands_list[5],#労働者6座標
                    "hands_list_7": hands_list[6],#労働者7座標
                    "hands_list_8": hands_list[7],#労働者8座標
                    "hands_list_9": hands_list[8],#労働者9座標
                    "hands_list_10": hands_list[9],#労働者10座標
                    "hands_list_11": hands_list[10],#労働者11座標
                    "hands_list_12": hands_list[11],#労働者12座標
                    "hands_list_13": hands_list[12],#労働者13座標
                    "hands_list_14": hands_list[13],#労働者14座標
                    "hands_list_15": hands_list[14],#労働者15座標
                    "hands_list_16": hands_list[15],#労働者16座標
                    "hands_list_17": hands_list[16],#労働者17座標
                    "hands_list_18": hands_list[17],#労働者18座標
                    "hands_list_19": hands_list[18],#労働者19座標
                    "hands_list_20": hands_list[19],#労働者20座標


                    "hands_action_list_1": hands_action_list[0],#労働者1の行動
                    "hands_action_list_2": hands_action_list[1],#労働者2の行動
                    "hands_action_list_3": hands_action_list[2],#労働者3の行動
                    "hands_action_list_4": hands_action_list[3],#労働者4の行動
                    "hands_action_list_5": hands_action_list[4],#労働者5の行動
                    "hands_action_list_6": hands_action_list[5],#労働者6の行動
                    "hands_action_list_7": hands_action_list[6],#労働者7の行動
                    "hands_action_list_8": hands_action_list[7],#労働者8の行動
                    "hands_action_list_9": hands_action_list[8],#労働者9の行動
                    "hands_action_list_10": hands_action_list[9],#労働者10の行動
                    "hands_action_list_11": hands_action_list[10],#労働者11の行動
                    "hands_action_list_12": hands_action_list[11],#労働者12の行動
                    "hands_action_list_13": hands_action_list[12],#労働者13の行動
                    "hands_action_list_14": hands_action_list[13],#労働者14の行動
                    "hands_action_list_15": hands_action_list[14],#労働者15の行動
                    "hands_action_list_16": hands_action_list[15],#労働者16の行動
                    "hands_action_list_17": hands_action_list[16],#労働者17の行動
                    "hands_action_list_18": hands_action_list[17],#労働者18の行動
                    "hands_action_list_19": hands_action_list[18],#労働者19の行動
                    "hands_action_list_20": hands_action_list[19],#労働者20の行動



            }
            summary.append(turn_data)


        self.df = pd.DataFrame(summary)