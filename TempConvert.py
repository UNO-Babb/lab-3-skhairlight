#TempConvert.py
#Name: Salsabiel Khair Allah
#Date: Sep.14
#Assignment: Lab 3


def main():
    # Prompt the user for a Fahrenheit temperature
    tempF = float(input("Enter temperature in Fahrenheit: "))

    # Convert that temperature to Celsius, rounding to 1 decimal precision
    tempC = round((5/9) * (tempF - 32), 1)

    # Output converted temperature
    print(tempF, "degrees Fahrenheit is", tempC, "degrees Celsius.")

if __name__ == '__main__':
    main()

