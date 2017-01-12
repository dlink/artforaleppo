#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *
from menu import Menu

from basepage import BasePage

class Book(BasePage):
    
    def getBody(self):
        return 'book'
            
if __name__ == '__main__':
    Book().go()
