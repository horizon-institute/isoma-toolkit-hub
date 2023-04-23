ARG ROS2_DISTRO=humble
FROM ros:${ROS2_DISTRO}-ros-base
ARG ROS2_DISTRO

ENV HUB_UI_PKG_DIR=/soma-kit-hub_ws/src/soma_kit_hub
ENV HUB_UI_PORT=8000
ENV WS_SERVER_PORT=9090

RUN export DEBIAN_FRONTEND=noninteractive \
  && apt update \
  && apt install -y \
  python3-pip \
  ros-${ROS2_DISTRO}-rosbridge-suite \
  && pip3 install pipenv \
  && rm -rf /var/lib/apt/lists/*

ADD src /soma-kit-hub_ws/src/soma_kit_hub
ADD Pipfile /soma-kit-hub_ws/Pipfile
ADD https://bootswatch.com/5/lux/bootstrap.min.css \
  /soma-kit-hub_ws/src/soma_kit_hub/static/css/bootstrap.min.css
ADD https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js \
  /soma-kit-hub_ws/src/soma_kit_hub/static/js/bootstrap.bundle.min.js
ADD https://cdn.jsdelivr.net/npm/jquery@3.6.4/dist/jquery.min.js \
  /soma-kit-hub_ws/src/soma_kit_hub/static/js/jquery.min.js

WORKDIR /soma-kit-hub_ws

RUN pipenv lock && pipenv install --system

RUN rosdep install -i --from-path src --rosdistro ${ROS2_DISTRO} -y \
  && colcon build

ADD docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE ${HUB_UI_PORT}
EXPOSE ${WS_SERVER_PORT}

ENTRYPOINT [ "sh", "/docker-entrypoint.sh" ]
