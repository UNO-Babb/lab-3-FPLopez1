#TempConvert.py
#Name: Francisco Pineda Lopez
#Date: 09/14/2025
#Assignment: Temp Converter


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter temperature in Fahrenheit: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = round((5/9) * (tempF - 32), 2)
  #Output converted temperature.
  print(tempC, "degrees celsius")

  

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
