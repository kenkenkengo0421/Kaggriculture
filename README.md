
## Kaggriculture

2人のプレイヤーが、変動する市場に農産物を販売することで収入を最大化するために競い合う農業シミュレーションゲーム。

## 概要

各プレイヤーは、空の農場と少額の収入（いわば種金）を持ってゲームを開始します。各ターンでは、ボード上を移動したり、種や家畜を購入したり、種を植えたり、植物に水をやったり、農産物や畜産物を収穫したり、市場でその農産物を売ったりといった行動をとることができます。ゲームは1シーズンを表す一定時間行われ、終了時に最も多くの資金を持っているプレイヤーが勝者となります。


## オブジェクトの種類

|Type|Yield Type|Seed Cost|Base Market Price|Time to First Yield|Time to Max Yield|Subsequent Yields|Max Yield|Action Cost|Max yield / tile / DAY|
|---|---|---|---|---|---|---|---|---|---|
|**Wheat**|One-time|10|25|2 days|4 days|none|6|1|1.5|
|**Carrot**|One-time|20|35|2 days|3 days|none|4|1|1.333|
|**Tomato**|Ongoing|50|60|8 days|NA|every day|4|1|4|
|**Strawberry**|Ongoing|100|120|10 days|NA|every other day|4|1|2|
|**Melon**|One-time|80|250|10 days|12 days|none|6|1|.5|
|**Goose/Egg**|Ongoing|300|50|4 days|NA|every day|4|1 + 1 (build coop)|2|
|**Cow/Milk**|Ongoing|400|160|8 days|NA|every two days|6|1 + 1 (build pasture)|1|
|**Sheep/Wool**|Ongoing|500|200|6 days|NA|every three days|6|1 + 1 (build pasture)|.67|
|**Fertilizer**|NA|100|X||X|X||1|

👇

| タイプ        | 収量タイプ | 種子のコスト | 基本市場価格 | 初回収穫までの時間 | 最大収量を得るまでの時間 | その後の収益 | 最大収量 | アクションコスト        | タイル1枚あたりの最大収穫量／日 |
| ---------- | ----- | ------ | ------ | --------- | ------------ | ------ | ---- | --------------- | ---------------- |
| **小麦**     | 一度    | 10     | 25     | 2日間       | 4日間          | なし     | 6    | 1               | 1.5              |
| **ニンジン**   | 一度    | 20     | 35     | 2日間       | 3日間          | なし     | 4    | 1               | 1.333            |
| **トマト**    | 継続中   | 50     | 60     | 8日間       | 該当なし         | 毎日     | 4    | 1               | 4                |
| **いちご**    | 継続中   | 100    | 120    | 10日間      | 該当なし         | 隔日     | 4    | 1               | 2                |
| **メロン**    | 一度    | 80     | 250    | 10日間      | 12日間         | なし     | 6    | 1               | 0.5              |
| **ガチョウの卵** | 継続中   | 300    | 50     | 4日間       | 該当なし         | 毎日     | 4    | 1 + 1 (協力プレイ構築) | 2                |
| **牛/牛乳**   | 継続中   | 400    | 160    | 8日間       | 該当なし         | 2日ごとに  | 6    | 1 + 1 (牧草地を作る)  | 1                |
| **羊毛**     | 継続中   | 500    | 200    | 6日間       | 該当なし         | 3日ごとに  | 6    | 1 + 1 (牧草地を作る)  | 0.67             |
| **肥料**     | 該当なし  | 100    | X      |           | X            | X      |      | 1               |                  |

すべての植物は毎日水やりをしなければなりません。2日間連続で水やりをしないと雑草になってしまいます。すべての動物は毎日小麦を与えなければなりません。2日間連続で餌を与えないと逃げ出してしまい、捕まえられなくなります。小麦は市場でも購入でき、現在の市場価格で購入できます。

## 行動

各ターン、プレイヤーは1つのアクションを実行できます。1日は24ターン、シーズンは30日間なので、合計720ターンとなります。

### 農家／農場労働者の行動

各農夫／農作業員は毎ターン行動を行うことができます。農夫／農作業員は同じマスを占有することができます。


#### 動き

- 北、南、東、西 — その方向に1マス移動します

#### 物置

物置からアイテムを1つ取り出し（直交隣接している必要がある）、インベントリに追加します。

- ピックアップ`<item>` `[n]`— 小屋から最大(デフォルトは 1)`n`個の`<item>`アイテムを、作業中の農夫/作業員のインベントリに移動します。小屋にあるアイテムはすべて有効です (動物、肥料、収穫物など)。種は別のスロットにあり、ピックアップされることはなく、`PLANT`直接消費されます。
- DROP — 小屋に直交する隣接位置で、現在作業中の農夫／作業員の現在のインベントリ全体を小屋に投棄します。オーバーフローしたアイテムは`shedCapacity`破棄されます。小屋に隣接していない場合は何もしません。

#### 植物

- 植える — 市場で購入した種を植える  
    - 種子はすべての農家/農場作業員に自動的に提供されます
    - 特定のターンに植えすぎようとすると、何も植えられません。
    - つまり、メロンの種が1つしかないのに、2つのユニットが「メロンを植える」コマンドを実行する場合などです。
- 水やり ― 植物に水をあげてください。これは1日に1回だけで十分で、同じ日に2回目以降の水やりは不要です。
- 収穫 — 植物から収穫物を集めます。植物が次の収穫を期待できない場合、マップから削除されます。収穫アクションごとに少なくとも1単位の作物が収穫でき、水やりや肥料の量によっては追加の収穫量が得られる可能性があります（計算式は作物の種類によって異なります。下記の収穫量に関する説明を参照してください）。収穫されたアイテムはインベントリに追加されます。
- 施肥 — 植物に肥料を与えることで、収穫量を増やすことができます（下記の収穫量を参照）。  
    - 今後3日間、1日あたりの収穫量ボーナスが2倍になります。このボーナスは、植物に水やりを行った日（基本的なニーズが優先される日）にのみ適用されます。

#### 動物

- 配置`<item>` `[n]`— アクティブな農夫/手持ちのアイテムをタイルまたは小屋にドロップします。  
    - **動物の配置**：対応する空いている建造物（`GOOSE`鶏小屋、牧草地など）の上に立つと、インベントリから動物1匹がそのタイルに配置されます。`SHEEP`引数は無視されます。 `COW``n`
    - **小屋ドロップ**：小屋に直交する位置に立つと、インベントリから最大`n`（デフォルトは1）個のアイテムが`<item>`小屋に移動します。上限はで`shedCapacity`、超過分はインベントリに残ります。
- 餌を与える — 小麦を使って動物に餌を与える（1日1回で十分です）
- 収穫 ― 動物が生産した卵、牛乳、羊毛を集める。
- 肥料収集 — 動物から肥料を1つ収集します。生き残った動物はそれぞれ、毎日終わりに肥料を1つ提供します。収集するとその日の在庫が消費され、次の在庫は次の日の終わりの更新後に利用可能になります。
- 世話 ― 動物の世話をする（1日1回、既に世話をしている場合は不要）。動物の世話については下記を参照してください

#### 動物の世話

CAREは、動物の次回の出産予定時に支払われる収益ボーナスを積み立てます。

- 一日の終わりに、動物に餌を与え、かつ世話をした場合、`pending_care_bonus`ポイントが2増加します。動物に餌を与えなかった日はボーナスポイントは加算されません（基本的なニーズが優先されるため）。
- 予定された生産日に動物に餌を与えた場合、積み立てられたボーナス全額がその生産の収穫量に加算され（基本値1に加えて）、積み立て額は0にリセットされます。
- 生産日に動物に餌を与えなかった場合、その日は収穫量はゼロとなり、バンクもリセットされます。
- `pending_care_bonus`は、動物ごとの`max_held`上限によって間接的に制限されます`yield_units`。

#### 地形

- BUILD_COOP - 空いているタイルに鶏小屋を追加します
- BUILD_PASTURE - 空いているタイルに牧草地を追加する
- 掘る — スペースを確保するために区画から植物を取り除くか、区画から雑草を取り除く（収穫物は得られません）か、ガチョウ小屋/牧草地を取り除きます。

#### 他の

- PASS — 何もすることがない場合はデフォルトで実行されます（オプション）

### 市場の動き

各ターンで最大（デフォルトは10件）の市場取引注文を送信できます`maxMarketOrdersPerTurn`。この制限を超えた注文は自動的に破棄されます。これは注文リストであり、両プレイヤーが注文を出している間は、市場注文は順番に（各プレイヤーから1件ずつ）同時に処理されます。

- BUY_SEED — マーケットから単一のアイテムをN個購入します。  
    - 小麦の種を購入する 1
- 動物を購入する -  
    - 動物を購入する ガチョウ 1
- BUY_PRODUCT  
    - BUY_PRODUCT 小麦 1
    - 肥料1を購入する
- 販売 — 単一商品をN個、市場に販売する。  
    - 小麦を売る 1
- 雇用 ― 農作業員を一日雇用します。同日に雇用する作業員が増えるごとに費用も増加します。
- 土地を購入する - 新たに5x5の区画の土地をアンロックして、そこに作物を植えることができます。価格は上昇します。  
    - 費用は1,000ドル、2,000ドル、4,000ドルです。

## 水やり／動物の餌

植物（および動物）は、最低でも2日に1回は水やりと餌やりが必要です。水やりは1日1回で十分で、それ以降は水やりは不要です。2日間連続で水やりをしなかった植物は、その日の終わりに雑草と化します。動物の場合は、逃げ出し（捕獲不能）します。

収穫期に一度だけ収穫する植物に水やりをすると、収穫量が増えることに注意してください。これは、継続的に収穫する植物や動物には当てはまりません。詳細は下記をご覧ください。

## 収穫量

植物の収穫量は、どれだけ丁寧に手入れされたかによって大きく左右される可能性がある。

- **単作作物**（小麦、ニンジン、メロン）：植物の`max_yield_day`最大収穫までの時間を切り上げた半分から始め、ボーナス期間中に水やりをすると、収穫可能な総収穫量が1日あたり1単位増加します。  
    - 肥料を与えた植物は、代わりに1日あたり2個追加します。
- **継続栽培作物**（トマト、イチゴ）：計画された生産は一定の間隔で行われます。基本収量は計画された生産ごとに1です。その日に植物に肥料を与え、水やりも行った場合、収量は2倍の2になります。
- 植物が最大寿命に達すると、その植物から得られる総収穫量は2ターンごとに1ずつ減少し、0になると雑草となる。
    - **一度限りの作物は、**収穫後1日で寿命が最大になります`max_yield_day`。
    - **進行中の作物は、**累積生産量が上限に達した翌日から腐敗し始めます`max_yield`（つまり、収穫されたかどうかに関わらず、予定された生産量が上限に達した時点で腐敗が始まります）。

## 地図上の特徴

各プレイヤーはそれぞれ決められた数のマス目からなる自分の農場を持っています。プレイヤーは他のプレイヤーの小屋の状態を見ることはできませんが、対戦相手の農場の状態を見ることはできます。

### 農地

- あなたの農場周辺の土地は、`boardSize`×`boardSize`印のグリッド（デフォルトは10×10）で、5×5の4つの区画に分割されています。最初は、あなたの農場は1つの区画（全体の25%）をカバーしています。追加料金を支払うことで、隣接する区画を購入し、最終的には全体の100%をカバーできるようになります。
- それぞれの植物や動物は、農場内の1マスを占める。
- プレイヤーはこれらのマス目を、作物と家畜に自由に割り当てることができます。種類ごとの制限はありません。
- 農場内の空いている区画には雑草が生える可能性があり、その土地を他の用途に使う前に雑草を取り除く必要があります。
- 農場内のマス目は、植物、鶏小屋／牧草地、雑草、または空き地のいずれかになります。

### 物置（在庫）

- 収穫済みだがまだ販売されていない品物、またはまだ植えられていない種子の在庫として機能する。


# Kaggriculture：入門編

このガイドでは、エージェントの構築、ローカル環境でのテスト、そしてKaggleのKaggricultureコンペティションへの提出の手順を説明します。

ゲームの完全なルール、作物/動物/ショップのテーブル、価格関数、およびターン処理順序については、[README.md を](https://www.kaggle.com/competitions/kaggriculture/README.md)参照してください。

## ゲーム概要

Kaggricultureは2人プレイの農業シミュレーションゲームです。各プレイヤーは自分の農場を経営し、種や家畜の購入、植え付け、水やり、収穫、動物の飼育、従業員の雇用、そして変動する市場での取引などを通じて、固定されたシーズン中に最も多くのコインを獲得することを目指して競い合います。

- **農場**— 各プレイヤーは、 4つの5×5の象限に分割された`boardSize`×`boardSize`グリッド（デフォルトは10×10）を持ちます。開始時には北西象限のみがロック解除されています。他の3つの象限（`NE`、、 ）は、それぞれ$1k / $2k / $4kで購入できます`SW`。`SE``BUY_LAND`
- **初期資金**—`startingMoney`デフォルト値は3000ドル
- **農民と農作業員**― プレイヤーごとにメインの農民が1人、加えて1日に最大N人の農作業員を雇えます。雇い費は、その日にすでに雇った人数で決まります。デフォルト値はで`farmHandCostMult * fib(n)`、毎日開始時にリセットされます。各ユニットは毎ターン独立して行動します。`n``farmHandCostMult = 1``1, 1, 2, 3, 5, 8, 13, 21, ...`
- **作物**— 小麦、ニンジン、トマト（継続中）、イチゴ（継続中）、メロン。それぞれに種子コスト、生育期間、収量曲線、基本販売価格が設定されています（[README.md](https://www.kaggle.com/competitions/kaggriculture/README.md)のオブジェクトタイプ表を参照）。
- **水やりボーナス**— 単発作物の場合、ボーナス期間（開始時刻`ceil(max_yield_day / 2)`）中に水やりをすると、収穫可能量が1日あたり1単位増加します。 は`FERTILIZE`、そのボーナスを3日間2倍にします。継続作物の場合、予定生産量はデフォルトで1ですが、その日に施肥と水やりの両方を行うと2倍の2になります。
- **動物**― ガチョウ（卵、鶏舎が必要）、牛（牛乳、牧草地が必要）、羊（羊毛、牧草地が必要）。毎日小麦を与える必要があります。`CARE`収穫ボーナスが蓄積され、次回の生産時に支払われます。`COLLECT_FERTILIZER`動物1頭あたり1日1個の肥料を集めます。
- **水やり／給餌**― 植物には毎日水やりをし、動物には毎日餌を与えなければなりません。2日連続で終業時の給餌を怠ると、植物は雑草化し、動物は逃げ出し（回復不能）ます。植え付け日は、水やりを怠った最初の日としてカウントされます。
- **衰退**― 植物が最大寿命を過ぎると（`max_yield_day`単発作物の場合はその1日後、継続作物の場合は累積生産上限の1日後）、`yield_units`2ターンごとに1ずつ減少し、0になるとタイルは雑草になる。
- **雑草**— ロック解除されていない空のタイルには`weedSpawnChance`、一日の終わりに雑草が生える確率が（デフォルトは0.005）あります。`DIG`
- **保管場所**— 種子以外のアイテムの所持上限は100個です。1日の終わりに上限を超えたアイテムは破棄されます。種子は専用のスロットに保管されます（上限なし、拾われることはなく`PICKUP`、`PLANT`直接消費されます）。
- **市場**— 種子、動物、`BUY_PRODUCT`注文の価格は固定されています。収穫された農産物の販売価格は、市場の在庫に応じて動的に変動します。価格は共有`base`の初期在庫で`I0`始まり、在庫が減少すると上昇し、在庫が増加すると下落します。これは、資源ごとの形状関数（`linear`、、、`sq`または）を使用して行われ、の両側で異なる場合があります。そのため、供給過剰は高級品（イチゴ、メロン、牛乳、羊毛）に大きな打撃を与え、価格を1ドルまで押し下げますが、必需品は過剰供給をより緩やかに吸収します（[README.md](https://www.kaggle.com/competitions/kaggriculture/README.md)の価格関数表を参照）。肥料は購入のみ可能で、販売はできません。各ターン、プレイヤーごとに最大（デフォルトは10）の注文が処理され、余剰分は黙って破棄されます。`sqrt``log``I0`[](https://www.kaggle.com/competitions/kaggriculture/README.md)`maxMarketOrdersPerTurn`
- **町**— 町の中心部は常に製品を要求します（肥料以外の製品を毎`townCenterSellInterval`ターン1個ずつ、デフォルトは12個、10日目以降は2倍、20日目以降は4倍に増加）。追加のショップは毎日アンロックされます`townShopUnlockInterval`（デフォルトは3日、残りのプールからランダムに選択）。アンロックされた各ショップは、毎ターン要求する製品を1個ずつ消費します`townShopSellInterval`（デフォルトは4日、単一製品のショップは2倍消費）。詳細は[README.mdの「町の建物」表を参照してください。](https://www.kaggle.com/competitions/kaggriculture/README.md)
- **シーズン期間**— 1日24ターン × 30日間 = デフォルトでは720ターン
- **勝利条件**：シーズン終了時点で銀行に最も多くのコインを保有している者。同点となる可能性あり。


## あなたのエージェント

エージェントとは、観測値を受け取り、アクション辞書を返す関数です。

**観測分野：**

- `player`— プレイヤーインデックス（0または1）
- `step`— 現在のターン（0から始まるインデックス。kaggle-environmentsフレームワークによって提供される）
- `day`— 現在のゲーム内日数（0から始まる）
- `hour`— 1日以内のターン (0から始まるインデックス、0～`turnsPerDay`-1)
- `farms`— プレイヤーごとに1つのエントリを含むリスト（公開；両方の農場が閲覧可能）。各エントリには以下が含まれます。
    - `money`— 現在の銀行残高
    - `tiles`— 2D配列インデックス付き`tiles[y][x]`。各タイルは、（空`None`のロック解除）、`"LOCKED"`（ロックされた象限）、植物辞書（、、、、、、）、`kind="PLANT"`雑草辞書（）、または動物構造辞書（または、オプションで、、、、、、、、）です`crop`。`planted_day``watered_today``consecutive_unwatered``yield_units``max_lifespan_step``fertilized_until_day``kind="WEED"``kind="COOP"``"PASTURE"``animal``placed_day``yield_units``fed_today``consecutive_unfed``cared_today``fertilizer_available``pending_care_bonus`
    - `farmer`—`[x, y]`主たる農家の位置（x = 列、y = 行）
    - `hands``[x, y]`—本日雇用される農場労働者向けの職種一覧
    - `unlocked_quadrants`— サブセット`["NW", "NE", "SW", "SE"]`
    - `hires_today`— 本日これまでに採用した人数（次回の採用コストに影響します）
- `private`— プレイヤーのみ表示。対戦相手のプライベート状態は非公開です。
    - `shed``{item: count}`収穫された農産物、家畜、肥料の保管用
    - `seeds`— `{crop: count}`; 種子は専用のスロットに生息し、直接消費されます`PLANT`
    - `inventories`— `[main_farmer_inv, hand1_inv, ...]`; 現場で持ち運ばれる単位当たりの在庫
- `market`— 共有:
    - `inventory`—`{product: int}`現在の市場供給量
    - `prices`—`{product: int}`現在の1戸当たりの販売価格（四捨五入、1階）
- `town`— 共有: `unlocked_shops`— 現在アクティブなショップ名のリスト

**アクション形式:**

```maxima
{
  "farmer": [op, ...args],          # one main-farmer op this turn
  "hands":  [[op, ...args], ...],   # one op per hired hand, in hands order
  "market": [[op, ...args], ...],   # ordered list of market orders, capped at maxMarketOrdersPerTurn
}
```

農家／手作業員：

- 動き：`"NORTH"`、`"SOUTH"`、`"EAST"`、`"WEST"`、`"PASS"`
- 小屋／インベントリ：（`"PICKUP" <item> [n]`小屋から）、`"PLACE" <item> [n]`（小屋の上に立っていると、対応する構造物の上に動物を配置します。小屋に隣接している場合は、アイテムを小屋に落とします）、`"DROP"`（小屋に隣接している場合は、インベントリ全体を小屋に投入します。オーバーフローは`shedCapacity`破棄されます）
- 植物: `"PLANT" <crop>`、`"WATER"`、`"HARVEST"`、`"FERTILIZE"`
- 動物: `"BUILD_COOP"`、`"BUILD_PASTURE"`、`"FEED"`、`"COLLECT_FERTILIZER"`、`"CARE"`
- 地形：（`"DIG"`現在のタイルから植物、雑草、鶏小屋、または牧草地を削除します）

マーケット操作: `["BUY_SEED", crop, n]`、、、、、。`["BUY_PRODUCT", item, n]`無効な操作`["BUY_ANIMAL", animal, n]`はサイレントな`["SELL", item, n]`ノーオペレーションです。`["HIRE"]``["BUY_LAND"]`

**例 — 小麦ループ：**

小麦（`first_yield_day = 2`、`max_yield_day = 4`）の場合、ボーナス灌水期間は2～4日目です。この期間中に種をまき、灌水し、2日目以降に収穫します。

```prolog
def agent(obs):
    player = obs["player"]
    me = obs["farms"][player]
    private = obs["private"]
    fx, fy = me["farmer"]
    tile = me["tiles"][fy][fx]

    market = []
    if private["seeds"].get("WHEAT", 0) == 0 and me["money"] >= 10:
        market.append(["BUY_SEED", "WHEAT", 1])
    # Sell any wheat sitting in the shed.
    wheat_in_shed = private["shed"].get("WHEAT", 0)
    if wheat_in_shed > 0:
        market.append(["SELL", "WHEAT", wheat_in_shed])

    if tile is None and private["seeds"].get("WHEAT", 0) > 0:
        return {"farmer": ["PLANT", "WHEAT"], "hands": [], "market": market}
    if isinstance(tile, dict) and tile.get("kind") == "PLANT":
        crop_age = obs["day"] - tile["planted_day"]
        if crop_age >= 2:  # WHEAT first_yield_day = 2; harvest as soon as possible
            return {"farmer": ["HARVEST"], "hands": [], "market": market}
        if not tile["watered_today"]:
            return {"farmer": ["WATER"], "hands": [], "market": market}

    return {"farmer": ["PASS"], "hands": [], "market": market}
```

より詳しい例（およびニンジン、トマト、イチゴ、メロンの作物ごとの収量/コストの詳細）については、[README.md](https://www.kaggle.com/competitions/kaggriculture/README.md)のオブジェクトタイプとクイックスタートのセクションを参照してください。

## ローカルでテストする

PyPIから環境をインストールします（Kaggricultureを含む最新リリースであればどれでも構いません）。

```cmake
pip install -U kaggle-environments
```

Pythonまたはノートブックからゲームを実行します。エージェント関数を直接渡すことも、`.py`ファイルへのパスを指定することもできます。

```routeros
from kaggle_environments import make

env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=True)
env.run([agent, "random"])  # or env.run(["main.py", "random"]) to load from a file

# View result
final = env.steps[-1]
for i, s in enumerate(final):
    print(f"Player {i}: reward={s.reward}, status={s.status}")

# Render in a notebook
env.render(mode="ipython", width=1200, height=800)

# Or dump a replay JSON for the visualizer / offline analysis
import json
with open("replay.json", "w") as f:
    json.dump(env.toJSON(), f)
```

組み込みエージェントは、`"pass"`、`"random"`、 および`"starter"`（決定論的なベースライン）という名前で利用できます。

## Kaggle CLI をセットアップする

CLIをインストールしてください。

```cmake
pip install kaggle
```

Kaggleアカウントが必要です。アカウントをお持ちでない場合は、[https://www.kaggle.comでサインアップしてください。その後、](https://www.kaggle.com/) [https://www.kaggle.com/settings/api](https://www.kaggle.com/settings/api)にアクセスし、 「API」セクションの**「新しいトークンを生成」**をクリックして、 API認証情報をダウンロードしてください。

**推奨：APIトークンファイル。**トークン文字列を次の場所に保存してください`~/.kaggle/access_token`：

```bash
mkdir -p ~/.kaggle
# Paste the token from the Kaggle settings UI into this file
nano ~/.kaggle/access_token
chmod 600 ~/.kaggle/access_token
```

代替認証方法：

- **OAuth（ブラウザフロー）：** `kaggle auth login`
- **環境変数:** `export KAGGLE_API_TOKEN=xxxxxxxxxxxxxx`

CLIが正しく接続されていることを確認してください。

```lsl
kaggle competitions list -s "kaggriculture"
```

## 競合他社を見つける

```ada
kaggle competitions list -s "kaggriculture"
kaggle competitions pages kaggriculture
kaggle competitions pages kaggriculture --content
```

## 競技規則に同意する

提出する前に、Kaggleウェブサイトのルールに同意する**必要があります。** **「コンペティションに参加する」**`https://www.kaggle.com/competitions/kaggriculture`をクリックしてください。

参加済みであることを確認してください：

```crmsh
kaggle competitions list --group entered
```

## 競技データをダウンロード

```haskell
kaggle competitions download kaggriculture -p kaggriculture-data
```

## エージェントを提出する

提出物には、`main.py`ルートに関数を持つ`agent`ファイルが必要です。

**シングルファイルエージェント：**

```stylus
kaggle competitions submit kaggriculture -f main.py -m "Wheat loop v1"
```

**マルチファイルエージェント**`main.py`-ルートに以下の内容を含むtar.gzにバンドルします。

```stylus
tar -czf submission.tar.gz main.py helper.py model_weights.pkl
kaggle competitions submit kaggriculture -f submission.tar.gz -m "Multi-file agent v1"
```

**ノート提出：**

```stylus
kaggle competitions submit kaggriculture -k YOUR_USERNAME/kaggriculture-agent -f submission.tar.gz -v 1 -m "Notebook agent v1"
```

## 提出物を監視する

提出状況を確認する：

```ebnf
kaggle competitions submissions kaggriculture
```

出力結果から提出IDを控えておいてください。エピソードを作成する際に必要になります。

## エピソード一覧

提出物がいくつかのゲームをプレイした後：

```xml
kaggle competitions episodes <SUBMISSION_ID>
```

スクリプト用のCSV出力：

```xml
kaggle competitions episodes <SUBMISSION_ID> -v
```

## リプレイとログをダウンロードする

エピソードのリプレイJSONをダウンロードします（視覚化または分析用）：

```nix
kaggle competitions replay <EPISODE_ID>
kaggle competitions replay <EPISODE_ID> -p ./replays
```

エージェントの動作をデバッグするには、エージェントログをダウンロードしてください。

```nix
# Logs for the first agent (index 0)
kaggle competitions logs <EPISODE_ID> 0

# Logs for the second agent (index 1)
kaggle competitions logs <EPISODE_ID> 1 -p ./logs
```

## リーダーボードを確認する

```ebnf
kaggle competitions leaderboard kaggriculture -s
```

## 典型的なワークフロー

```vim
# Test locally
python -c "
from kaggle_environments import make
env = make('kaggriculture', debug=True)
env.run(['main.py', 'random'])
print([(i, s.reward) for i, s in enumerate(env.steps[-1])])
"

# Submit
kaggle competitions submit kaggriculture -f main.py -m "v1"

# Check status
kaggle competitions submissions kaggriculture

# Review episodes
kaggle competitions episodes <SUBMISSION_ID>

# Download replay and logs
kaggle competitions replay <EPISODE_ID>
kaggle competitions logs <EPISODE_ID> 0

# Check leaderboard
kaggle competitions leaderboard kaggriculture -s
```