from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
     {
         'id': 1,
         'title': 'O Senhor dos Anéis - A Sociedade do Anel',
         'author': 'J.R.R. Tolkien'
     },
     {
         'id': 2,
         'title': 'Harry Potter e a Pedra Filosofal',
         'author': 'J.K. Howling'
     },
     {
         'id': 3,
         'title': 'Hábitos Atômicos',
         'author': 'James Clear'
     }
 ]

# get all books
@app.route('/all', methods=['GET'])
def get_all_books():
    return jsonify(books)

# get book by id
@app.route('/book/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# edit book
@app.route('/book/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    updated_book = request.get_json()
    for index,book in enumerate(books):
        if book.get('id') == id:
            books[index].update(updated_book)
            return jsonify(books[index])

# create book
@app.route('/book', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

# delete book
@app.route('/book/<int:id>',methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]

    return jsonify(books)



app.run()
# app.run(port=5000, local='localhost', debug=True)




