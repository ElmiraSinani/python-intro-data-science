import json

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

    def reserve(self):
        pass

    def checkout(self):
        pass


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

    def reserve(self, room_id, count):
        self.__rooms[room_id]['count'] = self.__rooms[room_id]['count'] - count

    def checkout(self, room_obj):
        pass
        #self.__rooms[room_id]['count'] = self.__rooms[room_id]['count'] - count

    def rate(self):
        pass

    def add_room(self, room_id, new_room_obj):
        self.__rooms[room_id] = {new_room_obj}

    def delete_room(self, room_id):
        self.__rooms.pop(room_id)

def create_room_id(hotel_rooms):
    return sorted(hotel_rooms.keys())[-1] + 1

hotel_rooms = {
                1: dict(Room('KING DELUXE BEDROOM', 700, 7)),
                2: dict(Room('QUEEN DUPLEX BEDROOM', 800, 8)),
                3: dict(Room('CONTERMINOUS FAMILY SUITE', 1000, 10)),
                4: dict(Room('GRAND TWIN PREMIER SUITE', 900, 9)),
                5: dict(Room('TWOFOLD PENTHOUSE', 600, 6)),
                6: dict(Room('LUXURIOUS POSH CABANA', 1300, 13)),
                7: dict(Room('HEDONISTIC SPACIOUS LANAI', 650, 12))
            }

roomObj = dict(Room("KING DELUXE BEDROOM", 700, 7))

# print("Room type: ", type(roomObj))
# print("Room obj: ", roomObj['count'])
# print("Room obj len(): ", len(roomObj))
#
# roomSet = {'type': 'KING DELUXE BEDROOM', 'count': 7}
# print("Room set len(): ",len(roomSet))



h = Hotel("Hilton Garden Inn", 4, 250, hotel_rooms)
print(h)

h.add_room(create_room_id(hotel_rooms), Room('Single', 800, 10))
print(h)

h.delete_room(1)
print(h)

h.reserve(2, 5)
print(h)