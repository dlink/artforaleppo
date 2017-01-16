#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *
from menu import Menu

from basepage import BasePage

class WhoWeAre(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        self.style_sheets.extend(['css/whoweare.css'])
        
    def getBody(self):
        return open('html/whoweare.html', 'r').read()

    def getFooter(self):
        html = BasePage.getFooter(self)
        html = html.replace('id="whoWeAreLink"', 'class="selectedMenuItem"')
        return html
            
if __name__ == '__main__':
    WhoWeAre().go()
