def celsius_to_fahrenheit(celsius):
    try:
        return (float(celsius) * 9/5) + 32
    except ValueError:
        return "Invalid input"
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit("abc"))
print(celsius_to_fahrenheit(25.55))