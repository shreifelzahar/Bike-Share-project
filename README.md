# Bike-Share-project

## Project Overview

Over the past decade, bicycle-sharing systems have become increasingly popular in cities worldwide. These systems allow users to rent bicycles for short-term use, facilitating travel between points A and B or simply providing a means to enjoy a ride. Each bicycle can serve multiple users in a single day, enhancing urban mobility and promoting eco-friendly transportation.

This project aims to analyze bike share usage patterns in three major U.S. cities: Chicago, New York City, and Washington, DC. By leveraging data provided by Motivate, a prominent bike share system provider, we uncover insights into how these systems are utilized, focusing on usage trends, popular stations, trip durations, and user demographics.

## Datasets

The datasets include randomly selected data for the first six months of 2017 from the three cities. Each dataset contains six core columns:
- **Start Time** (e.g., 2017-01-01 00:07:57)
- **End Time** (e.g., 2017-01-01 00:20:53)
- **Trip Duration** (in seconds - e.g., 776)
- **Start Station** (e.g., Broadway & Barry Ave)
- **End Station** (e.g., Sedgwick St & North Ave)
- **User Type** (Subscriber or Customer)

Additionally, the Chicago and New York City datasets include:
- **Gender**
- **Birth Year**

## Statistics Computed

In this project, the following descriptive statistics are computed to provide insights into bike share usage:

1. **Popular times of travel**:
    - Most common month
    - Most common day of the week
    - Most common hour of the day

2. **Popular stations and trip**:
    - Most common start station
    - Most common end station
    - Most common trip from start to end

3. **Trip duration**:
    - Total travel time
    - Average travel time

4. **User info**:
    - Counts of each user type
    - Counts of each gender (available for NYC and Chicago)
    - Earliest, most recent, and most common year of birth (available for NYC and Chicago)

## Files

The project includes the following files:
- `bikeshare.py`: The main Python script where the analysis is performed.
- `chicago.csv`: Dataset for Chicago.
- `new_york_city.csv`: Dataset for New York City.
- `washington.csv`: Dataset for Washington, DC.

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have Python installed (version 3.6 or later recommended).
3. Run `bikeshare.py` to execute the analysis. You will be prompted to choose a city and specify filters for the data analysis.

## Learning Outcomes

By working on this project, you will enhance your skills in:
- Data cleaning and wrangling
- Exploratory data analysis
- Descriptive statistics computation
- Python programming with libraries such as pandas and numpy

## Future Work

In future iterations, additional analyses could include:
- Visualization of usage patterns
- Comparative analysis over different years
- Incorporating weather data to study its impact on bike share usage

## Acknowledgments

This project is part of the Data Analyst Nanodegree program offered by Udacity. The dataset is provided by Motivate, a bike share system provider for many major cities in the United States.
