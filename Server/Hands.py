import json

from flask import *
from Objects.Cards import *

app = Flask(__name__)

hand_chances_db = 'card-probabilities-old.json'
hand_chances = {}


def load_hand_probabilities(probability_db):
    with open(probability_db, 'r') as file_handler:
        temp_chances = json.loads(file_handler.read())
    return temp_chances

@app.route('/api/hand-chances/', methods=['GET'])
def get_hand_chance():
    raw_hand = request.data
    hand = raw_hand.decode('utf-8')
    return hand_chances[hand]


@app.route('/')
def hands():
    return render_template("Hands.html")


if __name__ == '__main__':
    hand_chances = load_hand_probabilities(hand_chances_db)
    print(hand_chances)
    app.run()
