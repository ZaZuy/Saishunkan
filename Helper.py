# region header
# ---------------------------------------------------------------------------
# System    :
# Class Name   : Day3
# Overview    : Học python trên udemy
# Designer    : DuyHG＠SSV
# Programmer   : DuyHG＠SSV
# Created Date   : 2025/04/02
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
import datetime


# region method


# convert string to datetiom with format m/d/y
def convert(date_time: str) -> datetime.datetime:
    format = "%m/%d/%Y"
    try:
        datetime_obj = datetime.datetime.strptime(date_time, format)
        return datetime_obj
    except ValueError:
        return None


# endregion method
