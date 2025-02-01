"""Ejercicio
https://retosdeprogramacion.com/roadmap/"""

#! Incorrecta
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
  def save_to_db(self): ## Primera responsabilidad
    pass
  def send_email(self):  ## Segunda responsabilidad
    pass
  
#! Correcta con SRP
    """Lo que pasa aqui, es que creamos clases para cada responsabilidad, y no mezclamos las responsabilidades en una sola clase.
    De esta manera, si hay un cambio en una responsabilidad, no afecta a la otra.
    """
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
class UserService:
  def save_to_db(self, user): ## Primera responsabilidad
    pass

class EmailService:
  def send_email(self, mail, message):    ## Segunda responsabilidad
    pass


"""Extra"""

#! Incorrecta
"""El problema aqui es que tenemos varias responsabilidades en una misma clase, y si modificamos algo, afectaria a todo el codigo y eso es demasiado malo"""

class Library:
  def __init__(self):
    self.books = []
    self.users = []
    self.loans = []
    
  def add_book(self, title, author, copies):  ## Primera responsabilidad
    self.books.append({'title': title, 'author': author, 'copies': copies})
  def add_user(self, name, email, id):  ## Segunda responsabilidad
    self.users.append({'name': name, 'email': email, "id": id})
  def lend_book(self, user_id, book_title):  ## Tercera responsabilidad
    for book in self.books:
      if book['title'] == book_title and book['copies'] > 0:
        self.loans.append({'user_id': user_id, 'book_title': book_title})
        book['copies'] -= 1
        self.loans.append({'user_id': user_id, 'book_title': book_title})
        return True
    return False
  def return_book(self, user_id,book_title):  
    for loan in self.loans:
      if loan['user_id'] == user_id and loan['book_title'] == book_title:
        self.loans.remove(loan)
        for book in self.books:
          if book['title'] == book_title:
            book['copies'] += 1
        return True
    return False
  
#! Correcta con SRP

class Book: ## Primera responsabilidad
  def __init__(self, title, author, copies):
    # Ya tenemos una estructura bien
    self.title = title
    self.author = author
    self.copies = copies
class User: ## Segunda responsabilidad
  def __init__(self, name, email, id):
    self.name = name
    self.email = email
    self.id = id
class Loan: ## Tercera responsabilidad
  def __init__(self, user_id, book_title):
    self.user_id = user_id
    self.book_title = book_title
    self.loans = []
  def loan_book(self, user, book):
    
    if book.copies > 0:
      book['copies'] -= 1
      self.loans.append({'user_id': user.id, 'book_title': book.title})
      
  
      return True
    return False

  def return_book(self, user, book):  
    for loan in self.loans:
      if loan['user_id'] == user.id and loan['book_title'] == book.title:
        self.loans.remove(loan)
        book['copies'] += 1
        return True
    return False
class Library:
  def __init__(self):
    self.books = []
    self.users = []
    self.loans = Loan()
    
  def add_book(self, book ):  ## Primera responsabilidad
    self.books.append(book)
  def add_user(self,user):  ## Segunda responsabilidad
    self.users.append(user)
  def loan_book(self, user_id, book_title):  ## Tercera responsabilidad
    user = next((u for u in self.users if u.id == user_id), None) ### Next: Devuelve el primer elemento que cumple con la condicion dada en la lista de usuarios
    book = next((b for b in self.books if b.title == book_title), None) ### Next: Devuelve el primer elemento que cumple con la condicion dada en la lista de libros 
    if user and book:
      return self.loans.loan_book(user, book)
    return False
  def return_book(self, user_id,book_title):  
    user = next((u for u in self.users if u.id == user_id), None) ### Next: Devuelve el primer elemento que cumple con la condicion dada en la lista de usuarios
    book = next((b for b in self.books if b.title == book_title), None) ### Next: Devuelve el primer elemento que cumple con la condicion dada en la lista de libros
    if user and book:
      return self.loans.return_book(user, book)
    return False