#Clean all files from flash 
# use with care ; there is no undo or trashcan 

import uos as os 

def whipe_dir( path=".",sub=True):
        l = os.listdir(path)
        l.sort()
        for f in l:
            child = "%s/%s" % (path, f)
            st = os.stat(child)
            if st[0] & 0x4000:  # stat.S_IFDIR
                print("   <dir> %s" % child)
                if sub:
                    
                    whipe_dir(child,sub)
                    os.rmdir(child)
            else:
                os.remove(child)

def main():
    a = input("Do you wish to whipe the /flash folder and all underlying files ?")
    if a=='Y' or a=='y':
        whipe_dir(path='/flash',sub=True)

if __name__ == "__main__":
    main()

