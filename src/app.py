from flask import Flask, request, jsonify, json
app = Flask(__name__)

todos = [
    { "label": "First task", "done": False }
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def new_todos():
    request_body = json.loads(request.data)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)