import logging

logger = logging.getLogger('app1.main')
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")
fh = logging.FileHandler("../lesson_5/log/client.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')