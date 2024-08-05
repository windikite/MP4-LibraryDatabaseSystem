class Genre:
    def __init__(self, genre_name, genre_description, genre_category, genre_id):
        self.genre_name = genre_name
        self.genre_description = genre_description
        self.genre_category = genre_category
        self.genre_id = genre_id
        
    # getters
    def get_genre_name(self):
        return self.genre_name
    
    def get_genre_description(self):
        return self.genre_description
    
    def get_genre_category(self):
        return self.genre_category
    
    def get_genre_id(self):
        return self.genre_id
    
    # setters
    def update_genre_name(self, new_genre_name):
        if isinstance(new_genre_name, str) and len(new_genre_name) > 0:
            self.genre_name = new_genre_name
            return 1
        else:
            print("Please make sure the new genre name is a string that is longer than 0 characters.")
            return -1
    
    def update_genre_description(self, new_genre_description):
        if isinstance(new_genre_description, str) and len(new_genre_description) > 0:
            self.genre_description = new_genre_description
            return 1
        else:
            print("Please make sure the new genre_description is a string that is longer than 0 characters.")
            return -1
    
    def update_genre_category(self, new_genre_category):
        if isinstance(new_genre_category, str) and len(new_genre_category) > 0:
            self.genre_category = new_genre_category
            return 1
        else:
            print("Please make sure the new genre_category is a string that is longer than 0 characters.")
            return -1
            
    def info(self):
        print(f"{self.genre_name} - {self.genre_description}")
        return 1