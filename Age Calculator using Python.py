def ageCalculator():
    import datetime

    # Getting input from the user
    y = int(input("Enter the year of birth (YYYY): "))
    m = int(input("Enter the month of birth (MM): "))
    d = int(input("Enter the day of birth (DD): "))

    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365.25)
    
    print("Your age is:", age)

# Call the function to calculate age
ageCalculator()
