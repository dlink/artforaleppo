#!/usr/bin/env python

from basepage import BasePage

class Donate(BasePage):

    def getBody(self):
        html =  open('html/donate.html', 'r').read()
        return html
            
if __name__ == '__main__':
    Donate().go()
