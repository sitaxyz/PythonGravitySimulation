import datetime

def seconds_to_date(seconds):
    date = datetime.datetime.fromtimestamp(seconds)
    return date.strftime('%Y:%m:%d:%H:%M:%S')

print(seconds_to_date(100))