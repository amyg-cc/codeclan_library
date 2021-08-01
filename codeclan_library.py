library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# from art import *
# Art=text2art(f'{library["name"]}') # Return ascii text (default font) and default chr_ignore=True 
# print(Art)

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...")
        print(f'The books we habe available are: {library["books"]}')

    if option == "2":
        print("Searching for a book by title...")
        search = input("Input the Title of the book you're looking for: ")
        book_exists = False
        for book in library["books"]:
            if search == book["title"]:
                book_exists = True
                search_result = book
        if book_exists == True:
            search_result_title = search_result["title"]
            search_result_author = search_result["author"]
            print(f"Yes, we have {search_result_title} by {search_result_author} in our library.")
        else:
            print(f"Sorry, we don't have {search} in our library.")
        
    if option == "3":
        print("Adding a book...")
        book_title = input("Enter the book title you wish to add: ")
        book_author = input("Who is the author of that book?: ")
        book_addition = {"title": book_title, "author": book_author}
        library["books"].append(book_addition)

    if option == "4":
        print("Removing a book...")
        delete_request = input("What is the title of the book you wish to delete?: ")
        delete_request_valid = False
        for book in library["books"]:
            if delete_request == book["title"]:
                delete_request_valid = True
                delete_selection = book 
        if delete_request_valid == True:
            library["books"].remove(delete_selection)
            print(f"{delete_request} has been removed from the Library.")
        else:
            print(f"We couldn't find {delete_request} in our Library.")

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book