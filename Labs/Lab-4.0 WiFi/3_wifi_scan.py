def wifiscan():
    #Scan for accesspoints
    #and display them sorted by network strength
    import network #pylint: disable=import-error
    wlan = network.WLAN(network.STA_IF)
    _ = wlan.active(True)

    #Scan WiFi network and return the list of available access points.
    #If the optional argument hidden is set to True the hidden access points (not broadsasting SSID) will also be scanned.
    #Each list entry is a tuple with the following items:
    #(ssid, bssid, primary_chan, rssi (signal Strength), auth_mode, auth_mode_string, hidden)
    _networks = wlan.scan(True)
    #sort on signal strength 
    _networks = sorted(_networks, key=lambda x: x[3], reverse=True)
    #string to define columns and formatting
    _f = "{0:<32} {2:>8} {3:>8} {5:12} {6:>8}"
    print( _f.format("SSID",'mac',"Channel","Signal","0","Authmode","Hidden") )
    for row in _networks: 
        print( _f.format( *row ) ) 
    del _f

def main():
    wifiscan()

if __name__ == '__main__':
    main()

