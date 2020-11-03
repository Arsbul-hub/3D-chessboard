from direct.gui.OnscreenImage import OnscreenImage 
from panda3d.core import *

import array
l = []
def genMap():
	

	for i in range(8):
	            mas = []
	            for j  in range(8):
	                    if (i+j)%2 == 0:
	                        num = {'type': 'cell', 'pos':((0.25*i)-0.875, 0, (0.25*j)-0.875), 'scale': (0.125, 0,0.125), 'path': 'figures/black.png','color':'black'}
	                    else:
	                        num = {'type': 'cell', 'pos':((0.25*i)-0.875, 0, (0.25*j)-0.875), 'scale': (0.125, 0,0.125), 'path': 'figures/white.png','color':'white'}
	                    mas.append(num)
	                    
	            l.append(mas)
def getMap():
	return l
def showMap():
        for j in range(8):
            for i  in range(8):

                if l[j][i].get('color') == 'black':
                    cs = CollisionBox(0.5, 0.5, 0.5, 0.5)
                    pcn1 = render.attachNewNode(CollisionNode('black'))
                    pcn1.node().addSolid(cs)
                    pcn1.setPos(j,i,0)
                    pcn1.show()
                    g=loader.loadModel('models/box')
                    g.setName('black')
                    g.setScale(1,1,1)
                    #print(g)
                    #tex = loader.loadTexture(l[j][i].get('path'))
                   # g.setTexture(tex)
                    #g.setPos(i,j,0)
                    #g.setCollideMask(BitMask32.bit(1))
                    #g.reparentTo(render)
                    g.copyTo(pcn1)
                    tex = loader.loadTexture(l[j][i].get('path'))
                    pcn1.setTexture(tex, 1) 
                if l[j][i].get('color') == 'white':
                    cs = CollisionBox(0.5, 0.5, 0.5, 0.5)
                    pcn1 = render.attachNewNode(CollisionNode('white'))
                    pcn1.node().addSolid(cs)
                    pcn1.setPos(j,i,0)
                    pcn1.show()
                    g=loader.loadModel('models/box')
                    g.setName('white')
                    #g.setScale(1,1,1)

                    #g.setCollideMask(BitMask32.bit(1))

                    g.copyTo(pcn1)
                    tex = loader.loadTexture(l[j][i].get('path'))
                    pcn1.setTexture(tex, 1) 
