#!/bin/sh

. /opt/ros/humble/setup.sh
. /soma-kit-hub_ws/install/setup.sh
ros2 launch soma_kit_hub default.launch.yaml \
  hub_ui_pkg_dir:=${HUB_UI_PKG_DIR} \
  hub_ui_port:=${HUB_UI_PORT} \
  ws_server_port:=${WS_SERVER_PORT}
