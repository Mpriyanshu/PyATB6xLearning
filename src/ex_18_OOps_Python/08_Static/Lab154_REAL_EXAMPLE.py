class ExcelReader:
    @staticmethod
    def readexcelFile():
        print("Reading Excel File")

class MYSQLDBConnection:
    @staticmethod
    def readMySQLFile():
        print("Reading MySQL File")

class TC1:

    def runTC(self):
        ExcelReader.readexcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("HI")

class TC2:

    def runTC(self):
        ExcelReader.readexcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("HI")

tc1 = TC1()
tc2 = TC2()
tc1.runTC()
tc2.runTC()