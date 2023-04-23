import asyncio
from pathlib import Path

from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

import rclpy
from rclpy import logging


import uvicorn

from . import discovery, routing


class RPCRouter(WebSocketEndpoint):
    router = routing.WebSocketRouter(
        {
            "discover_devices": discovery.discover_devices,
        }
    )

    async def on_receive(self, websocket, data):
        asyncio.ensure_future(self.router.do_rpc(websocket, data))


def main(args=None):
    rclpy.init(args=args)
    n = rclpy.create_node("hub")
    n.declare_parameter("pkg_dir", value="")
    n.declare_parameter("port", value=8000)

    pkg_dir = Path(n.get_parameter("pkg_dir").value)
    templates = Jinja2Templates(directory=pkg_dir.joinpath("templates"))

    async def homepage(request):
        return templates.TemplateResponse("index.html", {"request": request})

    app = Starlette(
        debug=True,
        routes=[
            Route("/", homepage),
            WebSocketRoute("/ws", endpoint=RPCRouter),
            Mount(
                "/static",
                app=StaticFiles(directory=pkg_dir.joinpath("static")),
                name="static",
            ),
        ],
    )

    config = uvicorn.Config(
        app,
        port=n.get_parameter("port").value,
        host="0.0.0.0",
        log_level="info",
    )
    server = uvicorn.Server(config)
    asyncio.run(server.serve())
    """
    # https://github.com/mavlink/MAVSDK-Python/issues/419#issuecomment-1008905339
    async def run_ros2():
        while True:
            rclpy.spin_once(n, timeout_sec=0)
            await asyncio.sleep(0.0)

    async def gather():
        await asyncio.gather(server.serve(), run_ros2())

    asyncio.run(gather())
    """
    n.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
