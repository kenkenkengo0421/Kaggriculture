import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style
import pandas as pd
import seaborn as sns
import math

"""
ヒストグラム（全体を見るとき）
Hist(data=<DF>, column_name=<DFのcolumn>, bins=<bins>, figsize=(<横大きさ,縦大きさ>), step=<区切り>)

"""
class Hist:
    def __init__(self, data, column_name, bins=30, figsize=(10, 10), step=1):
        self.df = pd.DataFrame(data)
        self.column_name = column_name
        self.bins = bins
        self.figsize = figsize
        self.step = step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        plt.figure(figsize=self.figsize)
        target_data = self.df[self.column_name].dropna()
        plt.hist(target_data, bins=self.bins, edgecolor='white')
        plt.xticks(np.arange(int(target_data.min()), int(target_data.max()) + 1, self.step))        
        plt.show()



"""
ヒストグラム ( snsバージョン )
sns_Hist(data=<DF>, x=<横軸>, hue=<基準のcolumn>, figsize=(<横大きさ,縦大きさ>), step=<区切り>)
"""
class sns_Hist:
    def __init__(self, data, x, hue, figsize=(10, 10), step=1):
        self.df = pd.DataFrame(data)
        self.x = x
        self.hue = hue
        self.figsize = figsize
        self.step = step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        plt.figure(figsize=self.figsize)

        plot_df = self.df.dropna(subset=[self.x,
                                         self.hue])
        
        sns.histplot(data=plot_df,
                     x=self.x,
                     hue=self.hue,
                     multiple='stack'
                     )
        min_val = int(plot_df[self.x].min())
        max_val = int(plot_df[self.x].max())
        plt.xticks(np.arange(min_val, max_val + 1, self.step))    
        plt.show()

"""
 KDEプロット(滑らかなヒストグラム)
sns_kde(data=<DF>,
        x=<横軸>,
        hue=<基準のcolumn>,
        fill=<True>,                    #塗りつぶすかどうか
        common_norm=<False>,　　　　　　 #よくわからん 
        figsize=(<横大きさ,縦大きさ>),
        step=<区切り>)
"""


class sns_kde:
    def __init__(self, data, x, hue, fill=True, common_norm=False, figsize=(10, 10), step=1):
        self.df = pd.DataFrame(data)
        self.x = x
        self.hue = hue
        self.fill = fill
        self.common_norm = common_norm
        self.figsize = figsize
        self.step = step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        plt.figure(figsize=self.figsize)

        plot_df = self.df.dropna(subset=[self.x,
                                         self.hue])
        
        sns.kdeplot(data=plot_df,
                    x=self.x,
                    hue=self.hue,
                    fill=self.fill,
                    common_norm=self.common_norm
                     )
        min_val = int(plot_df[self.x].min())
        max_val = int(plot_df[self.x].max())
        plt.xticks(np.arange(min_val, max_val + 1, self.step))    
        plt.show()


"""
文字列の値をカウント(棒グラフ)
目的変数と比べる。

sns_countplot(data=<df>,
              x=<DFのcolumn>,
              hue=<基準のcolumn>,
              figsize=(<横大きさ,縦大きさ>),
              y_step=<区切り>)
"""


class sns_countplot:
    def __init__(self, data, x, hue=None, figsize=(5, 10), y_step=10000):
        self.df = pd.DataFrame(data)
        self.x = x
        self.hue = hue
        self.figsize = figsize
        self.y_step = y_step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        plt.figure(figsize=self.figsize)
        
        sns.countplot(data=self.df, x=self.x, hue=self.hue)
        
        max_count = self.df[self.x].value_counts().max()
        plt.yticks(np.arange(0, max_count + self.y_step, self.y_step))
        
        plt.xlabel(self.x)
        plt.ylabel("Count")
        plt.show() 


#======

"""
折れ線グラフ

sns_line(df, x='step', y='money', step=100)

"""


class sns_line:
    def __init__(self, data, x, y, hue=None, figsize=(15, 5), step=100):
        self.df = pd.DataFrame(data)
        self.x = x
        self.y = y          
        self.hue = hue
        self.figsize = figsize
        self.step = step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        plt.figure(figsize=self.figsize)

        # xまたはyが欠損している行を削除
        plot_df = self.df.dropna(subset=[self.x, self.y])
        
        # 折れ線グラフを描画
        sns.lineplot(data=plot_df,
                     x=self.x,
                     y=self.y,
                     hue=self.hue)
        
        # x軸のメモリをstep間隔で設定
        min_val = int(plot_df[self.x].min())
        max_val = int(plot_df[self.x].max())
        plt.xticks(np.arange(min_val, max_val + 1, self.step))
        
        plt.title(f"{self.y} over {self.x}") # わかりやすくタイトルを追加
        plt.show() 


"""
折れ線グラフ複数の項目

見たい項目をリストにまとめる

cols_to_plot = [
    'money', 
    'wheat_price', 
    'melon_price', 
    'wheat_in_shed', 
    'melon_in_shed'
]

クラスを1回呼ぶだけ！

sns_line_s(df, x='step', y=cols_to_plot, step=30)
"""

class sns_line_s:
    def __init__(self, data, x, y, hue=None, step=100):
        self.df = pd.DataFrame(data)
        self.x = x
        # yが単一の文字ならリストに変換、すでにリストならそのまま受け取る
        self.y = [y] if isinstance(y, str) else y 
        self.hue = hue
        self.step = step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        
        # グラフの数を数えて、自動的に行数と列数（最大3列）を計算する
        n_plots = len(self.y)
        ncols = min(3, n_plots)
        nrows = math.ceil(n_plots / ncols)
        
        # グラフの枠のサイズも自動でいい感じにする
        fig_width = ncols * 7
        fig_height = nrows * 5
        
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(fig_width, fig_height))
        
        # 扱いやすいように枠(axes)を1次元のリストにする
        if n_plots == 1:
            axes = [axes]
        else:
            axes = axes.flatten()

        # 指定されたyの数だけループしてグラフを描く
        for i, col in enumerate(self.y):
            ax = axes[i]
            plot_df = self.df.dropna(subset=[self.x, col])
            
            if not plot_df.empty:
                sns.lineplot(data=plot_df, x=self.x, y=col, hue=self.hue, ax=ax)
                
                # メモリとタイトルの設定
                min_val = int(plot_df[self.x].min())
                max_val = int(plot_df[self.x].max())
                ax.set_xticks(np.arange(min_val, max_val + 1, self.step))
                ax.tick_params(axis='x', rotation=45)
                ax.set_title(col, fontweight='bold')
        
        # 余った空白の枠があれば消す
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])
            
        plt.tight_layout()
        plt.show()