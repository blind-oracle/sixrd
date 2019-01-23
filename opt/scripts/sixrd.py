#!/usr/bin/env python3

import ipaddress, sys

if len(sys.argv) != 4:
    print('usage: {} <ipv6 6rd prefix> <ipv4 addr> <ext|int>'.format(sys.argv[0]))
    exit(1)

sixrd_pfx = sys.argv[1]
addr = sys.argv[2]
t = sys.argv[3]

ipv4 = ipaddress.ip_address(addr)
ipv4_i = int.from_bytes(ipv4.packed, 'big')

pfx = ipaddress.ip_network(sixrd_pfx)
pfx_i = int.from_bytes(pfx.network_address.packed, 'big')

sixrd_i = pfx_i + (ipv4_i << (64 + 32 - pfx.prefixlen))

if t == 'int':
    sixrd_i += (1 << 64)
elif t == 'ext':
    pass
else:
    print('unsupported type')
    exit(1)

sixrd = ipaddress.ip_address(sixrd_i)
print(sixrd)
