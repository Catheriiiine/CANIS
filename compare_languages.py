"""
This file contains the function that observations that have region & language mismatch
of the same entity.
Author: Yuxuan Wu
Date: Nov 18, 2023

Disclaimer: this file is for the purpose of the 2023 CANIS Hackathon only.
"""

import pandas as pd

from load_data import load_data

import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

# Load your dataset
df = load_data()

# Example of a region-language mapping
# You will need to create a comprehensive mapping based on your data
region_language_map = {
    'ASEAN': ['Multiple'],  # ASEAN has multiple official languages depending on the member country
    'Afghanistan': ['Pashto', 'Dari'],
    'African Union': ['Arabic', 'English', 'French', 'Portuguese', 'Spanish', 'Swahili'],
    'Albania': ['Albanian'],
    'Algeria': ['Arabic', 'Berber'],
    'Anglosphere': ['English'],
    'Angola': ['Portuguese'],
    'Anhui': ['Chinese'],  # Anhui is a province in China where Mandarin is the official language
    'Antigua and Barbuda': ['English'],
    'Argentina': ['Spanish'],
    'Australia': ['English'],
    'Austria': ['German'],
    'Bahrain': ['Arabic'],
    'Bangladesh': ['Bengali'],
    'Barbados': ['English'],
    'Beijing': ['Chinese'],  # Mandarin is the official language in Beijing
    'Belarus': ['Belarusian', 'Russian'],
    'Belgium': ['Dutch', 'French', 'German'],
    'Bolivia': ['Spanish', 'Quechua', 'Aymara', 'Guaraní'],
    'Botswana': ['English', 'Setswana'],
    'Brazil': ['Portuguese'],
    'Bulgaria': ['Bulgarian'],
    'Burundi': ['Kirundi', 'French', 'English'],
    'Cambodia': ['Khmer'],
    'Cameroon': ['English', 'French'],
    'Canada': ['English', 'French'],
    'Chad': ['Arabic', 'French'],
    'Chile': ['Spanish'],
    'China': ['Chinese'],  # Mandarin is the official language
    'Chongqing': ['Chinese'],  # Chongqing is a municipality in China where Mandarin is the official language
    'Colombia': ['Spanish'],
    'Costa Rica': ['Spanish'],
    'Croatia': ['Croatian'],
    'Cuba': ['Spanish'],
    'Cyprus': ['Greek', 'Turkish'],
    'Czech Rep.': ['Czech'],
    'Dem. Rep. of Congo': ['French'],
    'Denmark': ['Danish'],
    'Djibouti': ['Arabic', 'French'],
    'Dominican Republic': ['Spanish'],
    'EU': ['English'],  # The EU has 24 official languages
    'East African Community': ['English', 'French', 'Portuguese', 'Swahili'],
    'Ecuador': ['Spanish'],
    'Egypt': ['Arabic'],
    'El Salvador': ['Spanish'],
    'Equatorial Guinea': ['Spanish', 'French', 'Portuguese'],
    'Eritrea': ['Tigrinya', 'Arabic', 'English'],
    'Estonia': ['Estonian'],
    'Ethiopia': ['Amharic'],
    'Fiji': ['English', 'Fijian', 'Hindi'],
    'Finland': ['Finnish', 'Swedish'],
    'France': ['French'],
    'Fujian': ['Chinese'],  # Fujian is a province in China where Mandarin is the official language
    'Gambia': ['English'],
    'Gansu': ['Chinese'],  # Gansu is a province in China where Mandarin is the official language
    'Germany': ['German'],
    'Ghana': ['English'],
    'Greece': ['Greek'],
    'Grenada': ['English'],
    'Guangdong': ['Chinese'],  # Guangdong is a province in China where Mandarin is the official language, though Cantonese is also widely spoken
    'Guangxi': ['Chinese'],  # Guangxi is a region in China where Mandarin is the official language
    'Guinea': ['French'],
    'Guyana': ['English'],
    'Hainan': ['Chinese'],  # Hainan is a province in China where Mandarin is the official language
    'Heilongjiang': ['Chinese'],  # Heilongjiang is a province in China where Mandarin is the official language
    'Henan': ['Chinese'],  # Henan is a province in China where Mandarin is the official language
    'Hispanophone': ['Spanish'],  # Refers to Spanish-speaking regions
    'Hong Kong': ['Chinese', 'English', 'Cantonese'],
    'Hubei': ['Chinese'],
    'Hunan': ['Chinese'],
    'Hungary': ['Hungarian'],
    'Iceland': ['Icelandic'],
    'India': ['Hindi', 'English', 'Tamil'],  # India has many regional languages, with Hindi being the most widely spoken
    'Indonesia': ['Indonesian', 'Bahasa Indonesia'],
    'Iran': ['Persian'],
    'Iraq': ['Arabic', 'Kurdish'],
    'Ireland': ['English', 'Irish'],
    'Israel': ['Hebrew', 'Arabic'],
    'Italy': ['Italian'],
    'Japan': ['Japanese'],
    'Jiangsu': ['Chinese'],  # Jiangsu is a province in China where Mandarin is the official language
    'Jiangxi': ['Chinese'],  # Jiangxi is a province in China where Mandarin is the official language
    'Jilin': ['Chinese'],
    'Jordan': ['Arabic'],
    'Kazakhstan': ['Kazakh', 'Russian'],
    'Kenya': ['English', 'Swahili'],
    'Kuwait': ['Arabic'],
    'Kyrgyzstan': ['Kyrgyz', 'Russian'],
    'Laos': ['Lao'],
    'Latvia': ['Latvian'],
    'Lebanon': ['Arabic'],
    'Lesotho': ['Sesotho', 'English'],
    'Liberia': ['English'],
    'Lithuania': ['Lithuanian'],
    'Lusophone': ['Portuguese'],  # Refers to Portuguese-speaking regions
    'MENA': ['Arabic'],  # Refers to the Middle East and North Africa region
    'Malawi': ['English', 'Chichewa'],
    'Malaysia': ['Malay'],
    'Maldives': ['Dhivehi'],
    'Mali': ['French'],
    'Malta': ['Maltese', 'English'],
    'Mauritania': ['Arabic'],
    'Mauritius': ['English', 'French'],
    'Mexico': ['Spanish'],
    'Mongolia': ['Mongolian'],
    'Montenegro': ['Montenegrin'],
    'Morocco': ['Arabic', 'Berber', 'French'],
    'Myanmar': ['Burmese'],
    'Namibia': ['English'],
    'Nepal': ['Nepali', 'Nepalese'],
    'Netherlands': ['Dutch'],
    'New Zealand': ['English', 'Maori'],
    'Nigeria': ['English'],
    'North Macedonia': ['Macedonian', 'Albanian'],
    'Norway': ['Norwegian'],
    'Pakistan': ['Urdu', 'English'],
    'Panama': ['Spanish'],
    'Papua New Guinea': ['English', 'Tok Pisin', 'Hiri Motu'],
    'Peru': ['Spanish', 'Quechua', 'Aymara'],
    'Philippines': ['Filipino', 'English'],
    'Poland': ['Polish'],
    'Portugal': ['Portuguese'],
    'Qatar': ['Arabic'],
    'Rep. of Congo': ['French'],
    'Romania': ['Romanian'],
    'Russia': ['Russian'],
    'Rwanda': ['Kinyarwanda', 'English', 'French'],
    'Samoa': ['Samoan', 'English'],
    'Saudi Arabia': ['Arabic'],
    'Senegal': ['French'],
    'Serbia': ['Serbian'],
    'Shaанxi': ['Chinese'],  # Shaanxi is a province in China where Mandarin is the official language
    'Shandong': ['Chinese'],  # Shandong is a province in China where Mandarin is the official language
    'Shanghai': ['Chinese'],  # Shanghai is a city in China where Mandarin is the official language
    'Shanxi': ['Chinese'],  # Shanxi is a province in China where Mandarin is the official language
    'Sichuan': ['Chinese'],  # Sichuan is a province in China where Mandarin is the official language
    'Sierra Leone': ['English'],
    'Singapore': ['English', 'Malay', 'Chinese', 'Tamil'],
    'Slovakia': ['Slovak'],
    'Slovenia': ['Slovene'],
    'Somalia': ['Somali', 'Arabic'],
    'South Africa': ['11 official languages including English, Zulu, Xhosa, Afrikaans'],
    'South Korea': ['Korean'],
    'South Sudan': ['English'],
    'Spain': ['Spanish'],
    'Sri Lanka': ['Sinhala', 'Tamil', 'Sinhalese'],
    'Sudan': ['Arabic', 'English'],
    'Suriname': ['Dutch'],
    'Switzerland': ['German', 'French', 'Italian', 'Romansh'],
    'São Tomé and Príncipe': ['Portuguese'],
    'Taiwan': ['Chinese', 'Taiwanese Hokkien'],
    'Tanzania': ['Swahili', 'English'],
    'Thailand': ['Thai'],
    'Tibet': ['Tibetan', 'Chinese'],  # Tibet is an autonomous region in China
    'Tonga': ['Tongan', 'English'],
    'Trinidad and Tobago': ['English'],
    'Türkiye': ['Turkish'],
    'UAE': ['Arabic'],
    'UK': ['English'],
    'UN': ['Arabic', 'Chinese', 'English', 'French', 'Russian', 'Spanish'],
    'USA': ['English'],
    'Uganda': ['English', 'Swahili'],
    'Ukraine': ['Ukrainian'],
    'Uruguay': ['Spanish'],
    'Venezuela': ['Spanish'],
    'Vietnam': ['Vietnamese'],
    'Xinjiang': ['Uighur', 'Chinese'],  # Xinjiang is an autonomous region in China
    'Yemen': ['Arabic'],
    'Yunnan': ['Chinese'],  # Yunnan is a province in China where Mandarin is the official language
    'Zhejiang': ['Chinese'],  # Zhejiang is a province in China where Mandarin is the official language
    'Zimbabwe': ['English', 'Shona', 'Sindebele'],
    'la Francophonie': ['French'],  # Represents French-speaking countries
}


territory_to_country = {
    'ASEAN': 'Association of Southeast Asian Nations',
    'Afghanistan': 'Afghanistan',
    'African Union': 'African Union',
    'Albania': 'Albania',
    'Algeria': 'Algeria',
    'Anglosphere': 'Multiple Countries',  # English-speaking countries
    'Angola': 'Angola',
    'Anhui': 'China',
    'Antigua and Barbuda': 'Antigua and Barbuda',
    'Argentina': 'Argentina',
    'Australia': 'Australia',
    'Austria': 'Austria',
    'Bahrain': 'Bahrain',
    'Bangladesh': 'Bangladesh',
    'Barbados': 'Barbados',
    'Beijing': 'China',
    'Belarus': 'Belarus',
    'Belgium': 'Belgium',
    'Bolivia': 'Bolivia',
    'Botswana': 'Botswana',
    'Brazil': 'Brazil',
    'Bulgaria': 'Bulgaria',
    'Burundi': 'Burundi',
    'Cambodia': 'Cambodia',
    'Cameroon': 'Cameroon',
    'Canada': 'Canada',
    'Chad': 'Chad',
    'Chile': 'Chile',
    'China': 'China',
    'Chongqing': 'China',
    'Colombia': 'Colombia',
    'Costa Rica': 'Costa Rica',
    'Croatia': 'Croatia',
    'Cuba': 'Cuba',
    'Cyprus': 'Cyprus',
    'Czech Rep.': 'Czech Republic',
    'Dem. Rep. of Congo': 'Democratic Republic of the Congo',
    'Denmark': 'Denmark',
    'Djibouti': 'Djibouti',
    'Dominican Republic': 'Dominican Republic',
    'EU': 'European Union',
    'East African Community': 'East African Community',
    'Ecuador': 'Ecuador',
    'Egypt': 'Egypt',
    'El Salvador': 'El Salvador',
    'Equatorial Guinea': 'Equatorial Guinea',
    'Eritrea': 'Eritrea',
    'Estonia': 'Estonia',
    'Ethiopia': 'Ethiopia',
    'Fiji': 'Fiji',
    'Finland': 'Finland',
    'France': 'France',
    'Fujian': 'China',
    'Gambia': 'Gambia',
    'Gansu': 'China',
    'Germany': 'Germany',
    'Ghana': 'Ghana',
    'Greece': 'Greece',
    'Grenada': 'Grenada',
    'Guangdong': 'China',
    'Guangxi': 'China',
    'Guinea': 'Guinea',
    'Guyana': 'Guyana',
    'Hainan': 'China',
    'Heilongjiang': 'China',
    'Henan': 'China',
    'Hispanophone': 'Multiple Countries',  # Spanish-speaking countries
    'Hong Kong': 'China',  # Special Administrative Region of China
    'Hubei': 'China',
    'Hunan': 'China',
    'Hungary': 'Hungary',
    'Iceland': 'Iceland',
    'India': 'India',
    'Indonesia': 'Indonesia',
    'Iran': 'Iran',
    'Iraq': 'Iraq',
    'Ireland': 'Ireland',
    'Israel': 'Israel',
    'Italy': 'Italy',
    'Japan': 'Japan',
    'Jiangsu': 'China',
    'Jiangxi': 'China',
    'Jilin': 'China',
    'Jordan': 'Jordan',
    'Kazakhstan': 'Kazakhstan',
    'Kenya': 'Kenya',
    'Kuwait': 'Kuwait',
    'Kyrgyzstan': 'Kyrgyzstan',
    'Laos': 'Laos',
    'Latvia': 'Latvia',
    'Lebanon': 'Lebanon',
    'Lesotho': 'Lesotho',
    'Liberia': 'Liberia',
    'Lithuania': 'Lithuania',
    'Lusophone': 'Multiple Countries',  # Portuguese-speaking countries
    'MENA': 'Middle East and North Africa',
    'Malawi': 'Malawi',
    'Malaysia': 'Malaysia',
    'Maldives': 'Maldives',
    'Mali': 'Mali',
    'Malta': 'Malta',
    'Mauritania': 'Mauritania',
    'Mauritius': 'Mauritius',
    'Mexico': 'Mexico',
    'Mongolia': 'Mongolia',
    'Montenegro': 'Montenegro',
    'Morocco': 'Morocco',
    'Myanmar': 'Myanmar',
    'Namibia': 'Namibia',
    'Nepal': 'Nepal',
    'Netherlands': 'Netherlands',
    'New Zealand': 'New Zealand',
    'Nigeria': 'Nigeria',
    'North Macedonia': 'North Macedonia',
    'Norway': 'Norway',
    'Pakistan': 'Pakistan',
    'Panama': 'Panama',
    'Papua New Guinea': 'Papua New Guinea',
    'Peru': 'Peru',
    'Philippines': 'Philippines',
    'Poland': 'Poland',
    'Portugal': 'Portugal',
    'Qatar': 'Qatar',
    'Rep. of Congo': 'Republic of the Congo',
    'Romania': 'Romania',
    'Russia': 'Russia',
    'Rwanda': 'Rwanda',
    'Samoa': 'Samoa',
    'Saudi Arabia': 'Saudi Arabia',
    'Senegal': 'Senegal',
    'Serbia': 'Serbia',
    'Shannxi': 'China',
    'Shanxi': 'China',
    'Shandong': 'China',
    'Shanghai': 'China',
    'Shaanxi': 'China',
    'Sichuan': 'China',
    'Sierra Leone': 'Sierra Leone',
    'Singapore': 'Singapore',
    'Slovakia': 'Slovakia',
    'Slovenia': 'Slovenia',
    'Somalia': 'Somalia',
    'South Africa': 'South Africa',
    'South Korea': 'South Korea',
    'South Sudan': 'South Sudan',
    'Spain': 'Spain',
    'Sri Lanka': 'Sri Lanka',
    'Sudan': 'Sudan',
    'Suriname': 'Suriname',
    'Switzerland': 'Switzerland',
    'São Tomé and Príncipe': 'São Tomé and Príncipe',
    'Taiwan': 'Taiwan',
    'Tanzania': 'Tanzania',
    'Thailand': 'Thailand',
    'Tibet': 'China',  # Autonomous region of China
    'Tonga': 'Tonga',
    'Trinidad and Tobago': 'Trinidad and Tobago',
    'Türkiye': 'Turkey',
    'UAE': 'United Arab Emirates',
    'UK': 'United Kingdom',
    'UN': 'United Nations',  # Not a country, but an international organization
    'USA': 'United States of America',
    'Uganda': 'Uganda',
    'Ukraine': 'Ukraine',
    'Uruguay': 'Uruguay',
    'Venezuela': 'Venezuela',
    'Vietnam': 'Vietnam',
    'Xinjiang': 'China',
    'Yemen': 'Yemen',
    'Yunnan': 'China',
    'Zhejiang': 'China',
    'Zimbabwe': 'Zimbabwe',
    'la Francophonie': 'Organisation internationale de la Francophonie',  # Not a country, but an international organization
}

# Function to check if language matches any of the official languages of the region


# Check for language mismatch
def check_mismatch(row):
    region = row['Region of Focus']
    language = row['Language']
    official_languages = region_language_map.get(region, [])
    return language not in official_languages
pd.set_option('display.max_rows', 500)

column = df['Region of Focus']

sorted_unique_values = column.sort_values().drop_duplicates()

def get_country(region):
    """根据地区名获取国家名"""
    return territory_to_country[region]

import pandas as pd
import matplotlib.pyplot as plt

def check_mismatch(row):
    region = row['Region of Focus']
    language = row['Language']
    official_languages = region_language_map.get(region, [])
    return language not in official_languages

# 计算匹配和不匹配的数量
df['Mismatch'] = df.apply(check_mismatch, axis=1)
mismatch_counts = df.groupby('Region of Focus')['Mismatch'].value_counts(normalize=True).unstack()


import matplotlib.pyplot as plt

# 计算不匹配的总数量
total_mismatches = df['Mismatch'].sum()

# 计算数据表格的总行数
total_rows = len(df)

# 准备饼图的数据
sizes = [total_mismatches, total_rows - total_mismatches]
labels = ['Mismatches', 'Matches']

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Language Mismatches')
plt.show()






