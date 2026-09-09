# Kaggriculture Optunaパラメータ探索


1. 作業員数
2. 土地・牛・牧草地
3. 担当エリアの効き方
4. 作物の生産量と植付期限
5. 収穫時期
6. 牛乳・終盤売却


## 1. [作業員数の探索](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/optuna/param_1.ipynb)

最初に作業能力を決める。作業員数が変わると、植付け・水やり・収穫・牛の世話の処理可能量がすべて変わる。

| パラメータ | 現在値 | 探索範囲 |メモ|
|---|---:|---:|---:|
| `INITIAL_TARGET_HANDS` | 6 | 4～8、1刻み |対戦開始時の目標作業員数|
| `MIN_LARGE_FARM_HANDS` | 10 | 7～10、1刻み |土地が3区画以上になった場合の最低作業員数|
| `MAX_HANDS` | 10 | 8～10、1刻み |PASS率による増員で許可する作業員の上限数|
| `MAX_HIRES_PER_TURN` | 2 | 1～3、1刻み |1ターンに雇用する作業員の上限数|
| `PASS_RATE_TO_INCREASE` | 0.05 | 0.00～0.10、0.01刻み |作業員を1人増やすPASS率|
| `PASS_RATE_TO_DECREASE` | 0.15 | 0.10～0.30、0.01刻み |作業員を1人減らすPASS率|



## 2. [土地・牛・牧草地の探索](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/optuna/param_2.ipynb)

作業員設定を仮固定した後、生産設備の規模を探索する。

| パラメータ | 現在値 | 探索範囲 |メモ|
|---|---:|---:|---:|
| `TARGET_LAND_COUNT` | 3 | 2～4、1刻み |購入を進める土地の目標区画数|
| `LAND_PRICE` | 5000 | 3000～7000、500刻み |土地購入を許可する最低所持金|
| `TARGET_COW_COUNT` | 4 | 2～5、1刻み |購入を進める牛の目標頭数|
| `TARGET_PASTURE_COUNT` | 4 | 2～5、1刻み |建設を進める牧草地の目標数|


## 3. [担当エリアの効き方の探索](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/optuna/param_3.ipynb)

| パラメータ | 現在値 | 探索範囲 |メモ|
|---|---:|---:|---:|
| `OUTSIDE_AREA_PENALTY` | 30 | 0～60、5刻み |担当エリア外の作業候補に与える減点|


## 4. 作物の生産量・植付期限の探索

作業能力と土地規模を固定してから、作物ごとに分けて探索する。

### 4A. [メロン](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/optuna/param_4A.ipynb)

| パラメータ | 現在値 | 探索範囲 |メモ|
|---|---:|---:|---:|
| `MELON_TARGET_COUNT` | 10 | 4～16、2刻み |メロンの種数と植付済み数を合わせた購入目標数|
| `MELON_PLANT_END_DAY` | 8 | 4～10、1刻み |メロンの植付けと種購入を許可する期限|

### 4B. [いちご](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/optuna/param_4B.ipynb)

| パラメータ | 現在値 | 探索範囲 |メモ|
|---|---:|---:|---:|
| `STRAWBERRY_TARGET_COUNT` | 35 | 10～45、5刻み |いちごの種数と植付済み数を合わせた購入目標数|
| `STRAWBERRY_PLANT_END_DAY` | 20 | 14～24、2刻み |いちごの植付けと種購入を許可する期限|
| `MIN_STRAWBERRY_DEMAND_SHOPS` | 1 | 0～2、1刻み |いちご需要店舗が何店舗以上なら種を購入するか|

### 4C. [ニンジン・小麦](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/optuna/param_4C.ipynb)

| パラメータ | 現在値 | 探索範囲 |メモ|
|---|---:|---:|---:|
| `CARROT_TARGET_PER_PET_CAFE` | 7 | 3～12、1刻み |PET_CAFE1店舗あたりのニンジン目標数|
| `GENERAL_PLANT_END_DAY` | 27 | 22～29、1刻み |作業対象探索から雑草と空き地を除外し始める日|
| `WHEAT_SEED_BUY_COUNT` | 6 | 2～10、1刻み |小麦種がない場合に購入する数量|
| `MIN_FEED_WHEAT` | 2 | 1～6、1刻み |牛の餌として最低限確保する小麦数|

探索順は 4A → 4B → 4C とし、各小段階で上位設定を仮固定する。最後に4A～4Cの上位範囲だけを合同探索する。

各小段階の目安：80～150 trials。

## 5. [収穫時期の探索](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/optuna/param_5.ipynb)

生産数が固まった後に、収穫量と作業負荷のバランスを探索する。

| パラメータ | 現在値 | 探索範囲 |メモ|
|---|---:|---:|---:|
| `MELON_HARVEST_AGE` | 10 | 10～12、1刻み |メロンを収穫対象として扱い始める経過日数|
| `STRAWBERRY_HARVEST_AGE` | 10 | 10～14、2刻み |いちごを収穫対象として扱い始める経過日数|
| `CARROT_HARVEST_AGE` | 3 | 2～3、1刻み |人参を収穫対象として扱い始める経過日数|
| `DEFAULT_HARVEST_AGE` | 2 | 2～4、1刻み |メロン・いちご以外の作物に使用する収穫経過日数|

メロンは資料上、初回収穫10日・最大収穫12日。ニンジンは初回2日・最大3日、小麦は初回2日・最大4日である。このゲーム上の範囲を探索境界に用いる。


## 6. [牛乳・終盤売却の探索](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/optuna/param_6.ipynb)

牛数と生産量が固まった最後に売却条件を探索する。

| パラメータ | 現在値 |探索範囲 |メモ|
|---|---:|---:|---:|
| `MILK_SELL_PRICE` | 160 | 120～240、10刻み |牛乳を通常売却する最低価格|
| `MILK_SELL_BATCH` | 6 | 1～12、1刻み |終盤以外で一度に売却する牛乳の上限数|
| `SHED_EMERGENCY_SELL_LEVEL` | 95 | 75～99、2刻み |牛乳の緊急売却を開始する非種子アイテムの保有数|
| `FINAL_SELL_STEP` | 710 | 690～715、5刻み |牛乳・メロンの強制売却を開始するSTEP|


