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
#  Import third-party modules
from typing import List

#  Import standard modules
from enum import Enum, auto, StrEnum


# region main
class ExtendedEnum(Enum):
    @classmethod
    def list_name(cls) -> List[str]:
        """Convert enum properties to a list of names."""
        return [c.name for c in cls]

    @classmethod
    def list_value(cls) -> List:
        """Convert enum properties to a list of values."""
        return [c.value for c in cls]


class Gender(ExtendedEnum):
    # region enum
    Male = auto()
    Female = auto()


class Status(ExtendedEnum):
    # region enum
    Online = auto()
    Offline = auto()


class StatusDiaLog(ExtendedEnum):
    # region enum
    Yes = auto()
    No = auto()


class ColumnHeaders(StrEnum, ExtendedEnum):
    """Enum for column headers, values act as strings."""

    FULL_NAME = "Họ tên"
    ADDRESS = "Địa chỉ"
    EMAIL = "Email"
    PHONE_NUMBER = "Số điện thoại"
    STATUS = "Trạng thái"
    GENDER = "Giới tính"
    DATE_OF_BIRTH = "Ngày Sinh"


# endregion main
