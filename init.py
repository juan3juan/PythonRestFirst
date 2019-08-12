from flask import Flask, jsonify, request

app = Flask(__name__)
print(__name__)
app.debug = True

books = [
    {
        "name":"jihan",
        "price":1,
    },
    {
        "name": "yury",
        "price": 3,
    }
]
@app.route('/')
def hello_World():
    return 'Hello World!'

@app.route('/books')
def get_books():
    return jsonify({'book--':books})

@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    books.insert(0, request_data)

@app.route('/books/<string:name>')
def get_book_by_name(name):
    return_value = {}
    print(type(name))
    for book in books:
        if book["name"] == name:
            return_value = {
                "name": book["name"],
                "price": book["price"]
            }
    return jsonify(return_value)

app.run(port=5000)