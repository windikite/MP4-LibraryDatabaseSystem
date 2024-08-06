from .utilityFunctions import generateUniqueID, askMenu, check_date
from lib.mySQLFunctions import add_author_to_database, search_database_for_author_by_name, delete_author_from_database_by_id, get_all_authors, add_genre_to_database,search_database_for_genre_by_name, delete_genre_from_database_by_id, get_all_genres, add_book_to_database, search_database_for_book_by_name, delete_book_from_database_by_id, get_all_books, add_member_to_database, search_database_for_member_by_name, delete_member_from_database_by_id, get_all_members, update_book, add_borrowed_book_to_database, delete_borrowed_book_from_database_by_id, search_database_for_borrowed_book_by_book_id, search_database_for_borrowed_book_by_member_id, search_database_for_borrowed_book_by_id, get_all_borrowed_books, search_database_for_book_by_id, update_genre, update_member, update_author
from classes.book import Book
from classes.member import Member
from classes.author import Author
from classes.genre import Genre
from classes.borrowed_book import BorrowedBook

def create_book():
    genres = [build_genre_class_from_data(c) for c in get_all_genres()]
    authors = [build_author_class_from_data(c) for c in get_all_authors()]
    genre_names = [f"{genre.get_genre_name()} - {genre.get_genre_description()}" for genre in genres]
    author_names = [f"{author.get_author_name()} - {author.get_author_description()}" for author in authors]
    book_name = str(input("Please input a name for the book: "))
    genre = ""
    while genre == "":
        genre_index = search_list(genre_names, "Please choose a genre: ")
        if genre_index == -1:
            genre_index = create_genre(genres)
        elif genre_index == -2:
            return -1
        elif genre_index != -1 and genre_index != -2 and genre_index != -3:
            genre = genres[genre_index-1]
    author = ""
    while author == "":
        author_index = search_list(author_names, "Please choose an author: ")
        if author_index == -1:
            author_index = create_author(authors)
        elif author_index == -2:
            return -1
        elif author_index != -1 and author_index != -2 and author_index != -3:
            author = authors[author_index-1]
    book_year = int(input("Please input a publish year: "))
    book_ISBN = int(input("Please input an ISBN: "))
    book_description = str(input("Please input a description for the book: "))
    num_avail = int(input("Please input number available: "))
    new_book = Book(book_name, book_ISBN, book_year, author.get_author_id(), genre.get_genre_id(), book_description, num_avail, None)
    add_book_to_database(new_book)
    return new_book

def create_author():
    book_author = str(input("Please input an author name: "))
    author_bio = str(input("Please input author biography: "))
    new_author = Author(book_author, author_bio, None)
    add_author_to_database(new_author)
    return new_author

def create_genre():
    genre_name = str(input("Please input a genre name: "))
    genre_description = str(input("Please input genre description: "))
    genre_category = str(input("Please input genre category: "))
    new_genre = Genre(genre_name, genre_description, genre_category, None)
    add_genre_to_database(new_genre)
    return new_genre

def create_member():
    member_name = str(input("Please input a name for the member: "))
    ID = generateUniqueID()
    new_member = Member(member_name, ID, {})
    add_member_to_database(new_member)
    return new_member

def search_list(list, text):
    entry_list = list
    entry_list.append("Quit to main menu")
    entry_index = askMenu(entry_list, text)
    try:
        entry_index = int(entry_index)
        if entry_index == len(entry_list):#Quit to menu
            return -1
    except ValueError:
        print("Function error! Please make sure to choose one of the chosen options!")
        return -3
    except TypeError:
        print("Function error! Please make sure to input numbers for menu selections!")
        return -3
    except IndexError:
        print("Index error! Please make sure to choose one of the chosen options!")
        return -3
    else:
        return entry_index
    
def delete_book():
    book = select_book()
    delete_book_from_database_by_id(book.get_book_id())

def delete_author():
    author = select_author()
    delete_author_from_database_by_id(author.get_author_id())

def delete_genre():
    genre = select_genre()
    delete_genre_from_database_by_id(genre.get_genre_id())

def delete_member():
    member = select_member()
    delete_member_from_database_by_id(member.get_member_id())

def edit_book():
    book = select_book()
    user_input = askMenu([
        "Title", 
        "Description", 
        "Availability",
        "Quit to main menu"], 
        "Please choose what to edit: ")
    if user_input == 1:
        new_title = str(input("Please enter new title: "))
        success = book.update_book_name(new_title)
        while success == -1:
            book.update_book_name(new_title)
    elif user_input == 2:
        new_description = str(input("Please enter new description: "))
        success = book.update_book_description(new_description)
        while success == -1:
            book.update_book_description(new_description)
    elif user_input == 3:
        new_availability = int(input("Please enter new availability: "))
        success = book.update_availability(new_availability)
        while success == -1:
            book.update_availability(new_availability)
    elif user_input == 4:#quit to main menu
        return -1
    update_book(book)

def edit_genre():
    genre = select_genre()
    user_input = askMenu([
        "Name", 
        "Description",
        "Category",
        "Quit to main menu"], 
        "Please choose what to edit: ")
    if user_input == 1:
        new_name = str(input("Please enter new name: "))
        success = genre.update_genre_name(new_name)
        while success == -1:
            genre.update_genre_name(new_name)
    elif user_input == 2:
        new_description = str(input("Please enter new description: "))
        success = genre.update_genre_description(new_description)
        while success == -1:
            genre.update_genre_description(new_description)
    elif user_input == 3:
        new_category = str(input("Please enter new category: "))
        success = genre.update_genre_category(new_category)
        while success == -1:
            genre.update_genre_category(new_category)
    elif user_input == 4:#quit to main menu
        return -1
    update_genre(genre)

def edit_author():
    author = select_author()
    user_input = askMenu([
        "Name", 
        "Description",
        "Quit to main menu"], 
        "Please choose what to edit: ")
    if user_input == 1:
        new_name = str(input("Please enter new name: "))
        success = author.update_author_name(new_name)
        while success == -1:
            author.update_author_name(new_name)
    elif user_input == 2:
        new_description = str(input("Please enter new description: "))
        success = author.update_author_description(new_description)
        while success == -1:
            author.update_author_description(new_description)
    elif user_input == 3:#quit to main menu
        return -1
    update_author(author)

def edit_member():
    member = select_member()
    user_input = askMenu([
        "Name", 
        "Library ID"
        "Quit to main menu"], 
        "Please choose what to edit: ")
    if user_input == 1:
        new_name = str(input("Please enter new name: "))
        success = member.update_member_name(new_name)
        while success == -1:
            member.update_member_name(new_name)
    elif user_input == 2:
        new_description = int(input("Please enter new library ID (10 digit limit): "))
        success = member.update_library_id(new_description)
        while success == -1:
            member.update_library_id(new_description)
    elif user_input == 3:#quit to main menu
        return -1
    update_member(member)

def select_book():
    books = ""
    while books == "":
        user_input = askMenu([
        "Choose from list of books", 
        "Search books by name", 
        "Quit to main menu"], 
        "Please choose an operation: ")
        found_books = ""
        if user_input == 1:
            found_books = [build_book_class_from_data(c) for c in get_all_books()]
        elif user_input == 2:
            name_to_search = str(input("Please enter name to search by: "))
            found_books = [build_book_class_from_data(c) for c in search_database_for_book_by_name(name_to_search)]
        elif user_input == 3:
            return -1
        
        if len(found_books) > 0:
            books = found_books
        else:
            print("No books found!")
    book_names = [f"{book.get_book_name()} - {book.get_book_description()}" for book in books]
    book = ""
    while book == "":
        book_index = search_list(book_names, "Please choose book: ")
        if book_index == -1:
            return -1
        elif book_index == -2:
            return -2
        
        if book_index > 0 and book_index < len(book_names):
            book = books[book_index-1]
    return book

def select_author():
    authors = ""
    while authors == "":
        user_input = askMenu([
        "Choose from list of authors", 
        "Search authors by name", 
        "Quit to main menu"], 
        "Please choose an operation: ")
        found_authors = ""
        if user_input == 1:
            found_authors = [build_author_class_from_data(c) for c in get_all_authors()]
        elif user_input == 2:
            name_to_search = str(input("Please enter name to search by: "))
            found_authors = [build_author_class_from_data(c) for c in search_database_for_author_by_name(name_to_search)]
        elif user_input == 3:
            return -1
        
        if len(found_authors) > 0:
            authors = found_authors
        else:
            print("No authors found!")
    author_names = [f"{author.get_author_name()} - {author.get_author_description()}" for author in authors]
    author = ""
    while author == "":
        author_index = search_list(author_names, "Please choose author: ")
        if author_index == -1:
            return -1
        elif author_index == -2:
            return -2
        
        if author_index > 0 and author_index < len(author_names):
            author = authors[author_index-1]
    return author

def select_genre():
    genres = ""
    while genres == "":
        user_input = askMenu([
        "Choose from list of genres", 
        "Search genres by name", 
        "Quit to main menu"], 
        "Please choose an operation: ")
        found_genres = ""
        if user_input == 1:
            found_genres = [build_genre_class_from_data(c) for c in get_all_genres()]
        elif user_input == 2:
            name_to_search = str(input("Please enter name to search by: "))
            found_genres = [build_genre_class_from_data(c) for c in search_database_for_genre_by_name(name_to_search)]
        elif user_input == 3:
            return -1
        
        if len(found_genres) > 0:
            genres = found_genres
        else:
            print("No genres found!")
    genre_names = [f"{genre.get_genre_name()} - {genre.get_genre_description()}" for genre in genres]
    genre = ""
    while genre == "":
        genre_index = search_list(genre_names, "Please choose genre: ")
        if genre_index == -1:
            return -1
        elif genre_index == -2:
            return -2
        
        if genre_index > 0 and genre_index < len(genre_names):
            genre = genres[genre_index-1]
    return genre

def select_member():
    members = ""
    while members == "":
        user_input = askMenu([
        "Choose from list of members", 
        "Search members by name", 
        "Quit to main menu"], 
        "Please choose an operation: ")
        found_members = ""
        if user_input == 1:
            found_members = [build_member_class_from_data(c) for c in get_all_members()]
        elif user_input == 2:
            name_to_search = str(input("Please enter name to search by: "))
            found_members = [build_member_class_from_data(c) for c in search_database_for_member_by_name(name_to_search)]
        elif user_input == 3:
            return -1
        
        if len(found_members) > 0:
            members = found_members
        else:
            print("No members found!")
    member_names = [f"{member.get_member_name()} - {member.get_library_id()}" for member in members]
    member = ""
    while member == "":
        member_index = search_list(member_names, "Please choose member: ")
        if member_index == -1:
            return -1
        elif member_index == -2:
            return -2
        
        if member_index > 0 and member_index < len(member_names):
            member = members[member_index-1]
    return member

def checkout_book():
    member = select_member()
    book = select_book()
    availability = book.get_availability()
    if availability > 0:
        # borrow date
        borrow_date = str(input("Please enter borrow date(yyyy/mm/dd): "))
        borrow_date = check_date(borrow_date)
        while borrow_date == -1:
            print("Please try again using the correct format.")
            borrow_date = str(input("Please enter borrow date(yyyy/mm/dd): "))
        # return date
        return_date = str(input("Please enter return date(yyyy/mm/dd): "))
        return_date = check_date(return_date)
        while return_date == -1:
            print("Please try again using the correct format.")
            return_date = str(input("Please enter return date(yyyy/mm/dd): "))
        success = add_borrowed_book_to_database(member.get_member_id(), book.get_book_id(), borrow_date, return_date)
        if success != -1:
            book.update_availability(availability-1)
            success = update_book(book)
            if success != -1:
                print(f"{member.get_member_name()} checked out {book.get_book_name()}.")
            else:
                print("Failed to update availability for checked out book.")
        else:
            print("Failed to check out book.")
    else:
        print("There are no more copies of this book available!")

def return_book():
    member = select_member()
    found_records = search_database_for_borrowed_book_by_member_id(member.get_member_id())
    record_classes = [build_borrowed_book_class_from_data(c) for c in found_records]
    searched_books = [search_database_for_book_by_id(record.get_book_id()) for record in record_classes]
    books = [build_book_class_from_data(book[0]) for book in searched_books]
    book_names = []
    for book in books:
        book_names.append(f"{book.get_book_name()} - {book.get_book_description()}")
    index = search_list(book_names, "Please choose a book to return: ")
    if index < 1:
        return -1
    book = books[index-1]
    availability = book.get_availability()
    success = delete_borrowed_book_from_database_by_id(member.get_member_id(), book.get_book_id())
    if success != -1:
        book.update_availability(availability+1)
        success = update_book(book)
        if success != -1:
            print(f"{member.get_member_name()} returned {book.get_book_name()}.")
        else:
            print("Failed to update availability for returned book.")
    else:
        print("Failed to return book.")

def build_genre_class_from_data(data):
    new_genre = Genre(data[1], data[2], data[3], data[0])
    return new_genre

def build_author_class_from_data(data):
    new_author = Author(data[1], data[2], data[0])
    return new_author

def build_book_class_from_data(data):
    new_book = Book(data[1], data[4], data[5], data[2], data[3], data[7], data[6], data[0])
    return new_book

def build_member_class_from_data(data):
    new_member = Member(data[1], data[2], data[0])
    return new_member

def build_borrowed_book_class_from_data(data):
    new_borrowed_book = BorrowedBook(data[1], data[2], data[3], data[4], data[0])
    return new_borrowed_book