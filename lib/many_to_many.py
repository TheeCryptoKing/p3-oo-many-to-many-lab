class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(name)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    # needed solution refrence
    def books(self):
        return [contract.book for contract in self.contracts()]
    # needed solution no way i would have known to do this, with the wording, theres so many ways to creat a class object wtf
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    # creates a new contract using the Contract(and leaving paramerters in )
    
    # not sure on how to go about need to add all royalties for input so for loop?
    def total_royalties(self):
        # needed solution
        # need help doing list comprhension 
        return sum([contract.royalties for contract in self.contracts()])
    # wasn't thinking about returing from and iterating contracts this way 
    # iif need to iterate through array with


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(title)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
    

class Contract:
    all= []

    def __init__(self, author, book, date, royalties):
        # if not isinstance(book, Book) or book not in Book.all:
        #     raise Exception
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
         if not isinstance(author, Author):
            raise Exception
         self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
         if not isinstance(book, Book):
            raise Exception
         self._book = book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception 
        self._date = date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception 
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contracts: contracts.date)
        # needed to reference solution was kinda close also test and read me say different things 
        # needed to grab cls.all becasue that is where all the data lives for the cotracts
        # contracts could have been anything 
        # lambda is a anonomyous fnction basically. The key parameter specifies a function that will be applied to each element in the list to determine the sorting order.
