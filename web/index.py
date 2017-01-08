#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *
from menu import Menu

class Index(HtmlPage):
    
    def __init__(self):
        name = 'Art for Aleppo'
        HtmlPage.__init__(self, name, include_form_tag=0)
        
        self.style_sheets = [
            'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/' \
                'bootstrap.min.css',
            'css/index.css']
        
        self.javascript_src.extend(['js/index.js'])

        self.page = '1'
        
    def process(self):
        HtmlPage.process(self)
        if 'p' in self.form:
            self.page = self.form['p'].value
        
    def getHtmlContent(self):
        o = \
            Menu().getHeader() + \
            self.getBody() + \
            self.getFooter()
        return div(o, class_='container body')

    def getBody(self):
        html =  open('body.html', 'r').read()
        # set all but this page to display: none
        for i in range(1, 6):
            if str(i) != self.page:
                html = html.replace('id="page%s"' % i,
                                    'id="page%s" style="display: none;"' % i)
        return html
            

    def getFooter(self):
        o = ''
        return div(o, class_='footer')

if __name__ == '__main__':
    Index().go()
