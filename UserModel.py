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
import re
from datetime import date, datetime
from typing import Union
from InforEnum import Gender, Status  # Assuming Gender and Status enums are imported

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
        birth_date: Union[date, str] = "",
    ):
        self.full_name = full_name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.status = status
        self.gender = gender
        self.birth_date = birth_date

    # region Getter and Setter for full_name
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value: str):
        if not value:
            raise ValueError("Full name cannot be empty")
        if len(value) > 50:
            raise ValueError("Name is too long")
        if not re.match(r"^[a-zA-ZÀ-ỹ\s]+$", value):
            raise ValueError("Invalid name")
        self._full_name = value.strip()

    # region Getter and Setter for address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: str):
        if not value:
            raise ValueError("Address cannot be empty")
        if len(value) > 100:
            raise ValueError("Address is too long")
        self._address = value.strip()

    # region Getter and Setter for email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if len(value) > 50:
            raise ValueError("Email is too long")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            raise ValueError("Invalid email format")
        self._email = value.strip()

    # region Getter and Setter for phone_number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if not re.match(r"^\+?(\d{1,3})?[-.\s]?(\d{9,12})$", value):
            raise ValueError("Invalid phone number format")
        self._phone_number = value.strip()

    # region Getter and Setter for status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        if value not in Status.list_name():
            raise ValueError("Status must be 'Online' or 'Offline'")
        self._status = value

    # region Getter and Setter for gender
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value: str):
        if value not in Gender.list_name():
            raise ValueError("Gender must be 'Male' or 'Female'")
        self._gender = value

    # region Getter and Setter for birth_date
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: Union[date, str]):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, "%Y-%m-%d").date()  # Convert string to date
            except ValueError:
                raise ValueError("Invalid date format, must be 'YYYY-MM-DD'")
        elif not isinstance(value, date):
            raise ValueError("birth_date must be a date object or a valid date string")
        self._birth_date = value

    def to_list(self):
        """Convert user object to a list for CSV writing."""
        # Ensure all required fields are valid before converting
        if not self.full_name or not self.address or not self.email or not self.phone_number:
            raise ValueError("Missing required user information")
        return [
            self.full_name,
            self.address,
            self.email,
            self.phone_number,
            self.status,
            self.gender,
            self.birth_date.isoformat() if isinstance(self.birth_date, date) else self.birth_date,
        ]


# endregion
