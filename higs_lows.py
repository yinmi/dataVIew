import csv

fileName="sitka_weather_07-2014.csv"
with open(fileName) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    hight=[]
    for row in reader:
        hight.append(row[1])
    print(hight)