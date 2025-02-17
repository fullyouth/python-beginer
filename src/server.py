from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!!!'

@app.route('/')
def home():
    return render_template('index.html', name='Haoqi',date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 运行应用
if __name__ == '__main__':
    app.run(debug=True)