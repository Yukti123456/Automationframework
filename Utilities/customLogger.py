import logging
import os


class LogGen:

    @staticmethod
    def logger():

        log_dir = os.path.join(os.path.abspath(os.curdir), "Logs")
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "automation.log")

        logging.basicConfig(
            filename=log_file,
            format="%(asctime)s : %(levelname)s : %(message)s",
            datefmt="%d/%m/%Y %I:%M:%S %p",
            level=logging.DEBUG,
            force=True
        )

        logger = logging.getLogger()
        return logger