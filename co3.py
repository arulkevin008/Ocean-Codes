class electronics:
    def __init__(self,computer,mouse,keyboard):
        self.computer=computer
        self.mouse=mouse
        self.keyboard=keyboard
    
    def information(self):
        print(f"Computer:{self.computer},Mouse:{self.mouse},Keyboard:{self.keyboard}")

details=electronics("Zebronics","HP","Dell")
details.information()