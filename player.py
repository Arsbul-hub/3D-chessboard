from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
import sys
from direct.gui.OnscreenImage import OnscreenImage 
from direct.gui.OnscreenText import OnscreenText   

class player():
	def __init__(self):

		self.picker = CollisionTraverser()
		self.picker.showCollisions(render)
		self.pq = CollisionHandlerQueue() 

		self.pickerNode = CollisionNode('mouseRay')
		self.pickerNP = camera.attachNewNode(self.pickerNode)



		self.pickerRay = CollisionRay()
		self.pickerNode.addSolid(self.pickerRay)
		self.picker.addCollider(self.pickerNP,self.pq)

		self.l = []
		self.step = 1
		self.set= 1
		self.player = 'white'
		self.text =OnscreenText(text = 'player - '+self.player, parent=base.a2dTopLeft, scale=0.06,
                        pos=(0.05,-0.07,0), fg=(1, 1, 1, 1),
                        shadow=(0, 0, 0, 0.5), align=TextNode.ALeft) 

	def addFigure(self):
		if base.mouseWatcherNode.hasMouse() and self.set == 1:

			mpos = base.mouseWatcherNode.getMouse()
			mw =  base.mouseWatcherNode.getMouse()
        
			x, y = mw.getX(), mw.getY()

			self.pickerRay.setFromLens(base.camNode,mpos.getX(),mpos.getY())

			self.picker.traverse(render)

			if self.pq.getNumEntries() > 0 :
					self.pq.sortEntries()
					pickedObj = self.pq.getEntry(0).getIntoNodePath()

					x,y,z = self.pq.getEntry(0).getIntoNodePath().getPos()
					################ Если чёрный ################
					if pickedObj.getName()=='black' and pickedObj.getName()!='blackF' and pickedObj.getName() != 'whiteF' and y > 4:
							
							x,y,z = self.pq.getEntry(0).getIntoNodePath().getPos()
							cs = CollisionBox(0.5, 0.5, 0.5, 0.5)
							pcn1 = render.attachNewNode(CollisionNode('blackF'))
							pcn1.node().addSolid(cs)

							pcn1.show()
							g=loader.loadModel('models/box')
							g.setName('blackF')
							g.setScale(1,1,1)

							tex = loader.loadTexture("figures/blackF.png")
							pcn1.setTexture(tex, 1) 
							g.copyTo(pcn1)
							pcn1.setPos(int(x),int(y),int(1))

					################ Если белый ################
					elif pickedObj.getName() == 'black' and pickedObj.getName() != 'whiteF' and pickedObj.getName() != 'blackF' and y <3:
							x,y,z = self.pq.getEntry(0).getIntoNodePath().getPos()
							cs = CollisionBox(0.5, 0.5, 0.5, 0.5)
							pcn1 = render.attachNewNode(CollisionNode('whiteF'))
							pcn1.node().addSolid(cs)
							
							pcn1.show()
							g=loader.loadModel('models/box')
							g.setName('whiteF')
							g.setScale(1,1,1)

							tex = loader.loadTexture("figures/whiteF.png")
							pcn1.setTexture(tex, 1) 
							g.copyTo(pcn1)
							pcn1.setPos(int(x),int(y),int(1))



	def movement(self):

		if base.mouseWatcherNode.hasMouse():

			mpos = base.mouseWatcherNode.getMouse()

			self.pickerRay.setFromLens(base.camNode,mpos.getX(),mpos.getY())

			self.picker.traverse(render)
			
			if self.pq.getNumEntries() > 0:
					self.pq.sortEntries()
					pickedObj = self.pq.getEntry(0).getIntoNodePath()

					################ 1 клик ################
					if self.step == 1 and pickedObj.getZ() != 0: # если не кусок карты, а фигура
						pickedObj = self.pq.getEntry(0).getIntoNodePath()

						pickedObj = self.pq.getEntry(0).getIntoNodePath()
						self.x,self.y,self.z = pickedObj.getPos()
						self.Np = pickedObj

						self.figure = pickedObj.getName()
						self.step = 2
					################ 2 клик ################
					elif self.step == 2:

                        
						if self.pq.getEntry(0).getIntoNodePath().getZ() != 0:


							x,y,z = self.pq.getEntry(0).getIntoNodePath().getPos()
							if y > self.y and y < self.y+2 and self.figure == 'whiteF' and self.player == 'white': # если кликнули на белую фишку
                            
								self.Np.setPos(int(x),int(y),1)

								self.player = 'black'
								if self.Np.getY() > 6:
									self.Np.setName('kingW')

									tex = loader.loadTexture("figures/white_king.png")
									self.Np.setTexture(tex, 1) 
							elif y < self.y and y > self.y-2 and self.figure == 'blackF' and self.player == 'black':# если кликнули на чёрную фишку
                            	

								self.Np.setPos(int(x),int(y),1)

								self.player = 'white'
								if self.Np.getY() <1:
									self.Np.setName('kingB')

									tex = loader.loadTexture("figures/black_king.png")
									self.Np.setTexture(tex, 1) 
							

							self.step = 1


########################### Eat figures ###########################
						if self.pq.getEntry(0).getIntoNodePath().getName() != 'white' and self.pq.getEntry(0).getIntoNodePath().getName() != 'black':
							x,y,z = self.pq.getEntry(0).getIntoNodePath().getPos()
							if y < self.y + 2 and y > self.y-2 and self.figure != self.pq.getEntry(0).getIntoNodePath().getName(): # если не фигура одного цвета
								if self.figure == 'whiteF' and self.player == 'white' and (self.x,self.y) != (x,y):# если кликнули на белую фишку
													if self.Np.getY() > 6:
														self.Np.setName('kingW')

														tex = loader.loadTexture("figures/white_king.png")
														self.Np.setTexture(tex, 1) 

													g=loader.loadModel('models/box')
							
													g.setScale(1,1,1)
													g.setPos(int(x+(x-self.Np.getX())),int(y+1),1)
													g.setName('GGGGGGGG')

													for i in render.findAllMatches("blackF"):
														self.l.append(i.getPos())

													if str(self.l).find(str(g.getPos())) < 0 and int(g.getY()) != 8 and int(g.getY()) != -1 and  int(g.getX()) != 8 and int(g.getX())!= -1: # если впереди, куда я хожу нет фишки
			
														self.Np.setPos(int(x+(x-self.Np.getX())),int(y+(y-self.Np.getY())),1)
														self.pq.getEntry(0).getIntoNodePath().remove()
						
														g.remove()
														#break
											
													self.l = []
													self.step = 1
						
													
								elif self.figure == 'blackF' and self.player == 'black' and (self.x,self.y) != (x,y):# если кликнули на чёрную фишку
											if self.Np.getY() <1:
												self.Np.setName('kingB')

												tex = loader.loadTexture("figures/black_king.png")
												self.Np.setTexture(tex, 1) 
											g=loader.loadModel('models/box')

											g.setScale(1,1,1)
											g.setPos(int(x+(x-self.Np.getX())),int(y-1),1)
											g.setName('GGGGGGGG')



											for i in render.findAllMatches("whiteF"):
														self.l.append((i.getX(),i.getY()))
													
											if str(self.l).find(str((g.getX(),g.getY()))) < 0 and int(g.getY()) != 8 and int(g.getY()) != -1 and  int(g.getX()) != 8 and int(g.getX())!= -1: # если впереди, куда я хожу нет фишки
												self.Np.setPos(int(x+(x-self.Np.getX())),int(y+(y-self.Np.getY())),1)
												self.pq.getEntry(0).getIntoNodePath().remove()

												g.remove()
												#break
											self.l = []
											self.step = 1




########################### Eat kings ###########################

					self.text.setText('player - '+self.player)
