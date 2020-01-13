from datetime import datetime
from flask import Flask
from flask import make_response
from flask import request
import json
from gevent.pywsgi import WSGIServer
import requests
import time
from threading import Timer
import os


APP = Flask(__name__)
BOT_TOKEN = None

def main():
    global BOT_TOKEN
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    if BOT_TOKEN is None:
        exit(1)

    http_server = WSGIServer(('', 5001), APP)
    http_server.serve_forever()

@APP.route("/bot", methods=['POST'])
def endpoint():
    print (request.form)
    if "payload" in request.form:
        # handling form responses
        payload = json.loads(request.form["payload"])
        action = payload["actions"][0]
        action_id = action.get("action_id")
        user_id = payload["user"]["id"]

        # needs a return


    # simple requests
    if request.form['text'] == "check":
        return check()
    if request.form['text'] == "create":
        return create()

    return help()

def help():
    body = {"text": """
check - Check the WebEx rooms schedule
create - Create a WebEx meeting
"""}

    resp = make_response(json.dumps(body), 200)
    resp.headers["Content-type"] = "application/json"

    return resp

def check():
    body = {"text": "", "response_type": "in_channel"}

    #todo implement check

    resp = make_response(json.dumps(body), 200)
    resp.headers["Content-type"] = "application/json"

    return resp

# Exapmle form (leftover)
'''
def request_reservation():

    body = {"blocks":[
    {
        "type": "section",
        "block_id": "header",
        "text": {
            "type": "plain_text",
            "text": "Choose account"
        }
    },
    {
        "type": "section",
        "block_id": "acc_pick_section",
        "text": {
            "type": "plain_text",
            "text": "There are %s accounts in the pool" % len(STATUS)
        },
        "accessory": {
            "action_id": "account_reservation",
            "type": "static_select",
            "confirm": {
                "title": {
                    "type": "plain_text",
                    "text": "Confirm"
                    },
                "text": {
                    "type": "plain_text",
                    "text": "Plese confirm"
                },
                "confirm": {
                    "type": "plain_text",
                    "text": "OK"
                },
                "deny": {
                    "type": "plain_text",
                    "text": "I've changed my mind!"
                }
            },
            "placeholder": {
                "type": "plain_text",
                "text": "..."
            },
            "options": []
        }
    }]}

    for acc in STATUS:
        option = {
            "text": {
                "type": "plain_text",
                "text": acc["name"]
            },
            "value": "reserve_%s" % acc["id"]
        }
        body["blocks"][1]["accessory"]["options"].append(option)


    resp = make_response(json.dumps(body), 200)
    resp.headers["Content-type"] = "application/json"

    return resp
'''
if __name__ == "__main__":
    main()
