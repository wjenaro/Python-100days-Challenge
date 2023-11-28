import csv

try:
    with open('weather_data.csv') as myfile:
        mydata = csv.reader(myfile)
        temperature = []  # Temperature data will be in the form of integers

        for row in mydata:
            if row[1] != 'temp':  # Assuming temperature is in the second column
                temperature.append(int(row[1]))

        print(temperature)

except FileNotFoundError:
    print("The file 'weather_data.csv' was not found.")
except IndexError:
    print("Index error: Check if the CSV file has the expected structure.")
except ValueError:
    print("Value error: Check if the temperature data is a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")
