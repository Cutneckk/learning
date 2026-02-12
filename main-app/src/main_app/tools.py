import re
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, value: str):
        pass


class EmailValidator(Validator):
    def validate(self, email: str):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return email
        raise ValueError('Invalid email')


class QuantityValidator(Validator):
    def validate(self, quantity: int):
        """валидация количества товара"""
        if quantity <= 0:
            raise ValueError('quantity must be greater than 0')
        return quantity
