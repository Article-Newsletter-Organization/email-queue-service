from log.custom_logger import CustomLogger
from app import App


def main():
    logger = CustomLogger()

    logger.info("Script initialized!")

    App().run()


if __name__ == "__main__":
    main()
