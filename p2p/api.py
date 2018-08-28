# -*- coding: utf-8 -*-

import json
from utils.ppool import PeersPool
from flask import Blueprint
from flask import request


api = Blueprint("api", __name__, url_prefix="/api/1.0")

def make_response(msg="OK", data=None):
    data = {
        "meta": {
            "code": 0,
            "message": msg
        },
        "data": data
    }
    return json.dumps(data)


@api.route("/peers", methods=['GET'])
def get_all_peers():
    pool = PeersPool()
    return make_response(data=pool.peers())


@api.route("/peer/add", methods=['POST'])
def add_peer():
    pool = PeersPool()
    data = request.json
    address = (data.get("host"), data.get("port"))
    if not pool.is_exist(address):
        pool.add_peer(address)
    return make_response()

