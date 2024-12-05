import os
import logging
from collections import namedtuple
import argparse

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Определяем namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_directory'])

# Функция для сбора информации о содержимом директории
def collect_directory_info(directory_path):
    # Проверяем, является ли указанный путь директорией
    if not os.path.isdir(directory_path):
        logging.error(f"Путь {directory_path} не является директорией.")
        print(f"Ошибка: {directory_path} не является директорией.")
        return

    # Получаем содержимое директории
    directory_contents = os.listdir(directory_path)
    collected_info = []

    for item in directory_contents:
        item_path = os.path.join(directory_path, item)
        parent_directory = os.path.basename(directory_path)

        if os.path.isdir(item_path):
            # Если это директория
            info = FileInfo(name=item, extension=None, is_dir=True, parent_directory=parent_directory)
        else:
            # Если это файл, получаем имя и расширение
            name, extension = os.path.splitext(item)
            extension = extension.lstrip('.')  # Убираем точку из расширения, если оно есть
            info = FileInfo(name=name, extension=extension, is_dir=False, parent_directory=parent_directory)

        # Добавляем информацию в список и логируем
        collected_info.append(info)
        logging.info(f"Объект: {info}")

    # Выводим всю собранную информацию в лог
    for info in collected_info:
        print(f"Имя: {info.name}, Расширение: {info.extension}, Каталог: {info.is_dir}, Родительский каталог: {info.parent_directory}")

# Основная функция, которая получает аргумент из командной строки
def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Соберите информацию о содержимом директории.")
    parser.add_argument('directory', type=str, help="Путь к директории для сбора информации")
    args = parser.parse_args()

    # Запускаем сбор информации
    collect_directory_info(args.directory)

# Запуск основной функции
if __name__ == "__main__":
    main()
