import pandas as pd

cost_of_living_file = 'data/cost-of-living-by-country-2024.csv'
crime_rate_file = 'data/crime-rate-by-country-2024.csv'
# most_visited_file = 'data/most-visited-countries-2024.csv'
human_development_index_file = 'data/human-development-index-by-country-2024.csv'

cost_of_living_df = pd.read_csv(cost_of_living_file)
crime_rate_df = pd.read_csv(crime_rate_file)
# most_visited_df = pd.read_csv(most_visited_file)
hdi_df = pd.read_csv(human_development_index_file)

dataframes = {
    "cost_of_living": cost_of_living_df,
    "crime_rate": crime_rate_df,
    # "most_visited": most_visited_df,
    "hdi": hdi_df
}

# for name, df in dataframes.items():
#     print(f"{name} data:")
#     print("columns:", df.columns.tolist())
#     print("num countries:", df.shape[0], "\n")
#     print(df.head())

# print(cost_of_living_df)


first_merged_df = pd.merge(hdi_df, cost_of_living_df, on='country', how='inner')
merged_df = pd.merge(first_merged_df, crime_rate_df, on='country', how='inner')
cleaned_df = merged_df.dropna(subset=['costOfLivingLC'])
cleaned_df = merged_df.dropna(subset=['crimeRateByCountry_crimeIndex'])
cleaned_df = merged_df.dropna(subset=['Hdi2021'])

# min max scaling to get values into (0,1)
for col_name, scaled_col_name in (('costOfLivingLC', 'cost_of_living_scaled'), ('Hdi2021', 'hdi_scaled'), ('crimeRateByCountry_crimeIndex', 'crime_rate_scaled')):
    min_value = cleaned_df[col_name].min()
    max_value = cleaned_df[col_name].max()
    cleaned_df[scaled_col_name] = (cleaned_df[col_name] - min_value) / (max_value - min_value)

col_factor = 1.4
hdi_factor = 0.6
cr_factor = 1

# merged_df['hdi_cost_ratio'] = merged_df['Hdi2021'] / merged_df['costOfLivingLC']
# merged_df['hdi_crime_rate_ratio'] = merged_df['Hdi2021'] / merged_df['crimeRateByCountry_crimeIndex']
cleaned_df['joss_ratio'] = cleaned_df['hdi_scaled'] * hdi_factor - cleaned_df['crime_rate_scaled'] * cr_factor  - cleaned_df['cost_of_living_scaled'] * col_factor
cleaned_df = cleaned_df.dropna(subset=['joss_ratio'])
sorted_df = cleaned_df.sort_values(by='joss_ratio', ascending=False)

top_10_countries = sorted_df.head(20)
bottom_10_countries = sorted_df.tail(10)

print("top 10:")
print(top_10_countries[['country', 'joss_ratio', 'cost_of_living_scaled', 'hdi_scaled', 'crime_rate_scaled']])

print("\nbottom 10:")
print(bottom_10_countries[['country', 'joss_ratio', 'cost_of_living_scaled', 'hdi_scaled', 'crime_rate_scaled']])
