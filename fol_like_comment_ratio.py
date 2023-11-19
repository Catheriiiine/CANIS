
from load_data import load_data
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib


def bar_plot_ratio(df, name):
    plt.bar(df['X_account'], df[name], color="green")
    plt.title(name)
    plt.xlabel("Account")
    plt.ylabel('ratio')
    plt.xticks(rotation=45)  # Rotates the language names for better readability
    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    plt.show()


if __name__ == "__main__":
    df = pd.read_excel("fol_like_data.xlsx")
    ratios_to_visualize = ['fol_like_ratio', 'fol_comment_ratio', 'amplification_rate', 'average_engagement_rate']

    for ratio in ratios_to_visualize:
        bar_plot_ratio(df, ratio)





