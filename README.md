# Bubble Tea Shops - Statistical Modelling with Python

## Project/Goals
Are bubble tea shops better in certain areas of the city? This project will use the CityBikes, Foursquare and Yelp APIs to return information on the closest bubble tea shops for each bike station, with ratings provided. 

## Process
##### 1. CityBikes API
Using the CityBikes API, a database of bike stations was established for the city of Vancouver.
After establishing the dataframe, a csv was exported to reduce amount of code required.

##### 2. Foursquare/Yelp APIs
These APIs provided information on the bubble tea shops closest to the various bike stations.
After establishing the dataframes, a csv was exported for each the Foursquare results and the Yelp results.

##### 3. Joining Data
Using the previously exported csv files, I merged all three dataframes together with a full outer join in order to set up to clean.
Cleaning the data included removing all NaN values, any duplicates (based on shop name and coordinates) and then using the cleaned data to plot a scatterplot.
Using the scatterplot, interpretations can then be visualized and summarized.

##### 4. Building Model
I used the cleaned data to run the OLS Regression to see if the data provided was correlated (x and y variables). Lastly, I transformed the model into a classification model by casting anything above rating 4 as "high rating" (given value 1) and anything below that as "low rating" (given value 0). 

## Results
The P-values received were not smaller than 0.05, so it signifies that Longitude and Latitude have little to no significance in determination of good yelp rated Bubble Tea Shops in Vancouver. Using the other tests, we can summarize the following:

- Omnibus test/prob(Omnibus): the data does not follow a normal distribution. This makes sense as the data is clustered towards downtown Vancouver.
- Durbin-Watson (value between 0 and 4): a value close to 2 signified no strong evidence of autocorrelation.
- Jarque-Bera/prob(JB): prob(JB) < 0.05 means that the data is not normally distributed.
- Skew: it is negatively skewed.
- Kurtosis: the value of 5.603 means that the Kurtosis is 'heavy-tailed' - explains the density factor of the shops (downtown Vancouver).
- Cond. No: The high number indicated multicollinearity, meaning independent variables are correlated. Simply visualizing the data, shops are irregularly scattered as it keeps to commercial areas vs residential areas.

The classification model was better at describing the trend of the data, with P-values < 0.05. My interpretation is that since there are more bubble tea shops in one area (downtown Vancouver), the quality of their products could be higher due to higher competition. In order to garner more revenue and have more satisfied customers (as per rating), the quality control must be better, otherwise the stores might lose business to their competitor down the street.

## Challenges 
The main challenges included limited API calls (Yelp) and the overall structure of how the code needed to be set up.
Implementing everything into a database was confusing and difficult. Originally, I had written code over and over again to run. This took too much time to run and was taxing on my system and API calls. After review, it was recommended to export the dataframes into a .csv file for future reference.

## Future Goals
If I had more time, I'd try to break it down by district and compare results between residential and retail locations or neighbourhoods. Analysing the frequency of riders at each bike station would be helpful as well to chart out the potential foot traffic that specific region/station is receiving in comparison to others. The likelihood of someone visiting these bubble tea stores might inherently be higher as there is more foot traffic. If there was more data, pulling the sales information might be helpful too to see which store is more popular, but not necessarily the one with the highest rating.
