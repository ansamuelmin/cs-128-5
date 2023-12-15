# Real Data Information Retrieval
**Westmont College Fall 2023**

**CS 128 Information Retrieval and Big Data**

## [Presentation Link](https://docs.google.com/presentation/d/1erT-hamAlMktCLs4XP8RrxOa5tyH1ziZqTlAUIASJlM/edit#slide=id.p)

## Author Information
* **Name(s)**: Samuel An, Andy Chung 
* **Email(s)**: san@westmont.edu, anchung@westmont.edu

## Overview

* Using the DataReader class, This code analyzes air quality data, focusing on PM2.5 levels. It reads data from a CSV file, filters and plots relevant information for a specified city, and calculates the average PM2.5 level for the years 1999 through 2022.

## Project Structure

**'data' Directory**
(Contains the dataset used for air quality analysis)
* 'Air_Quality_Changes_in_The_US.csv': CSV file containing air quality data.

**'src' Directory**
(Source code for air quality analysis)
* 'analysis_models.py': Defines the DataReader class with methods for reading data, plotting air quality data, and implementing data analysis models.
* 'analysis_runner.py': Runs air quality analysis by taking user input for the city and plotting PM2.5 levels.


## Software Utilization

1. **Install Dependencies:**
    * Ensure that you have the necessary dependencies installed:
       * *pip install pandas matplotlib numpy*
   
2. **Run the Code:**
    * Execute the code by running the analysis_runner.py file.

3. **Provide a Query:**
    * The query must be a specific city name in the United States.


## Citations
***This system was developed with the assistance of ChatGPT through a series of the following queries after providing an initially written code:***

* Please edit the following code so that I can create a method that reads through a specific csv file: <br/>
  * *import pandas as pd <br/>*
  
    *def read_file(self): <br/>*
    &ensp; *data = pd.read_csv("Air_Quality_Changes_in_The_US.csv")* <br/>
    &ensp; *print(data) <br/>*

* How do I edit this code so that it outputs all the columns in the data file?

* How would I show the data for columns labeled: Core Based Statistical Area and Pollutant? 

* Edit the code so that it takes an input for a city asking the user "Please provide a city: ". If the inputted city is not contained within the column 'Core Based Statistical Area', please return a statement saying "There is no data for air quality in this region".  If the inputted city is contained within the column, please return a graph with the title "PM2.5 Levels in (the inputted city)" with the x value being the years from 1999-2022, and the y value being the numbers contained in the columns from 1999-2022. In the legend for the graph, please include the rows present in the column "Pollutant" with the value "PM2.5" for the specific city that the data is outputting.

* Have the code take the inputted city, look at the value of the "CBSA" column for this city, look for all of the rows that share this same "CBSA" value, look for the rows that have "PM2.5" in the "Pollutant" column, and have the legend of the graph return the levels of PM2.5

* In the "Core Based Statistical Area" column, there is a value of Bakersfield, CA. I want the code to be able to run even if the user simply inputs Bakersfield instead of Bakersfield, CA.

* I want the title of the graph to show the case-sensitive value of the corresponding value in the "Core Based Statistical Area" column, replacing any "-" with a "," instead. 

* Take the average of all of the values under the years '1999' through '2022' from the PM2.5 rows that have the value "Weighted Annual Mean" for the 'Trend Statistic' column? Then label this average as PM2.5 Average Weighted Annual Mean Level.

    
