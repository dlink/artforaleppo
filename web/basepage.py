#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *
from menu import Menu

class BasePage(HtmlPage):
    
    def __init__(self):
        name = 'Art for Aleppo'
        HtmlPage.__init__(self, name, include_form_tag=0)
        
        self.style_sheets = [
            'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/' \
                'bootstrap.min.css',
            'css/main.css']
        
        self.javascript_src.extend(['js/main.js'])

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
        return 'book'
            

    def getFooter(self):
        html = open('footer.html', 'r').read()
        return html
