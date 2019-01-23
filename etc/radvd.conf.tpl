interface ###LAN_IF### {
    AdvSendAdvert on;
    AdvLinkMTU ###MTU###;
    AdvSendAdvert on;
    MaxRtrAdvInterval 5;
    AdvDefaultPreference high;
    AdvSourceLLAddress off;

    prefix ::/64 {
        AdvRouterAddr on;
        AdvValidLifetime 7202;
        AdvPreferredLifetime 7201;
        DeprecatePrefix on;
    };

    route ::/0 {};

    RDNSS ###DNS### {};
};
