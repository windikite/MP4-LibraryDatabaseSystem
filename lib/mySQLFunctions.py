import mysql.connector
from mysql.connector import Error
 
# Connect to database
def connect_to_database():
    db_name = "library_management_database"
    user = "root"
    password = "test"
    host = "localhost"
    conn = ""
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        return conn
    except Error as e:
        print(f"Error: {e}")

# Import data from database
def execute_fetch(query, variables, error_message):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(query, variables)
            results = cursor.fetchall()
            if results:
                return results
            else:
                print(f"{error_message}")
                return -1
        finally:
            cursor.close()
            conn.close()

def execute_change(query, variables, error_message):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(query, variables)
            conn.commit()
        except:
            print(f"{error_message}")
            return -1
        finally:
            cursor.close()
            conn.close()

# author functions
def add_author_to_database(author):
    conn = connect_to_database()
    if conn is not None:
        try:
            name = author.get_author_name()
            biography = author.get_author_description()
            cursor = conn.cursor()
            query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (name, biography))
            conn.commit()
            print("Author added successfully!")
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

def search_database_for_author_by_id(id_to_search):
    query = "SELECT * FROM Authors WHERE id = %s"
    variables = (id_to_search, )
    error_message = "Unable to find author!"
    results = execute_fetch(query, variables, error_message)
    return results

def search_database_for_author_by_name(name_to_search):
    query = "SELECT * FROM Authors WHERE name LIKE %s"
    variables = (f"%{name_to_search}%", )
    error_message = "Unable to find author!"
    results = execute_fetch(query, variables, error_message)
    return results

def get_all_authors():
    query = "SELECT * FROM Authors"
    variables = ()
    error_message = "Unable to find authors!"
    results = execute_fetch(query, variables, error_message)
    return results

def delete_author_from_database_by_id(id_to_delete):
    found = search_database_for_author_by_id(id_to_delete)
    if found:
        query = "DELETE FROM Authors WHERE id = %s"
        variables = (id_to_delete, )
        error_message = "Unable to modify database! Author likely in use by book which prevents deletion."
        results = execute_change(query, variables, error_message)
        if results != -1:
            print("Deleted entry!")
        else:
            print("Failed to delete author!")
        return results
    else:
        return -1
    
def update_author(author):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            name = author.get_author_name()
            description = author.get_author_description()
            author_id = author.get_author_id()
            found_author = search_database_for_author_by_id(author_id)
            if found_author == -1:
                print("Author not found!")
                return -1
            updated_book = (name, description, author_id)
            query = "UPDATE Authors SET name = %s, biography = %s WHERE id = %s"
            cursor.execute(query, updated_book)
            conn.commit()
            print("Author details updated successfully.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

# genre functions
def add_genre_to_database(genre):
    conn = connect_to_database()
    if conn is not None:
        try:
            name = genre.get_genre_name()
            description = genre.get_genre_description()
            category = genre.get_genre_category()
            cursor = conn.cursor()
            query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, description, category))
            conn.commit()
            print("genre added successfully!")
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

def search_database_for_genre_by_id(id_to_search):
    query = "SELECT * FROM Genres WHERE id = %s"
    variables = (id_to_search, )
    error_message = "Unable to find genre!"
    results = execute_fetch(query, variables, error_message)
    return results

def search_database_for_genre_by_name(name_to_search):
    query = "SELECT * FROM Genres WHERE name LIKE %s"
    variables = (f"%{name_to_search}%", )
    error_message = "Unable to find genre!"
    results = execute_fetch(query, variables, error_message)
    return results

def get_all_genres():
    query = "SELECT * FROM Genres"
    variables = ()
    error_message = "Unable to find genres!"
    results = execute_fetch(query, variables, error_message)
    return results

def delete_genre_from_database_by_id(id_to_delete):
    found = search_database_for_genre_by_id(id_to_delete)
    print(id_to_delete)
    if found:
        query = "DELETE FROM Genres WHERE id = %s"
        variables = (id_to_delete, )
        error_message = "Unable to modify database! Genre likely in use by book which prevents deletion."
        results = execute_change(query, variables, error_message)
        if results != -1:
            print("Deleted entry!")
        else:
            print("Failed to delete genre!")
        return results
    else:
        return -1

def update_genre(genre):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            name = genre.get_genre_name()
            description = genre.get_genre_description()
            category = genre.get_genre_category()
            genre_id = genre.get_genre_id()
            found_genre = search_database_for_genre_by_id(genre_id)
            if found_genre == -1:
                print("Genre not found!")
                return -1
            updated_book = (name, description, category, genre_id)
            query = "UPDATE Genres SET name = %s, description = %s, category = %s WHERE id = %s"
            cursor.execute(query, updated_book)
            conn.commit()
            print("Genre details updated successfully.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

# book functions
def add_book_to_database(book):
    conn = connect_to_database()
    if conn is not None:
        try:
            title = book.get_book_name()
            author_id = book.get_author_id()
            genre_id = book.get_genre_id()
            isbn = book.get_ISBN()
            publication_date = book.get_year()
            availability = book.get_availability()
            description = book.get_book_description()
            cursor = conn.cursor()
            query = "INSERT INTO Books (title, author_id, genre_id, isbn, publication_date, availability, description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (title, author_id, genre_id, isbn, publication_date, availability, description))
            conn.commit()
            print("Book added successfully!")
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

def search_database_for_book_by_id(id_to_search):
    query = "SELECT * FROM Books WHERE id = %s"
    variables = (id_to_search, )
    error_message = "Unable to find book!"
    results = execute_fetch(query, variables, error_message)
    return results

def search_database_for_book_by_name(name_to_search):
    query = "SELECT * FROM Books WHERE title LIKE %s"
    variables = (f"%{name_to_search}%", )
    error_message = "Unable to find book!"
    results = execute_fetch(query, variables, error_message)
    return results

def get_all_books():
    query = "SELECT * FROM Books"
    variables = ()
    error_message = "Unable to find books!"
    results = execute_fetch(query, variables, error_message)
    return results

def delete_book_from_database_by_id(id_to_delete):
    found = search_database_for_book_by_id(id_to_delete)
    if found:
        query = "DELETE FROM Books WHERE id = %s"
        variables = (id_to_delete, )
        error_message = "Unable to modify database! Book is likely being borrowed which prevents deletion."
        results = execute_change(query, variables, error_message)
        if results != -1:
            print("Deleted entry!")
        else:
            print("Failed to delete book!")
        return results
    else:
        return -1

def update_book(book):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            id = book.get_book_id()
            name = book.get_book_name()
            description = book.get_book_description()
            availability = book.get_availability()
            found_book = search_database_for_book_by_id(id)
            if found_book == -1:
                print("Book not found!")
                return -1
            updated_book = (name, description, availability, id)
            query = "UPDATE Books SET title = %s, description = %s, availability = %s WHERE id = %s"
            cursor.execute(query, updated_book)
            conn.commit()
            print("Book details updated successfully.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

# member functions
def add_member_to_database(member):
    conn = connect_to_database()
    if conn is not None:
        try:
            name = member.get_member_name()
            library_id = member.get_library_id()
            cursor = conn.cursor()
            query = "INSERT INTO Members (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, (name, library_id))
            conn.commit()
            print("Member added successfully!")
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

def search_database_for_member_by_id(id_to_search):
    query = "SELECT * FROM Members WHERE id = %s"
    variables = (id_to_search, )
    error_message = "Unable to find member!"
    results = execute_fetch(query, variables, error_message)
    return results

def search_database_for_member_by_name(name_to_search):
    query = "SELECT * FROM Members WHERE name LIKE %s"
    variables = (f"%{name_to_search}%", )
    error_message = "Unable to find member!"
    results = execute_fetch(query, variables, error_message)
    return results

def get_all_members():
    query = "SELECT * FROM Members"
    variables = ()
    error_message = "Unable to find members!"
    results = execute_fetch(query, variables, error_message)
    return results

def delete_member_from_database_by_id(id_to_delete):
    found = search_database_for_member_by_id(id_to_delete)
    if found:
        query = "DELETE FROM Members WHERE id = %s"
        variables = (id_to_delete, )
        error_message = "Unable to modify database!"
        results = execute_change(query, variables, error_message)
        if results != -1:
            print("Deleted entry!")
        else:
            print("Failed to delete member!")
        return results
    else:
        return -1

def update_member(member):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            name = member.get_member_name()
            library_id = member.get_library_id()
            member_id = member.get_member_id()
            found_member = search_database_for_member_by_id(member_id)
            if found_member == -1:
                print("Member not found!")
                return -1
            updated_book = (name, library_id, member_id)
            query = "UPDATE Members SET name = %s, library_id = %s WHERE id = %s"
            cursor.execute(query, updated_book)
            conn.commit()
            print("Member details updated successfully.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

# borrowed_book functions
def add_borrowed_book_to_database(member_id, book_id, borrow_date, return_date):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Borrowed_Books (member_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (member_id, book_id, borrow_date, return_date))
            conn.commit()
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database!")
        return -1

def search_database_for_borrowed_book_by_id(id_to_search):
    query = "SELECT * FROM Borrowed_Books WHERE id = %s"
    variables = (id_to_search, )
    error_message = "Unable to find borrowed book!"
    results = execute_fetch(query, variables, error_message)
    return results

def search_database_for_borrowed_book_by_member_id(id_to_search):
    query = "SELECT * FROM Borrowed_Books WHERE member_id = %s"
    variables = (id_to_search, )
    error_message = "Unable to find borrowed book!"
    results = execute_fetch(query, variables, error_message)
    return results

def search_database_for_borrowed_book_by_book_id(id_to_search):
    query = "SELECT * FROM Borrowed_Books WHERE book_id = %s"
    variables = (id_to_search, )
    error_message = "Unable to find borrowed book!"
    results = execute_fetch(query, variables, error_message)
    return results

def get_all_borrowed_books():
    query = "SELECT * FROM Borrowed_books"
    variables = ()
    error_message = "Unable to find borrowed books!"
    results = execute_fetch(query, variables, error_message)
    return results

def delete_borrowed_book_from_database_by_id(member_id, book_id):
    query = "DELETE FROM Borrowed_Books WHERE member_id = %s and book_id = %s"
    variables = (member_id, book_id, )
    error_message = "Unable to modify database!"
    results = execute_change(query, variables, error_message)
    if results != -1:
        print("Deleted entry!")
    else:
        print("Failed to delete borrowed book!")
    return results

# user authenticator
def authenticate_superuser():
    reconnects = 0
    attempts = 0
    while True and reconnects < 5 and attempts < 5:
        print('Please enter username and password. Type "exit" to close program.')
        username = input(str("Username: "))
        if username == "exit":
            return -1
        password = input(str("Password: "))
        found_users = (("admin", "test"), ("librarian", "test"))
        for user in found_users:
            if username == user[0] and password == user[1]:
                return user[0]
        print("Incorrect username/password combination. Please try again!")
            
                   