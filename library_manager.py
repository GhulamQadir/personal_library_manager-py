booksDict:dict={}

# add book function
def addBook():
    print("Add a book")
    title:str = input("Enter the book title:\t").capitalize()
    author:str = input("Enter the author:\t").capitalize()
    pubYear:int = int(input("Enter the publication year(Like this: 2002):\t"))
    genre:str = input("Enter the genre:\t").capitalize()
    readStatus:str = input("Have you read this book?(Yes/No):\t").capitalize()

    if readStatus=="Yes":
        readStatus=True
    else:
        readStatus=False
        
    booksDict[title] = {"title":title,"author":author,"publishedYear":pubYear,"genre":genre,"readStatus":readStatus}
    print(booksDict)
 
 
 
def removeBook():
    print("Remove book")

def searchBook():
    print("Search book")

def displayAllBooks():
    print("Display books")

def displayStatistics():
    print("Display Statistics")



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
                displayAllBooks()
            elif choice==5:
                displayStatistics()
            elif choice==6:
                break
        except ValueError as e:
            print(f"Invalid value: {e}")
            break
libraryManager()