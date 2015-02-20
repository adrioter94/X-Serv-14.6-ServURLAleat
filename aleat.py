#!/usr/bin/python

import webapp
import random

class Server(webapp.webApp):

    def process(self, parsedRequest):
        x = random.randrange(10000)
        url = "http://localhost:7777/" + str(x)
        Request = ("<html><body><h1>Hola!</h1>" +
                    "</p>" +
                    "<a href=" + url + ">Dame otra</a>"
                    "</body></html>"
                    "\r\n")
        return ("200 OK", Request)
        
if __name__ == "__main__":
    serv = Server("localhost", 7777)
