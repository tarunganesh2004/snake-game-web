from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_game', methods=['POST'])
def run_game():
    # Replace 'snake_game.py' with your game script name
    subprocess.run(['python', 'snake_game.py'])
    return "Game started!"


if __name__ == '__main__':
    app.run()
