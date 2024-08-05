My 4th miniproject in the course! This is a Library Management System, similar to an earlier one I made, but with one key difference; this one connects to a mySQL database to manage its collection.

Features:  
1. Create books, genres, authors, and members and automatically upload to the database. 
2. Read the data of any of the above schema.   
3. Update any of the above and have them save on the database.  
4. Delete any of the above.  
2. Check out books for users, as well as return them.  

Notes:  
1. When creating users, it will generate a library id number for them as well. This is different to the internal id which the database uses to refer to individual entries.  


Instructions:  
1. Create the database using mySQL. There is a setup script included that when run, will set up the database correctly.  
2. There is an admin account included to simulate logins. The username is admin and the password is 'test'.  
3. Utilize the command line interface to navigate and input information. An example is choosing 1 on the main menu to navigate to the books submenu, then 1 again to create a book, and typing in the name of the book you wish to create when prompted.  
4. Make sure to create at least one genre and author already if it doesn't come with one in the version you have. It won't crash, but you won't be able to make a book without one. 