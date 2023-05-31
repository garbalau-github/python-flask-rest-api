from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Alice"}
]

@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(data)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404


@app.route('/items', methods=['POST'])
def create_item():
    new_item = {'id': request.json['id'], 'name': request.json['name']}
    data.append(new_item)
    return jsonify(new_item)


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        item['name'] = request.json['name']
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        data.remove(item)
        return jsonify({'message': 'Item deleted'})
    else:
        return jsonify({'error': 'Item not found'}), 404


if __name__ == '__main__':
    app.run()
