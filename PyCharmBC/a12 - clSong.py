lisPlayList = []

# Class called clSong
class clSong:
    def __init__ (self, strTitle, strYear, strRating):
        self.strTitle = strTitle
        self.strYear = strYear
        self.strRating = strRating
        self.whSong = input
        self.conf = input

    def setYear(self,strYear):
        self.strYear = strYear

    def getYear(self):
        return self.strYear

def mainMenu():
    print("Choose one of the following:")
    print("1. View All")
    print("2. Add Song")
    print("3. Delete Song")
    print("4. Update Rating")
    print("5. Exit")

def view_all():
    try:
        print(song.strTitle + song.strYear + song.strRating)
    except:
        print("Invalid selection or no songs in library")

def add_song():
    song.strTitle = input("What is the new song?")
    song.strYear = input("Year?")
    song.strRating = input("Rating?")
    print(song.strTitle + song.strYear + song.strRating)

def remove_song():
    view_all()
    try:
        whSong = input("Which song number would you like removed?")
        if whSong == "1":
            conf = input("Are you sure")
            if conf == "y":
                del song.strTitle, song.strYear, song.strRating
            else:
                print("Never mind then")
        else:
            print("Invalid selection")
    except:
        print("Invalid selection or no songs in library")

def update_rating():
    try:
        song.strRating = input("What is the new rating?")
        print(song.strTitle + song.strYear + song.strRating)
    except:
        print("Invalid selection or no songs in library")

lisPlayList.append(clSong("Thriller ", "1988 ", "4.9"))

while True:
    mainMenu()
    strMenu = input(":")

    if strMenu == "1":
        for song in lisPlayList:
            view_all()
    elif strMenu == "2":
        for song in lisPlayList:
            add_song()
    elif strMenu == "3":
        for song in lisPlayList:
            remove_song()
    elif strMenu == "4":
        for song in lisPlayList:
            update_rating()
    elif strMenu == "5":
        break