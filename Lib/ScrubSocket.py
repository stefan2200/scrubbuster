import SocketServer
import sys
class ScrubHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        serverbanner = self.server.serverbanner
        detectionerrors = self.server.detectionerrors
        sendcalls = self.server.sendcalls
        debug = self.server.debug
        self.request.sendall("%s" % serverbanner)
        
        if debug:
            print "Service {} reported: Connection from {}:".format(serverbanner, self.client_address[0])
        while 1:
            try:
                self.data = self.request.recv(1024).strip()
                
                if not self.data:
                    break
                
                for error in detectionerrors:
                    if str(error) in self.data:
                        print "%s attepmpted to send exploit command to service" % self.client_address[0]
                        #handle exploit
                        self.close()
                    
                for call in sendcalls:
                    if call in self.data:
                        self.request.sendall(sendcalls[call] + "\n")
                print self.data
            except:
                if debug:
                    print ("Service %s reported Connection closed from %s" % (serverbanner, self.client_address[0]))
                break
class ScrubServer(SocketServer.TCPServer):
    def __init__(self, host, banner, calls, errors, debug):
        self.serverbanner = banner
        self.debug = debug
        self.sendcalls = calls
        self.detectionerrors = errors
        try:
            SocketServer.TCPServer.__init__(self, host, ScrubHandler)
        except:
            print "Socket> Error cannot listen on port %d (In use?)" % host[1]
            sys.exit(0)
        return None
    
def StartSocket(host, port, banner, calls, errors, debug):
    if debug:
        print "Socket> Starting service on port %d" % port
    server = ScrubServer((host, port), banner, calls, errors, debug)
    server.allow_reuse_address=True
    server.server_activate()
    server.serve_forever()
   
        
