from abc import ABC, abstractmethod
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE

class Engine(ABC):
    
    @abstractmethod
    def needs_service(self):
        pass