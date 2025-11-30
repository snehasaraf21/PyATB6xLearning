from abc import ABC, abstractmethod

class GearBox(ABC):
    @abstractmethod
    def gear(self):
        pass
class Engine:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class car(GearBox, Engine):
    def start(self):
        print("Starting")


    def stop(self):
        print("Stopping")

    def gear(self):
        print("Gear is ready")


    def drive(self):
         self.gear()
         self.start()
         self.stop()


tesla = car()
tesla.drive()
