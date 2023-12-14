import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataReader:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def read_file(self):
        data = pd.read_csv(self.csv_file_path)
        return data

    def plot_air_quality_data(self, city):
        data = self.read_file()

        # Convert both city names to lowercase for case-insensitive comparison
        lowercased_city = city.lower()

        # Check if the user input is a substring of any entry in the "Core Based Statistical Area" column
        matching_entries = data[data["Core Based Statistical Area"].str.lower().str.contains(lowercased_city, na=False)]

        if matching_entries.empty:
            print("There is no data for air quality in this region.")
            return

        # Extract CBSA value for the first matching entry
        cbsa_value = matching_entries["CBSA"].iloc[0]

        # Filter rows based on the CBSA value, "PM2.5" pollutant, and 'Trend Statistic' column
        filtered_data = data[(data["CBSA"] == cbsa_value) & (data["Pollutant"] == "PM2.5") & (data["Trend Statistic"] == "Weighted Annual Mean")]

        if filtered_data.empty:
            print(f"No data found for '{city}' with 'PM2.5' pollutant and 'Weighted Annual Mean' trend statistic.")
            return

        # Retrieve columns for the years dynamically
        year_columns = [str(year) for year in data.columns if year.isdigit()]

        # Check if there are matching entries with the specified city name
        if not matching_entries.empty:
            # Replace "-" with "," in the case-sensitive city name
            title_city = matching_entries["Core Based Statistical Area"].iloc[0].replace("-", ",")

            # Plotting
            plt.figure(figsize=(10, 6))
            plt.title(f"PM2.5 Levels in {title_city}")
            plt.xlabel("Year")
            plt.ylabel("PM2.5 Levels")

            # Iterate over rows and create a line for each year
            for index, row in filtered_data.iterrows():
                label = f"{city} - {row['Pollutant']} - {row['Trend Statistic']}"
                plt.plot(year_columns, row[year_columns], label=label)

            # Calculate the average of values under the years '1999' through '2022'
            selected_years = [str(year) for year in range(1999, 2023)]
            average_values = np.nanmean(filtered_data[selected_years].values)

            # Display the average on the graph with the new label
            plt.text(0.95, 0.05, f"Average PM2.5 Level (1999-2022): {average_values:.2f}",
                     transform=plt.gca().transAxes, color='red', ha='right', va='bottom')

            # Display legend
            plt.legend()

            # Rotate x-axis labels for better readability
            plt.xticks(rotation=45, ha='right')

            plt.show()
