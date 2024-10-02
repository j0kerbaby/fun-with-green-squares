# 29.09.2024 - niedziela obecna
# oct 8 2023 - od tego zaczynamy - niedziele
import os


dates = {
    "oct": ["16","17","18","19","20","27"],
    "nov": ["03","10","20","21","22","23","24","27"],
    "dec": ["01","04","08","11","15","18","19","20","21","22"],
    "jan": ["08","09","10","11","12","19","26"],
    "feb": ["02"]
}

combined_list_of_dates = []

for key in dates:
    one_month_combined = []
    if key == 'oct':
        translated_month = '10'
        year = 2023
    if key == 'nov':
        translated_month = '11'
        year = 2023
    if key == 'dec':
        translated_month = '12'
        year = 2023
    if key == 'jan':
        translated_month = '01'
        year = 2024
    if key == 'feb':
        translated_month = '02'
        year = 2024

    for date in dates[key]:
        combined_list_of_dates.append(f"2024-{translated_month}-{date}")

for index, element in enumerate(combined_list_of_dates):
    with open("file", "w") as file:
        file.write(f"{index}...")
    os.system("git add .")
    command = f"git commit --date \"{element}\" -m \"index: {index}\""
    # print(f"command: {command}")
    os.system(command)

    # print(element)

