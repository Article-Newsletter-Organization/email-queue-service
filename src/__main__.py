from log.custom_logger import CustomLogger
from errors.unexpected_error import UnexpectedError


def main():
    logger = CustomLogger()

    logger.info("Script initialized!")


if __name__ == "__main__":
    main()
