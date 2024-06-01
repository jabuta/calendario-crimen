import calendar
import datetime

# Get current year and month
now = datetime.datetime.now()
year = now.year
month = 6

# Create a calendar
cal = calendar.monthcalendar(year, month)

# Days of the week in Spanish
days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Your data
data = [
    {'FECHA': 1, 'DELITO': 'Hurto personas', 'HORARIO': 'night', 'Color': 'yellow'},
    {'FECHA': 5, 'DELITO': 'Delitos Sexuales', 'HORARIO': 'Dia', 'Color': 'red'},
    {'FECHA': 6, 'DELITO': 'Delitos Informáticos', 'HORARIO': 'day', 'Color': 'yellow'},
    {'FECHA': 8, 'DELITO': 'Feminicidios', 'HORARIO': 'night', 'Color': 'red'},
    {'FECHA': 9, 'DELITO': 'Homicidios', 'HORARIO': 'night', 'Color': 'red'},
    {'FECHA': 13, 'DELITO': 'Hurto a Residencias', 'HORARIO': 'day', 'Color': 'yellow'},
    {'FECHA': 14, 'DELITO': 'Hurto Bicicletas', 'HORARIO': 'day', 'Color': 'yellow'},
    {'FECHA': 15, 'DELITO': 'Extorsión', 'HORARIO': 'day', 'Color': 'red'},
    {'FECHA': 19, 'DELITO': 'Violencia Intrafamiliar', 'HORARIO': 'day', 'Color': 'red'},
    {'FECHA': 23, 'DELITO': 'Lesiones personales', 'HORARIO': 'night', 'Color': 'red'},
    {'FECHA': 24, 'DELITO': 'Hurto de Motos', 'HORARIO': 'night', 'Color': 'yellow'},
    {'FECHA': 28, 'DELITO': 'Hurto celulares', 'HORARIO': 'night', 'Color': 'yellow'},
]


# Convert the data to a dictionary for easier access
data_dict = {item['FECHA']: item for item in data}

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
            item = data_dict[day]
            html += f'<div class="calendar-item {item["Color"]} tooltip">'
            html += f'<div class="number">{day}</div>'
            html += f'<div class="{item["HORARIO"].lower()}"></div>'
            html += f'<span class="tooltiptext">{item["DELITO"]}</span>'
            html += '</div>'
        else:
            html += f'<div class="calendar-item current-month"><div class="number">{day}</div></div>'

# End of the calendar HTML
html += '</div>'

print(html)

