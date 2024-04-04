import datetime

def text_dump(input):
    error_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # names the file after the current date and time to prevent duplicates
    with open(f"error{error_time}.txt", 'w') as x:
        x.write(input) # writes information on the error
