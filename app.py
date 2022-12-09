from flask import Flask
from flask_restful import Api

from endpoints.file_resource import FileResource

app = Flask(__name__)
api = Api(app)


api.add_resource(FileResource, '/', '/<path:path>')

if __name__ == '__main__':
    app.run(debug=True)