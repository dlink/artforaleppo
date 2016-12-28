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

    def getHtmlContent(self):
        o = \
            self.getHeader() + \
            self.getBody() + \
            self.getFooter()
        return div(o, class_='container body')

    def getHeader(self):
        o = nav(
            ul(li('Art for Aleppo') + \
               li('Save the Children Syria') + \
               li('Call to Artists') + \
               li('Artwork Gallery') + \
               li('Make a Donation')))
        return div(o, class_='header')

    def getBody(self):
        return img(src='images/artforaleppo.jpg')

    def getFooter(self):
        o = ''
        return div(o, class_='footer')

if __name__ == '__main__':
    Index().go()
