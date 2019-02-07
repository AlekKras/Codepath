import unittest
import random
class Testing(unittest.TestCase):
    def test_int(self):
        weight = int(random.randrange(-1000,1000))
        height = int(random.randrange(-1000, 1000))
        self.assertNotEqual(weight, height)

def check_weight():
    try:
        global weight
        weight = int(input("What is your weight? \n"))
        if (weight < 0) or (weight > 1000):
            print("Invalid weight")
            print("Please, put the CORRECT weight!!!")
            check_weight()
        else:
            pass
    except:
        print("Please, put the right weight!")
        check_weight()
check_weight()

def check_height():
    try:
        global height
        height = int(input("What is your height? \n"))
        if (height<10) or (height > 2000):
            print("Invalid height")
            print("Please, put the CORRECT height")
            check_height()
    except:
        print("Please, put the correct height!")
        check_height()
check_height()
def main(weight, height):
    print("Your Weight is " + str(weight))
    print("Your Height is " + str(height))
    BMI = (weight * 703) / (height * height)
    print("Your BMI is " + str(float(BMI)))
main(weight, height)
if __name__ == "__main__":
    unittest.main()
