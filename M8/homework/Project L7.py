# Program to check exam eligibility

# Minimum requirements
MIN_ATTENDANCE = 75   # in percentage
MIN_MARKS = 40        # minimum internal marks

# Taking input from user
name = input("Enter your name: ")
attendance = float(input("Enter your attendance percentage: "))
marks = float(input("Enter your internal marks: "))

# Checking eligibility
if attendance >= MIN_ATTENDANCE and marks >= MIN_MARKS:
    print(f"✅ {name}, you are eligible to sit in the exam.")
elif attendance < MIN_ATTENDANCE and marks < MIN_MARKS:
    print(f"❌ {name}, you are NOT eligible due to low attendance and low marks.")
elif attendance < MIN_ATTENDANCE:
    print(f"❌ {name}, you are NOT eligible due to low attendance.")
else:
    print(f"❌ {name}, you are NOT eligible due to low marks.")
