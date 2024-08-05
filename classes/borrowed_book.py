class BorrowedBook():
    def __init__(self, member_id, book_id, borrow_date, return_date, checkout_id):
        self.member_id = member_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.checkout_id = checkout_id
    
    # getters
    def get_member_id(self):
        return self.member_id
    
    def get_book_id(self):
        return self.book_id
    
    def get_borrow_date(self):
        return self.borrow_date
    
    def get_return_date(self):
        return self.return_date
    
    def get_checkout_id(self):
        return self.checkout_id