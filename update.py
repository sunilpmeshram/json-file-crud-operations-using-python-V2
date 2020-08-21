from movies import MoviesClass

try:
    movieObj = MoviesClass()
    title = str(input("Please enter title: "))
    res = movieObj.update_record(title)

    if res:
        print("Title updated Successfully!")
    else:
        print("Error!")

except Exception as e:
    print("Error message: ", e)
