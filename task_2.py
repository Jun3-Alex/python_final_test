from datetime import datetime

# Получаем текущее время и дату
current_datetime = datetime.now()

# Форматируем дату и время в формате YYYY-MM-DD HH:MM:SS
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Получаем полный день недели (например, 'Monday')
day_of_week = current_datetime.strftime('%A')

# Получаем номер недели в году с помощью isocalendar()[1]
week_number = current_datetime.isocalendar()[1]

# Выводим результаты
print(f"Текущая дата и время: {formatted_datetime}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")
