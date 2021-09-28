"""Contains classes for different modes of transport"""

from abc import ABC
from abc import abstractmethod

from datetime import date


class Engine:
    """Parent class for transport"""

    @staticmethod
    def convert_energy():
        """Explains engine sens"""
        return 'Device that converts some form of energy into mechanical work.'


class Transport(Engine, ABC):
    """Abstract class for transport methods
    Attributes - int and str
    """

    def __init__(self, max_speed, fuel_type, capacity):
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        self._capacity = capacity

    @staticmethod
    def info():
        """Info about transport"""
        return 'This is the movement of humans, animals, and goods from one location to another.'

    @abstractmethod
    def move(self):
        """Abstract method for explaining movement"""

    @property
    def capacity(self):
        """Returns capacity of this transport"""
        return f'I can carry {self._capacity} passengers.'


class LandT(Transport):
    """Inherit all attributes from Transport"""

    def move(self):
        print('I can ride')
        return 'I am a key factor in urban planning'

    def __bool__(self):
        print('Call __bool__')
        return self.max_speed != 0 and self.capacity != 0


class AirT(Transport):
    """Inherit all attributes from Transport"""

    def move(self):
        print('I can fly')
        return 'I am the fastest method of transport'


class WaterT(Transport):
    """Inherit all attributes from Transport"""

    def move(self):
        print('I can sail')
        super().move()


class HumanPoweredT(Transport):
    """Inherit all attributes from Transport"""

    def move(self):
        print('I can use your muscle-power :)')
        print('I am the most available of any mode of transport')
        super().move()


class RailT(LandT):
    """Inherit all attributes from Transport"""

    @classmethod
    def surface_needed(cls):
        """Explains what type of surface needed"""
        return 'This mode of transport needs rail track, known as a railway or railroad.'


class RoadT(LandT):
    """Inherit all attributes from Transport"""

    @classmethod
    def surface_needed(cls):
        """Explains what type of surface needed"""
        return 'This mode of transport needs gravel, asphalt or concrete.'


class Car(RoadT):
    """Inherit all attributes from Transport
    Additional arg - year of issue
    """

    def __init__(self, max_speed, fuel_type, capacity, year_issue):
        super().__init__(max_speed, fuel_type, capacity)
        self.year_issue = year_issue

    def check_age(self):
        """Checks car`s age"""
        today = date.today()
        age = today.year - int(self.year_issue)
        return f'This car is {age} year(s)'

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.max_speed == other.max_speed and self.fuel_type == other.fuel_type and \
                   self._capacity == other._capacity and self.year_issue == other.year_issue

    def __hash__(self):
        return hash((self.max_speed, self.fuel_type, self._capacity, self.year_issue))

    def __iter__(self):
        return iter((self.max_speed, self.fuel_type, self._capacity, self.year_issue))

    def __contains__(self, value):
        if value in (self.max_speed, self.fuel_type, self._capacity, self.year_issue):
            return True


class Kayak(WaterT, HumanPoweredT):
    """Inherit all attributes from
    Water and Human powered transport
    """
    def move(self):
        print('I am very nice choice for travelling')
        print('The only problem is dependence on the weather.')
        super().move()


bmw = Car(375, 'petrol', 5, '2019')
toyota = Car(250, 'petrol', 5, '2019')
jeep = Car(100, 'petrol', 0, '2020')
# print(bmw.capacity)
# print(bmw.info())
# print(bmw.surface_needed())
# print(bmw.move())
# print(bmw.check_age())
# print(bmw == toyota)
# print(hash(bmw))
# print(hash(toyota))
# print(bool(bmw))
# print(bool(jeep))
# for x in jeep:
#     print(x)
# print('petro' in bmw)
kayak_1 = Kayak(20, 'muscle-energy', 3)
print(Kayak.__mro__)
kayak_1.move()
