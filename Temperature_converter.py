#Temp.pt.py
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def temperature_convertor():
    print(f"Temperature Convertor:")
    print(f"Select Your Choice: ")
    print(f"1. Celsius to fahrenheit: ")
    print(f"2. Fahrenheit to celsius:")
    choice = input("Enter Your Choice (1 or 2): ")
    if choice == '1':
        celsius_temperature = float(input("Enter Your celsius temperature: "))
        fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
        print(f"{celsius_temperature} celsius is equal to {fahrenheit_temperature: } fahrenheit.")
    else:
        fahrenheit_temperature = float(input("Enter Your fahrenheit temperature: "))
        celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
        print(f"{fahrenheit_temperature} fahrenheit is equal to {celsius_temperature: } celsius.")
if __name__ == '__main__':
    temperature_convertor()