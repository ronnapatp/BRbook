from datetime import date,timedelta

python = {
    'name':'python',
    'is_available':True,
    'return_date':None,
    'userid': None
}

python['is_available'] = False
python['return_date'] = date.today()-timedelta(days=3)
python['userid'] = 1

java = {
    'name':'java',
    'is_available':True,
    'return_date':None,
    'userid':None
}
scratch = {
    'name':'scratch',
    'is_available':True,
    'return_date':None,
    'userid':None
}
books = {1:python, 2:java, 3:scratch}
users = {1:'John',2:'Sally',3:'Susan'}

def borrowbook(bookid,userid):
    if books[bookid]['is_available'] == True:
        books[bookid]['is_available'] = False
        books[bookid]['return_date'] = date.today() + timedelta(days=7)
        books[bookid]['userid'] = userid

        print('Thank you {name}'.format(name=users[userid]))
        print('Please return {book} book before {returndate}'.format(book=books[bookid]['name'],returndate=books[bookid]['return_date']))
    
    else:
        print('This book is not available but you can borrow another book in our library')
        print('{book} book will be retruned on {returndate}'.format(book=books[bookid]['name'],returndate=books[bookid]['return_date']))
        print('Thank you {name}'.format(name=users[userid]))
        

def returnbook(bookid,userid):
    today = date.today()
    due_date = books[bookid]['return_date']
    day = (today-due_date).days

    if day > 0:
        charge = day*3
        print(f'charge: {charge} Bath')

        books[bookid]['is_available'] = True
        books[bookid]['return_date'] = None
        books[bookid]['userid'] = None

        print('Thank you {name}' .format(name=users[userid]))

    else :
        books[bookid]['is_available'] = True
        books[bookid]['return_date'] = none
        books[bookid]['userid'] = None

        print('Thank you {name}' .format(name=users[userid]))
    

action = input('Borrow or Return (B/R): ')
userid = int(input('User id: '))
bookid = int(input('Book id: '))

if action == 'b':
    borrowbook(bookid,userid)

if action == 'r':
    returnbook(bookid,userid)
#made by rs
