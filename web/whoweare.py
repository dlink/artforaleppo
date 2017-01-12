#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *
from menu import Menu

from basepage import BasePage

class WhoWeAre(BasePage):
    
    def getBody(self):
        return 'who we are'
            
if __name__ == '__main__':
    WhoWeAre().go()
