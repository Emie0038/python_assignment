

#4. Decode date
def decode_date(date_str):
    month_dict = {
        'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04',
        'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08',
        'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'
    }
    day, month_str, year = date_str.split('-')
    month = month_dict[month_str.upper()]

    if int(year) < 30:
        year = '20' + year
    else:
        year = '19' + year
    return (int(year), int(month), int(day))
print(decode_date('23-FEB-23'))



#Detailed with comments

def decode_date(date_str):
    # Create a dictionary to decode month names to numbers
    month_dict = {
        'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04',
        'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08',
        'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'
    }

    # Split the date into day, month, and year
    day, month, year = date_str.split('-')

    # Correct the year to include all of the digits
    if int(year) < 50:
        year = '20' + year
    else:
        year = '19' + year

    # Translate the month abbreviation to a number
    month_num = month_dict[month]

    # Return the year, month, and day as a tuple
    return year, month_num, day


#e.g
date_str = '23-MAR-22'
y, m, d = decode_date(date_str)
print(y, m, d)