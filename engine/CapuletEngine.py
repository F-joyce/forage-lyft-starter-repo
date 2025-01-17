from abc import ABC

from car import Car
from engine.Engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        doesIt = self.current_mileage-self.last_service_mileage > 30000
        return doesIt