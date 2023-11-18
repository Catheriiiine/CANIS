"""
This file contains the function that investigate the ratio between followers and register date of the
top 12 accounts with the most amount of twitter followers.
Author: Yinuo Zhao
Data: Nov 18, 2023

Disclaimer: this file is for the purpose of the 2023 CANIS Hackathon only.
"""
from load_data import load_data
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

def main():
    df = load_data()
    sorted_df = df.sort_values(by='X (Twitter) Follower #', ascending=False)

    # Get the top 12 rows with the highest values in the 'x' column
    top_12 = sorted_df.head(12)
    top_12= top_12[['Name (English)', 'X (Twitter) Follower #', 'X (Twitter) URL']]
    top_12['register_date'] = ['2013-01-01', '2012-02-01', '2011-05-01', '2009-11-01',
                               '2019-10-01', '2019-08-01', '2010-05-01', '2010-05-01',
                               '2009-06-01', '2015-08-01', '2010-05-01', '2019-08-01']
    top_12['register_date'] = pd.to_datetime(top_12['register_date'])

    current_date = pd.to_datetime(dt.date.today())
    top_12['MonthsToCurrentMonth'] = (current_date.year - top_12['register_date'].dt.year) * 12 + (
                current_date.month - top_12['register_date'].dt.month)

    print(top_12)

    x = top_12['MonthsToCurrentMonth'].values
    y = top_12['X (Twitter) Follower #'].values
    labels = top_12['Name (English)'].values
    print(len(x))
    print(len(labels))
    print(len(x))
    plt.figure(figsize=(8, 6))  # Optional: Set the figure size


    # Create the scatter plot
    plt.scatter(x, y, marker='o', color='blue', s=50, label='Data Points')
    plt.title("Months Since Registration vs. Number of Followers")

    # Add labels to each point
    # for i, label in enumerate(labels):
    #     plt.annotate(label, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    plt.annotate(labels[0], (x[0], y[0]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8)
    plt.annotate(labels[1], (x[1], y[1]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8)
    plt.annotate(labels[2], (x[2], y[2]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8)
    plt.annotate(labels[3], (x[3], y[3]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8)
    plt.annotate(labels[4], (x[4], y[4]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
    plt.annotate(labels[5], (x[5], y[5]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8)
    plt.annotate(labels[6], (x[6]-15, y[6]), textcoords="offset points", xytext=(0, -10), ha='center', fontsize=8)
    plt.annotate(labels[7], (x[7]-10, y[7]), textcoords="offset points", xytext=(0, 0), ha='center', fontsize=8)
    plt.annotate(labels[8], (x[8], y[8]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
    plt.annotate(labels[9], (x[9], y[9]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8)
    plt.annotate(labels[10], (x[10], y[10]), textcoords="offset points", xytext=(0, -10), ha='center', fontsize=8)
    plt.annotate(labels[11], (x[11], y[11]), textcoords="offset points", xytext=(0, -10), ha='center', fontsize=8)


    # Add axis labels and a legend (if needed)
    plt.xlabel('Number of Months Since Registered')
    plt.ylabel('Number of Followers(Million)')
    plt.legend()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
