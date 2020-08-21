from datetime import datetime
from movies import MoviesClass

try:
    movieObj = MoviesClass()
    key_type = int(input("Please Press 1 for list by Genre or 2 for release date and enter: "))
    if key_type == 1:
        key = 'Major_Genre'
        value = str(input("Please enter Genre: "))
    elif key_type == 2:
        key = 'Release_Date'
        value = int(input("Please enter Release Date: "))
    else:
        raise Exception("Invalid Input!")

    print(movieObj.listing(key, value))

except Exception as e:
    print("Error message: ", e)

