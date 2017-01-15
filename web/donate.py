#!/usr/bin/env python

from basepage import BasePage

class Donate(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        self.style_sheets.extend(['css/donate.css'])

    def getBody(self):
        html =  open('html/donate.html', 'r').read()
        return html
            
if __name__ == '__main__':
    Donate().go()
