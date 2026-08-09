


#!unzip -qo <zipのパス> -d <解凍先>

import os
import pandas as pd
import json

class Split_zip_file:
    def __init__(self, folder_path, num_splits):
        """

        from split_zip_file import Split_zip_file
        Split_zip_file(folder_path, num_splits)

        <in>:
        folder_path:フォルダのパス
        num_splits:分割数 ※目安20GBのフォルダは30分割それ以下はクラッシュしました。

        <out>
        フォルダの構造が変わります

        folder_path
                 |___groupe_1
                            |____test_n.json
                 |___groupe_2
                 .          |____test_n.json
                 .
                 .
                 |___groupe_n

        ※解凍してから渡す事
        colab環境なら一番上のコメントアウトのコードを
        mainの１番上セルで実行しやがってください。

        """
        json_files = []
        not_json_files = []

        for file_name in os.listdir(folder_path):
            if file_name.endswith('.json'):
                json_files.append(file_name)
            else:
                not_json_files.append(file_name)
                file_key_path = os.path.join(folder_path, file_name)
                os.remove(file_key_path)

        json_files.sort()

        print(f"{len(not_json_files)}件のjsonではないファイルを検出しました👨‍🔧🗾")
        print("内容は以下になります。👇")
        print(f"{not_json_files}を削除しました")


        NUM_SPLITS = num_splits
        total_files = len(json_files)
        chunk_size = (total_files + (NUM_SPLITS - 1)) // NUM_SPLITS

        groups = [
            json_files[i * chunk_size : (i + 1) * chunk_size] for i in range(NUM_SPLITS)
        ]

        print(
            f"データを {NUM_SPLITS} 分割しました（1グループあたり約 {len(groups[0])} 件ずつ処理します）"
        )
        print("========================\n")



        start_index = 0


        for g_idx, current_group in enumerate(groups):
            group_folder = os.path.join(folder_path, f"group_{g_idx}")
            os.makedirs(group_folder, exist_ok=True)

            all_data_1 = []
            renamed_files_1 = []

            for i, file_name in enumerate(current_group):
                current_id = start_index + i
                old_path = os.path.join(folder_path, file_name)

                new_name = f"test_{current_id}.json"
                new_path = os.path.join(group_folder, new_name)

                os.rename(old_path, new_path)
                renamed_files_1.append(new_name)

                with open(new_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    all_data_1.append(data)

            print(
                f"【成功】第{g_idx+1}グループの {len(all_data_1)} 件を、変数 'all_data_1' に一時格納し、フォルダ 'group_{g_idx}' へ仕分けました！"
            )

            start_index += len(current_group)


        print("\n✨ すべてのファイルの30分割リネームとフォルダ仕分けが完了しました！")