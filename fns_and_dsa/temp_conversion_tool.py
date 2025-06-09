FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def temperature_converter():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        temperature = float(temp_input)

        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result:.2f}°C")
        else: 
            print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        raise ValueError("Please enter a numeric value.")
    
temperature_converter()