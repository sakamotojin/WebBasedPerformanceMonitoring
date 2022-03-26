from flask import Flask
from UserInterface.UserInterface import UserInterface
from WebServices.WebServices import WebServices

def RunTestingService():
    from subprocess import Popen
    print('Running Testing Service')
    Popen(["node", "TestingService/index.js"])


app = Flask(__name__)

user_interface = UserInterface(app)
web_services = WebServices(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)

