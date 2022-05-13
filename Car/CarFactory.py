from abc import ABC
from datetime import date
from Battery.SpindlerBattery import SpindlerBattery
from Battery.NubbinBattery import NubbinBattery
import Car
from engine import *

class CarFactory(ABC):

    def __init__(self) -> None:
        super().__init__()

    def create_calliope(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        engine = engine.CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)

        car = Car(engine=engine, battery=battery)

        return car
    
    def create_glissade(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        engine = engine.WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)

        car = Car(engine=engine, battery=battery)

        return car

    def create_palindrome(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        engine = engine.SternamEngine(False)

        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)

        car = Car(engine=engine, battery=battery)

        return car

    def create_thovax(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        engine = engine.CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)

        car = Car(engine=engine, battery=battery)

        return car

    def create_rorschach(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        engine = engine.WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)

        car = Car(engine=engine, battery=battery)

        return car