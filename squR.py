#!/usr/bin/python

import SocketServer, sim
from os import getuid
from subprocess import check_output
from socket import error as socerr
from sys import exit

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        if self.data:
            sim.simulate(self.data)
            
        print self.data

#HOST = check_output("ifconfig wlan0 | grep \"inet addr\" | awk '{print $2}' | awk -F: '{print $2}'",shell=True)
HOST= '0.0.0.0'
PORT=9999

if __name__ == "__main__":
    if not getuid():
        
        #HOST, PORT = sim.defns.IP_ADDRESS, sim.defns.PORT
        # Create the server, binding to localhost on port 9999
        #try:
        if(HOST==""):
            print "Seems your wi-fi is off. Try again after connecting to a wifi"
            exit(1)
        SocketServer.TCPServer.allow_reuse_address = True
        server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
        try:
            print "\nsquRemote is running.\n"
            print "IP address:   {}".format(HOST)
            print "PORT:         {}".format(PORT)
            print "\nCtrl+c to exit."
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            print "\nGoodbye."
    
        except socerr:
            print "Sorry, something's wrong."

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        
    else:
        #tkMessageBox.showerror("Permissions Needed","Not enough permissions, are you root?")
        #sys.exit(1)
        print "Not enough permissions. Are you root?"

