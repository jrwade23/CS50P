# Prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636.
# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
# prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month 
# has 28, 29, 30, or 31 days.

def main():
        
    month, day, year = get_date("Date: ")

    print(f"{year}-{int(month):02}-{int(day):02}")
    
    
def get_date(prompt):  # All exceptions lead to a reprompt of date input
    while True:
        date = input(prompt).strip()
        
        try:
            m, d, y = date.split("/")  # Check if date format ##/##/####
        except ValueError:
            try:
                m, d, y = date.split(" ")  # Check if date format 'Month' Day, Year
            except ValueError:
                pass

            try:
                m, d, y = make_date_numerical(m, d, y)  
            except (ValueError, UnboundLocalError, AttributeError):
                pass

        try:
            if m == None or int(m) > 12 or int(d) > 31:  # Month/Day limits and month input not found in list
                pass
            else:
                return m, d, y
        except (ValueError, UnboundLocalError):
            pass


def make_date_numerical(x, y, z):  # If date format is 'Month' Day, Year; convert month and remove ',' after day

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    x = x.lower().title()

    try:
        m_index = months.index(x) + 1
    except ValueError:
        m_index = None

    y = y.removesuffix(",")

    return m_index, y, z
    

main()