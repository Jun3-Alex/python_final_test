import argparse


# Функция для основного выполнения
def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Скрипт для обработки числа и строки с дополнительными опциями.")

    # Добавляем обязательные аргументы: число и строку
    parser.add_argument('number', type=int, help="Целое число, которое нужно обработать")
    parser.add_argument('text', type=str, help="Строка, которую нужно вывести")

    # Добавляем опцию --verbose
    parser.add_argument('--verbose', action='store_true', help="Вывести дополнительную информацию о процессе")

    # Добавляем опцию --repeat для повторения строки
    parser.add_argument('--repeat', type=int, default=1, help="Количество раз для повторения строки")

    # Парсим аргументы командной строки
    args = parser.parse_args()

    # Обработка аргументов
    number = args.number
    text = args.text
    repeat = args.repeat
    verbose = args.verbose

    # Если установлен флаг --verbose, выводим дополнительную информацию
    if verbose:
        print(f"Получено число: {number}")
        print(f"Получена строка: '{text}'")
        print(f"Количество повторений строки: {repeat}")

    # Повторяем строку указанное количество раз
    for i in range(repeat):
        print(f"Повторение {i + 1}: {text}")


# Запуск основной функции
if __name__ == "__main__":
    main()
