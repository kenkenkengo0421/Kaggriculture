



```py
[googlecolab]

dir
  |__sub_main.ipynb
  |__split_zip_file.py
  |__dir_to_strong.py
  |__kaggriculture_df.py
  |__archive.zip
```


### 各クラス、ファイル
  

|**ファイル名**|**説明**|**引数**|
|---------|---------|---------|
|[sub_main.ipynb](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/sub_main.ipynb)|メイン|なし🍗|
|[split_zip_file.py](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/split_zip_file.py)|データが20GBと巨大なため、分割します|`<folder_path>`: （展開後の大容量フォルダのパス）<br><br>`<num_splits>`: 分割数<br><br>*30を推奨します。20ではクラッシュしました。|
|[dir_to_strong.py](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/dir_to_strong.py)|分割されたディレクトリとファイルから、最終ステップでの手持ち現金が上位xx%のプレイヤーのみを抽出します|`<target_dir>`: 分割フォルダを含むルートディレクトリのパス（例: `/content/data`）<br><br>`<output_dir>`: 出力ディレクトリの名前<br><br>`<top_percent>`: 抽出する上位の割合（例: 0.02は上位2%を意味します）|
|[kaggriculture_df.py](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/kaggriculture_df.py)|JSONをパースしてデータフレームに変換するクラス|`<jsonfile>`: JSONファイルのパス<br><br>`<player_num>`: JSONファイル内の2人のプレイヤーのうち、どちらをDFに設定するか<br><br>*トップランキングを忠実に再現するには、DirToStrongによって生成されたファイル名を使用してください：<br><br>`Kaggriculture_df(“/st_data/strong_rank1_score157577.0.json,”)`<br><br>*使用例については、メインの使用方法の説明をご覧ください。|
|archive.zip|このコンペティション用のデータセット|記載なし|


### 基本項目

| **column名**                  | **説明**         |
| ---------------------------- | -------------- |
| ["step"]                     |                |
| ["day"]                      |                |
| ["money"]                    | プレイヤー0の所持金     |
| ["tiles"]                    | 10x10のマス目の状態   |
| ["farmer_x_y"]               | 自分の座標          |
| ["hands_n"]                  | 労働者の人数         |
| ["hires_today"]              | 本日採用した人数       |
| ["unlocked_quadrants"]       | アンロックした土地サブセット |
| ["private_shed"]             | 小屋の収穫物在庫       |
| ["private_seeds"]            | 所持している種の数      |
| ["market_inv"]               | 市場の在庫数         |
| ["market_prices"]            | 現在の価格          |
| ["farmer_action"]            | メイン農家の行動       |
| ["hands_action"]             | 労働者の行動         |
| ["market_action"]            | 市場での売買・雇用アクション |

### 労働者n座標

| **column名**       | **説明**  |
| ----------------- | ------- |
| ["hands_list_1"]  | 労働者1座標  |
| ["hands_list_2"]  | 労働者2座標  |
| ["hands_list_3"]  | 労働者3座標  |
| ["hands_list_4"]  | 労働者4座標  |
| ["hands_list_5"]  | 労働者5座標  |
| ["hands_list_6"]  | 労働者6座標  |
| ["hands_list_7"]  | 労働者7座標  |
| ["hands_list_8"]  | 労働者8座標  |
| ["hands_list_9"]  | 労働者9座標  |
| ["hands_list_10"] | 労働者10座標 |
| ["hands_list_11"] | 労働者11座標 |
| ["hands_list_12"] | 労働者12座標 |
| ["hands_list_13"] | 労働者13座標 |
| ["hands_list_14"] | 労働者14座標 |
| ["hands_list_15"] | 労働者15座標 |
| ["hands_list_16"] | 労働者16座標 |
| ["hands_list_17"] | 労働者17座標 |
| ["hands_list_18"] | 労働者18座標 |
| ["hands_list_19"] | 労働者19座標 |
| ["hands_list_20"] | 労働者20座標 |

### 労働者nの行動

| **column名**              | **説明**   |
| ------------------------ | -------- |
| ["hands_action_list_1"]  | 労働者1の行動  |
| ["hands_action_list_2"]  | 労働者2の行動  |
| ["hands_action_list_3"]  | 労働者3の行動  |
| ["hands_action_list_4"]  | 労働者4の行動  |
| ["hands_action_list_5"]  | 労働者5の行動  |
| ["hands_action_list_6"]  | 労働者6の行動  |
| ["hands_action_list_7"]  | 労働者7の行動  |
| ["hands_action_list_8"]  | 労働者8の行動  |
| ["hands_action_list_9"]  | 労働者9の行動  |
| ["hands_action_list_10"] | 労働者10の行動 |
| ["hands_action_list_11"] | 労働者11の行動 |
| ["hands_action_list_12"] | 労働者12の行動 |
| ["hands_action_list_13"] | 労働者13の行動 |
| ["hands_action_list_14"] | 労働者14の行動 |
| ["hands_action_list_15"] | 労働者15の行動 |
| ["hands_action_list_16"] | 労働者16の行動 |
| ["hands_action_list_17"] | 労働者17の行動 |
| ["hands_action_list_18"] | 労働者18の行動 |
| ["hands_action_list_19"] | 労働者19の行動 |
| ["hands_action_list_20"] | 労働者20の行動 |

### 売買品

["CARROT"],#ニンジン
["EGG"],#たまご
["FERTILIZER"],#肥料
["MELON"],#メロン
["MILK"],#ミルク
["STRAWBERRY"],#イチゴ
["TOMATO"],#トマト
["WHEAT"],#小麦
["WOOL"],#ウール
