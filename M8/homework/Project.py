import datetime, calendar
# using now() to get current time
current_time = datetime.datetime.today()
#printing value of now.
print("Time now at greenwich meridian is:", current_time)
# print calender of year 2025
print("\n", calendar.calendar(2025))


# Birthday Reminder App 🎂

# दोस्तों और परिवार के जन्मदिन डिक्शनरी में
birthdays = {
    "Banita": "20 May 1985",
    "Pawan": "23 July 1989",
    "Vijay": "16 January 1985",
    "Sharmila": "08 October 1991",
    "Priyanshu": "10 February 2012"
}

# यूज़र से नाम लेना
name = input("नाम दर्ज करें: ").strip().lower()

# चेक करना कि नाम डिक्शनरी में है या नहीं
if name in birthdays:
    print(f"{name.capitalize()} का जन्मदिन है: {birthdays[name]}")
else:
    print("डेटा नहीं मिला")