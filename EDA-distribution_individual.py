import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from load_data import load_data


def bar_plot_ind(df, col_index):
    column_name = df.columns[col_index]
    postfix = "\n"

    def add_postfix(sentence):
        words = sentence.split()
        postfixed_words = [word + postfix for word in words]
        return ' '.join(postfixed_words)
    # Calculate the frequency of each language
    values_counts_sorted = df[column_name].apply(add_postfix).value_counts().sort_values(ascending=False)
    top_12 = values_counts_sorted.head(12)
    # print(top_12)

    # Sum the remaining values to create an 'Others' category
    others_sum = values_counts_sorted[12:].sum()
    total_sum = values_counts_sorted.sum()

    # Create a Series for 'Others'
    others_series = pd.Series({'Others': others_sum})

    # Use pd.concat to combine the top 12 values with the 'Others' Series
    top_12_with_others = pd.concat([top_12, others_series])

    percentages = []
    for value in top_12_with_others:
        per = round(value * 100 / total_sum, 2)
        percentages.append(str(per) + "%")


# Create a bar plot
    plt.figure(figsize=(15, 10))
    graph = top_12_with_others.plot(kind='bar')
    for i, per in enumerate(percentages):
        graph.text(i, top_12_with_others[i], per, ha='center', va='bottom')

    plt.title(column_name + " Distribution")
    plt.xlabel(column_name)
    plt.ylabel('Number')
    plt.xticks(rotation=0)  # Rotates the language names for better readability
    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    plt.show()


if __name__ == "__main__":
    df = load_data()
    bar_plot_ind(df, 2)
    bar_plot_ind(df, 3)
    bar_plot_ind(df, 4)
    bar_plot_ind(df, 6)
