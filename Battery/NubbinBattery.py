from datetime import datetime
from Battery.Battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = datetime.today().date()
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        doesIt = service_threshold_date < self.current_date

        return doesIt