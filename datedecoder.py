def convert_date(date_str):
# Split the date string into day, month, and year parts
    day, month, year = date_str.split("-")

# Convert the month abbreviation to a number
    month_num = {
        "JAN": "01",
        "FEB": "02",
        "MAR": "03",
        "APR": "04",
        "MAY": "05",
        "JUN": "06",
        "JUL": "07",
        "AUG": "08",
        "SEP": "09",
        "OCT": "10",
        "NOV": "11",
        "DEC": "12"
    }[month.upper()]

# Combine the day, month, and year parts into a formatted date string
    year = "20" + year if int(year) < 70 else "19" + year
    date_formatted = f"{day}-{month_num}-{year}"

    return date_formatted


date_str = "8-MAR-85"
converted_date_str = convert_date(date_str)
print(converted_date_str)

#Create a dict suitable for decoding month names to numbers.
month_dict = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}
month_name = 'MAR'
month_num = month_dict[month_name]
print(month_num)

#Create a function which uses string operations to split the date into 3 items using the "-" character
def split_date(date_str):
    day, month, year = date_str.split("-")
    return day, month, year

date_str = "8-MAR-85"
day, month, year = split_date(date_str)
print(day)
print(month)
print(year)

#Translate the month, correct the year to include all of the digits.
def process_date(date_str):
    # Split the date string into day, month, and year parts
    day, month, year = date_str.split("-")

    # Translate the month abbreviation to a number
    month_dict = {
        'JAN': 1,
        'FEB': 2,
        'MAR': 3,
        'APR': 4,
        'MAY': 5,
        'JUN': 6,
        'JUL': 7,
        'AUG': 8,
        'SEP': 9,
        'OCT': 10,
        'NOV': 11,
        'DEC': 12
    }
    month_num = month_dict[month.upper()]

    # Correct the year to include all of the digits
    year = '19' + year if int(year) >= 0 and int(year) <= 21 else '20' + year

    return day, str(month_num), year

date_str = "8-MAR-85"
day, month, year = process_date(date_str)
print(day)
print(month)
print(year)

#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).
def process_date(date_str):
    # Translate the month abbreviation to a number
    month_dict = {
        'JAN': 1,
        'FEB': 2,
        'MAR': 3,
        'APR': 4,
        'MAY': 5,
        'JUN': 6,
        'JUL': 7,
        'AUG': 8,
        'SEP': 9,
        'OCT': 10,
        'NOV': 11,
        'DEC': 12
    }
    day, month, year = date_str.split('-')
    year = '20' + year if int(year) < 50 else '19' + year
    month_num = month_dict[month.upper()]

    return year, str(month_num), day

#call function in the string argument
date_str = "8-MAR-85"
year, month, day = process_date(date_str)
print(year)
print(month)
print(day)
