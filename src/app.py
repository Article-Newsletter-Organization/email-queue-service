from log.custom_logger import CustomLogger


class App():
    logger = CustomLogger()

    def __init__(self):
        """
            Constructor
        """

    def run(self):
        self.logger.info("Application running!")
