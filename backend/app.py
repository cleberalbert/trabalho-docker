from flask import Flask, request, jsonify
import base64
import random
from uuid import uuid4

app = Flask(__name__)
games = {}

@app.route('/create', methods=['POST'])
def create_game():
    data = request.get_json()
    secret_phrase = data.get('phrase')
    game_id = str(uuid4())
    encoded_phrase = base64.b64encode(secret_phrase.encode()).decode()
    games[game_id] = {
        'phrase': encoded_phrase,
        'attempts': []
    }
    return jsonify({'game_id': game_id}), 201

@app.route('/guess/<game_id>', methods=['POST'])
def guess(game_id):
    data = request.get_json()
    guess = data.get('guess')
    
    if game_id not in games:
        return jsonify({'message': 'Game not found.'}), 404
    
    encoded_phrase = games[game_id]['phrase']
    secret_phrase = base64.b64decode(encoded_phrase).decode()
    attempts = games[game_id]['attempts']
    
    if guess == secret_phrase:
        return jsonify({'message': 'Parabéns! Você adivinhou a senha!'}), 200
    
    feedback = []
    for i, char in enumerate(guess):
        if i < len(secret_phrase):
            if char == secret_phrase[i]:
                feedback.append(f"{char} está na posição correta.")
            elif char in secret_phrase:
                feedback.append(f"{char} está na senha, mas na posição errada.")
    
    attempts.append(guess)
    games[game_id]['attempts'] = attempts
    
    return jsonify({'feedback': feedback}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)