from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id: str, model: str, base_rate: float):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.base_rate = base_rate

    @property
    def vehicle_id(self) -> str:
        return self.__vehicle_id

    @property
    def model(self) -> str:
        return self.__model

    @property
    def base_rate(self) -> float:
        return self.__base_rate

    @base_rate.setter
    def base_rate(self, value: float):
        if value <= 0:
            raise ValueError("Base rate must be greater than 0.")
        self.__base_rate = float(value)

    @abstractmethod
    def calculate_rental_cost(self, days: int) -> float:
        pass

    @abstractmethod
    def display_details(self) -> None:
        pass


class Car(Vehicle):
    def __init__(
        self,
        vehicle_id: str,
        model: str,
        base_rate: float,
        num_doors: int,
        luxury_fee: float = 0.0,
    ):
        super().__init__(vehicle_id, model, base_rate)
        self.num_doors = num_doors
        self.luxury_fee = luxury_fee

    def calculate_rental_cost(self, days: int) -> float:
        return (self.base_rate * days) + self.luxury_fee

    def display_details(self) -> None:
        print(f"""[CAR] ID: {self.vehicle_id}   Model: {self.model}
                 Base Rate: ${self.base_rate:.2f}/day
                 Doors: {self.num_doors}
                 Luxury Fee: ${self.luxury_fee:.2f}""")


class Bike(Vehicle):
    def __init__(
        self, vehicle_id: str, model: str, base_rate: float, engine_capacity: int
    ):
        super().__init__(vehicle_id, model, base_rate)
        self.engine_capacity = engine_capacity

    def calculate_rental_cost(self, days: int) -> float:
        total = self.base_rate * days
        if days > 5:
            total *= 0.90
        return total

    def display_details(self) -> None:
        print(f"""[BIKE] ID: {self.vehicle_id}  Model: {self.model} 
                 Base Rate: ${self.base_rate:.2f}/day
                 Engine: {self.engine_capacity}cc""")


if __name__ == "__main__":
    fleet: list[Vehicle] = [
        Car("C101", "Tesla Model 3", 80.0, num_doors=4, luxury_fee=25.0),
        Car("C102", "Toyota Camry", 50.0, num_doors=4),
        Bike("B201", "Yamaha MT-07", 35.0, engine_capacity=689),
        Bike("B202", "Honda Rebel 500", 30.0, engine_capacity=471),
    ]

    rental_days = 7
    print(f"VEHICLE RENTAL FLEET REPORT ({rental_days} Days):\n")

    for vehicle in fleet:
        vehicle.display_details()
        cost = vehicle.calculate_rental_cost(rental_days)
        print(f"Total Cost ({rental_days} days): ${cost:.2f}\n")