#!/usr/bin/env python

from basepage import BasePage

class SaveTheChildren(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        self.style_sheets.extend(['css/savethechildren.css'])

    def getBody(self):
        html =  open('html/savethechildren.html', 'r').read()
        return html
            
if __name__ == '__main__':
    SaveTheChildren().go()
