#!/usr/bin/env python

from basepage import BasePage

class CallToArtists(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        self.style_sheets.extend(['css/calltoartists.css'])

    def getBody(self):
        html =  open('html/calltoartists.html', 'r').read()
        return html
            
if __name__ == '__main__':
    CallToArtists().go()
