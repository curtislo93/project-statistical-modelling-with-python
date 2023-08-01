# Final-Project-Statistical-Modelling-with-Python

## Project/Goals
My goal is to use the CityBikes, Foursquare and Yelp APIs to return information on the closest bubble tea shops for each bike station.
Let us enjoy a nice cold drink after a bike ride!

## Process
##### 1. CityBikes API
Using the CityBikes API, a database of bike stations was established for the city of Vancouver.

##### 2. Foursquare/Yelp APIs
These APIs provided information on the bubble tea shops closest to the various bike stations.

##### 3. Joining Data
"Are bubble tea shops better in a specific area of the city?"

Yelp Limitations - limited API calls

##### 4. Building Model
Multivariate Linear Regression with scatterplot to visualize. Lighter colored dots meant better results - darker is worse.

##### 5. Final Thoughts

## Results
The P-values received were not smaller than 0.05, it signifies that Longitude and Latitude have little to no significance in determination of good yelp rated Bubble Tea Shops in Vancouver. This is completely understandable as quantitative data might not be a great way to create a model for qualitative data, such as taste (preference), quality of materials/ingredients, customer experience with service, customer behaviour, etc... These bubble tea shops could very much be established in a specific area and quality might increase (thus increasing ratings) due to more competition. For example, in Vancouver, Robson Street is a well known retail street. These shops might want their own 'market share' and compete with others to have the best bubble tea shop on the street. However, there is not a lot of correlation between location and the shops' ratings.

## Challenges 
The main challenges included limited API calls (Yelp) and the overall structure of how the code needed to be set up. Due to the lack of API calls remaining via Yelp, I created a model using random data in order to fulfill the requirements of this project. However, the structure and analysis of the hypothesis would be similar, only the results may be more favourable or unfavourable.

## Future Goals
If I had more time, I'd try to break it down by district and compare results between residential and retail locations or neighbourhoods. Analysing the frequency of riders at each bike station would be helpful as well to chart out the potential foot traffic that specific region/station is receiving in comparison to others. The likelihood of someone visiting these bubble tea stores might inherently be higher as there is more foot traffic.
