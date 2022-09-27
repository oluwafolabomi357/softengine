from flask import Flask

app = Flask(__name__)


@app.route('/softengine/<name>')
def hello_world(name):
    return f'<p>HELLO,{name.upper()}</p>'

@app.route("/ola/<float:amount>")
def new_world(amount):
    return f"Amount ${amount} saved!"

@app.route("/jegs/<int:score>")
def second_world(score):
    return f"The score {score} has just been saved here."

if __name__ == '__main__':
    app.run()