print("Entering Main.py")

print("network connected: {0} , IP: {1}, router: {4}".format(wifisetup.isconnected(), *wifisetup.wlan_sta.ifconfig() ))

