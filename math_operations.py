from breezypythongui import EasyFrame
import math
class Operations(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title="Math Operations", width=300, height=200)
        self.addLabel(text="Enter a positive number:", row=0, column=0)
        self.numberField = self.addIntegerField(value=0.0, row=0, column=1, width=10)
        self.addButton(text="Calculate Factorial", row=1, column=0, columnspan=2, command=self.calculateFactorial)
        self.addButton(text="Calculate Square Root", row=2, column=0, columnspan=2, command=self.calculateSquareRoot)
        self.addLabel(text="Factorial:", row=3, column=0)
        self.factorialField = self.addIntegerField(value=0.0, row=3, column=1)
        self.addLabel(text="Square Root:", row=4, column=0)
        self.sqrtField = self.addFloatField(value=0.0, row=4, column=1)

    def calculateFactorial(self):
            number = int(self.numberField.getNumber())
            result = math.factorial(number)
            self.factorialField.setNumber(result)
    
    def calculateSquareRoot(self):
        number = self.numberField.getNumber()
        if number >= 0:
            result = math.sqrt(number)
            self.sqrtField.setNumber(result)

if __name__ == "__main__":
    Operations().mainloop()
