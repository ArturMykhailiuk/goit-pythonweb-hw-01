from abc import ABC, abstractmethod
import logging

# Налаштування логування
file_handler = logging.basicConfig(
    format=("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
    level=logging.INFO,
    handlers=[
        logging.FileHandler(".\\factorymethod\program.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class Vehicle(ABC):

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        logger.info(f"{make} (US Spec) {model}: Автомобіль виготовлено")
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        logger.info(f"{make} (US Spec) {model}: Мотоцикл виготовлено")
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        logger.info(f"{make} (EU Spec) {model}: Автомобіль виготовлено")
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        logger.info(f"{make} (EU Spec) {model}: Мотоцикл виготовлено")
        return Motorcycle(f"{make} (EU Spec)", model)


# Використання фабрик для створення транспортних засобів
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Створення транспортних засобів для США
us_car = us_factory.create_car("Ford", "Mustang")
us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

# Створення транспортних засобів для ЄС
eu_car = eu_factory.create_car("Toyota", "Corolla")
eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1250GS")

# Запуск двигунів
us_car.start_engine()
us_motorcycle.start_engine()
eu_car.start_engine()
eu_motorcycle.start_engine()
