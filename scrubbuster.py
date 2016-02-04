import argparse
import sys
import os
import thread
import datetime
sys.path.append("Lib/")
import scrublib

from scrubsocket import StartSocket

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",  help="Display verbose messages",
                    action="store_true",  default=False)
parser.add_argument("-d", "--daemon",  help="Start application and exit",
                    action="store_true", default=False)
parser.add_argument("-o", "--output",  help="Location to put output",
                    type=str, default="Cache\\")
parser.add_argument("-f", "--filename",  help="Output filename {ts} for timestamp",
                    type=str, default="output_{ts}")
parser.add_argument("-b", "--blacklist",  help="Blacklist filename",
                    type=str, default="blacklist")
args = parser.parse_args()
if not os.path.exists("config.py"):
    print "Error! Config file not present, please create config.py and start the application again\n"
    sys.exit(0)
import config

outputpath = scrublib.loader(args.output, args.filename, args.blacklist, args.verbose)

try:
    for configitem in config.configuration:
        if args.verbose:
            print "Starting service %s on port %s\n" % (configitem, config.configuration[configitem]["port"])
        thread.start_new_thread( StartSocket, ("192.168.0.11", config.configuration[configitem]["port"], config.configuration[configitem]["banner"], config.configuration[configitem]["calls"], config.configuration[configitem]["errors"], args.verbose) )
        
    while 1:
       pass
except (KeyboardInterrupt, SystemExit):
        print "Stopping threads"
