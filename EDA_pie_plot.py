import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from load_data import load_data

def pie_plot(df, col_index):
    column_name = df.columns[col_index]
    values_counts_sorted = df[column_name].value_counts().sort_values(ascending=False)
    top_12 = values_counts_sorted.head(12)
    # print(top_12)

    # Sum the remaining values to create an 'Others' category
    others_sum = values_counts_sorted[12:].sum()

    # Create a Series for 'Others'
    others_series = pd.Series({'Others': others_sum})

    # Use pd.concat to combine the top 12 values with the 'Others' Series
    top_12_with_others = pd.concat([top_12, others_series])

    values = top_12_with_others.values
    categories = top_12_with_others.keys()
    # Creating the pie chart
    plt.figure(figsize=(10, 10))
    # plt.pie(values, labels=categories, autopct='%1.1f%%')
    # plt.title(column_name + ' Distribution')


    #
    # explode = [0.1 for _ in values]  # Adjust as needed
    # explode=explode,
    wedges, _, autotexts = plt.pie(values, autopct='%1.1f%%', shadow=False, textprops={'fontsize': 15})

    # Add connection lines
    # for wedge, label in zip(wedges, categories):
    #     ang = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    #     x = wedge.r * 0.95 * np.cos(np.deg2rad(ang))
    #     y = wedge.r * 0.95 * np.sin(np.deg2rad(ang))
    #
    #     # Determine if label goes to left or right
    #     horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    #     connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    #
    #     # Create annotation
    #     plt.annotate(label, xy=(x, y), xytext=(1.5 * np.sign(x), 2.0 * y),
    #                  horizontalalignment=horizontalalignment, fontsize=10,
    #                  arrowprops=dict(arrowstyle="->", connectionstyle=connectionstyle))
    plt.tight_layout()
    # plt.savefig('pie_chart.png', bbox_inches='tight', pad_inches=1.0)
    plt.legend(categories, loc='best', fontsize=10)
    plt.show()


if __name__ == "__main__":
    df = load_data()
    pie_plot(df, 2)
    pie_plot(df, 3)
    pie_plot(df, 4)
    pie_plot(df, 6)