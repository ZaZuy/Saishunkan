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
from datetime import date
from InforEnum import Gender, Status
import re

# endregion import


class User:
    # region init
    def __init__(
        self,
        full_name: str = "",
        address: str = "",
        email: str = "",
        phone_number: str = "",
        status: str = "",
        gender: str = "",
        birth_date: date = "",
    ):
        self._full_name = full_name
        self._address = address
        self._email = email
        self._phone_number = phone_number
        self._status = status
        self._gender = gender
        self._birth_date = birth_date

    # region Getter and Setter for full_name
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        if not value:
            raise ValueError("Full name cannot be empty")
        for char in value:
            if not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z")):
                raise ValueError("Name is valid")
        self._full_name = value

    # region Getter and Setter for address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not value:
            raise ValueError("Address cannot be empty")
        self._address = value

    # region Getter and Setter for email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            raise ValueError("Invalid email format")
        self._email = value

    # region Getter and Setter for phone_number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")
        self._phone_number = value

    # region Getter and Setter for status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in Status.list_name():
            raise ValueError("Status must be 'Online' or 'Offline'")
        self._status = value

    # regionGetter and Setter for gender
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in Gender.list_name():
            raise ValueError("Gender must be 'Male', 'Female', or 'Other'")
        self._gender = value

    # region Getter and Setter for birth_date
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    def to_list(self):
        """Convert user object to a list for CSV writing."""
        return [
            self.full_name,
            self.address,
            self.email,
            self.phone_number,
            self.status,
            self.gender,
            self.birth_date,
        ]
