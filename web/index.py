#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *

class Index(HtmlPage):
    
    def getHtmlContent(self):
        return \
            self.getHeader() + \
            self.getBody() + \
            self.getFooter()

    def getHeader(self):
        return p('header')

    def getBody(self):
        return p('body')

    def getFooter(self):
        return p('footer')

if __name__ == '__main__':
    Index().go()
