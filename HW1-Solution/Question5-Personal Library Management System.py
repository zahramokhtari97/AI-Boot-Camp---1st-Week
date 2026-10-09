
books = {}

print("Welcome to the Personal Library Management System!")
print("Available commands: add, search, show, exit")

while True:
    command = input("\nEnter a command: ").strip().lower()

    if command == "add":
        title = input("Enter the book title: ").strip()
        author = input("Enter the author's name: ").strip()

        if not title or not author:
            print("Book title and author cannot be empty.")
            continue

        books[title] = author
        print(f'"{title}" by {author} has been added successfully.')

    elif command == "search":
        title = input("Enter the book title to search for: ").strip()

        if title in books:
            print(f"Book found: {title}")
            print(f"Author: {books[title]}")
        else:
            print("The requested book was not found.")

    elif command == "show":
        if not books:
            print("The library is empty.")
        else:
            print("\nBooks in your library:")

            for title, author in books.items():
                print(f"Title: {title} | Author: {author}")

    elif command == "exit":
        print("Exiting the library system. Goodbye!")
        break

    else:
        print("Invalid command. Please enter add, search, show, or exit.")