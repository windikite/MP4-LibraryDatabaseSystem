class Book():
    def __init__(self, book_name, ISBN, year, author_id, genre_id, book_description, availability, book_id):
        self.book_name = book_name
        self.ISBN = ISBN
        self.year = year
        self.author_id = author_id
        self.genre_id = genre_id
        self.book_description = book_description
        self.availability = availability
        self.book_id = book_id
    
    # getters
    def get_book_name(self):
        return self.book_name
    
    def get_ISBN(self):
        return self.ISBN
    
    def get_year(self):
        return self.year
    
    def get_count(self):
        return self.count
    
    def get_author_id(self):
        return self.author_id
    
    def get_genre_id(self):
        return self.genre_id
    
    def get_book_description(self):
        return self.book_description
    
    def get_availability(self):
        return self.availability
    
    def get_book_id(self):
        return self.book_id
    
    def get_data(self):
        raw_data = {
            "book_name": self.book_name,
            "ISBN": self.ISBN,
            "year": self.year,
            "book_description": self.book_description,
            "author_id": self.author_id,
            "genre_id": self.genre_id,
            "availability": self.availability
        }
        return raw_data
    
    # setters
    def update_book_name(self, new_book_name):
        if isinstance(new_book_name, str) and len(new_book_name) > 0:
            self.book_name = new_book_name
            return 1
        else:
            print("Please make sure the new book_name is a string that is longer than 0 characters.")
            return -1
    
    def update_ISBN(self, new_ISBN):
        if isinstance(new_ISBN, int):
            if self.year >= 2007 and len(new_ISBN) == 13 or self.year < 2007 and len(new_ISBN) == 10:
                self.ISBN = new_ISBN
                return 1
            else:
                print("Please make sure the new ISBN is an int with the following lengths according to the publish year:\n - Books published earlier than Jan 1 2007 must be 10 digits long\n - Books published on or after Jan 1 2007 must be 13 digits long")
                return -1
        else:
            print("Please make sure the new ISBN is an int with no dashes.")
            return -1
    
    def update_year(self, new_year):
        if isinstance(new_year, int):
            if len(str(new_year)) > 0 and len(str(new_year)) < 5:
                self.year = new_year
                return 1
            else:
                print("Please make sure the new ISBN is an int with the following lengths according to the publish year:\n - Books published earlier than Jan 1 2007 must be 10 digits long\n - Books published on or after Jan 1 2007 must be 13 digits long")
                return -1
        else:
            print("Please make sure the new year is an int with no dashes, slashes or dots.")
            return -1
    
    def update_book_description(self, new_book_description):
        if isinstance(new_book_description, str) and len(new_book_description) > 0:
            self.book_description = new_book_description
            return 1
        else:
            print("Please make sure the new bookdescription is a string that is longer than 0 characters.")
            return -1
        
    def update_availability(self, new_availability):
        if isinstance(new_availability, int) and new_availability >= 0:
            self.availability = new_availability
        else:
            print("Please make sure the new ID is at least 0.")
            return -1
    
    def info(self):
        print(f"{self.book_name} book printed in {self.year} under ISBN {self.ISBN}. There are {self.availability} copies available.")
        


# default_books = {ISBN: Book(name, ISBN, author_name, genre_name, year, available, borrowed, genre_description, book_description, author_description) for name, ISBN, author_name, genre_name, year, available, borrowed, genre_description, book_description, author_description in [
#         ["An Encyclopedia of Fairies", 1325763258, "Katherine Briggs", "Folklore", 1976, 0, 1, "Tales from people about supernatural stuff!", "A book written about fairies.", "An American folklorist."],
#         ["Fairy Folk Tales of Ireland", 8927982364, "William Butler Yeats", "Folklore", 1888, 1, 1, "Tales from people about supernatural stuff!", "A book about folk tales in Ireland", "19th century American folklorist."],
#         ["The Secret Commonwealth", 2392356235, "Robert Kirk", "Folklore", 1815, 1, 2, "Tales from people about supernatural stuff!", "A book about popular beliefs in the parishes of Ireland in the 17th century.", "Modern american linguist with a specialty in norse mythology."]
#         ]}

# for book in default_books.items():
#     # print(book[1].get_book_name())
#     # print(book[1].get_book_description())
#     # print(book[1].get_genre_name())
#     # print(book[1].get_genre_description())
#     print(book[1].get_data())
#     print("------------")


