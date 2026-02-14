""" Task 3 – Abstract Factory
Write a program in which two Abstract Car Factories (left and right hand drive) produce 3 types of cars (sedan,
station wagon, coupe). """

class Sedan:
    def car_type(self):
        pass


class LeftSideSteeringWheelSedan(Sedan):
    def car_type(self):
        return "» Sedan with a left-hand steering wheel"


class RightSideSteeringWheelSedan(Sedan):
    def car_type(self):
        return "» Sedan with a right-hand steering wheel"


class StationWagon:
    def car_type(self):
        pass


class LeftSideSteeringWheelStationWagon(StationWagon):
    def car_type(self):
        return "» Station Wagon with a left-hand steering wheel"


class RightSideSteeringWheelStationWagon(StationWagon):
    def car_type(self):
        return "» Station Wagon with a right-hand steering wheel"


class Coupe:
    def car_type(self):
        pass


class LeftSideSteeringWheelCoupe(Coupe):
    def car_type(self):
        return "» Coupe with a left-hand steering wheel"


class RightSideSteeringWheelCoupe(Coupe):
    def car_type(self):
        return "» Coupe with a right-hand steering wheel"


class CarFactory:
    def build_sedan_car(self):
        pass

    def build_station_wagon_car(self):
        pass

    def build_coupe_car(self):
        pass


class LeftSideSteeringWheelCarFactory(CarFactory):
    def build_sedan_car(self):
        return LeftSideSteeringWheelSedan()

    def build_station_wagon_car(self):
        return LeftSideSteeringWheelStationWagon()

    def build_coupe_car(self):
        return LeftSideSteeringWheelCoupe()


class RightSideSteeringWheelCarFactory(CarFactory):
    def build_sedan_car(self):
        return RightSideSteeringWheelSedan()

    def build_station_wagon_car(self):
        return RightSideSteeringWheelStationWagon()

    def build_coupe_car(self):
        return RightSideSteeringWheelCoupe()


def main():
    print("Cars with a right-hand steering wheel:\n")
    car_factory = RightSideSteeringWheelCarFactory()

    sedan = car_factory.build_sedan_car()
    print(sedan.car_type())

    station_wagon = car_factory.build_station_wagon_car()
    print(station_wagon.car_type())

    coupe = car_factory.build_coupe_car()
    print(coupe.car_type())

    print()

    print("Cars with a left-hand steering wheel:\n")
    car_factory = LeftSideSteeringWheelCarFactory()

    sedan = car_factory.build_sedan_car()
    print(sedan.car_type())

    station_wagon = car_factory.build_station_wagon_car()
    print(station_wagon.car_type())

    coupe = car_factory.build_coupe_car()
    print(coupe.car_type())


main()
