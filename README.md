# country-travel-data

Some data and analysis to help me figure out what countries I want to visit.

My main goal is to find countries that are cheap, safe, and high hdi.  The goal of this is to rank countries by the ratio between those.

We first scale each column we're interested in by min max to have them all be within (0,1), then construct a polynomial 

`rank = hdi * hdi_factor - crime_rate * crime_rate_factor - cost_of_living * cost_of_living_factor`

And change the factors to represent which columns are more/less important to the rankings.

# data sources
- `cost-of-living-by-country-2024.csv` [https://worldpopulationreview.com/country-rankings/cost-of-living-by-country](https://worldpopulationreview.com/country-rankings/cost-of-living-by-country)
- `crime-rate-by-country-2024.csv` [https://worldpopulationreview.com/country-rankings/crime-rate-by-country](https://worldpopulationreview.com/country-rankings/crime-rate-by-country)
- `most-visited-countries-2024.csv` [https://worldpopulationreview.com/country-rankings/most-visited-countries](https://worldpopulationreview.com/country-rankings/most-visited-countries)
    - data for each country isn't guarenteed to be the same year, this is also pre-covid data
    - most visited countries data isn't included for now, because the data isn't representative of what I was hoping for
- `human_development-index-by-country-2024` [https://worldpopulationreview.com/country-rankings/hdi-by-country](https://worldpopulationreview.com/country-rankings/hdi-by-country)
    - This is actually hdi for 2021