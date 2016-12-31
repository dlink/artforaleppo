#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *

class Index(HtmlPage):
    
    def __init__(self):
        name = 'Art for Aleppo'
        HtmlPage.__init__(self, name, include_form_tag=0)
        
        self.style_sheets = [
            'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/' \
                'bootstrap.min.css',
            'css/index.css']
        
        self.javascript_src.extend(['js/index.js'])

    def getHtmlContent(self):
        o = \
            self.getHeader() + \
            self.getBody() + \
            self.getFooter()
        return div(o, class_='container body')

    def getHeader(self):
        o = nav(
            ul(li('Art for Aleppo'         , onClick='showPage(1)') + \
               li('Save the Children Syria', onClick='showPage(2)') + \
               li('Open Call to Artists'   , onClick='showPage(3)') + \
               li('Artwork Gallery'        , onClick='showPage(4)') + \
               li('Make a Donation'        , onClick='showPage(5)')))
        return div(o, class_='header')

    def getBody(self):
        return open('body.html', 'r').read()

    def getFooter(self):
        o = ''
        return div(o, class_='footer')

if __name__ == '__main__':
    Index().go()
