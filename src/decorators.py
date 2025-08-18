import datetime
import functools
import logging


def log(filename=None):
    """Декоратор для логирования вызовов функции. Логи пишутся в файл или консоль."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Обернутая функция с логированием времени выполнения."""

            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
            logger.handlers.clear()  # Очищаем хендлеры, чтобы избежать дублирования логов

            if filename:
                handler = logging.FileHandler(filename, mode="w", encoding="utf-8")
            else:
                handler = logging.StreamHandler()

            handler.setFormatter(logging.Formatter("%(message)s"))
            logger.addHandler(handler)

            # Логируем вызов функции
            start_time = datetime.datetime.now()
            log_message = f"[{start_time}] CCalling {func.__name__} with args: {args}, kwargs: {kwargs}"
            print(log_message)
            logger.info(log_message)

            try:
                result = func(*args, **kwargs)  # Вызов функции
                end_time = datetime.datetime.now()
                duration = (end_time - start_time).total_seconds()

                log_message = f"[{end_time}] {func.__name__} ok, result: {result} (Executed in {duration:.4f}s"
                print(log_message)
                logger.info(log_message)
                return result

            except Exception as e:
                end_time = datetime.datetime.now()
                duration = (end_time - start_time).total_seconds()

                log_message = (f"[{end_time}] {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs} "
                               f"(Failed in {duration:.4f}s)")
                print(log_message)
                logger.error(log_message)
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Складывает два числа и возвращает результат"""
    return x + y


@log(filename="mylog.txt")
def divide(a, b):
    """Функция делит одно число на другое"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено!")
    return a / b


my_function(1, 2)  # Должно пройти успешно
divide(4, 2)
