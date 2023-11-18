
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from load_data import load_data


def bar_plot(df, col_index):
    column_name = df.columns[col_index]
    # Calculate the frequency of each language
    values_counts_sorted = df[column_name].value_counts().sort_values(ascending=False)
    top_12 = values_counts_sorted.head(12)
    # Sum the remaining values to create an 'Others' category
    others_sum = values_counts_sorted[12:].sum()

    # Create a Series for 'Others'
    others_series = pd.Series({'Others': others_sum})

    # Use pd.concat to combine the top 12 values with the 'Others' Series
    top_12_with_others = pd.concat([top_12, others_series])
    # Create a bar plot
    plt.figure(figsize=(15, 10))
    top_12_with_others.plot(kind='bar')
    plt.title(column_name + " Distribution")
    plt.xlabel(column_name)
    plt.ylabel('Number')
    plt.xticks(rotation=45)  # Rotates the language names for better readability
    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    plt.show()


if __name__ == "__main__":
    df = load_data()
    bar_plot(df, 2)
    bar_plot(df, 3)
    bar_plot(df, 4)
    bar_plot(df, 6)


