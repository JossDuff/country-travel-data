# country-travel-data

Some data and analysis to help me figure out what countries I want to visit.

My main goal is to find countries that are cheap, safe, and high hdi.  The goal of this is to rank countries by the ratio between those.

We first scale each column we're interested in by min max to have them all be within (0,1), then construct a polynomial 

example:
`rank = human_development_index * 1.2 + crime_rate * -0.8 + cost_of_living * -1.5`

And change the factors to represent which columns are more/less important to the rankings.

# data sources
All data is from [https://worldpopulationreview.com/](https://worldpopulationreview.com/)