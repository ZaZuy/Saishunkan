# region header
# ---------------------------------------------------------------------------
# System    :
# Class Name   : Day2
# Overview    : Học python trên udemy
# Designer    : DuyHG＠SSV
# Programmer   : DuyHG＠SSV
# Created Date   : 2025/03/02
# -----------------< History >-----------------------------------------------
# ID     :
# Designer    :
# Programmer   :
# Updated Date   :
# Comment    :
# Version    :
# -----------------< History >-----------------------------------------------
# endregion header

# region import
# Python
import csv

# endregion import


class HandleFileCsv:
    # region start method
    @staticmethod
    # region read file csv
    def readfile():
        with open("datatest.csv", mode="r") as file:
            csvFile = csv.reader(file)
            return list(csvFile)

    @staticmethod
    # region read write csv
    def writefile(data):
        with open("datatest.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    # region end method
