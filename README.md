# i-Soma Toolkit Hub

The i-Soma toolkit hub is an IoT hub-like service for connecting Soma bit 
hardware dynamically to [Robot Operating System](https://www.ros.org/)
infrastructure.

## Installation

The hub has been developed to run on a [LattePanda V1](https://www.lattepanda.com/lattepanda-v1)
running [Lubuntu 22.04](https://lubuntu.me/jammy-released/). Other systems 
(e.g., Raspberry Pi) may work as long as they support Bluetooth LE. Connection
to a 2.4Ghz Wi-Fi network is also necessary (in the case of the LattePanda, it
can be configured as a wireless AP).

Use [Docker](https://www.docker.com/) and 
[Docker Compose](https://docs.docker.com/compose/) to build and run the hub.

Once running, open a web browser to the configured IP address.

## License

[AGPVv3](https://choosealicense.com/licenses/agpl-3.0/)

## Acknowledgements

This research development is supported by EPSRC under grant reference numbers
EP/V00784X/1: TAS-Hub and EP/T022493/1: Horizon.
