import PIL

def intro():
    print("#"*80)
    print("Old School Photo")
    print("#"*80)

def edges():
    from PIL import Image
    img = Image.open('picture.png')
    img.load()
    from PIL import ImageFilter
    img_gray = img.convert("L")
    edges = img_gray.filter(ImageFilter.FIND_EDGES)
    edges.show()
    maySave = input("Would you like to save this picture? ")
    if maySave == "y":
        edges.save("edges.png")
    else:
        print("Never mind")

def emboss():
    from PIL import Image
    img = Image.open('picture.png')
    img.load()
    from PIL import ImageFilter
    emboss = img.filter(ImageFilter.EMBOSS)
    emboss.show()
    maySave = input("Would you like to save this picture? ")
    if maySave == "y":
        emboss.save("emboss.png")
    else:
        print("Never mind")


while True:
    intro()
    whImage = input("Which image would you like to add a filter too? You can do: picture.png(1): please enter 1: ")
    if whImage == "1":
        whFilter = input("Which filter would you like to apply? edges, or emboss: ")
        if whFilter == "edges":
            edges()
        elif whFilter == "emboss":
            emboss()
        else:
            print("Filter not found")
    else:
        print("Not valid")


    more = input("Anything else?")
    if more != "y":
        break

