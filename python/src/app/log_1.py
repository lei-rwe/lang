import os
from python.src.utils.zwidgets import mylogger

class Main(object):

    @staticmethod
    def main():
        mylogger.debug("1")
        mylogger.info("2")
        mylogger.warn("3")
        mylogger.error("4")
        mylogger.critical("5")

if __name__ == "__main__":
    print(os.getcwd())
    Main.main()