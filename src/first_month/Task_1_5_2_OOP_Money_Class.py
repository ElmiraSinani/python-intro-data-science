import requests
from CustomExceptions import InvalidInputError


class Money:
    api_url = "https://api.exchangerate-api.com/v4/latest/AMD"
    json_data = requests.get(api_url).json()
    rates = json_data['rates']

    def __init__(self, amount, currency):
        try:
            if (amount == int or amount == float) and amount < 0:
                raise InvalidInputError("Negative Number is not acceptable for amount", amount)
            if type(amount) != int or type(amount) != float:
                raise InvalidInputError("Amount must be number", amount)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)
        else:
            self.amount = amount
            self.currency = currency

    def __repr__(self):
        return str(self.amount) + " " + str(self.currency)

    def __add__(self, obj2):
        try:
            return Money(self.amount+obj2.amount, self.currency)
        except TypeError:
            print("Type Error")

    def __sub__(self, obj2):
        try:
            return Money(self.amount-obj2.amount, self.currency)
        except TypeError:
            print("Type Error")

    def conversion(self, convert_from, convert_to):
        try:
            converted_amount = self.amount/self.rates[convert_from] * self.rates[convert_to]
            return converted_amount
        except TypeError:
            print("Type Error")

def main():
    obj1 = Money("-50", 'USD')
    obj2 = Money(50, 'USD')
    print("obj1: ", obj1)
    print("obj2: ", obj2)
    print("obj1+obj2: ", obj1+obj2)
    print("obj1-obj2: ", obj1-obj2)
    print(obj1.conversion("RUB", "AMD"))
    print(obj1.conversion("USD", "AMD"))
    print(obj1.conversion("AMD", "AMD"))
#main()
