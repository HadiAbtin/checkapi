# CheckAPI makes failure on CHECK API and returns http Down status.
# It is used for making keyus situation to trigger Liveness probe
# or readyness probes in k8s. 
# Copyright 2024, Hadi Abtinfar <hadi.abtinfar@gmail.com>

from flask import Flask, url_for
from random import randrange

app = Flask(__name__)

app.config["JSONIFY_PRETTYPRINT_REGULAR"] = 1

REQUESTS=0
HEALTH=1
TARGET=randrange(100, 500)

@app.before_request
def count_request():
    global REQUESTS, HEALTH
    if REQUESTS >= TARGET:
        HEALTH = 0
    REQUESTS += 1

@app.route("/check")
def check():

    """
    Check API make comparison between random number and exact number of requests 
    on check endpoint up to now. if requests number equals to the fixed number,
    status of API will be DOWN. Otherwise the status is UP.
    """
    if HEALTH:
        return {"max": TARGET, "requests": REQUESTS}, 200
    return "DOWN", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
