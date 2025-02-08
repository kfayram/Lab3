#TempConvert.py
#Name: Kyle Fayram 
#Date: 2/8/25
#Assignment: lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = float(input("Enter temperature in Fahrenheit to convert to Celsius. "))

  tempC = (tempF - 32) * 5 / 9
  tempCR = round(tempC, 1)

  print(tempF, "degrees Fahrenheit is", tempCR, "degrees celsius.")
if __name__ == '__main__':
  main()
