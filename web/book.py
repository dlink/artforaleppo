#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *
from menu import Menu

from basepage import BasePage

class Book(BasePage):
    
    def getBody(self):
        return open('html/book.html', 'r').read()
    
    def getFooter(self):
        html = BasePage.getFooter(self)
        html = html.replace('id="footerItem1"', 'class="selectedMenuItem"')
        return html
    
if __name__ == '__main__':
    Book().go()
