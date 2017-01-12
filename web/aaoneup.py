#!/usr/bin/env python

from vweb.html import *

from oneup import Oneup
from pages import Page

from menu import Menu

from aanav import AaNav

class aaOneup(Oneup):
    '''Art for Aleppo subclass of Collection'''

    def __init__(self):
        Oneup.__init__(self)
        
        # change css/ and js/ to vpics/css and vpics/js
        for i, s in enumerate(self.style_sheets):
            self.style_sheets[i] \
                = self.style_sheets[i].replace('css/', 'vpics/css/')
        for i, j in enumerate(self.javascript_src):
            self.javascript_src[i] \
                = self.javascript_src[i].replace('js/', 'vpics/js/')
            
        self.style_sheets.append('https://maxcdn.bootstrapcdn.com/bootstrap'
                                 '/3.3.6/css/bootstrap.min.css')
        self.style_sheets.append('css/main.css')
        self.javascript_src.append('js/index.js')

        self.nav = AaNav()

    def getHtmlContent(self):
        return div(
            self.header() +\
            self.navAndDisplayArea(),
            class_='container body')
    
    def header(self):
        return Menu().getHeader(type=2)

    
    def picNav(self):
        page = Page(self.pic.page_name)

        prev_pic_name = None
        next_pic_name = None
        old_pic_name = None
        found = 0

        # loop thru first page of pics, find prev and next pic_names
        for pic in page.pics:
            pic_name = pic.name
            if found:
                next_pic_name = pic_name
                break
            if pic_name == self.pic.name:
                if old_pic_name:
                    prev_pic_name = old_pic_name
                found = 1
            old_pic_name = pic_name

        #prev
        if prev_pic_name:
            prev = a('prev', href='aaoneup.py?id=%s' % prev_pic_name)
        else:
            prev = font('prev', color='lightgrey')

        # next
        if next_pic_name:
            next = a('next', href='aaoneup.py?id=%s' % next_pic_name)
        else:
            next = font('next', color='lightgrey')
        return div('%s | %s' % (prev, next), class_='picNav')

if __name__ == '__main__':
    aaOneup().go()
