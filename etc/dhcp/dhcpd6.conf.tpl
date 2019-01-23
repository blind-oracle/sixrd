authoritative;
ddns-update-style none;

default-lease-time 300;
max-lease-time 300;

subnet6 ###SUBNET###/###PREFIX### {
    range6 ###SUBNET###1000 ###SUBNET###1fff;
    option dhcp6.name-servers ###DNS###;
    option dhcp6.domain-search "example.net";
}
