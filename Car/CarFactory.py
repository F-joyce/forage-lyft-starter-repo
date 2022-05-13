from abc import ABC
from datetime import date
from Battery.SpindlerBattery import SpindlerBattery
import Car
from engine.CapuletEngine import CapuletEngine

class CarFactory(ABC):

    def __init__(self) -> None:
        super().__init__()

    def create_calliope(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
    
    def create_glissade(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        return Car

    def create_palindrome(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        return Car

    def create_thovax(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        return Car

    def create_rorschach(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int):
        return Car