from datetime import date, datetime


def calculate_age(dob: date) -> int:
    """Return age in years based on today's date."""
    today = date.today()
    before_birthday = (today.month, today.day) < (dob.month, dob.day)
    return today.year - dob.year - int(before_birthday)


def age_tip(age: int) -> str:
    """Return a health/life tip based on age bracket."""
    if age < 0:
        return "That age looks invalid. Please check your birth date."
    if age <= 14:
        return "Play a lot, sleep well, and keep learning new skills."
    if age <= 24:
        return "Exercise regularly, build good study/work habits, and protect your sleep."
    if age <= 39:
        return "Stay active, manage stress, and keep regular health checkups."
    if age <= 59:
        return "Prioritize strength training, balanced diet, and routine screenings."
    return "Keep moving, stay social, eat well, and follow your doctor's guidance."


def main() -> None:
    print("Welcome! Let's calculate your age.")
    name = input("What is your name? ").strip()
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ").strip()

    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
    except ValueError:
        print("Please use the YYYY-MM-DD format, e.g., 2010-04-15.")
        return

    age = calculate_age(dob)
    print(f"\nHi {name or 'there'}! You are {age} years old.")
    print(f"Tip: {age_tip(age)}")


if __name__ == "__main__":
    main()