import os
import sys

from flask import Flask,request
import json


app = Flask(__name__)


@app.route('/configure', methods=['POST'])
def configure():
    arm = app.config['OBJECT']
    arm.configrue(json.loads(request))
    return True

@app.route("/getconfig", methods=['GET'])
def get_config():
    arm = app.config["OBJECT"]
    return arm.show_configuration()


def start_server(host="0.0.0.0", port=9998):
    app.config["OBJECT"] = ARM()
    app.run(host=host,
            port=int(port))

if __name__ == "__main__":
    real_path = os.path.dirname(os.path.realpath(__file__)) + "/../../../"
    sys.path.append(real_path)

    from server.device.arm.arm import ARM
    start_server()