
# Analysing the Relationship Between the Weather and TFL

I set out on this project, to determine how changes in different aspects of the weather affects the usages of services provided by Transport for London.

The dataset used in this project was obtained from public sources and contained weather data and transportation usage statistics over several years. The key features included:

**Weather Features**: cloud cover (oktas), sunshine (hours), global radiation (W/m2), max temperature (°C), mean temperature (°C), min temperature (°C), precipitation (mm), pressure (Pascals), snow depth (cm)

**Target Variables**: Bus journeys, Underground journeys, DLR Journeys, Tram Journeys, Overground Journeys, Emirates Airline Journeys, TfL Rail Journeys

I made use of Excel to carry out the merging of the weather dataset and the TFL dataset which contained the metrics of the average use for each of the transportation services that they offered to the public.

This is what the weather dataset looked like initially:


This is what the TFL dataset looked like initially:



The weather dataset had daily readings while the TFL dataset had monthly readings with time periods specified. So, I wrote the following algorithm so that the weather readings within the time period specified by the TFL dataset would get averaged and summarised into one row of data.

This was the final preprocessed and clean Excel spreadsheet:


After this I commenced feature engineering by creating one new feature that summed up all the usages of every single TFL service into one column called 'Total Ridership'. I also then proceeded to apply a scaler to all of my input features (weather) to make sure every value has an **equal** contribution to the final prediction. I made use of Ridge Regression with a lambda value of 1 as it offered the best performance out of Lasso regularisation, cross-validation and random forest regressor models by a marginal amount.


Most of the errors are sort of concentrated between **0 and 50** and the model has produced an error of only **10.68%**, implying that predictions were, on average, within 10.68% of actual values. This level of accuracy demonstrates the model's reliability and potential for practical application in optimising public transport resources.

In other words we could say that this model is around **90% accurate** in predicting the demand for TFL services based on weather conditions.

To make the model accessible, I developed and deployed a Flask API, allowing users to input weather conditions and receive ridership predictions. This API was containerized using Docker to ensure consistent and scalable deployment.



