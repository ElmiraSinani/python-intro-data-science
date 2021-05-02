import requests

class Money:
    api_url = "https://api.exchangerate-api.com/v4/latest/AMD"
    json_data = requests.get(api_url).json()
    rates = json_data['rates']

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def print_obj(self):
        return str(self.amount)+" "+str(self.currency)

    def __str__(self):
        return str(self.amount) + " " + str(self.currency)

    def sum(self, obj2):
        return Money(self.amount+obj2.amount, self.currency)

    def sub(self, obj2):
        return Money(self.amount-obj2.amount, self.currency)

    def conversion(self, convert_from, convert_to):
        converted_amount = self.amount/self.rates[convert_from] * self.rates[convert_to]
        return converted_amount

def main():

    obj1 = Money(100, 'USD')
    obj2 = Money(50, 'USD')
    print("obj1: ", obj1.print_obj())
    print("obj2: ", obj2.print_obj())
    print("obj1+obj2: ", obj1.sum(obj2).print_obj())
    print("obj1-obj2: ", obj1.sub(obj2).print_obj())

    print(obj1.conversion("RUB", "AMD"))
    print(obj1.conversion("USD", "AMD"))
    print(obj1.conversion("AMD", "AMD"))

#main()
