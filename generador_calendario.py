import pandas as pd
import calendar
import datetime
from collections import defaultdict

# Read data from Excel file
df = pd.read_excel('data.xlsx')  # Replace 'data.xlsx' with your Excel file name

# Map 'HORARIO' to 'day' or 'night'
def map_horario(horario):
    if horario.lower() == 'noche':
        return 'night'
    else:
        return 'day'

df['HORARIO'] = df['HORARIO'].apply(map_horario)

# Ensure 'FECHA' is an integer
df['FECHA'] = df['FECHA'].astype(int)

# Convert the DataFrame to a list of dictionaries
data = df.to_dict(orient='records')

# Get current year
now = datetime.datetime.now()
default_year = now.year

# Get year input from user with validation
while True:
    try:
        year_input = input(f"Enter year (press Enter for current year {default_year}): ").strip()
        if year_input == "":
            year = default_year
        else:
            year = int(year_input)
            if year < 1900 or year > 2100:
                print("Please enter a year between 1900 and 2100")
                continue
        break
    except ValueError:
        print("Please enter a valid year number")

# Ask the user for the month
while True:
    try:
        month = int(input("Please enter the month number (1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print("Please enter a valid month number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 12.")

# Create a calendar
cal = calendar.monthcalendar(year, month)

# Days of the week in Spanish
days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Convert the data to a dictionary with 'FECHA' as key
# Since there may be multiple items on the same date, we store a list of items for each date
data_dict = defaultdict(list)
for item in data:
    data_dict[item['FECHA']].append(item)

# Start of the calendar HTML
html = '<div class="calendar-container">'

# Add days of the week
for day in days:
    html += f'<div class="calendar-item"><div class="cal-header">{day}</div></div>'

# Add days of the month
for week in cal:
    for day in week:
        if day == 0:
            html += '<div class="calendar-item other-month"><div class="number"></div></div>'
        elif day in data_dict:
            # Handle multiple events on the same day
            items = data_dict[day]
            # Determine the color (red if any item is red)
            colors = set(item['Color'] for item in items)
            color_class = 'red' if 'red' in colors else 'yellow'
            # Determine the horarios
            horarios = set(item['HORARIO'] for item in items)
            # Build the HTML
            html += f'<div class="calendar-item {color_class} tooltip">'
            html += f'<div class="number">{day}</div>'
            if 'day' in horarios:
                html += '<div class="day"></div>'
            if 'night' in horarios:
                html += '<div class="night"></div>'
            # Concatenate 'DELITO's for tooltip
            delitos = ', '.join(item['DELITO'] for item in items)
            html += f'<span class="tooltiptext">{delitos}</span>'
            html += '</div>'
        else:
            html += f'<div class="calendar-item current-month"><div class="number">{day}</div></div>'

# End of the calendar HTML
html += '</div>'

print(html + "\n")

# Start of the table HTML
html = '<table><thead><tr><th style="background-color: black; color: white;">Fecha</th><th style="background-color: black; color: white;">Delito</th><th style="background-color: black; color: white;">Horario más habitual</th></tr></thead><tbody>'

# Add rows to the table
for item in data:
    html += '<tr>'
    html += f'<td>{item["FECHA"]}</td>'
    html += f'<td class="{item["Color"]}" style="color: white;">{item["DELITO"]}</td>'
    html += f'<td>{"Día" if item["HORARIO"] == "day" else "Noche"}</td>'
    html += '</tr>'

# End of the table HTML
html += '</tbody></table>'

print(html)
