# Filename: 
# Names: Dylan Gill, Shahmeir Shaikh, Amanjot Singh
# Date: February 11, 2024
# Description: This Program will allow the user to add, store, and retrieve books
#               from the csv file system.

# Imports
import csv

# Function to load books from the BooksInput.csv file
def load_books():
    try:
        with open('BooksInput.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            books = [row for row in reader]
        return books
    except FileNotFoundError:
        return []

# Function to save books to the BooksInput.csv file
def save_to_csv(books):
    with open('BooksInput.csv', 'w', newline='') as csvfile:
        fieldnames = ['Title', 'Author', 'Year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            writer.writerow(book)

# Function to add_book to the books list
def add_book(books):
    title = input("\nEnter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the publication: ")
    books.append({'Title': title, 'Author': author, 'Year': year})
    save_to_csv(books)
    print("\nBook added successfully!")

#Function to output all the books
def list_books(books):
    if not books:
        print("\nNo books in the reading list.")
    else:
        for book in books:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}")

# Function to search for a specific book by title
def search_book(books):
    title = input("\nEnter the title of the book to search: ").lower()
    found_books = [book for book in books if book['Title'].lower() == title]
    if found_books:
        print("\nMatching books:")
        for book in found_books:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}")
    else:
        print("No matching books found.")

# Function for display menu
def display_menu():
    print("\n=========================")
    print("Menu")
    print("1. Add a book")
    print("2. List all books")
    print("3. Search for a book")
    print("4. Quit")
    print("=========================")

# Function for main
def main():
    books = load_books()
    while True:
        display_menu()
        try:
            userInput = int(input("Please enter a number from 1-4: "))
            if userInput == 1:
                add_book(books)
            elif userInput == 2:
                list_books(books)
            elif userInput == 3:
                search_book(books)
            elif userInput == 4:
                print("Exitiing the application... Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid option.")

# Call the main function
main()
