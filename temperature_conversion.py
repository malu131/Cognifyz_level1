def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_temperature(value, unit):
    if unit.lower() == 'c':
        return celsius_to_fahrenheit(value), 'F'
    elif unit.lower() == 'f':
        return fahrenheit_to_celsius(value), 'C'
    else:
        return None, None


# Main program
if __name__ == "__main__":
    user_input = input("Enter the temperature value: ")
    unit_input = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")

    try:
        temperature_value = float(user_input)
        converted_value, converted_unit = convert_temperature(temperature_value, unit_input)

        if converted_value is not None:
            print(f"{temperature_value}°{unit_input.upper()} is equal to {converted_value:.2f}°{converted_unit}")
        else:
            print("Invalid unit entered. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
