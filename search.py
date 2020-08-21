from movies import MoviesClass

try:
    movieObj = MoviesClass()
    title = str(input("Please enter title: "))
    print(movieObj.find_record(title))

except Exception as e:
    print("Error message: ", e)

