import csv

"Ez a program kiírja az űrhajósok születési dátumát"


def main():
    months = []

    with open('astronauts.csv', 'r') as file:
        csv_reader = csv.reader(file)

        next(csv_reader)

        for line in csv_reader:
            months.append(f"{line[4]}")

    for month in months:
        print(month)


main()




