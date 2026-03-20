from flask import Flask, jsonify, request, send_from_directory
from variance import _find_variance

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/variance', methods=['POST'])
def compute_variance():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'Invalid JSON payload'}), 400

    if 'scores' not in data:
        return jsonify({'error': 'Missing "scores" key'}), 400

    scores = data['scores']
    if not isinstance(scores, list):
        return jsonify({'error': 'scores must be a list of integers'}), 400

    try:
        variance = _find_variance(scores)
    except (TypeError, ValueError) as exc:
        return jsonify({'error': str(exc)}), 400
    except Exception as exc:
        return jsonify({'error': 'Internal server error', 'detail': str(exc)}), 500

    return jsonify({'variance': variance, 'input': scores}), 200


@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
