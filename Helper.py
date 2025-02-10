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
#  Import third-party modules
import datetime


# region method

DATE_FORMAT = "%m/%d/%Y"


# convert string to datetiom with format m/d/y
def convert(date_time: str) -> datetime.datetime:
    """Chuyển đổi chuỗi ngày tháng thành đối tượng datetime. Ném lỗi nếu sai định dạng."""
    try:
        return datetime.datetime.strptime(date_time, DATE_FORMAT)
    except ValueError:
        raise ValueError(
            f"Invalid date format '{date_time}'. Expected format: {DATE_FORMAT}"
        )


# endregion method
