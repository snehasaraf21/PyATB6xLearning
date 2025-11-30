class ExcelReader:
    @staticmethod
    def readExcelFile():
        print("Reading Excel File")

class MySQLDBConnection:
    @staticmethod
    def readMySQLFile():
        print("Reading from MYSQL File")

class TC1:
    def runTC(self):
        ExcelReader.readExcelFile()
        MySQLDBConnection.readMySQLFile()
        print("MySQL Connection Complete")

class TC2:
    def runTC(self):
        ExcelReader.readExcelFile()
        MySQLDBConnection.readMySQLFile()
        print("MySQL Connection Complete")

t1 = TC1()
t2= TC2()
t1.runTC()
t2.runTC()

