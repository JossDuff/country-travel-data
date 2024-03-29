import pandas as pd

cost_of_living_file = 'cost-of-living-by-country-2024.csv'
crime_rate_file = 'crime-rate-by-country-2024.csv'
murder_rate_file = 'murder-rate-by-country-2024.csv'


col_df = pd.read_csv(cost_of_living_file)



# Display the first few rows of the DataFrame
print(col_df.head())