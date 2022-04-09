import requests
import datetime
# Use os.path to write output to different directory
import os.path

# --- Defang date time ---
def defang_datetime():
    current_datetime = f'_{datetime.datetime.now()}'
    #length_current_datetime = len(current_datetime)

    '''for chars in current_datetime:
        #print(chars)
        if chars == '.' or ':':
            #chars = "_"
            chars.replace(chars, '_')'''
    
    current_datetime = current_datetime.replace(":","_")
    current_datetime = current_datetime.replace(".","-")
    current_datetime = current_datetime.replace(" ","_")
    
    #print(current_datetime)
    return current_datetime

# --- 

## main


output = defang_datetime()

print(output)