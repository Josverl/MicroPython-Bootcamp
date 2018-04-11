def wifiscan():
    #Scan for accesspoints
    #and display them sorted by network strength
    import network;
    _nic = network.WLAN(network.STA_IF);
    _ = _nic.active(True)
    #sort on signal strength 
    _networks = sorted(_nic.scan(), key=lambda x: x[3], reverse=True)
    _f = "{0:<32} {2:>8} {3:>8} {4:>8} {5:>8}"
    print( _f.format("SSID","bssid","Channel","Signal","Authmode","Hidden") )
    for row in _networks: 
        print( _f.format( *row ) ) 
    del _f

wifiscan()
