#!/usr/bin/env python

from basepage import BasePage

class Index(BasePage):

    def getBody(self):
        html =  open('html/index.html', 'r').read()
        return html
            
if __name__ == '__main__':
    Index().go()
