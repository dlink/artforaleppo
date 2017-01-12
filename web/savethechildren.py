#!/usr/bin/env python

from basepage import BasePage

class SaveTheChildren(BasePage):

    def getBody(self):
        html =  open('html/savethechildren.html', 'r').read()
        return html
            
if __name__ == '__main__':
    SaveTheChildren().go()
