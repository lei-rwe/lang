import os
from python.src.utils.zwidgets import mylogger

class Main(object):

    @staticmethod
    def main():
        mylogger.debug("my debug log")
        mylogger.info("my info log")
        mylogger.warning("my warning log")
        mylogger.error("my error log")
        mylogger.critical("my critical log")

if __name__ == "__main__":
    print(os.getcwd())
    Main.main()