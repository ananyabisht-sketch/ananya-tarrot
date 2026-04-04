from flask import Flask, render_template

app = Flask(__name__)

SESSIONS = [
    {'name': 'General Spread',       'duration': '10+ min', 'price': '₹20', 'desc': 'A quick, focused read on whatever is on your mind right now.'},
    {'name': 'Love & Relationships', 'duration': '10+ min', 'price': '₹20', 'desc': 'Clarity on connections, patterns, and what you truly want.'},
    {'name': 'Career & Path',        'duration': '10+ min', 'price': '₹20', 'desc': 'For crossroads, decisions, and figuring out what comes next.'},
]

QUOTES = [
    {'text': 'The mind is everything. What you think, you become.', 'author': 'Buddha'},
    {'text': 'Peace comes from within. Do not seek it without.', 'author': 'Buddha'},
    {'text': 'In the end, only three things matter — how much you loved, how gently you lived, and how gracefully you let go of things not meant for you.', 'author': 'Buddha'},
    {'text': 'You yourself, as much as anybody in the entire universe, deserve your love and affection.', 'author': 'Buddha'},
    {'text': 'The trouble is, you think you have time.', 'author': 'Buddha'},
]

@app.route('/')
def index():
    return render_template('index.html', sessions=SESSIONS, quotes=QUOTES)

if __name__ == '__main__':
    app.run(debug=True)
