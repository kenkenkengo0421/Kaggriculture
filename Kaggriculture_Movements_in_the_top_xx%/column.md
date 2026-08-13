


# 実行環境
```[googlecolab]```



# 各クラス、ファイル
  

| **ファイル名** | **説明**| **引数** |
|-----|-----|-----|
|[split_zip_file.py](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/split_zip_file.py)|データが20GBと巨大なため、分割します|`<folder_path>`: （展開後の大容量フォルダのパス）<br><br>`<num_splits>`: 分割数<br><br>*30を推奨します。20ではクラッシュしました|
|[dir_to_strong.py](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/dir_to_strong.py)|分割されたディレクトリとファイルから、最終ステップでの手持ち現金が上位xx%のプレイヤーのみを抽出します |`<target_dir>`: 分割フォルダを含むルートディレクトリのパス（例: `/content/data`）<br><br>`<output_dir>`: 出力ディレクトリの名前<br><br>`<top_percent>`: 抽出する上位の割合（例: 0.02は上位2%を意味します）|
|[dirtobeginner.py](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/dirtobeginner.py)|分割されたディレクトリとファイルから、最終ステップでの手持ち現金が上位ではなくピンポイントでxx%のプレイヤーのみを抽出します| `<target_dir>`: 分割フォルダを含むルートディレクトリのパス（例: `/content/data`）<br><br>`<output_dir>`: 出力ディレクトリの名前<br><br>`<top_percent>`: 抽出する割合（例: 0.02はピンポイント2%を意味します）15人に厳選されます|
|[kaggriculture_df.py](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/kaggriculture_df.py)|JSONをパースしてデータフレームに変換する| `<jsonfile>`: JSONファイルのパス<br><br>`<player_num>`: JSONファイル内の2人のプレイヤーのうち、どちらをDFに設定するか|
|[kaggle_kaggriculture.py](https://github.com/kenkenkengo0421/Kaggriculture/blob/main/Kaggriculture_Movements_in_the_top_xx%25/kaggle_kaggriculture.py)|文字列の "[4, 4]" などを、リストの [4, 4] に変換|`convert(val)`|
||df[""]をヒートマップに変換：単体|xy_plt_2d(df)<br>`<df>`:2D配列のdf[x,y]|
||df[""]をヒートマップに変換：複数|xy_plt_2d_all(df, cols, n_rows, n_cols)<br>`<df>`:2D配列のdf[x,y]<br>`xy_plt_2d_all(df_st, ["hands_list_1", "hands_list_2"], 1, 2)`|
||["hands_list_1"] 〜 ["hands_list_20"] を合算し<br>"all_hands" 列を作成する|`create_all_hands_feature(df)`|
||df[""]をヒートマップに変換：複数座標の合算専用|`<df>`: 複数座標のdf[[x,y], [x,y]...] (例: all_hands)|



