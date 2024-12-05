import logging

# Создаем главный логгер
logger = logging.getLogger("multi_file_logger")
logger.setLevel(logging.DEBUG)

# Создаем обработчик для логов уровня DEBUG и INFO (debug_info.log)
debug_info_handler = logging.FileHandler("debug_info.log")
debug_info_handler.setLevel(logging.DEBUG)

# Создаем обработчик для логов уровня WARNING и выше (warnings_errors.log)
warnings_errors_handler = logging.FileHandler("warnings_errors.log")
warnings_errors_handler.setLevel(logging.WARNING)

# Создаем форматтер, который будем использовать для всех логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Применяем форматтер к обработчикам
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к главному логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Примеры логов разного уровня
logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")
