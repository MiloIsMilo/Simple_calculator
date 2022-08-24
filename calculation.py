class Calculation():
    """Class that hold mathematical operations"""
    def __init__(self, num_1, calculations=0):
        self.num_1 = num_1
        self.calculations = calculations

    def addition(self):
        """Function that adds two numbers"""
        print(str(self.calculations) + " + " + str(self.num_1))
        self.calculations += self.num_1
        print("result: " + str(self.calculations))
        calculations = self.calculations
        return calculations

    def subtraction(self):
        """Function that subtract two numbers"""
        print(str(self.calculations) + " - " + str(self.num_1))
        self.calculations -= self.num_1
        print("result: " + str(self.calculations))
        calculations = self.calculations
        return calculations

    def multiplication(self):
        """Function that multiplicate two numbers"""
        print(str(self.calculations) + " * " + str(self.num_1))
        self.calculations *= self.num_1
        print("result: " + str(self.calculations))
        calculations = self.calculations
        return calculations

    def division(self):
        """Function that divide two numbers"""
        print(str(self.calculations) + " / " + str(self.num_1))
        self.calculations /= self.num_1
        print("result: " + str(self.calculations))
        calculations = self.calculations
        return calculations

    def reset(self):
        """Function that reset calculator"""
        calculations = float(input("\nEnter first number: "))
        return calculations