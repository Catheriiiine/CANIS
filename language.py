import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import load_data


def load_language_data():
    # Your code to load data goes here
    # Replace this with your data loading logic
    english_data = pd.read_csv('english_data.csv')
    french_data = pd.read_csv('french_data.csv')
    chinese_data = pd.read_csv('chinese_data.csv')
    spanish_data = pd.read_csv('spanish_data.csv')
    arabic_data = pd.read_csv('arabic_data.csv')
    german_data = 6

    portuguese = 9
    vietnamese = 1
    japanese = 1

    # Counting unique countries where Primary language is 'Yes'
    english = english_data['Country'].nunique()
    french = french_data['Country'].nunique()
    chinese = chinese_data['Country'].nunique()
    spanish = spanish_data['Country'].nunique()
    arabic = arabic_data['Country'].nunique()

    total_country = 195
    # Count of different languages
    language_counts = [english, french, chinese, spanish, arabic,
                       german_data, portuguese, vietnamese, japanese]
    # all languages
    languages = ['English', 'French', 'Chinese', 'Spanish', 'Arabic', 'German', 'Portuguese', 'Vietnamese', 'Japanese']

    # number of total countries, list of language, total country number
    return language_counts, languages, total_country


def analyze_language_data(data):

    # Counting occurrences of each language
    language_counts = data['Language'].value_counts()

    # Total number of rows in the dataset
    total_rows = len(data)

    # Calculating the ratio for each language and converting to percentage
    language_percentages = (language_counts / total_rows) * 100

    # Filtering languages with percentages greater than 1%
    filtered_percentages = language_percentages[language_percentages > 1]

    # Returning the filtered language percentages as a list
    return filtered_percentages.tolist()


def plot_language_comparison(language_counts, languages, total_country, dataset_percent):
    # Calculate percentages
    country_percentages = [count / total_country * 100 for count in language_counts] # percent of country that speak certain language / total country

    # Define the width for each bar
    bar_width = 0.35

    # Set the positions for the bars
    bar_positions_country = list(range(len(languages)))
    bar_positions_language = [pos + bar_width for pos in bar_positions_country]

    # Plotting the comparison side by side
    plt.figure(figsize=(12, 6))

    bars1 = plt.bar(bar_positions_country, country_percentages, width=bar_width, color='skyblue', label='Percentage of Country use It as Offical Language')
    bars2 = plt.bar(bar_positions_language, dataset_percent, width=bar_width, color='orange', alpha=0.7, label='Percentage of Appearance of Language in Dateset')

    plt.xlabel('Languages')
    plt.ylabel('Percentage')
    plt.title('Comparison of Country vs Language Percentage')
    plt.xticks([pos + bar_width / 2 for pos in bar_positions_country], languages)
    plt.legend()
    for bar, percent in zip(bars1, country_percentages):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{percent:.2f}%', ha='center', va='bottom')

    for bar, percent in zip(bars2, dataset_percent):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{percent:.2f}%', ha='center', va='bottom')
    plt.tight_layout()
    # plt.show()


def get_language_population(language):
    population_data = pd.read_csv('language_speaking_population.csv')

    if language == 'Arabic':
        language_cate = population_data[population_data['Language'].str.contains('Arabic')]
        # Calculate the sum of the 'Total speakers (L1+L2)' for Arabic languages
        language_population = language_cate['Total speakers (L1+L2)'].sum()
    else:
        language_population = population_data[population_data['Language'] == language]['Total speakers (L1+L2)']

    if isinstance(language_population, pd.Series):
        language_population = language_population.iloc[0]

    return language_population


def population():
    total_amount = 8045311447
    languages = ['English', 'French', 'Chinese', 'Spanish', 'Arabic', 'German', 'Portuguese', 'Vietnamese', 'Japanese']

    language_populations = []
    for language in languages:
        language_speaker = get_language_population(language)
        language_populations.append(language_speaker)

    # print(language_populations)

    return language_populations, languages, total_amount


def language_percentage(population_lst, total_population):
    # population_data = pd.read_csv('language_speaking_population.csv')
    # total_population = population_data['Total speakers (L1+L2)'].sum()

    language_percentages = [(language_speaker/total_population) * 100 for language_speaker in population_lst]
    # print(language_percentages)
    return language_percentages

def plot_population_comparison(language_percent, languages, dataset_percent):
    # Calculate percentages
    # country_percentages = [count / total_country * 100 for count in language_counts] # percent of country that speak certain language / total country
    # language_percentages = [count / sum(language_counts) * 100 for count in language_counts]

    # Define the width for each bar
    bar_width = 0.35

    # Set the positions for the bars
    bar_positions_country = list(range(len(language_percent)))
    bar_positions_language = [pos + bar_width for pos in bar_positions_country]

    # Plotting the comparison side by side
    plt.figure(figsize=(12, 6))

    bars1 = plt.bar(bar_positions_country, language_percent, width=bar_width, color='skyblue', label='Percentage of Language Speaker')
    bars2 = plt.bar(bar_positions_language, dataset_percent, width=bar_width, color='orange', alpha=0.7, label='Percentage of Appearance of Language in Dataset')

    plt.xlabel('Languages')
    plt.ylabel('Percentage')
    plt.title('Comparison of Speaker Population vs Language Percentage')
    plt.xticks([pos + bar_width / 2 for pos in bar_positions_country], languages)
    plt.legend()
    # Adding numbers on top of the bars
    for bar, percent in zip(bars1, language_percent):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{percent:.2f}%', ha='center', va='bottom')

    for bar, percent in zip(bars2, dataset_percent):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{percent:.2f}%', ha='center', va='bottom')
    plt.tight_layout()
    plt.show()


def main():

    # Loading data
    data = load_data.load_data()

    # Analyzing language data and get the language bigger than 1%
    data_set_percent = analyze_language_data(data)

    # number of total countries, list of language, total country number
    language_counts, languages, total_country = load_language_data()

    # Plotting the comparison
    plot_language_comparison(language_counts, languages, total_country, data_set_percent)

    # number of total population for each language, list of language, total country number
    language_populations, languages, total_amount = population()

    population_percent = language_percentage(language_populations, total_amount)

    plot_population_comparison(population_percent, languages, data_set_percent)





if __name__ == "__main__":
    main()
