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
from typing import List, Optional

class HandleFileCsv:
    @staticmethod
    def readfile(file_path: str) -> Optional[List[List[str]]]:
        """Đọc file CSV và trả về danh sách các dòng dưới dạng list."""
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                return [row for row in csv_reader]
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def writefile(file_path: str, data: List[List[str]]) -> bool:
        """Ghi dữ liệu vào file CSV, trả về True nếu thành công, False nếu có lỗi."""
        if not data or not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            print("Error: Data must be a non-empty list of lists.")
            return False
        
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


    # region end method
