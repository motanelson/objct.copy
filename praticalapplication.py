class state3:
    def __init__(self,red:float,green:float,blue:float):
        self.red=red
        if red>1.00:
            self.red=1.00
        self.green=green
        if green>1.00:
            self.green=1.00
        self.blue=blue
        if blue>1.00:
            self.blue=1.00

    def report(self):
        print("RED : "+str(int(self.red * 100.00)))
        print("GREEN : "+str(int(self.green * 100.00)))
        print("BLUE : "+str(int(self.blue * 100.00)))



a=state3(0.10,0.50,1.10)

a.report()