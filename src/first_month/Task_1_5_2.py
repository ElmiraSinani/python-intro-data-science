class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def print_obj(self):
        return str(self.amount)+" "+str(self.currency)

    def sum(self, obj2):
        return str(self.amount+obj2.amount)+" "+self.currency

    def sub(self, obj2):
        return str(self.amount - obj2.amount) + " " + self.currency


def main():
    obj1 = Money(150, 'USD')
    obj2 = Money(200, 'USD')
    print(obj1.print_obj())
    print(obj1.sum(obj2))
    print(obj2.sub(obj1))

main()
