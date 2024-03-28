import math
class AreaCalculator:

    def circleArea(self, radius):
        areaC = math.pi * radius **2
        return areaC
    
    def trapArea(self, a, b, h):
        areaT = 0.5 * (a + b) * h
        return areaT
    
    def rhombArea(self, a, q):
        areaR = a * q / 2
        return areaR
    
    def ellipseArea(self, axisA, axisB):
        areaE = math.pi * axisA * axisB
        return areaE
    
def UserInput():
        shapeInput = input("Please enter the shape you would like to get area of: ")
        return shapeInput
    
def main():
        calculator = AreaCalculator()
        shape = UserInput()

        if shape == "circle":
            radiusInput = float(input("Please enter the radius of the cirlce: "))
            output = calculator.circleArea(radiusInput)
            print(f"The Area Of The Cirlce Is: " , math.ceil(output*100)/100)
            

        elif shape == "trapezoid":
            inputA = float(input("Please enter the length of a: "))
            inputB = float(input("Please enter the length of b: "))
            inputH = float(input("Please enter the length of height: "))
            output = calculator.trapArea(inputA, inputB, inputH)
            print("The Area Of The Trapezoid Is: " , math.ceil(output*100)/100)

            

        elif shape == "rhombus":
            aInput = float(input("Please enter number for the a: "))
            qInput = float(input("Please enter number for the b: "))
            output = calculator.rhombArea(aInput,qInput)
            print("The Area Of The Rhombus Is: " , math.ceil(output*100)/100)
            


        elif shape =="ellipse":
            inputAxis = float("Please input the a axis: ")
            inputBaxix = float("Please input the b axis: ")
            output = calculator.ellipseArea(inputAxis, inputBaxix)
            print("The Area Of The Ellipse Is: " , math.ceil(output*100)/100)
        else:
            print("Please input a valid shape")
            
if __name__ =="__main__":
    main()