class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_rented = False

    def __str__(self):
        return f"{self.title}"

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rented_books = []

    def rent_book(self, book):
        if not book.is_rented:
            book.is_rented = True
            self.rented_books.append(book)
            return f"{book.title}을 대여함."
        else:
            return f"{book.title}은 대여중."

    def return_book(self, book):
        if book in self.rented_books:
            book.is_rented = False
            self.rented_books.remove(book)
            return f"{book.title}을 반납함."
        else:
            return "당신이 대여한 책이 아님."

class ClassLibrary:
    def __init__(self):
        self.books = []
        self.rental_records = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def check_rental_records(self, student):
        if student.rented_books:
            print(f"{student.name}가 대여한 책: ", end='')
            for book in student.rented_books:
                print(book)
        else:
            print("대여한 책이 없습니다.")

    def rent_book_to_student(self, book, student):
        result = student.rent_book(book)
        if "대여함" in result:
            self.rental_records.append((student, book))
        return result

    def return_book_from_student(self, book, student):
        result = student.return_book(book)
        if "반납함" in result:
            self.rental_records.remove((student, book))
        return result


# 사용 예시
library = ClassLibrary()
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
library.add_book(book1)
library.add_book(book2)

student1 = Student("2021001", "Alice")

print(library.rent_book_to_student(book1, student1))
library.check_rental_records(student1)
print(library.return_book_from_student(book1, student1))
library.check_rental_records(student1)