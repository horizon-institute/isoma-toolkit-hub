import inspect
import json
import logging


class WebSocketRouter:
    routes = {}

    def __init__(self, routes) -> None:
        self.routes = routes

    async def do_rpc(self, websocket, body):
        request = json.loads(body)
        if "function" in request and request["function"] in self.routes:
            if "id" in request:
                _id = request["id"]
                f = self.routes[request["function"]]
                data = request["data"] if "data" in request else {}
                sig = inspect.signature(f)
                args = []
                for k in sig.parameters.keys():
                    if k in data:
                        args.append(data[k])
                    else:
                        logging.error(f"Required parameter '{k}' missing from data")
                        return
                result = await f(*args)
                await websocket.send_json(
                    {
                        "id": _id,
                        "result": result,
                    }
                )
