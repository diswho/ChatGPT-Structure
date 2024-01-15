# app/utils/custom_exceptions.py
class CustomException(Exception):
    def __init__(self, detail: str):
        self.detail = detail
