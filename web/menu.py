import os
import inspect

from vweb.html import *

class Menu(object):

    def getHeader(self, caller):
        caller_name = '/' + os.path.basename(inspect.getfile(caller.__class__))
        if caller_name == '/index.py':
            caller_name = '/'
        elif caller_name in ('/aacollection.py', '/aaoneup.py'):
            caller_name = '/vpics.py'
            
        menu = [['Art for <strong>Aleppo</strong>', '/'],
                ['Save the <strong>Children</strong>', '/savethechildren.py'],
                ['Open Call to <strong>Artists</strong>','/calltoartists.py'],
                ['Artwork <strong>Gallery</strong>', '/vpics.py'],
                ['Make a <strong>Donation</strong>', '/donate.py']]

        menu_str = ''
        for m, href in menu:
            classes = 'menuItem'
            if caller_name == href:
                classes += ' selectedMenuItem'
            menu_str += li(span('<a href="%s">%s</a>' % (href, m),
                                class_=classes))
        # hamberger icon
        menu_str += li('&#9776;',
                       class_='icon',
                       href="javascript:void(0);",
                       onclick='menuHamberger()')
        
        o = nav(ul(menu_str, class_='topnav', id='topnav'))
        return div(o, class_='header')

