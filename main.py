import pandas as pd
import plotly.express as px
from functools import reduce

cost_of_living_file = 'data/cost-of-living-by-country-2024.csv'
crime_rate_file = 'data/crime-rate-by-country-2024.csv'
human_development_index_file = 'data/human-development-index-by-country-2024.csv'
education_index_file = 'data/education-index-by-country-2024.csv'
freedom_index_file = 'data/freedom-index-by-country-2024.csv'
happiest_countries_in_the_world_file = 'data/happiest-countries-in-the-world-2024.csv'
internet_speeds_file = 'data/internet-speeds-by-country-2024.csv'
most_conservative_countries_file = 'data/most-conservative-countries-2024.csv'
social_progress_index_file = 'data/social-progress-index-by-country-2024.csv'


cost_of_living_df = pd.read_csv(cost_of_living_file)
crime_rate_df = pd.read_csv(crime_rate_file)
hdi_df = pd.read_csv(human_development_index_file)
education_df = pd.read_csv(education_index_file)
freedom_df = pd.read_csv(freedom_index_file)
happiness_df = pd.read_csv(happiest_countries_in_the_world_file)
internet_df = pd.read_csv(internet_speeds_file)
conservative_df = pd.read_csv(most_conservative_countries_file)
social_progress_df = pd.read_csv(social_progress_index_file)

# negative number means it should negatively impact total score
# heigher the number the more important it is

# readable df name, df, column of interest, factor
dataframes = [
    ("cost_of_living", cost_of_living_df, "costOfLivingLC" , -1.3),
    ("crime_rate", crime_rate_df, "crimeRateByCountry_crimeIndex", -0.8),
    ("hdi", hdi_df, "Hdi2021", 0.8),
    ("education", education_df, "EducationalIndex2021", 0.5),
    ("freedom", freedom_df, "freedomIndexByCountry_humanFreedom2023", 1.1),
    ("hapiness", happiness_df, "HappiestCountriesWorldHappinessReportRankings2024", 1.3),
    ("internet", internet_df, "InternetSpeedsFixedBroadbandDownloadSpeed", 0.4),
    ("conservative", conservative_df, "MostConservativeRank2023", -0.7),
    ("social_progress", social_progress_df, "SocialProgressIndexScore2022", 1.4)
]

# Initialize variables to track the highest and lowest num_countries
highest = {"name": None, "num_countries": 0}
lowest = {"name": None, "num_countries": float('inf')}

for name, df, descriptor, _ in dataframes:
    num_countries = df.shape[0]
    
    # Update highest and lowest if necessary
    if num_countries > highest['num_countries']:
        highest = {"name": name, "num_countries": num_countries}
    if num_countries < lowest['num_countries']:
        lowest = {"name": name, "num_countries": num_countries}

# Print the results
print(f"Highest num_countries: {highest['num_countries']} in {highest['name']} dataframe")
print(f"Lowest num_countries: {lowest['num_countries']} in {lowest['name']} dataframe\n")

dataframes_list = [df for _, df, _, _ in dataframes]
merged_df = reduce(lambda left, right: pd.merge(left, right, on='country', how='inner'), dataframes_list)


# merged_df = merged_df.dropna(subset=['costOfLivingLC'])
# merged_df = merged_df.dropna(subset=['crimeRateByCountry_crimeIndex'])
# merged_df = merged_df.dropna(subset=['Hdi2021'])

col_factor = 1.3
hdi_factor = 1.2
cr_factor = 0.9

for readable_name, _, col_name, col_factor in dataframes:
    # min max scaling to get values into (0,1)*col_factor
    min_value = merged_df[col_name].min()
    max_value = merged_df[col_name].max()
    merged_df[readable_name] = ((merged_df[col_name] - min_value) / (max_value - min_value)) * col_factor

# create total score column
merged_df['total_score'] = 0
for column_name, _, _, _ in dataframes:
    # Apply the weight, fill NaN values with 0, and add to the total_score column
    merged_df['total_score'] += merged_df[column_name].fillna(0)

sorted_df = merged_df.sort_values(by='total_score', ascending=False)

top_10_countries = sorted_df.head(20)
bottom_10_countries = sorted_df.tail(10)

print("weights for each data point:")
print("(negative means it negatively impacts total_score)")
for col_name, _, _, factor in dataframes:
    print(f"    {col_name}: {factor}")

print("\ntop 20:")
print(top_10_countries[['country', 'total_score']].to_string(index=False))

print("\nbottom 10:")
print(bottom_10_countries[['country', 'total_score']].to_string(index=False))

# fig = px.choropleth(merged_df,
#                     locations='country',  # This column should contain the countries' names or ISO codes
#                     locationmode='country names',  # Or 'ISO-3' if using ISO codes
#                     color='total_score',  # This column will color the countries
#                     color_continuous_scale=px.colors.sequential.Plasma,  # You can choose any color scale
#                     title='World Map Colored by Total Score')

# fig.show()
