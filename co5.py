class season:
    def __init__(self,months,season):
        self.months=months
        self.season=season
    
    def month(self):
        print(f"Month:{self.months}")

data1=season("May","Summer")
data2=season("December","Winter")
print(data1.season)
data1.month()
print(data2.season)
data2.month()