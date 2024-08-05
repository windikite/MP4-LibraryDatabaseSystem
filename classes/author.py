class Author:
    def __init__(self, author_name, author_description, author_id):
        self.author_name = author_name
        self.author_description = author_description
        self.author_id = author_id
        
    # getters
    def get_author_name(self):
        return self.author_name
    
    def get_author_description(self):
        return self.author_description
    
    def get_author_id(self):
        return self.author_id
        
    # setters
    def update_author_name(self, new_author_name):
        if isinstance(new_author_name, str) and len(new_author_name) > 0:
            self.author_name = new_author_name
            return 1
        else:
            print("Please make sure the new name is a string that is longer than 0 characters.")
            return -1
    
    def update_bio(self, new_bio):
        if isinstance(new_bio, str) and len(new_bio) > 0:
            self.author_description = new_bio
            return 1
        else:
            print("Please make sure the new author_description is a string that is longer than 0 characters.")
            return -1
            
    def info(self):
        print(f"{self.author_name} - {self.author_description}")
        return 1
