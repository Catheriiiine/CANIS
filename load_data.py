"""
This file contains the function that loads the data using Pandas.
Author: Yinuo Zhao
Data: Nov 17, 2023

Disclaimer: this file is for the purpose of the 2023 CANIS Hackathon only.
"""

import pandas as pd


def load_data():
    """

    :return: the data set as a pandas data frame df
    """
    df = pd.read_excel(r"CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx")
    return df
    # print(df)

# def main():
#     data = load_data()
#     print(data.describe())
#
#
# if __name__ == "__main__":
#     main()
