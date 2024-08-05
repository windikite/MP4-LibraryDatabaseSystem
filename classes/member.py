class Member:
    def __init__(self, member_name, library_id, member_id):
        self.member_name = member_name
        self.library_id = library_id
        self.member_id = member_id
        
    # getters
    def get_member_name(self):
        return self.member_name
    
    def get_library_id(self):
        return self.library_id
    
    def get_member_id(self):
        return self.member_id
        
    # setters
    def update_member_name(self, new_member_name):
        if isinstance(new_member_name, str) and len(new_member_name) > 0:
            self.member_name = new_member_name
            return 1
        else:
            print("Please make sure the new member_name is a string that is longer than 0 characters.")
            return -1
            
    def update_library_id(self, new_library_id):
        if isinstance(new_library_id, int) and new_library_id > 0:
            self.library_id = new_library_id
        else:
            print("Please make sure the new library ID is a positive number.")
            return -1
            
    def info(self):
        print(f"member {self.member_name} with ID: {self.library_id}.")