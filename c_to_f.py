"""Convert Celsius to Fahrenheit with input validation."""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using F = (C * 9/5) + 32."""
    return (celsius * 9 / 5) + 32


def main() -> None:
    print("Celsius to Fahrenheit Converter")
    user_input = input("Enter temperature in Celsius: ").strip()

    try:
        celsius = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a number, e.g. 25 or -3.5.")
        return

    fahrenheit = celsius_to_fahrenheit(celsius)
    # :.2f formats the number to 2 decimal places
    print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")


if __name__ == "__main__":
    main()

