import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def logging_decorator(fn):

    def wrapper(*args, **kwargs):
        logging.info(f'{fn.__name__} args: {args}')
        logging.info(f'{fn.__name__} kwargs: {kwargs}')

        result = fn(*args, **kwargs)

        logging.info(f'{fn.__name__} result: {result}')
        return result

    return wrapper


@logging_decorator
def add(a, b):
    return a + b


add(2, 3)