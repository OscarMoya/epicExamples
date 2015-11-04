import os
import sys

from flask import Flask,request
import json


app = Flask(__name__)


@app.route('/configure', methods=['POST'])
def configure():
        adm = app.config['OBJECT']
        adm.configrue(json.loads(request))

@app.route("/getconfig", methods=['GET'])
def get_config():
    arm = app.config["OBJECT"]
    return arm.show_configuration()

def start_server(host="0.0.0.0", port=9999):
    app.config["OBJECT"] = ADM()
    app.run(host=host,
            port=int(port))

if __name__ == "__main__":
    real_path = os.path.dirname(os.path.realpath(__file__)) + "/../../../"
    sys.path.append(real_path)
    print real_path
    print sys.path
    from server.device.adm.adm import ADM
    start_server()