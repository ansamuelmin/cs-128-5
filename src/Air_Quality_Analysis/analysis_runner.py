# Example usage:
from src.Air_Quality_Analysis.analysis_models import DataReader

csv_file_path = "~/Desktop/CS-128/cs-with-mike/cs-128-5/data/Air_Quality_Changes_in_The_US.csv"
data_reader = DataReader(csv_file_path)

# Take user input for the city
user_input_city = input("Please provide a city: ")

# Plot PM2.5 levels for the specified city (handling variations in formatting)
data_reader.plot_air_quality_data(user_input_city)
