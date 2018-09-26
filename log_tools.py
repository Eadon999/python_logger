from cloghandler import ConcurrentRotatingFileHandler
import logging
import os


def log(message, path = None, level = None, filename = None, log_type = None):
    if not filename:
        filename = 'python_logs'
    if not path:
        path = './logs/'
        if not os.path.exists(path):
            os.makedirs(path)
    logger = logging.getLogger(filename)

    if not level:
        logger.setLevel(logging.INFO)
    elif level == 'debug':
        logger.setLevel(logging.DEBUG)

    #  若logger.handlers列表为空,则添加,否则,直接去写日志,避免重复写入日志
    if not logger.handlers:
        filehandler = ConcurrentRotatingFileHandler(path + filename + '.log')
        formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(name)s|%(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

    if not log_type:
        logger.info(message)
    elif log_type == 'error':
        logger.error(message)
    elif log_type == 'warning':
        logger.warning(message)
    elif log_type == 'debug':
        logger.debug(message)

    # return logger


if __name__ == '__main__':
    # log('hi')
    # log('hi too')
    # log('hi three')
    log(message='dd', level='debug', log_type='error')
    log(message='tt')
    log(message='ff')
