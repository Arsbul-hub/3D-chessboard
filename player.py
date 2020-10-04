from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
import sys
from direct.gui.OnscreenImage import OnscreenImage 
class player():
	def __init__(self):
		self.picker = CollisionTraverser()
		self.picker.showCollisions(render)
		self.pq = CollisionHandlerQueue() 

		self.pickerNode = CollisionNode('mouseRay')
		self.pickerNP = camera.attachNewNode(self.pickerNode)

		#self.pickerNode.setFromCollideMask(BitMask32.bit(1))


		self.pickerRay = CollisionRay()
		self.pickerNode.addSolid(self.pickerRay)
		self.picker.addCollider(self.pickerNP,self.pq)

		#self.f = Figure()
		self.Return = ''
		self.step = 1
		self.list = []
		self.list1 = []
		
		self.player = 0
	def addFigure(self):
		if base.mouseWatcherNode.hasMouse():
			#x1,y1 = self.getSize()
			# get the mouse position
			mpos = base.mouseWatcherNode.getMouse()
			mw =  base.mouseWatcherNode.getMouse()
        

			# get the window manager's idea of the mouse position
			x, y = mw.getX(), mw.getY()
			# set the position of the ray based on the mouse position
			self.pickerRay.setFromLens(base.camNode,mpos.getX(),mpos.getY())
			#self.pickerNP.setHpr(mx,my,0)
			self.picker.traverse(render)
			print(self.pq.getNumEntries())
			if self.pq.getNumEntries() > 0 :
					self.pq.sortEntries()
					pickedObj = self.pq.getEntry(0).getIntoNodePath()
                	#if pickedObj.getZ() != 1:

					xp,yp,zp = self.pq.getEntry(0).getIntoNodePath().getPos()
					x,y,z =self.pq.getEntry(0).getSurfaceNormal(render)
					#xp,yp,zp =  pickedObj.getPos()
					print(pickedObj.getName())
					if pickedObj.getName()=='black' and pickedObj.getName()!='blackF' and yp > 4 and len(self.list) < 12:
							cs = CollisionBox(0.5, 0.5, 0.5, 0.5)
							pcn1 = render.attachNewNode(CollisionNode('blackF'))
							pcn1.node().addSolid(cs)

							pcn1.show()
							g=loader.loadModel('models/box')
							g.setName('blackF')
							g.setScale(1,1,1)

							tex = loader.loadTexture("black1.png")
							pcn1.setTexture(tex, 1) 
							g.copyTo(pcn1)
							pcn1.setPos(int(xp),int(yp),int(1))
							self.list.append(pcn1)
							#self.camera.lookAt(g)
							#self.camera.setPos(xp,yp,20)
					elif pickedObj.getName() == 'black' and pickedObj.getName() != 'whiteF' and yp < 3 and len(self.list1) < 12:
							cs = CollisionBox(0.5, 0.5, 0.5, 0.5)
							pcn1 = render.attachNewNode(CollisionNode('whiteF'))
							pcn1.node().addSolid(cs)
							
							pcn1.show()
							g=loader.loadModel('models/box')
							g.setName('whiteF')
							g.setScale(1,1,1)
							

							print(g)
							tex = loader.loadTexture("wh.png")
							pcn1.setTexture(tex, 1) 
							g.copyTo(pcn1)
							pcn1.setPos(int(xp),int(yp),int(1))
							self.list1.append(pcn1)   
	def movement(self):
		if base.mouseWatcherNode.hasMouse():
			#x1,y1 = self.getSize()
			# get the mouse position
			mpos = base.mouseWatcherNode.getMouse()
			#mw =  base.mouseWatcherNode.getMouse()
        

			# get the window manager's idea of the mouse position
			#x, y = mw.getX(), mw.getY()
			# set the position of the ray based on the mouse position
			self.pickerRay.setFromLens(base.camNode,mpos.getX(),mpos.getY())
			#self.pickerNP.setHpr(mx,my,0)
			self.picker.traverse(render)
			#print(self.pq.getNumEntries())
			if self.pq.getNumEntries() > 0:
					self.pq.sortEntries()
					pickedObj = self.pq.getEntry(0).getIntoNodePath()
					print(pickedObj.getPos())
			    

					if self.step == 1 and pickedObj.getZ() != 0:
						pickedObj = self.pq.getEntry(0).getIntoNodePath()
						#print(pickedObj.getPos())
						if str(pickedObj):
                            
                            #self.pq.sortEntries()
							pickedObj = self.pq.getEntry(0).getIntoNodePath()
							self.x,self.y,self.z = pickedObj.getPos()
							#xp,yp,zp = self.pq.getEntry(0).getIntoNodePath().getParent().getPos()
							#x,y,z =self.pq.getEntry(0).getSurfaceNormal(render)
							self.Np = pickedObj
                            #pickedObj.remove()
                           
							self.figure = pickedObj.getName()
						self.step = 2
					elif self.pq.getNumEntries() > 0 and self.step == 2:
                        #self.pq.sortEntries()
						x,y,z = self.pq.getEntry(0).getIntoNodePath().getPos()
                        #print(self.pq.getEntry(0).getIntoNodePath().getName() != 'whiteF' and self.pq.getEntry(0).getIntoNodePath().getName() != 'blackF' )
						if self.pq.getEntry(0).getIntoNodePath().getName() != 'whiteF' and self.pq.getEntry(0).getIntoNodePath().getName() != 'blackF' and self.pq.getEntry(0).getIntoNodePath().getName() != 'white':
							print('gfd')
							if y > self.y and y < self.y+2 and self.figure == 'whiteF' and self.player == 0:
                            #print('hjkl')
								self.Np.setPos(int(x),int(y),1)
								self.player = 1
							elif y < self.y and y > self.y-2 and self.figure == 'blackF' and self.player == 1:
                            #print('hjkl')
								self.Np.setPos(int(x),int(y),1)
								self.player = 0
						self.step = 1
						if self.pq.getEntry(0).getIntoNodePath().getName() == 'whiteF' or self.pq.getEntry(0).getIntoNodePath().getName() == 'blackF':

							if y < self.y+2 and self.figure == 'whiteF' and self.player == 0:
								
									#print(self.list[i].getPos() , (int(x+(x-self.Np.getX())),int(y+1),1))
									#if self.list[i].getPos() != (int(x+(x-self.Np.getX())),int(y+1),1):
									for i in range(len(self.list)):
											
											if self.list[i].getPos() == (int(x+(x-self.Np.getX())*2),int(y+1*2),1):
												print(self.list[i].getPos() == (int(x+(x-self.Np.getX())*2),int(y+1*2),1),self.list[i].getPos() , (int(x+(x-self.Np.getX())*2),int(y+1*2),1))
												self.Return = True
												break
									if self.Return == True:
											print('You can not go forward to eat not your figures')
											#break
									else:
											self.Np.setPos(int(x+(x-self.Np.getX())),int(y+1),1)
											self.pq.getEntry(0).getIntoNodePath().remove()
											self.list.pop(i)
											self.player = 0
											#break
									self.Return = ''

									self.step = 1
							elif y > self.y-2 and self.figure == 'blackF' and self.player == 1:
                            #print('hjkl')
								for i in range(len(self.list1)):
									#if self.list1[i].getPos() != (int(x+(x-self.Np.getX())),int(y-1),1):
										self.Np.setPos(int(x+(x-self.Np.getX())),int(y-1),1)
										self.pq.getEntry(0).getIntoNodePath().remove()
										self.list.pop(i)
										self.player =  0 
										break
								self.step = 1

