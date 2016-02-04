import os
import sys
import re
import time
import platform
def loader(output_dir, output_file, blacklist_file, debug):
    odir = output_dir
    if not odir.endswith("/") or not odir.endswith("\\"):
        odir = odir + os.path.sep
    filename = output_file
    ts = time.time()
    filename = filename.replace("{ts}",str(int(ts)))
    if not os.path.exists(odir):
        if debug:
            print "Loader> Ouput folder does not exist, creating new one"
        os.mkdir(odir)
    if not os.path.exists(odir + filename):
        if debug:
            print "Loader> Ouput file does not exist, creating new one"
        f = file(odir + filename, "w")
        f.close()
    if not os.path.exists(odir + filename):
        if debug:
            print "Loader> Blacklist file does not exist, creating new one"
        f = file(odir + blacklist_file, "w")
        f.close()
    return odir + filename
