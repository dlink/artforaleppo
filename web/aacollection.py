from vweb.htmlpage import HtmlPage
from vweb.html import *

from collection import Collection
from index import Index
from menu import Menu

class AaCollection(Collection):
    '''Art for Aleppo subclass of Collection'''

    def __init__(self):
        Collection.__init__(self)
        
        # change css/ and js/ to vpics/css and vpics/js
        for i, s in enumerate(self.style_sheets):
            self.style_sheets[i] \
                = self.style_sheets[i].replace('css/', 'vpics/css/')
        for i, j in enumerate(self.javascript_src):
            self.javascript_src[i] \
                = self.javascript_src[i].replace('js/', 'vpics/js/')
            
        self.style_sheets.append('https://maxcdn.bootstrapcdn.com/bootstrap'
                                 '/3.3.6/css/bootstrap.min.css')
        self.style_sheets.append('css/index.css')
        self.javascript_src.append('js/index.js')

    def getHtmlContent(self):
        return div(
            self.header() +\
            self.messageLine() +\
            self.navAndDisplayArea(),
            class_='container body')
    def header(self):
        return Menu().getHeader(type=2)

