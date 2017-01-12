#!/usr/bin/env python

from basepage import BasePage

class CallToArtists(BasePage):

    def getBody(self):
        html =  open('html/calltoartists.html', 'r').read()
        return html
            
if __name__ == '__main__':
    CallToArtists().go()
