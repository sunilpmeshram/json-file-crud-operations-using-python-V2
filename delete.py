from movies import MoviesClass

try:
    movieObj = MoviesClass()
    title = str(input("Please enter title: "))
    res = movieObj.delete_record(title)

    if res:
        print("Record deleted successfully!")
    else:
        print("Error!")

except Exception as e:
    print("Error message: ", e)
