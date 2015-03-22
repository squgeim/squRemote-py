#!/usr/bin/python

import SocketServer, sim
from os import getuid
from socket import error as socerr

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
        #print self.data
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    if not getuid():
        HOST, PORT = sim.defns.IP_ADDRESS, sim.defns.PORT
        # Create the server, binding to localhost on port 9999
        #try:
        server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
        try:
            print "squRemote is running,"
            print "IP address: ",HOST,
            print "PORT: ",PORT
            print "Ctrl+c to exit."
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            print "\nGoodbye."
    
        #except socerr:
         #   print "Sorry, something's wrong."

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        
    else:
        print "Not enough permissions. Are you root?"

