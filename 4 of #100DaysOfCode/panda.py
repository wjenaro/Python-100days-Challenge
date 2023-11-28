import pandas as pd

try:
    # Data
    data = pd.read_csv('weather_data.csv')

    # Print the data
    print(data['temp'])

except FileNotFoundError:
    print("The file 'weather_data.csv' was not found.")
except pd.errors.EmptyDataError:
    print("The file 'weather_data.csv' is empty.")
except pd.errors.ParserError:
    print("Error parsing 'weather_data.csv'. Check if the file has the correct format.")
except Exception as e:
    print(f"An error occurred: {e}")
