from movies import MoviesClass

try:
    movieObj = MoviesClass()

    new_movie = dict()

    Title = str(input("Please enter title: "))
    if Title == '':
        new_movie['Title'] = None
    else:
        new_movie['Title'] = Title

    US_Gross = int(input("Please enter gross: "))
    if US_Gross == 0:
        new_movie['US_Gross'] = None
    else:
        new_movie['US_Gross'] = US_Gross

    Worldwide_Gross = int(input("Please Worldwide Gross: "))
    if Worldwide_Gross == 0:
        new_movie['Worldwide_Gross'] = None
    else:
        new_movie['Worldwide_Gross'] = US_DVD_Sales

    US_DVD_Sales = int(input("Please enter DVD Sales: "))
    if US_DVD_Sales == 0:
        new_movie['US_DVD_Sales'] = None
    else:
        new_movie['US_DVD_Sales'] = US_DVD_Sales

    Production_Budget = int(input("Please enter Production Budget: "))
    if Production_Budget == 0:
        new_movie['Production_Budget'] = None
    else:
        new_movie['Production_Budget'] = US_DVD_Sales

    Release_Date = str(input("Please enter Release_Date: "))
    if Release_Date == 0:
        new_movie['Release_Date'] = None
    else:
        new_movie['Release_Date'] = US_DVD_Sales

    MPAA_Rating = str(input("Please enter MPAA Rating: "))
    if MPAA_Rating == 0:
        new_movie['MPAA_Rating'] = None
    else:
        new_movie['MPAA_Rating'] = US_DVD_Sales

    Running_Time_min = float(input("Please enter Running Time in min: "))
    if Running_Time_min == 0:
        new_movie['Running_Time_min'] = None
    else:
        new_movie['Running_Time_min'] = US_DVD_Sales

    Distributor = str(input("Please enter Distributor: "))
    if Distributor == 0:
        new_movie['Distributor'] = None
    else:
        new_movie['Distributor'] = US_DVD_Sales

    Source = str(input("Please enter Source: "))
    if Source == 0:
        new_movie['Source'] = None
    else:
        new_movie['Source'] = US_DVD_Sales

    Major_Genre = str(input("Please enter Major Genre: "))
    if Major_Genre == 0:
        new_movie['Major_Genre'] = None
    else:
        new_movie['Major_Genre'] = US_DVD_Sales

    Creative_Type = str(input("Please enter Creative Type: "))
    if Creative_Type == 0:
        new_movie['Creative_Type'] = None
    else:
        new_movie['Creative_Type'] = US_DVD_Sales

    Director = str(input("Please enter Director: "))
    if Director == 0:
        new_movie['Director'] = None
    else:
        new_movie['Director'] = US_DVD_Sales

    Rotten_Tomatoes_Rating = float(input("Please enter Rotten Tomatoes Rating: "))
    if Rotten_Tomatoes_Rating == 0:
        new_movie['Rotten_Tomatoes_Rating'] = None
    else:
        new_movie['Rotten_Tomatoes_Rating'] = US_DVD_Sales

    IMDB_Rating = float(input("Please enter IMDB Rating: "))
    if IMDB_Rating == 0:
        new_movie['IMDB_Rating'] = None
    else:
        new_movie['IMDB_Rating'] = US_DVD_Sales

    IMDB_Votes = int(input("Please enter IMDB Votes: "))
    if IMDB_Votes == 0:
        new_movie['IMDB_Votes'] = None
    else:
        new_movie['IMDB_Votes'] = US_DVD_Sales

    res = movieObj.add_record(new_movie)
    if res:
        print("Record added successfully!")
    else:
        print("Error!")
except Exception as e:
    print("Error message: ", e)