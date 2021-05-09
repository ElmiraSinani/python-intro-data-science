import requests
from CustomExceptions import InvalidInputError


class Money:
    api_url = "https://api.exchangerate-api.com/v4/latest/AMD"
    json_data = requests.get(api_url).json()
    rates = json_data['rates']

    def __init__(self, amount, currency):
        try:
            if type(amount) == int and amount <= 0:
                raise InvalidInputError("Amount must be a positive number:", amount)
            elif type(amount) != int:
                raise InvalidInputError("Amount must be number", amount)
            elif type(currency) != str:
                raise InvalidInputError('Currency must be a string type:', currency)
            else:
                self.__amount = amount
                self.__currency = currency
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
       return str(self.__amount) + " " + str(self.__currency)

    def __add__(self, obj2):
        return Money(self.__amount+obj2.__amount, self.__currency)

    def __sub__(self, obj2):
        return Money(self.__amount-obj2.__amount, self.__currency)

    def conversion(self, convert_from, convert_to):
        converted_amount = self.__amount/self.rates[convert_from] * self.rates[convert_to]
        return converted_amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, val):
        try:
            if type(val) == int and val>0:
                self.__amount = val
            else:
                raise InvalidInputError("Invalid value for amount", val)
        except InvalidInputError:
            print("Amount must be positive number")

    def get_currency(self):
        return self.__currency

    def set_currency(self, val):
        try:
            if type(val) == str:
                self.__currency = val
            else:
                raise InvalidInputError("Invalid value for currency", val)
        except InvalidInputError:
            print("currency must be string")


def main():
    obj1 = Money("100", 'USD')
    obj2 = Money(50, 'USD')
    print("obj1: ", obj1)
    print("obj2: ", obj2)
    print("obj1+obj2: ", obj1+obj2)
    print("obj1-obj2: ", obj1-obj2)
    print(obj1.conversion("RUB", "AMD"))
    print(obj1.conversion("USD", "AMD"))
    print(obj1.conversion("AMD", "AMD"))
main()
