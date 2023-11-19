"""
This file contains the function that compares the use of different media platforms
of the same entity.
Author: Yinuo Zhao
Date: Nov 17, 2023

Disclaimer: this file is for the purpose of the 2023 CANIS Hackathon only.


COLUMN NAMES
'Name (English)'
'Name (Chinese)'
'Region of Focus'
'Language'
'Entity owner (English)'
'Entity owner (Chinese)'
'Parent entity (English)'
'Parent entity (Chinese)'
'X (Twitter) handle'
'X (Twitter) URL'
'X (Twitter) Follower #'
'Facebook page'
'Facebook URL'
'Facebook Follower #'
'Instragram page'
'Instagram URL'
'Instagram Follower #'
'Threads account'
'Threads URL'
'Threads Follower #'
'YouTube account'
'YouTube URL'
'YouTube Subscriber #'
'TikTok account'
'TikTok URL'
'TikTok Subscriber #'


"""
import venn
from load_data import load_data
from radar_chart import radar_factory
import matplotlib.pyplot as plt
import matplotlib
# uncomment the following line to run account_platform_count()
matplotlib.use('Agg')


def full_pie(df, platforms):
    """
    pie chart of average followers
    :param df:
    :param platforms:
    """
    average_followers = [df['X (Twitter) Follower #'].mean(), df['Facebook Follower #'].mean(),
                         df['Instagram Follower #'].mean(), df['Threads Follower #'].mean(),
                         df['YouTube Subscriber #'].mean(), df['TikTok Subscriber #'].mean()]
    explode = (0.1, 0, 0.1, 0.1, 0.1, 0.1)
    fig, ax = plt.subplots()
    pie_colors = ['#00ffda', '#ff9fdc', '#6c6bfe', '#252ac1', '#c7c3e8', '#f8f3e3']
    ax.pie(average_followers, labels=platforms, autopct='%1.1f%%',
           shadow={'ox': -0.05, 'edgecolor': 'none', 'shade': 0.9}, startangle=90,
           explode=explode, pctdistance=1.1, labeldistance=1.3, colors=pie_colors)
    plt.title("Average Followers by Platform",
              fontsize=15, pad=40)
    plt.show()


def zoomed_pie(df):
    """
    pie chart of average followers with facebook removed
    :param df:
    """
    platforms = ['twitter', 'instagram', 'thread', 'youtube', 'tiktok']
    average_followers = [df['X (Twitter) Follower #'].mean(),
                         df['Instagram Follower #'].mean(), df['Threads Follower #'].mean(),
                         df['YouTube Subscriber #'].mean(), df['TikTok Subscriber #'].mean()]

    fig, ax = plt.subplots()
    explode = (0, 0, 0.2, 0, 0)
    pie_colors = ['#00ffda', '#6c6bfe', '#252ac1', '#c7c3e8', '#f8f3e3']
    ax.pie(average_followers, labels=platforms, autopct='%1.1f%%', colors=pie_colors, explode=explode)
    plt.title("Average Followers by Platform",
              fontsize=15, pad=30)
    plt.show()


def most_followed_accounts_on_platforms(df, platforms):
    """
    count of users on each platform
    :param df:
    :param platforms:
    """
    followers_colum = ['X (Twitter) Follower #',
                       'Facebook Follower #',
                       'Instagram Follower #',
                       'Threads Follower #',
                       'YouTube Subscriber #',
                       'TikTok Subscriber #']
    counts = []
    for i in range(6):
        counts.append(df[followers_colum[i]].count())
    fig, ax = plt.subplots()
    bar_colors = ['#6c6bfe', '#6c6bfe', '#6c6bfe', '#6c6bfe', '#6c6bfe', '#6c6bfe']
    bars = ax.bar(platforms, counts, color=bar_colors)
    ax.bar_label(bars)
    # ax.set_facecolor('#f8f3e3')
    # fig.patch.set_facecolor('#f8f3e3')
    plt.xlabel("Platforms")
    plt.ylabel("Entity Count")
    plt.title("Number of Entities that Use Each Platform",
              fontsize=15)
    plt.show()


def platform_radar(platforms):
    """
    radar plot of the overall summary of platforms
    :param platforms:
    """
    # average_followers = [121711.5, 3214201.3, 106382.9, 12325.0, 189849.2, 171444.2]
    # entity_counts = [573, 326, 139, 35, 159, 118]
    # total_user = [528.3, 3049, 2350, 137, 2780, 1060]
    # daily_active_user = [237.8, 2037, 990, 10.3, 122, 47]
    # growth_rate = [-1, 3.08, 5.47, 0, 10.6, 16]
    # variables = ['Average Entity Followers', 'Entity Counts', 'Total User',
    #              'Daily Active User', 'User Growth Rate']
    variables = ['A', 'B', 'C', 'D', 'E']

    # average_followers = [3, 6, 2, 1, 5, 4]
    # entity_counts     = [6, 5, 3, 1, 4, 2]
    # total_user        = [2, 6, 4, 1, 5, 3]
    # daily_active_user = [4, 6, 5, 1, 3, 2]
    # growth_rate       = [1, 3, 4, 2, 5, 6]

    data = [variables,
            (platforms[0], [[3, 6, 2, 4, 1]]),
            (platforms[1], [[6, 5, 6, 6, 3]]),
            (platforms[2], [[2, 3, 4, 5, 4]]),
            (platforms[3], [[1, 1, 1, 1, 2]]),
            (platforms[4], [[5, 4, 5, 3, 5]]),
            (platforms[5], [[4, 2, 3, 2, 6]])]

    N = 5
    theta = radar_factory(N, frame='polygon')
    spoke_labels = data.pop(0)
    fig, axs = plt.subplots(figsize=(9, 9), nrows=2, ncols=3,
                            subplot_kw=dict(projection='radar'), sharey=True)
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['#ff9fdc']

    for ax, (title, case_data) in zip(axs.flat, data):
        ax.set_rgrids([1, 2, 3, 4, 5, 6])
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(case_data, colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25, label='_nolegend_')
        ax.set_varlabels(spoke_labels)

    fig.text(0.5, 0.965, 'Comparing the 6 Platforms',
             horizontalalignment='center', color='black', weight='bold',
             size='large')

    plt.show()


def account_platform_count(df, platforms):
    """
    create a venn diagram to see the overlap between platforms
    :param df:
    :param platforms:
    """
    followers_column = ['X (Twitter) Follower #',
                        'Facebook Follower #',
                        'Instagram Follower #',
                        'Threads Follower #',
                        'YouTube Subscriber #',
                        'TikTok Subscriber #']
    df['num_platforms'] = df[followers_column].count(axis=1)
    print(df[df['num_platforms'] == 6]['Name (English)'])

    twitter_users = set(df[df['X (Twitter) handle'].notna()]['Name (English)'].values.tolist())
    facebook_users = set(df[df['Facebook page'].notna()]['Name (English)'].values.tolist())
    instagram_users = set(df[df['Instragram page'].notna()]['Name (English)'].values.tolist())
    thread_users = set(df[df['Threads account'].notna()]['Name (English)'].values.tolist())
    youtube_users = set(df[df['YouTube account'].notna()]['Name (English)'].values.tolist())
    tiktok_users = set(df[df['TikTok account'].notna()]['Name (English)'].values.tolist())

    labels = venn.get_labels([twitter_users, facebook_users, instagram_users, thread_users,
                              youtube_users, tiktok_users],
                             fill=['number'])
    fig, ax = venn.venn6(labels, names=platforms, figsize=(10, 10))
    fig.savefig('venn6.png', bbox_inches='tight')
    plt.close()


def main():
    """
    main function to draw the plots

    """
    platforms = ['Twitter', 'Facebook', 'Instagram', 'Thread', 'Youtube', 'Tiktok']
    df = load_data()
    full_pie(df, platforms)
    zoomed_pie(df)
    most_followed_accounts_on_platforms(df, platforms)
    platform_radar(platforms)
    account_platform_count(df, platforms)


if __name__ == "__main__":
    main()
