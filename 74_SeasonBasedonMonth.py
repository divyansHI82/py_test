# Write a python code to demonstrate season based on month.

def get_season(month):
    month = month.lower()

    if month in ("december", "january", "february"):
        return "Winter"
    elif month in ("march", "april", "may"):
        return "Spring"
    elif month in ("june", "july", "august"):
        return "Summer"
    elif month in ("september", "october", "november"):
        return "Autumn"
    else:
        return "Invalid month name."

# User input
user_input = input("Enter the name of a month: ")
season = get_season(user_input)

# Output
print(f"The season in {user_input.capitalize()} is: {season}")

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
