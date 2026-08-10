

import os
import json
import pandas as pd
import shutil

class DirToStrong:
    def __init__(self, target_dir, output_dir="data_now", top_percent=0.01):
        """
        <入力>
        target_dir: 分割済みフォルダ群が格納されている大元のディレクトリパス (例: '/content/data')
        output_dir: 出力先のディレクトリ名 (例: 'data_now')
        top_percent: 抽出する上位の割合 (例: 0.02 なら上位2%)

        DirToStrong(
            target_dir="",
            output_dir="",
            top_percent=0.01
        )




        """
        self.target_dir = target_dir
        self.output_dir = output_dir
        self.top_percent = top_percent

        os.makedirs(self.output_dir, exist_ok=True)

        print("--- 処理を開始します ---")
        player_scores = self._flow1_and_3_get_all_scores()
        threshold = self._calculate_threshold(player_scores)
        self._flow2_and_4_extract_strong_players(player_scores, threshold)
        print("--- 処理が完了しました ---")

    def _flow1_and_3_get_all_scores(self):
        print("フロー1 & 3: 全フォルダのJSONファイルを走査し、スコアを抽出中...")
        player_scores = []

        for root, dirs, files in os.walk(self.target_dir):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)

                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)

                            final_step = data["steps"][-1]

                            money_0 = final_step[0]["observation"]["farms"][0]["money"]
                            money_1 = final_step[1]["observation"]["farms"][1]["money"]

                            player_scores.append({"file_path": file_path, "player_num": 0, "money": money_0})
                            player_scores.append({"file_path": file_path, "player_num": 1, "money": money_1})

                    except Exception as e:
                        print(f"エラー: {file_path} の読み込みに失敗しました。スキップします。({e})")

        return player_scores


    # 中間処理:上位〇%のボーダーライン

    def _calculate_threshold(self, player_scores):
        if not player_scores:
            raise ValueError("有効なスコアデータが1件も見つかりませんでした。")

        all_money = [item["money"] for item in player_scores]

        series = pd.Series(all_money)
        threshold = series.quantile(1.0 - self.top_percent)

        print(f"抽出ボーダーライン計算完了: 上位 {self.top_percent * 100}% の基準額は {threshold} です。")
        return threshold

    #上位プレイヤーのJSONファイルを抽出・保存する

    def _flow2_and_4_extract_strong_players(self, player_scores, threshold):
        print("フロー2 & 4: 上位プレイヤーのデータを抽出・出力中...")

        strong_players = [item for item in player_scores if item["money"] >= threshold]

        strong_players = sorted(strong_players, key=lambda x: x["money"], reverse=True)

        for rank, player_info in enumerate(strong_players, start=1):
            file_path = player_info["file_path"]
            p_num = player_info["player_num"]
            money = player_info["money"]

            output_name = f"strong_rank{rank}_score{money}_p{p_num}.json"
            output_path = os.path.join(self.output_dir, output_name)

            shutil.copy2(file_path, output_path)
            print(f"[{rank}位] プレイヤー{p_num} (スコア:{money}) のJSONをコピーしました: {output_name}")