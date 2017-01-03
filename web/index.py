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
        menu = ['Art for <strong>Aleppo</strong>',
                      'Save the <strong>Children</strong>',
                      'Open Call to <strong>Artists</strong>',
                      'Artwork <strong>Gallery</strong>',
                      'Make a <strong>Donation</strong>']
        menu_str = ''
        for i, s in enumerate(menu):
            if i != 0:
                menu_str += li('|')
            menu_str += li(s, onClick='showPage(%s)' % (i+1))

        o = nav(ul(menu_str))
        return div(o, class_='header')

    def getBody(self):
        return open('body.html', 'r').read()

    def getFooter(self):
        o = ''
        return div(o, class_='footer')

if __name__ == '__main__':
    Index().go()
