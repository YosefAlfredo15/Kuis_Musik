from flask import Flask, jsonify, request, render_template, send_from_directory
from waitress import serve
import webbrowser
import threading
import socketio
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
sio = socketio.Server()
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# Data jawaban yang benar
correct_answers = {
    'q1': 'Gitar',
    'q2': 'Gendang',
    'q3': 'Biola',
    'q4': 'Semua Benar',
    'q5': 'Ditiup dan Ditekan',
    'q6': 'Kunci C',
    'q7': 'Kunci Em',
    'q8': 'Kunci D',
    'q9': 'Kunci Am',
    'q10': 'Kunci G'
}

# Error Handler API
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions', methods=['GET'])
def get_questions():
    questions = {k: v for k, v in correct_answers.items()}
    return jsonify(questions)

@app.route('/questions/<string:question_id>', methods=['GET'])
def get_question(question_id):
    question = correct_answers.get(question_id)
    if question is None:
        return jsonify({"error": "Question not found"}), 404
    return jsonify({question_id: question})

# Fungsi WebSocket untuk fitur real-time 
@sio.event
def connect(sid, environ):
    print('Client connected:', sid)

@sio.event
def disconnect(sid, environ):
    print('Client disconnected:', sid)

@sio.event
def submit_answer(sid, data):
    try:
        question_id = data.get('question_id')
        answer = data.get('answer')
        if not question_id or not answer:
            raise ValueError("Invalid input")

        correct_answer = correct_answers.get(question_id)
        if correct_answer is None:
            raise ValueError("Question not found")

        result = "Correct" if answer == correct_answer else "Incorrect"
        sio.emit('answer_result', {'question_id': question_id, 'result': result})
    except Exception as e:
        sio.emit('answer_result', {'error': str(e)})

# Setup Swagger UI
SWAGGER_URL = '/api/docs'
API_URL = '/statics/swagger.yaml'  # URL untuk file swagger.yaml
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Polling/Q&A System API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Serve Swagger YAML dan file statis lainnya
@app.route('/statics/<path:path>')
def send_statics(path):
    if path == 'swagger.yaml':
        return send_from_directory('statics', path, mimetype='text/yaml')
    return send_from_directory('statics', path)



def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000/")

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    serve(app, host='0.0.0.0', port=8000)
