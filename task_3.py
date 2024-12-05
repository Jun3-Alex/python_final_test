from datetime import datetime, timedelta


# Функция для получения даты через указанное количество дней
def get_future_date(days_from_now):
    # Получаем текущую дату и время
    current_datetime = datetime.now()

    # Создаем объект timedelta с указанным количеством дней
    future_timedelta = timedelta(days=days_from_now)

    # Добавляем timedelta к текущей дате для получения будущей даты
    future_date = current_datetime + future_timedelta

    # Преобразуем дату в строку в формате YYYY-MM-DD
    formatted_future_date = future_date.strftime('%Y-%m-%d')

    # Возвращаем отформатированную будущую дату
    return formatted_future_date


# Пример использования функции
days = 10
future_date = get_future_date(days)
print(f"Дата через {days} дней: {future_date}")
