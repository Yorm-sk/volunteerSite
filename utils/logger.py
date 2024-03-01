import logging


class Logger:
    _log_format: str = (f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - "
                        f"%(message)s")

    def get_file_handler(self):
        file_handler = logging.FileHandler(filename="logs/program.log", mode="w")
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(logging.Formatter(self._log_format))
        return file_handler

    def get_stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(logging.Formatter(self._log_format))
        return stream_handler

    def get_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.get_file_handler())
        logger.addHandler(self.get_stream_handler())
        return logger
