from abc import ABC, abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def readfromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def openBrowser(self):
        pass

    @abstractmethod
    def closeBrowser(self):
        pass

class tc1(Browser):
      def openBrowser(self):
          print("openBrowser")


      def closeBrowser(self):
          print("closeBrowser")

      def readfromExcel(self):
          print("readfromExcel")

      def runtest(self):
        self.openBrowser()
        self.closeBrowser()
        self.readfromExcel()


t = tc1()
t.runtest()
