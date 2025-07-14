# Book Catalogue 

def add_book(collection, title, author, genre, isbn, tags):
    """add a book to the collection - outputs collection with new book"""
    isbn_conflict = False

    for i in range(0, len(collection)):
        if isbn in collection[i].values():
            isbn_conflict = True
            break

    if isbn_conflict:
        print("ISBN already taken.")
        return collection
    
    book = {}
    book["title"] = title
    book["author"] = author
    book["genre"] = genre
    book["isbn"] = isbn
    book["tags"] = tags
    collection.append(book)
    print(f"{title} added to your collection.")
    return collection

def input_add_book(collection):
    """take user input to add a book"""
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    isbn = input("ISBN: ")
    tags = input("Tags (seperate tags with a comma and space): ")

    tags = set(tags.split(", "))

    collection = add_book(collection, title, author, genre, isbn, tags)

    return collection

def print_book(book):
    """print a book"""
    for key in book.keys():
        key_up = key
        print(f"{key_up[0].upper() + key_up[1:]}: {book[key]}")

def print_collection(collection):
    """print all the books in your collection"""
    for i in range(0, len(collection)):
        book = collection[i]
        print_book(book)
        print()

def search_by_tags(collection, tags):
    """searches through tags and returns all books with those tags"""
    searched = []
    for i in range(0, len(collection)):
        if tags.issubset(collection[i]["tags"]):
            searched.append(collection[i])
    return searched

def input_to_set(text):
    """turns string of tags into a set"""
    user_input = input(text)
    user_set = set(user_input.split(", "))
    return user_set

def search_by_isbn(collection, isbn):
    found = {}

    for i in range(0, len(collection)):
        if isbn == collection[i]["isbn"]:
            found = collection[i]
            break

    return found

isbn_conflict = False
collection = []
collection = add_book(collection, "Test Book", "Test", "Test", '1234', {"test", 'test1', 'test2'})

while True:
    print("Options:")
    print("0: Quit")
    print("1: Print Collection")
    print("2: Add a Book")
    print("3: Remove a Book")
    print("4: Search by Tags")
    print("5: Search by ISBN")


    user_input = input("Choose Option: ")

    print()

    if user_input not in ["0", "1", "2", '3', '4', '5']:
        print("Invalid Input\n")
        continue

    if user_input == "0":
        print("Goodbye")
        break
    elif user_input == "1":
        print_collection(collection)
    elif user_input == "2":
        collection = input_add_book(collection)
        print()
    elif user_input == '3':
        pass
    elif user_input == '4':
        tags_to_search = input_to_set("Tags (seperate tags with a comma and space): ")
        print()
        searched = search_by_tags(collection, tags_to_search)
        if searched == []:
            print("No books with those tags in collection.\n")
        else:
            print(f'Found {len(searched)} books with those tags:\n')
            print_collection(searched)
    elif user_input == "5":
        isbn_search = input("Enter ISBN: ")
        found = search_by_isbn(collection, isbn_search)
        if found == {}:
            print("ISBN not in collection.\n")
        else:
            print("Found matching ISBN:\n")
            print_book(found)
