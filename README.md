# sixrd
Scripts and configuration files for IPv6 connectivity with ISPs using 6rd (SixRD) protocol on Linux.

# About protocol
SixRD (or 6rd) is an acronym for *IPv6 Rapid Deployment*. It's a successor to the 6to4 protocol to easily make IPv6 available over existing IPv4 network. 

* IPv6 traffic is tunneled over IPv4 from your box up to ISP's gateway which decapsulates it and after that packets go natively over Internet.
* ISP has some fixed prefix like *2a02:1200::/28* to which your IPv4 address should be appended to form a IPv6 subnet which is used by the client.
* After appending 32 bits of IPv4 to e.g. 28-bit prefix you have 4 bits for your own 64-bit subnets.

# Purpose of these scripts
They were made to facilitate automatic IPv6 configuration when the provider is using 6rd, in my case it's Swisscom (Switzerland). Your mileage may vary, but it should be similar.

We'll use the following:
* 6rd DHCP hook to set up things
* Python script to do IPv6 math which is hard to do in *bash*
* Configuration templates for *radvd* and *isc-dhcp-server* if you want to make IPv6 available on your LAN.
  - For most use cases *radvd* is enough, but some clients (like Windows) are unable to get DNS info from Router-Advertisement packets - they need DHCPv6 for this.
  - If you use Dual-Stack v4/v6 and have DNS in v4 which supports IPv6 AAAA resolving then it's not a problem, as IPv6 addresses will be resolved through it.

# How it works
* We acquire an IPv4 address using *dhclient* in the usual way (`iface XXX inet dhcp` in */etc/network/interfaces*)
* After address is obtained, DHCP hook is executed which:
  - Calculates the required IPv6 address using prefix and IPv4 address
  - Sets up 6rd tunnel (**i6** interface by default)
  - Optionally:
    - Calculates the LAN IPv6 address (adds *1* to the external subnet)
    - Sets up IPv6 on LAN interface
    - Generates configs for *radvd* and/or *isc-dhcp-server*
    - Restarts the daemons

# Requirements
* Linux with *dhclient* (I've tested only on Ubuntu)
* Python3 or Python2 with *ipaddress* module backported (`apt install python-ipaddress`, change interpreter to *python* in this case)
* Optionally *radvd* and/or *isc-dhcp-server* installed (`apt install radvd isc-dhcp-server`) to provide IPv6 on LAN.

# Usage
* Put hook, script and templates where they should belong. This repo is already organized in the right way for Ubuntu, but you might need to adjust to your distribution.
* Edit the hook to provide, at least, **sixrd_gateway** and **sixrd_prefix** (plus, possibly, **mtu**) which are ISP-specific.
  - Currently the DNS given out to the clients is set to the IPv6 address of your router, but you can use anything else, just replace *###DNS###* in the templates.
* Optionally adjust *radvd* and *dhcpd* configuration and templates according to your needs.
* Do *ifdown* & *ifup* to reinitialize the interface

# Credits
Based on an [article](https://vincent.bernat.ch/en/blog/2014-swisscom-router) by [Vincent Bernat](https://github.com/vincentbernat)
