from abc import ABC

from car import Car
from engine.Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        doesIt = self.warning_light_is_on
        return doesIt