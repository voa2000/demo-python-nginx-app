from flask import request, Flask
import json
webapp = Flask(__name__)
@awebapp.route('/')
def hello_world():
  return 'ArgoCD course, this is Webapp :) '
if __name__ == '__main__':
  webapp.run(debug=True, port=8000,host='0.0.0.0')