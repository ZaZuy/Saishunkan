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
from enum import Enum


# Python
# region main
class ExtendedEnum(Enum):

    @classmethod
    # region method
    # convert properties enum to list by name
    def list_name(cls):
        return [c.name for c in cls]

    @classmethod
    # region method
    # convert properties enum to list by name
    def list_value(cls):
        return [c.value for c in cls]


class Gender(ExtendedEnum):
    # region enum
    Male = 0
    Female = 1


class Status(ExtendedEnum):
    # region enum
    Online = 0
    Offline = 1


class StatusDiaLog(ExtendedEnum):
    # region enum
    Yes = 1
    No = 2


class ColumnHeaders(ExtendedEnum):
    FULL_NAME = "Họ tên"
    ADDRESS = "Địa chỉ"
    EMAIL = "Email"
    PHONE_NUMBER = "Số điện thoại"
    STATUS = "Trạng thái"
    GENDER = "Giới tính"
    DATE_OF_BIRTH = "Ngày Sinh"


# endregion main
