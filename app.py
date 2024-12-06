from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Priyanshu mishra 2201330100190'

if __name__ == '__main__':
    app.run(port=5000)
