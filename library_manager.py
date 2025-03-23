booksDict:dict={}  # BOOKS DICTIONARY(LIBRARY)

# add book function
def addBook():
    print("Add a book")
    title:str = input("Enter the book title:\t").title()
    author:str = input("Enter the author:\t").title()
    pubYear:int = int(input("Enter the publication year(Like this: 2002):\t"))
    genre:str = input("Enter the genre:\t").title()
    readStatus:str = input("Have you read this book?(Yes/No):\t").capitalize()

    if readStatus=="Yes":
        readStatus=True
    else:
        readStatus=False
        
    global booksDict
    booksDict[title] = {"title":title,"author":author,"publishedYear":pubYear,"genre":genre,"readStatus":readStatus}
 
 
# remove specific book
def removeBook():
    global booksDict
    if len(booksDict) < 1:
        print("Your library is currently empty")
    else:
        bookToRemove = input("Enter the title of the book to remove:\t").title()
        if bookToRemove in booksDict:
            tempData = booksDict.copy()
            del tempData[bookToRemove]
            booksDict=tempData
            print(booksDict)
        else:
            print("Book not found!")


# search for a specific book
def searchBook():
    global booksDict
    if len(booksDict)<1:
        print("Your library is currently empty!")
    else:
        searchedBook = input("Enter book title:\t").title()
        if searchedBook in booksDict:
            title,author,pubYear,genre,readStatus= booksDict[searchedBook].values()
            print(f"""Matching Book:
{title} by {author} ({pubYear}) - {genre} - {readStatus}""")
        else:
            print("Book not found!")


# display all books
def displayAllBooks(booksDict):
    if len(booksDict)<1:
        print("Your library is currently empty!")
    else:
        print("Your Library:")
        for index, books in enumerate(booksDict.values()):
            title,author,pubYear,genre,readStatus = books.values()
            print(f"{index+1}. {title} by {author} ({pubYear}) - {genre} - {readStatus}")
    

# display statistics (how many books are added in library and which how many are read)
def displayStatistics(booksDict):
    
    if len(booksDict)<1:
        print("Your library is currently empty!")
    else:
        readCount=0
        for book in booksDict.values():
            if book["readStatus"] is True:
                print(book)
                readCount+=1
                    
        readPercentage:float = round((readCount/len(booksDict))*100,2)
        print(f"Total Books: {len(booksDict)}\nPercentage read: {readPercentage}%")



# starting function
def libraryManager():
    print("Welcome to your personal Library Manager!")
    while True:
        try:
            print("""1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display Statistics
6. Exit""")          
        
            choice = int(input("Enter your choice:\t"))
            if choice==1:
                addBook()
            elif choice==2:
                removeBook()
            elif choice==3:
                searchBook()
            elif choice==4:
                displayAllBooks(booksDict)
            elif choice==5:
                displayStatistics(booksDict)
            elif choice==6:
                break
        except ValueError as e:
            print(f"Invalid value: {e}")
            break
libraryManager()
