"""
BMI Calculator with tips.
Formula: BMI = weight (kg) / height (m)^2
"""


def get_bmi_category(bmi: float) -> str:
    """Return category name from BMI value."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def get_bmi_tips(bmi: float) -> list[str]:
    """
    Return tips for this BMI: one supportive (happy) and one honest/motivational.
    """
    if bmi < 18.5:
        return [
            "You're in the light range — your body might need more fuel to feel its best.",
            "Eating a bit more and some strength training can make you feel stronger and happier.",
        ]
    if bmi < 25:
        return [
            "You're in a healthy range — well done!",
            "Keep moving and eating well; your future self will thank you.",
        ]
    if bmi < 30:
        return [
            "You're carrying a bit extra — no drama, many of us do.",
            "Moving more and eating mindfully can make you feel lighter and more energetic.",
        ]
    # Obese
    return [
        "Your body is carrying extra load; it's okay to be honest with yourself.",
        "Small steps — a short walk, one less sugary drink — add up. You've got this!",
    ]


def main() -> None:
    print("BMI Calculator")
    print("You'll need your weight in kg and height in cm.")
    print("-" * 40)

    try:
        weight = float(input("Enter your weight (kg): ").strip())
        height_cm = float(input("Enter your height (cm): ").strip())
    except ValueError:
        print("Invalid input. Please enter numbers only (e.g. 70 or 175.5).")
        return

    if weight <= 0 or height_cm <= 0:
        print("Weight and height must be positive numbers.")
        return

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    category = get_bmi_category(bmi)
    tips = get_bmi_tips(bmi)

    print()
    print(f"Your BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print()
    print("Tips for you:")
    for i, tip in enumerate(tips, 1):
        print(f"  {i}. {tip}")


if __name__ == "__main__":
    main()
