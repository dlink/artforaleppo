from vweb.html import *

class Menu(object):

    def getHeader(self, type=1):
        '''type 1 = normal page, uses js and css to change pages
                2 = from vpics, need to refesh page. use url args
        '''
        menu = ['Art for <strong>Aleppo</strong>',
                'Save the <strong>Children</strong>',
                'Open Call to <strong>Artists</strong>',
                'Artwork <strong>Gallery</strong>',
                'Make a <strong>Donation</strong>']
        menu_str = ''
        for i, s in enumerate(menu):
            # introduce menuItem span to allow inserting '| between elements
            item = span(s, class_='menuItem')
            if type == 1:
                menu_str += li(item, onClick='showPage(%s)' % (i+1))
            else:
                menu_str += li(item,
                               onClick="window.location.href='/?p=%s'" % (i+1))
                
        # hamberger icon
        menu_str += li('&#9776;',
                       class_='icon',
                       href="javascript:void(0);",
                       onclick='menuHamberger()')
        
        o = nav(ul(menu_str, class_='topnav', id='topnav'))
        return div(o, class_='header')

