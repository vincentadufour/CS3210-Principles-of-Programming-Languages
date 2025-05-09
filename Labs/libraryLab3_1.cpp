/*
Student:    Vincent Dufour
Professor:  Dr. Ranjidha Rajan
Assignment: Lab 3.1
Date:       13.04.2025
Time Taken: 7 hours ish
*/


#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>


class Book
{
    private:
        std::string title;
        std::string author;
        std::string isbn;
        bool isAvailable;

    public:
        Book(const std::string& title, const std::string& author, const std::string& isbn)
            : title(title), author(author), isbn(isbn), isAvailable(true) {}

        std::string getTitle() const { return title; }
        std::string getAuthor() const { return author; }
        std::string getISBN() const { return isbn; }
        bool getAvailability() { return isAvailable; }

        // affects availability when book is checked out/returned
        void checkOut() { isAvailable = false; }
        void returnBook() { isAvailable = true; }

        void displayDetails() const
        {
            std::cout << "Title: " << title << "\nAuthor: " << author 
                    << "\nISBN: " << isbn << "\nStatus: " 
                    << (isAvailable ? "Available" : "Checked Out") << '\n';   // perfect use case for the ternary operator
        }
};



class Member
{
    private:
        std::string name;
        std::string memberId;
        std::vector<std::string> borrowedBooks;             // vector for storing which books are currently checked out


    public:
        Member(const std::string& name, const std::string& memberId)
            : name(name), memberId(memberId) {}


        std::string getName() const { return name; }
        std::string getMemberId() const { return memberId; }

        bool borrowBook(const std::string& isbn)
        {
            if (borrowedBooks.size() < 5)                   // 5 book limit per client
            {
                borrowedBooks.push_back(isbn);
                return true;
            }
            return false;
        }


        // 'it' is an iterator pointer, starts at the start of the vector, goes until
        // it finishes the vector, increments memory address along the way
        // dereferences pointer to access actual value to match isbn
        bool returnBook(const std::string& isbn)
        {
            for (auto it = borrowedBooks.begin(); it != borrowedBooks.end(); ++it)
            {
                if (*it == isbn)
                {
                    borrowedBooks.erase(it);
                    return true;
                }
            }
            return false;
        }
};



class Library {
private:
    // keys, isbn and member ID
    std::unordered_map<std::string, Book> books;
    std::unordered_map<std::string, Member> members;

    bool bookExists(const std::string& isbn) const
    {
        return books.find(isbn) != books.end();
    }

    bool memberExists(const std::string& memberId) const
    {
        return members.find(memberId) != members.end();
    }

public:
    void addBook(const std::string& title, const std::string& author, const std::string& isbn)
    {
        if (!bookExists(isbn))
        {
            books.emplace(isbn, Book(title, author, isbn));
            std::cout << "New book '" << title << "' added successfully.\n";
        } else
        {
            std::cout << "This book is already in the library!\n";
        }
    }


    void addMember(const std::string& name, const std::string& memberId)
    {
        if (!memberExists(memberId))
        {
            members.emplace(memberId, Member(name, memberId));
            std::cout << "New member '" << name << "' added successfully.\n";
        } else
        {
            std::cout << "This ID is already taken!\n";
        }
    }


    bool checkOutBook(const std::string& memberId, const std::string& isbn)
    {
        if (!memberExists(memberId))
        {
            std::cout << "Member not found!\n";
            return false;
        }
        if (!bookExists(isbn))
        {
            std::cout << "Book not found!\n";
            return false;
        }

        Book& book = books.at(isbn);
        if (!book.getAvailability())
        {
            std::cout << "Book is already checked out! Please try again later.\n";
            return false;
        }

        Member& member = members.at(memberId);
        if (member.borrowBook(isbn))
        {
            book.checkOut();
            std::cout << "Book checked out successfully.\n";
            return true;
        } else {
            std::cout << "You've reached the borrowing limit. Please return a book before checking out another.\n";
            return false;
        }
    }

    bool returnBook(const std::string& memberId, const std::string& isbn)
    {
        if (!memberExists(memberId))
        {
            std::cout << "Member not found.\n";
            return false;
        }
        if (!bookExists(isbn))
        {
            std::cout << "Book not found.\n";
            return false;
        }

        Member& member = members.at(memberId);
        Book& book = books.at(isbn);

        if (member.returnBook(isbn))
        {
            book.returnBook();
            std::cout << "Book returned successfully.\n";
            return true;
        } else                          // ISBN found, but member ID mismatch
        {
            std::cout << "You didn't borrow this book. Please return this book to its owner and have them return it.\n";
            return false;
        }
    }

    void displayAllBooks() const
    {
        std::cout << "\n\nAll Books in Library:\n";
        
        if (books.empty())
        {
            std::cout << "The library is empty!\n";
            return;
        }

        
        for (const auto& pair : books)
        {
            pair.second.displayDetails();
            std::cout << "--------------------\n";
        }
    } 
};



// Test case
int main()
{
    ///////////////////////////////////
    // Library Set Up

    Library vincentLibrary;

    // stocking library
    vincentLibrary.addBook("Madame Bovary", "Gustave Flaubert", "9783963178832");
    vincentLibrary.addBook("The C++ Programming Language", "Bjarne Stroustrup", "9780321563842");
    vincentLibrary.addBook("Midnight's Children", "Salman Rushdie", "9783492107167");

    // adding members
    vincentLibrary.addMember("Ranjidha Rajan", "001");
    vincentLibrary.addMember("Callie Campbell", "002");

    // showing current library contents
    vincentLibrary.displayAllBooks();

    // Dr. Rajan borrows the C++ book
    vincentLibrary.checkOutBook("001", "9780321563842");

    // Callie borrows Midnight's Children
    vincentLibrary.checkOutBook("002", "9783492107167");

    // showing current library contents with two books marked as "Checked Out"
    vincentLibrary.displayAllBooks();

    ///////////////////////////////////



    ///////////////////////////////////
    // Test Cases

    // Dr. Rajan gives her C++ book to Callie, then Callie tries to return it
    std::cout << "\nTest Case 1:" << '\n';
    vincentLibrary.returnBook("002", "9780321563842");

    // Callie returns the book to Dr. Rajan, then Dr. Rajan returns the book to the library
    std::cout << "\nTest Case 2:" << '\n';
    vincentLibrary.returnBook("001", "9780321563842");

    // User that doesn't exist attempts to borrow book
    std::cout << "\nTest Case 3:" << '\n';
    vincentLibrary.checkOutBook("003", "9780321563842");

    // Registered user tries to borrow a book that doesn't exist in the library
    std::cout << "\nTest Case 4:" << '\n';
    vincentLibrary.checkOutBook("002", "9780545392495");

    // New user tries to take a pre-existing user ID
    std::cout << "\nTest Case 5:" << '\n';
    vincentLibrary.addMember("Vincent Dufour", "001");

    // Attempting to add a book already in the library
    std::cout << "\nTest Case 6:" << '\n';
    vincentLibrary.addBook("Madame Bovary", "Gustave Flaubert", "9783963178832");

    // Attempting to borrow a book already checked out
    std::cout << "\nTest Case 6:" << '\n';
    vincentLibrary.checkOutBook("001", "9783492107167");
    

    ///////////////////////////////////

    return 0;
}
