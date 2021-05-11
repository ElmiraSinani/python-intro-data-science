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

    def __iter__(self):
        yield 'count', self.__room_count
        yield 'type', self.__room_type
        yield 'price', self.__room_price

    def get_room_type(self):
        return self.__room_type

    def get_room_count(self):
        return self.__room_count

    def get_room_price(self):
        return self.__room_price

    def set_room_count(self, v):
        try:
            if self.__room_count == int:
                self.__room_count = v
            else:
                raise InvalidInputError("You can set only integer value as a Room count", v)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def reserve(self, count):
        self.__room_count = self.__room_count - count

    def checkout(self):
        self.__room_count = self.__room_count - 1


class Hotel:
    def __init__(self, name, rating, rater_count, rooms):
        try:
            if type(rating) != int:
                raise InvalidInputError("Rating must me number", rating)
            elif type(rater_count) != int:
                raise InvalidInputError("rater_count must be Integer", rater_count)
            elif type(name) != str:
                raise InvalidInputError("Hotel name must be string", name)
            else:
                self.__name = name
                self.__rating = rating
                self.__rater_count = rater_count
                self.__rooms = rooms
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return "{} - Rating: {}, From Raters Count: {}, Rooms: {}".format(self.__name, self.__rating, self.__rater_count, self.__rooms)

    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating

    def get_rooms(self):
        return self.__rooms

    def add_room(self, room_id, new_room_obj):
        self.__rooms[room_id] = {new_room_obj}

    def delete_room(self, room_id):
        self.__rooms.pop(room_id)

    def reserve(self, room_id, room_obj, count):
        Room.reserve(room_obj, count)
        self.__rooms[room_id] = dict(room_obj)

    def checkout(self, room_id, room_obj):
        Room.checkout(room_obj)
        self.__rooms[room_id]['count'] = self.__rooms[room_id]['count'] + 1

    def rate(self):
        pass


def create_room_id(hotel_rooms):
    return sorted(hotel_rooms.keys())[-1] + 1


r1 = Room('KING DELUXE BEDROOM', 700, 7)
r2 = Room('QUEEN DUPLEX BEDROOM', 800, 8)
r3 = Room('CONTERMINOUS FAMILY SUITE', 1000, 10)
r4 = Room('GRAND TWIN PREMIER SUITE', 900, 9)
r5 = Room('TWOFOLD PENTHOUSE', 600, 6)
r6 = Room('LUXURIOUS POSH CABANA', 1300, 13)
r7 = Room('HEDONISTIC SPACIOUS LANAI', 650, 12)
r8 = Room('Single', 800, 10)
hotel_rooms = {1: dict(r1), 2: dict(r2), 3: dict(r3), 4: dict(r4), 5: dict(r5), 6: dict(r6), 7: dict(r7)}

h = Hotel("Hilton Garden Inn", 4, 250, hotel_rooms)
print(h)
#
# h.add_room(create_room_id(hotel_rooms), r8)
# print(h)
#
# h.delete_room(1)
# print(h)


h.reserve(1, r1, 5)
print(h)

h.checkout(1, r1)
print(h)