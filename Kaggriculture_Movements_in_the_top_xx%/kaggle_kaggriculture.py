

import pandas as pd
import ast
from numpy import astype
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import math

"""
from kaggle_Kaggriculture import xy_plt_2d, convert,xy_plt_2d,........
"""


#1
def convert(val):
    """
    文字列の "[4, 4]" などを、リストの [4, 4] に変換

    """
    if isinstance(val, str):
        return ast.literal_eval(val)
    else:
        return val


import seaborn as sns
import matplotlib.pyplot as plt
import math


#2
def xy_plt_2d(df):
    """
    df[""]をヒートマップに変換：単体

    <df>:2D配列のdf[x,y]
    """
    df = df.apply(convert)
    df_xy = pd.DataFrame(df.tolist(), columns=["x", "y"])
    df_xy = df_xy.dropna().astype(int)
    heatmap_data = pd.crosstab(df_xy['y'], df_xy['x'])
    grid_range = list(range(10))
    heatmap_data = heatmap_data.reindex(
        index=grid_range, columns=grid_range, fill_value=0
    )

    plt.figure(figsize=(6, 5))

    sns.heatmap(heatmap_data, annot=True, cmap="Blues", fmt="d")
    plt.show()


#3
def xy_plt_2d_all(df, cols, n_rows, n_cols):
    """
    df[""]をヒートマップに変換：複数

    <df>:2D配列のdf[x,y]

    xy_plt_2d_all(df_st, ["<列>", "<列>"], <行の数>, <列の数>)
    """
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 4, n_rows * 4))
    axes = axes.flatten()

    grid_range = list(range(10))

    for i, col in enumerate(cols):
        ax = axes[i]

        s = df[col].apply(convert)
        df_xy = pd.DataFrame(s.tolist(), columns=["x", "y"])
        df_xy = df_xy.dropna().astype(int)
        heatmap_data = pd.crosstab(df_xy['y'], df_xy['x'])

        heatmap_data = heatmap_data.reindex(
            index=grid_range, columns=grid_range, fill_value=0
        )



        sns.heatmap(heatmap_data, annot=True, cmap="Blues", fmt="d", ax=ax, cbar=False)
        ax.set_title(col)

    plt.tight_layout()
    plt.show()

#4
def create_all_hands_feature(df):
    """
    ["hands_list_1"] 〜 ["hands_list_20"] を合算し、
    "all_hands" 列を作成する。
    """
    hands_cols = [f"hands_list_{i}" for i in range(1, 21)]

    def agg_hands(row):
        combined = []
        for col in hands_cols:
            if col in row.index:
                val = row[col]
                if isinstance(val, (str, list)):
                    val = convert(val)
                    if isinstance(val, list) and len(val) == 2:
                        combined.append(val)
        return combined

    df["all_hands"] = df.apply(agg_hands, axis=1)
    return df


#5
def new_xy_plt_2d(df):
    """
    df[""]をヒートマップに変換：複数座標の合算専用

    <df>: 複数座標のdf[[x,y], [x,y]...] (例: all_hands)
    """
    all_coords = []

    for val in df:
        val = convert(val)
        if isinstance(val, list) and len(val) > 0 and isinstance(val[0], list):
            all_coords.extend(val)

    df_xy = pd.DataFrame(all_coords, columns=["x", "y"])
    df_xy = df_xy.dropna().astype(int)
    heatmap_data = pd.crosstab(df_xy['y'], df_xy['x'])
    grid_range = list(range(10))
    heatmap_data = heatmap_data.reindex(
        index=grid_range, columns=grid_range, fill_value=0
    )

    plt.figure(figsize=(6, 5))

    sns.heatmap(heatmap_data, annot=True, cmap="Blues", fmt="d")
    plt.show()