from CustomExceptions import InvalidInputError


class Room:
    def __init__(self, room_type, room_price, room_count):
        try:
            if type(room_type) != str:
                raise InvalidInputError("Room type must be string", room_type)
            elif type(room_count) != int or room_count <= 0:
                raise InvalidInputError("Room count must me positive integer", room_count)
            elif type(room_price) != int or room_price <= 0:
                raise InvalidInputError("Room price must me positive integer", room_count)
            else:
                self.__room_type = room_type
                self.__room_price = room_price
                self.__room_count = room_count
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return "'type': '{}', 'count': {}".format(self.__room_type, self.__room_count)

    def get_room_type(self):
        return self.__room_type

    def get_room_count(self):
        return self.__room_count

    def get_room_price(self):
        return self.__room_price

    def set_room_count(self, v):
        try:
            if type(self.__room_count) == int:
                self.__room_count = v
            else:
                raise InvalidInputError("You can set only integer value as a Room count", v)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def reserve(self, count):
        try:
            if type(count) != int:
                raise InvalidInputError("Room count must be integer", count)
            elif count < 1:
                raise InvalidInputError("Room count must be >0 integer", count)
            elif count > self.__room_count:
                raise InvalidInputError("Reserve count can't be > than total rooms count", count)
            else:
                self.__room_count = self.__room_count - count
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def checkout(self, count):
        try:
            if type(count) != int:
                raise InvalidInputError("Room count must be integer", count)
            elif count < 1:
                raise InvalidInputError("Room count must be >0 integer", count)
            else:
                self.__room_count = self.__room_count + count
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)


class Hotel:
    def __init__(self, name, rooms):
        try:
            if type(name) != str:
                raise InvalidInputError("Hotel name must be string", name)
            else:
                self.__rating = 0
                self.__rater_count = 0
                self.__rating_sum = 0
                self.__name = name
                self.__rooms = rooms
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return "{} - Rating: {}, From {} raters, Rooms: {}".format(self.__name, self.__rating, self.__rater_count, self.__rooms)

    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating

    def get_rooms(self):
        return self.__rooms

    def add_room(self, room_obj):
        try:
            if type(room_obj) == Room:
                self.__rooms.append(room_obj)
            else:
                raise InvalidInputError("Room must be Room Type", Room)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def delete_room(self, room_obj):
        try:
            if type(room_obj) == Room:
                self.__rooms.remove(room_obj)
            else:
                raise InvalidInputError("Room must be Room Type", Room)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def rate(self, new_rating):
        try:
            if type(new_rating) != int:
                raise InvalidInputError("Rating must be integer", new_rating)
            elif 1 > new_rating > 5:
                raise InvalidInputError("Rating must be >0 integer", new_rating)
            else:
                self.__rater_count = self.__rater_count + 1
                self.__rating_sum = self.__rating_sum + new_rating
                self.__rating = self.__rating_sum / self.__rater_count
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    @staticmethod
    def reserve(room_obj, count):
        try:
            if type(count) != int:
                raise InvalidInputError("Reserve count must be integer", count)
            elif count < 1:
                raise InvalidInputError("Room count must be positive integer", count)
            elif type(room_obj) != Room:
                raise InvalidInputError("Room Type must be Room", room_obj)
            else:
                Room.reserve(room_obj, count)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    @staticmethod
    def checkout(room_obj, count):
        try:
            if type(count) != int:
                raise InvalidInputError("Reserve count must be integer", count)
            elif count < 1:
                raise InvalidInputError("Room count must be positive integer", count)
            elif type(room_obj) != Room:
                raise InvalidInputError("Room Type must be Room", room_obj)
            else:
                Room.checkout(room_obj, count)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)


def main():
    r1 = Room('KING DELUXE BEDROOM', 700, 7)
    r2 = Room('QUEEN DUPLEX BEDROOM', 800, 8)
    r3 = Room('CONTERMINOUS FAMILY SUITE', 1000, 10)
    r4 = Room('GRAND TWIN PREMIER SUITE', 900, 9)
    r5 = Room('TWOFOLD PENTHOUSE', 600, 6)
    r6 = Room('LUXURIOUS POSH CABANA', 1300, 13)
    r7 = Room('HEDONISTIC SPACIOUS LANAI', 650, 12)
    hotel_rooms = [r1, r2, r3, r4, r5, r6, r7]

    h = Hotel("Hilton Garden Inn", hotel_rooms)
    print(h)

    h.add_room(Room('Single', 800, 10))
    print(h)

    h.delete_room(r1)
    print(h)

    h.rate(5)
    h.rate(4)
    h.rate(3)
    h.rate(5)

    h.reserve(r2, 5)
    print('Reserve: ', h)

    h.checkout(r2, 9)
    print('Checkout: ', h)


main()




