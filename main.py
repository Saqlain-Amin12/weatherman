import os
import sys
from colorama import Fore


def weatherman():
    folder_path = "lahore_weather"
    command = sys.argv[1]
    year = sys.argv[2]
    file_pattern = f"lahore_weather_{year}"
    if len(sys.argv) < 3 or sys.argv[1] not in ("-a", "-b", "-c", "-d"):
        print("Usage: python main.py -a <year>")
        print("Usage: python main.py <-b|-c|-d> <year/month>")
        sys.exit(1)

    if sys.argv[1] == "-a":
        if len(sys.argv) != 3:
            print("Usage: python main.py -a <year>")
            sys.exit(1)
        year = sys.argv[2]
        print("Year:", year)
    else:
        if sys.argv[1] in ("-b", "-c", "-d"):
            try:
                year, month = sys.argv[2].split("/")
                file_pattern = f"lahore_weather_{year}_{month}"
                # print("Year:", year, "Month:", month)
            except ValueError:
                print("Usage: python main.py <-b|-c|-d> <year/month>")
                sys.exit(1)
            

    if command == "-a":

        overall_max_temp = -999
        overall_min_temp = 100
        date_of_max_temp = ""
        date_of_min_temp = ""
        overall_max_humidity = -99
        date_of_min_humidity = ""

        for filename in os.listdir(folder_path):
            if filename.startswith(file_pattern) and filename.endswith(".txt"):
                filepath = os.path.join(folder_path, filename)

                with open(filepath, 'r') as f:
                    lines = f.readlines()

                for line in lines:
                    try:
                        parts = line.split(",")
                        temp = int(parts[1].strip())
                        date = parts[0].strip()
                        temp_minimum = int(parts[3].strip())
                        max_humidity = int(parts[7].strip())

                        if temp > overall_max_temp:
                            overall_max_temp = temp
                            date_of_max_temp = date

                        if overall_min_temp > temp_minimum:
                            overall_min_temp = temp_minimum
                            date_of_min_temp = date

                        if max_humidity > overall_max_humidity:
                            overall_max_humidity = max_humidity
                            date_of_min_humidity = date

                    except (ValueError, IndexError):

                        continue

        print(
            f"Highest  Tempreature: {overall_max_temp}°C on {date_of_max_temp}")
        print(
            f"Lowest  Tempreature: {overall_min_temp}°C on {date_of_min_temp}")
        print(
            f"Highest Humidity : {overall_max_humidity} on {date_of_min_humidity}")

    elif (command == "-b"):

        overall_avg_heighest_temp = -999
        overall_avg_lowest_temp = 100
        overall_avg_humidity = -99

        for filename in os.listdir(folder_path):
            if filename.startswith(file_pattern) and filename.endswith(".txt"):
                filepath = os.path.join(folder_path, filename)

                with open(filepath, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        try:
                            parts = line.split(",")
                            temp_mean_max = int(parts[2].strip())
                            mean_humidity = int(parts[8].strip())

                            if temp_mean_max > overall_avg_heighest_temp:
                                overall_avg_heighest_temp = temp_mean_max

                            if temp_mean_max < overall_avg_lowest_temp:
                                overall_avg_lowest_temp = temp_mean_max

                            if mean_humidity > overall_avg_humidity:
                                overall_avg_humidity = mean_humidity

                        except (ValueError, IndexError):
                            continue

        print(f"Average Highest Temp: {overall_avg_heighest_temp}°C  ")
        print(f"Average Lowest Temp: {overall_avg_lowest_temp}°C ")
        print(f"Average Humidity: {overall_avg_humidity} ")

    elif (command == "-c"):

        for filename in os.listdir(folder_path):
            if filename.startswith(file_pattern) and filename.endswith(".txt"):
                filepath = os.path.join(folder_path, filename)

                with open(filepath, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        try:
                            parts = line.strip().split(",")
                            date = parts[0].split("-")[2]
                            temp_high = int(parts[1].strip())
                            temp_low = int(parts[3].strip())

                            print(
                                Fore.BLACK +
                                f"{date} " +
                                Fore.RED +
                                "+" *
                                temp_high +
                                f" {temp_high}C")

                            print(
                                Fore.BLACK +
                                f"{date} " +
                                Fore.BLUE +
                                "+" *
                                temp_low +
                                f" {temp_low}C")

                        except (ValueError, IndexError):
                            continue

    elif (command == "-d"):

        for filename in os.listdir(folder_path):
            if filename.startswith(file_pattern) and filename.endswith(".txt"):
                filepath = os.path.join(folder_path, filename)
                with open(filepath, 'r') as f:

                    lines = f.readlines()

                    for line in lines:
                        try:
                            parts = line.split(",")
                            date = parts[0].split("-")[2]
                            temp_high_max = int(parts[1].strip())
                            temp_low_min = int(parts[3].strip())

                            print(
                                Fore.BLACK + f"{date} " +
                                Fore.RED + "+" * temp_high_max +
                                Fore.BLUE + "+" * temp_low_min + Fore.BLACK +
                                f" {temp_high_max}C {temp_low_min}C"
                            )

                        except (ValueError, IndexError):
                            continue

    else:
        print("Invalid command. Please enter a valid command.")


if __name__ == "__main__":

    weatherman()
