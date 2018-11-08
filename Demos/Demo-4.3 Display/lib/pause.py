# Note that the pymakr > run file command sends a few (4) additional keystrokes 
# as a result of this 

def pause(Status = None, msg='Press Enter to continue'):
    from sys import stdin
    if Status:
        print(Status)
    print("\033[1m\033[92m{}\033[0m".format(msg), end = ':>')
    x = stdin.readline()
    print("")
'''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
'''
