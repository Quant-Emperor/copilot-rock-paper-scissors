from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    if not data or 'user_choice' not in data:
        return jsonify({"error": "Invalid input. Please provide 'user_choice'."}), 400

    user_choice = data['user_choice'].strip().lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        return jsonify({"error": "Invalid choice. Valid options are 'rock', 'paper', or 'scissors'."}), 400

    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)