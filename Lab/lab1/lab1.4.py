class Time:
    def __init__(self,HH,MM,SS):
        self.HH = HH
        self.MM = MM
        self.SS = SS
    
    def set(self,HH,MM,SS):
        self.HH = HH
        self.MM = MM
        self.SS = SS

    def get(self):
        return (self.HH, self.MM, self.SS)
    
    def print(self):
        print(f"{str(self.HH).zfill(2)}"+":"+f"{str(self.MM).zfill(2)}"+":"+f"{str(self.SS).zfill(2)}")
    
time1 = Time(9,30,0)
time1.print()