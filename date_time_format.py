import datetime

# formatted date and time for output file names and breakpoints
def get_formatted_date_time():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")