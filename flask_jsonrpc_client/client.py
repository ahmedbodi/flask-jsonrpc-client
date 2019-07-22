import itertools
import json
import requests
from decimal import Decimal
from flask import current_app, _app_ctx_stack

class Client(object):
    def __init__(self, app=None):
        self.app = app
        self.id_counter = itertools.count()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('JSONRPC_SERVERS', {})

    def request(self, server, method, params):
        if not server in app.config['JSONRPC_SERVERS']:
            raise Exception("Server not found in Configuration. Key: 'JSON_SERVERS'")

        payload = json.dumps({"method": method, "params": params, 'jsonrpc': '2.0', 'id': next(self.id_counter)})
        headers = {"content-type": "application/json"}
        try:
            response = requests.POST(app.config['JSONRPC_SERVERS'][server]['url'],
                data=payload, headers=headers, auth=(
                    app.config['JSONRPC_SERVERS'][server]['username'],
                    app.config['JSONRPC_SERVERS'][server]['password']
                )
            )
            return response.json(parse_float=Decimal)
        except Exception as exc:
            raise exc
