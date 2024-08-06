from lib.utilityFunctions import askMenu
from lib.coreFunctions import checkout_book, return_book, build_author_class_from_data, build_genre_class_from_data, build_member_class_from_data, build_book_class_from_data, edit_book, create_book, create_author, create_genre, create_member, select_author, select_book, select_genre, select_member, delete_author, delete_genre, delete_member, delete_book, edit_author, edit_genre, edit_member
from lib.mySQLFunctions import authenticate_superuser, get_all_authors, get_all_books, get_all_genres, get_all_members
    
def main():
    member_name = authenticate_superuser()
    if member_name != -1:
        print(f"Welcome to the Library Management System, {member_name}!")
    while True and member_name != -1:
        try:
            user_input = askMenu([
            "Book Operations", 
            "Member Operations", 
            "Author Operations", 
            "Genre Operations", 
            "Quit program"], 
            "Please choose an operation: ")
            if user_input == 1:
                user_input = askMenu([
                "Add a new book", 
                "View book details", 
                "Edit a book",
                "Delete a book",
                "Display all books",
                "Borrow a book", 
                "Return a book", 
                "Quit to main menu"], 
                "Please choose an operation: ")
                if user_input == 1:#Add book
                    create_book()
                elif user_input == 2:#View book details
                    book = select_book()
                    if book != -1:
                        book.info()
                elif user_input == 3:#Edit book
                    edit_book()
                elif user_input == 4:#View author
                    delete_book()
                elif user_input == 5:#Display all books
                    books = [build_book_class_from_data(c) for c in get_all_books()]
                    if books == -1:
                        return -1
                    book_names = [f"{book.get_book_name()} - {book.get_book_description()}" for book in books]
                    for name in book_names:
                        print(name)
                elif user_input == 6:#Borrow book
                    checkout_book()
                elif user_input == 7:#Return book
                    return_book()
                elif user_input == 8:#Quit
                    continue
            elif user_input == 2:
                user_input = askMenu([
                "Add a member", 
                "View member details",
                "Edit a member",
                "Delete a member",
                "Display all members", 
                "Quit to main menu"], 
                "Please choose an operation: ")
                if user_input == 1:#Add member
                    create_member()
                elif user_input == 2:#View member details
                    member = select_member()
                    if member != -1:
                        member.info()
                elif user_input == 3:#Edit author
                    edit_member()
                elif user_input == 4:#View author
                    delete_member()
                elif user_input == 5:#Display all members
                    members = [build_member_class_from_data(c) for c in get_all_members()]
                    if members == -1:
                        return -1
                    member_names = [f"{member.get_member_name()} - {member.get_library_id()}" for member in members]
                    for name in member_names:
                        print(name)
                elif user_input == 6:#Quit to menu
                    continue
            elif user_input == 3:
                user_input = askMenu([
                "Add an author", 
                "View author details", 
                "Edit an author",
                "Delete an author",
                "Display all authors",
                "Quit to main menu"], 
                "Please choose an operation: ")
                if user_input == 1:#Add author
                    create_author()
                elif user_input == 2:#View author details
                    author = select_author()
                    if author != -1:
                        author.info()
                elif user_input == 3:#Edit author
                    edit_author()
                elif user_input == 4:#View author
                    delete_author()
                elif user_input == 5:#Display all authors
                    authors = [build_author_class_from_data(c) for c in get_all_authors()]
                    if authors == -1:
                        return -1
                    author_names = [f"{author.get_author_name()} - {author.get_author_description()}" for author in authors]
                    for name in author_names:
                        print(name)
                elif user_input == 6:#Quit to menu
                    continue
            elif user_input == 4:
                user_input = askMenu([
                "Add a genre", 
                "View genre details", 
                "Edit a genre",
                "Delete a genre",
                "Display all genres", 
                "Quit to main menu"], 
                "Please choose an operation: ")
                if user_input == 1:#Add genre
                    create_genre()
                elif user_input == 2:#View genre details
                    genre = select_genre()
                    if genres == -1:
                        print(genre.info())
                elif user_input == 3:#Edit genre
                    edit_genre()
                elif user_input == 4:#Delete genre
                    delete_genre()
                elif user_input == 5:#Display all genres
                    genres = [build_genre_class_from_data(c) for c in get_all_genres()]
                    if genres == -1:
                        return -1
                    genre_names = [f"{genre.get_genre_name()} - {genre.get_genre_description()}" for genre in genres]
                    for name in genre_names:
                        print(name)
                elif user_input == 6:#Quit to menu
                    continue
            elif user_input == 5:
                break
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        finally:
            print("----------------------")
main()

