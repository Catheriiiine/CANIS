"""
This file contains the function that compares CGTN and Embassy accounts.
Author: Yinuo Zhao
Data: Nov 18, 2023

Disclaimer: this file is for the purpose of the 2023 CANIS Hackathon only.
"""
from load_data import load_data

import matplotlib.pyplot as plt


def main():
    """
    main function to draw the plots

    """
    followers_column = ['X (Twitter) Follower #',
                        'Facebook Follower #',
                        'Instagram Follower #',
                        'Threads Follower #',
                        'YouTube Subscriber #',
                        'TikTok Subscriber #']
    platforms = ['Twitter', 'Facebook', 'Instagram', 'Thread', 'Youtube', 'Tiktok']
    df = load_data()
    cgtn_df = df[df['Name (English)'].str.contains('CGTN')]
    embassy_df = df[df['Name (English)'].str.contains('Chinese Embassy in')]

    cgtn_total = cgtn_df['X (Twitter) Follower #'].sum() + cgtn_df['Facebook Follower #'].sum() \
                                 + cgtn_df['Instagram Follower #'].sum() + cgtn_df['Threads Follower #'].sum() \
                                 + cgtn_df['YouTube Subscriber #'].sum() +cgtn_df['TikTok Subscriber #'].sum()

    embassy_total = embassy_df['X (Twitter) Follower #'].sum() + embassy_df['Facebook Follower #'].sum() \
                                    + embassy_df['Instagram Follower #'].sum() + embassy_df['Threads Follower #'].sum() \
                                    + embassy_df['YouTube Subscriber #'].sum() + embassy_df['TikTok Subscriber #'].sum()
    # print(cgtn_total)
    # print(embassy_total)
    cgtn_language_counts = cgtn_df['Language'].value_counts()
    embassy_language_counts = embassy_df['Language'].value_counts()
    # print(cgtn_language_counts)
    # print(embassy_language_counts)
    # print(embassy_df['Language'].unique())
    for i in range(6):
        # print(followers_column[i] + " total = " + str(cgtn_df[followers_column[i]].sum()))
        print(embassy_df[followers_column[i]].sum())
        print(cgtn_df[followers_column[i]].sum())


    plt.show()


if __name__ == "__main__":
    main()
