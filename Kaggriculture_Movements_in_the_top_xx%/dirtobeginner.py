

import os
import json
import pandas as pd
import shutil

class DirToBeginner:
    def __init__(self, target_dir, output_dir="data_now", top_percent=0.6):
        """
        <入力>
        target_dir: 分割済みフォルダ群が格納されている大元のディレクトリパス (例: '/content/data')
        output_dir: 出力先のディレクトリ名 (例: 'data_now')
        top_percent: 抽出する基準の割合 0.5～0.8 を固定値で選択 (例: 0.6 なら60%のライン)

        DirToBeginner(
            target_dir="",
            output_dir="",
            top_percent=0.6
        )
        """
        self.target_dir = target_dir
        self.output_dir = output_dir
        self.top_percent = top_percent

        os.makedirs(self.output_dir, exist_ok=True)

        print("--- 処理を開始します ---")
        player_scores = self._flow1_and_3_get_all_scores()
        threshold = self._calculate_threshold(player_scores)
        self._flow2_and_4_extract_beginner_players(player_scores, threshold)
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

    # 中間処理:指定した割合のボーダーライン
    def _calculate_threshold(self, player_scores):
        if not player_scores:
            raise ValueError("有効なスコアデータが1件も見つかりませんでした。")

        all_money = [item["money"] for item in player_scores]

        series = pd.Series(all_money)
        # 【編集箇所】上位XX%の逆算ではなく、指定された割合(top_percent)を直接分位数として計算
        threshold = series.quantile(self.top_percent)

        print(f"抽出ボーダーライン計算完了: {self.top_percent * 100}% の基準額は {threshold} です。")
        return threshold

    # 対象プレイヤーのJSONファイルを抽出・保存する
    def _flow2_and_4_extract_beginner_players(self, player_scores, threshold):
        print("フロー2 & 4: 対象プレイヤーのデータを抽出・出力中...")

        # 閾値以上のプレイヤーを抽出
        beginner_players = [item for item in player_scores if item["money"] >= threshold]

        # 【提案・追加ロジック】抽出対象を指定パーセンタイルのボーダーライン付近の15名に限定
        beginner_players = sorted(beginner_players, key=lambda x: x["money"])[:15]

        for rank, player_info in enumerate(beginner_players, start=1):
            file_path = player_info["file_path"]
            p_num = player_info["player_num"]
            money = player_info["money"]

            output_name = f"beginner_rank{rank}_score{money}_p{p_num}.json"
            output_path = os.path.join(self.output_dir, output_name)

            shutil.copy2(file_path, output_path)
            print(f"[{rank}件目] プレイヤー{p_num} (スコア:{money}) のJSONをコピーしました: {output_name}")