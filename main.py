import uuid

from flask import Flask, request, abort, jsonify

app = Flask(__name__)


todo_list_id_1 = "bd65600d-8669-4903-8a14-af88203add38"
todo_list_id_2 = "5361a11b-615c-42bf-9bdb-e2c3790ada14"
todo_list_id_3 = "16fd2706-8baf-433b-82eb-8c7fada847da"
user_id_1 = uuid.uuid4()
user_id_2 = uuid.uuid4()
user_id_3 = uuid.uuid4()
entry_id_1 = uuid.uuid4()
entry_id_2 = uuid.uuid4()
entry_id_3 = uuid.uuid4()

todo_lists = [
    {'id': todo_list_id_1, 'name': 'todo_list_1', 'description': 'Description for List 1'},
    {'id': todo_list_id_2, 'name': 'todo_list_2', 'description': 'Description for List 2'},
    {'id': todo_list_id_3, 'name': 'todo_list_3', 'description': 'Description for List 3'},
]

user_list = {[
    {'id': user_id_1, 'name': 'User 1'},
    {'id': user_id_2, 'name': 'User 2'},
    {'id': user_id_3, 'name': 'User 3'},
]}

entry_list = {[
    {'id': entry_id_1, 'name': 'Entry 1', 'description': 'Description for Entry 1', 'list': todo_list_id_1},
    {'id': entry_id_2, 'name': 'Entry 2', 'description': 'Description for Entry 2', 'list': todo_list_id_2},
    {'id': entry_id_3, 'name': 'Entry 3', 'description': 'Description for Entry 3', 'list': todo_list_id_3},
]}


@app.route('/list/<list_id>', methods=['DELETE', 'GET'])
def handle_list(list_id):
    list_item = None

    for i in todo_lists:
        if i['id'] == list_id:
            list_item = i
            break

    if not list_id:
        abort(404)

    if request.method == 'GET':
        print('Ausgeben der Einträge:')
        return jsonify([j for j in entry_list if j['list'] == list_id])
    elif request.method == 'DELETE':
        print('Löschen der Liste')
        todo_lists.remove(list_item)
        return 'Löschen komplett.', 200


@app.route('/lists', methods=['GET'])
def handle_list():
    return jsonify(todo_lists)


@app.route('/list', methods=['POST'])
def create_list():
    new_list = request.get_json(force=True)
    new_list['id'] = uuid.uuid4()
    todo_lists.append(new_list)
    return 'Neue Liste wurde erstellt.'


@app.route('/users', methods=['GET'])
def users_get():
    return 'SHOW ALL USERS'


@app.route('/user', methods=['POST'])
def user_add():
    return 'CREATE USER'


@app.route('/user/<user_id>', methods=['DELETE'])
def user_delete(user_id):
    return 'DELETE USER'


@app.route('/list/<list_id>/entry', methods=['POST'])
def entry_add(list_id):
    return 'CREATE ENTRY'


@app.route('/list/<list_id>/entry/<entry_id>', methods=['POST'])
def entry_update(list_id, entry_id):
    return 'UPDATE ENTRY'


@app.route('/list/<list_id>/entry/<entry_id>', methods=['DELETE'])
def entry_delete(list_id, entry_id):
    return 'DELETE ENTRY'


if __name__ == '__main__':
    app.run()

