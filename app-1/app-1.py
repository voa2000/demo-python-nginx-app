from flask import request, Flask
import json
app1 = Flask(__name__)
@app1.route('/')
def hello_world():
  return '<h1>Coding Black Females - DevOps Course - Session 5, this is App-1 :) </h1>'
if __name__ == '__main__':
  app1.run(debug=True, host='0.0.0.0')
  