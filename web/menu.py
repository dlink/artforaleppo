from vweb.html import *

class Menu(object):

    def getHeader(self):
        menu = [['Art for <strong>Aleppo</strong>', '/'],
                ['Save the <strong>Children</strong>', '/savethechildren.py'],
                ['Open Call to <strong>Artists</strong>','/calltoartists.py'],
                ['Artwork <strong>Gallery</strong>', '/vpics.py'],
                ['Make a <strong>Donation</strong>', 'donate.py']]

        menu_str = ''
        for m, href in menu:
            menu_str += li(span('<a href="%s">%s</a>' % (href, m),
                                class_='menuItem'))

        # hamberger icon
        menu_str += li('&#9776;',
                       class_='icon',
                       href="javascript:void(0);",
                       onclick='menuHamberger()')
        
        o = nav(ul(menu_str, class_='topnav', id='topnav'))
        return div(o, class_='header')

