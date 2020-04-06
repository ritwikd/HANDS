from flask import *
from flask_cors import CORS, cross_origin
from Simulator import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@cross_origin()
@app.route('/api/hand-chances/', methods=['POST'])
def get_hand_chance():
    rq = request.json
    print(rq)
    hand = [tuple(card) for card in rq['hand']]
    board = [tuple(card) for card in rq['board']]
    runs = rq['runs']
    print(runs)
    output = simulate_hand_probability(hand, runs, board)
    print(output)
    return jsonify(output)


@app.route('/')
def hands():
    return render_template("Hands.html")


if __name__ == '__main__':
    app.run()