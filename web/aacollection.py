#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *

from collection import Collection
from index import Index
from menu import Menu

from aanav import AaNav

NUM_COLS = 3
THUMBNAILS = '200px'

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
        self.style_sheets.append('css/main.css')
        self.javascript_src.append('js/index.js')

        self.nav = AaNav()
        
    def getHtmlContent(self):
        return div(
            self.header() +\
            self.messageLine() +\
            self.navAndDisplayArea(),
            class_='container body')
    
    def header(self):
        return Menu().getHeader(self)

    def pic_div(self, i):
        '''
        <center>
           <div class="pic">
              <a href="/aaoneup.py?id=NAME" class="captionLink">
                 <img src="URL" class="picImage">
                 <div class="picCaption">
                    <i>NAME </i>
                    <small>CAPTION</small>
                 <div>
              </a>
           <div>
        </center>
        '''
        pic_url = "/%s/%s/%s/%s" % (self.env.media_url,
                                    self.page.name,
                                    THUMBNAILS,
                                    self.page.pics[i].filename)
        pic_img = img(src=pic_url, class_='picImage')
        caption = self.picCaption(i)


        #href = "/%s/aaoneup.py?id=%s" % (self.env.base_url,
        #                              self.page.pics[i].name)
        if self.env.base_url:
            base = '/%s' % self.env.base_url
        else:
            base = ''
        href = "%s/aaoneup.py?id=%s" % (base,
                                      self.page.pics[i].name)
        return center(div(a(pic_img + caption, href=href, class_='captionLink'), class_='pic'))

if __name__ == '__main__':
    AaCollection().go()
