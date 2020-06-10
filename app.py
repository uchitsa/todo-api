#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title': u'Buy bread',
        'description': u'Fresh bread',
        'done': False
    },
    {
        'id':2,
        'title': u'Learn 7 langs in 7 weeks',
        'description': u'Need to find info about all of 7 langs',
        'done': False
    },
]


@app.route('/todo/api/v1/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(404)
    task = {
        'id':tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))


@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if not task:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
