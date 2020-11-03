from panda3d.core import *
loadPrcFileData('', 'win-size 640 640') 
loadPrcFileData('', 'window-title chessboard Demo')
loadPrcFileData('', 'sync-video True')
loadPrcFileData('', 'show-frame-rate-meter false')
loadPrcFileData('', 'texture-minfilter linear-mipmap-linear')

# Генератор
from Map import *
genMap()

from direct.showbase.ShowBase import ShowBase


import sys




from direct.gui.OnscreenImage import OnscreenImage 
#from numpy import *


from player import *            
class ButtonBar(ShowBase):
    
    def __init__(self):


        ShowBase.__init__(self)
        # Отрисовка

        showMap()

        self.disableMouse()

        # Настройка камеры
        self.pl = player()
        self.camera.setPos(3.5,3.5,20)
        self.camera.setHpr(0,-90,0)

        #self.f = Figure()
        if self.set == 1:

        	self.accept('mouse3',self.pl.addFigure)
        self.accept('enter',self.loop)
    def loop(self):
    	
        self.accept('mouse1',self.pl.movement)
        self.pl.set = 0




core = ButtonBar()
core.run()
