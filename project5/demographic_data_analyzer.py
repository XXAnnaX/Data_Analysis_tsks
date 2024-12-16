import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    # df = None
    df = pd.read_csv("adult.data.csv", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ])
    df['age'] = pd.to_numeric(df['age'], errors='coerce') 
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce')
    # race_count = None
    valid_races = ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
    df = df[df['race'].isin(valid_races)]
    race_count = df['race'].dropna().value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].dropna().mean(), 1)

    # Percentage with Bachelors degrees
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Higher and lower education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # Minimum number of hours a person works per week
    min_work_hours = int(df['hours-per-week'].dropna().min())

    # Percentage of rich among those who work minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    if len(num_min_workers) > 0:
        rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)
    else:
        rich_percentage = 0

    # Country with highest percentage of people earning >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country_percentage = round((country_salary / country_total * 100).max(), 1)
    highest_earning_country = (country_salary / country_total * 100).idxmax()

    # Most popular occupation for those earning >50K in India
    india_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_IN_occupation = india_occupations.value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


# Number of each race:
#  White                 27816
# Black                  3124
# Asian-Pac-Islander     1039
# Amer-Indian-Eskimo      311
# Other                   271
# Name: race, dtype: int64
# Average age of men: 39.4
# Percentage with Bachelors degrees: 16.4%
# Percentage with higher education that earn >50K: 46.5%
# Percentage without higher education that earn >50K: 17.4%
# Min work time: 1 hours/week
# Percentage of rich among those who work fewest hours: 10.0%
# Country with highest percentage of rich: Iran
# Highest percentage of rich people in country: 41.9%
# Top occupations in India: Prof-specialty