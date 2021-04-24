class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def print_obj(self):
        return str(self.amount)+" "+str(self.currency)

    def sum(self, obj2):
        return Money(self.amount+obj2.amount, obj2.currency)

    def sub(self, obj2):
        return Money(self.amount-obj2.amount, obj2.currency)


def main():
    obj1 = Money(250, 'USD')
    obj2 = Money(50, 'USD')
    print("obj1: ", obj1.print_obj())
    print("obj2: ", obj2.print_obj())
    print("obj1+obj2: ", obj1.sum(obj2).print_obj())
    print("obj1-obj2: ", obj1.sub(obj2).print_obj())

main()
