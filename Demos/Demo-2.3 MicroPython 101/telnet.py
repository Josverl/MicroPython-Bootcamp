#allow the board to be reached via telnet
try:
    import network
    network.telnet.start(user="micro", password="python", timeout=300)
except:
    pass
