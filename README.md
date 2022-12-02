# swiftclient-example

Containers must be attached to public-access-vlan (10.70.70.0/24) which has a sharednet router interface as the gateway to the public network.

Just a container with access to the public network:
```
networks.1.interface=eno12399np0,networks.1.ip=10.70.70.5/24,networks.1.routes=10.0.86.0/23-10.70.70.1
```
Run client container with the following lables if networks.1 is `5gue-net` and networks.2 is `public-access-vlan`.
```
networks.1.interface=ens5f1,networks.1.ip=10.42.3.2/24,networks.1.routes=10.99.99.0/24-10.42.3.1,networks.2.interface=eno12399np0,networks.2.ip=10.70.70.5/24,networks.2.routes=10.0.86.0/23-10.70.70.1
```
