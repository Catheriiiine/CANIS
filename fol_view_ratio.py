from load_data import load_data
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib


def top12_followers(df):
    """determine the top 12 accounts with the most X followers"""
    top_12 = df.sort_values(by="X (Twitter) Follower #", ascending=False).head(12)
    top_names = top_12["X (Twitter) handle"]
    top_values = top_12["X (Twitter) Follower #"]
    top_urls = top_12["X (Twitter) URL"]
    # Display the results
    print("Top 12 Names and Values:")
    for name, value in zip(top_names, top_values):
        print(f"{name}: {value}")
    # for name in top_names:
    #     print(name)
    # for value in top_values:
    #     print(value)
    # for url in top_urls:
    #     print(url)


def bar_plot_ratio(df):
    plt.bar(df['X_account'], df['fol_view_ratio'], color="green")
    plt.title("follow-view ratio")
    plt.xlabel("Account")
    plt.ylabel('ratio')
    plt.xticks(rotation=45)  # Rotates the language names for better readability
    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    plt.show()


if __name__ == "__main__":
    df = pd.read_excel("fol_view_data.xlsx")
    bar_plot_ratio(df)
