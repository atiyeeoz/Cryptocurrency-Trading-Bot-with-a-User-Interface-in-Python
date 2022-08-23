import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler


file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("a9683138182ad5501218e781ea603b62efbbb7852c95fea7af581b4d849b12fa",
                            "cd4cbde53452fb434741f78c200a96f65e7393f20561f4774f35764742519290",
                            testnet=True, futures=True)

    bitmex = BitmexClient("3z61amz3picjdtcHKkkd0jA2", "J7Rds6KhkeD2__lugxB3iowX3kNKuE8WpOxEJWab9m4gjx7z", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()

