import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import load_data


def load_language_data():
    # Your code to load data goes here
    # Replace this with your data loading logic
    english_data = pd.read_csv('english_data.csv')  # Replace 'your_data.csv' with your file name


    # Counting unique countries where Primary language is 'Yes'
    count_countries = english_data['Country'].nunique()

    print(f"Number of countries who speak english': {count_countries}")
    print(f"percent of countries that speak english in the world: {count_countries/195}")

    # return english_data


def analyze_language_data(data):
    # Extracting unique languages from the 'Language' column
    unique_languages = data['Language'].unique()
    print(unique_languages, len(unique_languages))

    # Counting occurrences of each language
    language_counts = data['Language'].value_counts()

    # Total number of rows in the dataset
    total_rows = len(data)

    # Calculating the ratio for each language and converting to percentage
    language_percentages = (language_counts / total_rows) * 100

    # Filtering languages with percentages greater than 0.5%
    filtered_languages = language_percentages[language_percentages > 0.6]

    # Displaying counts and ratios for filtered languages as percentages
    # print("Language Counts:")
    # print(language_counts)
    print("\nLanguage Percentages (greater than 0.5%):")
    print(filtered_languages)

def main():
    # Loading data

    data = load_data.load_data()

    load_language_data()

    # Analyzing language data
    analyze_language_data(data)

if __name__ == "__main__":
    main()
