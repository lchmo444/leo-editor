#@+leo-ver=4-thin
#@+node:ville.20090518182905.5419:@thin nav_qt.py
#@<< docstring >>
#@+node:ville.20090518182905.5420:<< docstring >>
'''This docstring should be a clear, concise description of
what the plugin does and how to use it.
'''
#@-node:ville.20090518182905.5420:<< docstring >>
#@nl

__version__ = '0.0'
#@<< version history >>
#@+node:ville.20090518182905.5421:<< version history >>
#@@killcolor
#@+at
# 
# Put notes about each version here.
#@-at
#@nonl
#@-node:ville.20090518182905.5421:<< version history >>
#@nl

#@<< imports >>
#@+node:ville.20090518182905.5422:<< imports >>
import leo.core.leoGlobals as g
import leo.core.leoPlugins as leoPlugins
from PyQt4 import QtGui

# Whatever other imports your plugins uses.
#@nonl
#@-node:ville.20090518182905.5422:<< imports >>
#@nl

#@+others
#@+node:ville.20090518182905.5423:init
def init ():


    ok = g.app.gui.guiName() == "qt"

    if ok:
        if 0: # Use this if you want to create the commander class before the frame is fully created.
            leoPlugins.registerHandler('before-create-leo-frame',onCreate)
        else: # Use this if you want to create the commander class after the frame is fully created.
            leoPlugins.registerHandler('after-create-leo-frame',onCreate)
        g.plugin_signon(__name__)

    return ok
#@-node:ville.20090518182905.5423:init
#@+node:ville.20090518182905.5424:onCreate
def onCreate (tag, keys):

    c = keys.get('c')
    if not c: return

    thePluginController = pluginController(c)
#@-node:ville.20090518182905.5424:onCreate
#@+node:ville.20090518182905.5425:class pluginController
class pluginController:

    #@    @+others
    #@+node:ville.20090518182905.5426:__init__
    def __init__ (self,c):

        self.c = c
        self.makeButtons()
        # Warning: hook handlers must use keywords.get('c'), NOT self.c.
    #@-node:ville.20090518182905.5426:__init__
    #@+node:ville.20090518182905.5427:makeButtons

    def makeButtons(self):
        ib_w = self.c.frame.iconBar.w
        icon_l = ib_w.style().standardIcon(QtGui.QStyle.SP_ArrowLeft)
        icon_r = ib_w.style().standardIcon(QtGui.QStyle.SP_ArrowRight)
        act_l = QtGui.QAction(icon_l, 'prev', ib_w)           
        act_r = QtGui.QAction(icon_r, 'next', ib_w)           

        self.c.frame.iconBar.add(qaction = act_l, command = self.clickPrev)
        self.c.frame.iconBar.add(qaction = act_r, command = self.clickNext)


    #@-node:ville.20090518182905.5427:makeButtons
    #@+node:ville.20090518182905.7867:clickPrev
    def clickPrev(self):
        c = self.c
        c.selectPosition(c.nodeHistory.goPrev())

    #@-node:ville.20090518182905.7867:clickPrev
    #@+node:ville.20090518182905.7868:clickNext
    def clickNext(self):
        c = self.c
        c.selectPosition(c.nodeHistory.goNext())
    #@-node:ville.20090518182905.7868:clickNext
    #@-others
#@-node:ville.20090518182905.5425:class pluginController
#@-others
#@nonl
#@-node:ville.20090518182905.5419:@thin nav_qt.py
#@-leo
