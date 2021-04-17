from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        'Contact': u'7894561230',
        'Name': u'Raju',
        'done': False,
        'id': 1
    },
    {
        'Contact': u'1234567890',
        'Name': u'Rahul',
        'done': False,
        'id': 2
    }
]

@app.route('/add-data', methods=['POST'])
def add_task():
    if not request.json:
        return jsonify(
            {
                'status': 'error',
                'message': 'Please provide the data'
            },
            400
        )

    task = {
        'id': tasks[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify(
        {
            'status': 'success',
            'message': 'Task added successfully'     
        }
    )

@app.route('/get-data')
def get_task():
    return jsonify(
        {
            'data': tasks,
        }
    )

if __name__ == '__main__':
    app.run(debug=True)