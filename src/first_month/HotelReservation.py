from CustomExceptions import InvalidInputError


class Room:
    def __init__(self, room_type, room_count):
        try:
            if type(room_type) != str:
                raise InvalidInputError("Room type must be string", room_type)
            elif type(room_count) != int or room_count <= 0:
                raise InvalidInputError("Room count must me positive integer", room_count)
            else:
                self.__room_type = room_type
                self.__room_count = room_count
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return "Room Type: {}, Count: {}".format(self.__room_type, self.__room_count)

    def reserve(self):
        pass

    def checkout(self):
        pass

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, v):
        try:
            if self.__room_type == str:
                self.__room_type = v
            else:
                raise InvalidInputError("You can set only String value as a Room type", v)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def get_room_count(self):
        return self.__room_count

    def set_room_count(self, v):
        try:
            if self.__room_count == int:
                self.__room_count = v
            else:
                raise InvalidInputError("You can set only integer value as a Room count", v)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)


class Hotel():
    def __init__(self, rating, rater_count, rooms):
        try:
            if type(rating) != int or type(rating) != float:
                raise InvalidInputError("Rating must me number")
            elif type(rater_count) != int:
                raise InvalidInputError("rater_count must be Integer")
            else:
                self.__rating = rating
                self.__rater_count = rater_count
                self.__rooms = rooms
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return "Rating: {}, Count: {}".format(self.__rating, self.__rater_count)

    def get_rating(self):
        return self.__rating

    def get_rooms(self):
        return self.__rooms

    def reserve(self):
        pass

    def checkout(self):
        pass

    def rate(self):
        pass
