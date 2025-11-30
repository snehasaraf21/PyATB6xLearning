from abc import ABC, abstractmethod

class BrowserManager(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Browser stopped")

class ChromeBowser(BrowserManager):
        def start(self):
            print("ChromeBowser started")

tc=ChromeBowser()
tc.start()
tc.stop()