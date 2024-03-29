import pandas as pd

cost_of_living_file = 'data/cost-of-living-by-country-2024.csv'
crime_rate_file = 'data/crime-rate-by-country-2024.csv'
most_visited_file = 'data/most-visited-countries-2024.csv'
human_development_index_file = 'data/human-development-index-by-country-2024.csv'

cost_of_living_df = pd.read_csv(cost_of_living_file)
crime_rate_df = pd.read_csv(crime_rate_file)
most_visited_df = pd.read_csv(most_visited_file)
hdi_df = pd.read_csv(human_development_index_file)

dataframes = {
    "cost_of_living": cost_of_living_df,
    "crime_rate": crime_rate_df,
    "most_visited": most_visited_df,
    "hdi": hdi_df
}

for name, df in dataframes.items():
    print(f"{name} data:")
    print("columns:", df.columns.tolist())
    print("num countries:", df.shape[0], "\n")
