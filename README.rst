Telnyx coding challenge
########################
A small script that can handle reservation requests for VLANs on network
devices.

These network devices have a primary port and sometimes a secondary one. Each
port has a range of available VLANs.

The requests can ask for redundancy, so there are two type of requests,
simple and redundant. Once a VLAN has been reserved, no other request can
reserve it.

For simple requests:

- A single VLAN, using the lowest available id on any port will be reserved
- In case of a tie, the device with the lowest id will be chosen

For redundant requests:

- Two VLANs will be reserved, one from a primary port and one from a secondary port.
- The ports will be on the same device and the VLAN ids will be the same on both ports.
- In case of a tie, the device with the lowest id will be chosen

Usage
#####

Install with::

    python setup.py install

Running::

    shinydisco [vlans.csv, requests.csv, output.csv] [-v]

Testing::

    pytest -p no:logging
