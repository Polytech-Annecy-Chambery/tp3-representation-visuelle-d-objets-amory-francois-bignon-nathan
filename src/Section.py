# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :
        # Parameters
        # position: position of the wall
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False

        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]

    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self

    # Defines the vertices and faces
    def generate(self):
        self.vertices = [
                [0, 0, 0],
                [0, 0, self.parameters['height']],
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                [self.parameters['width'], self.parameters['thickness'], 0],
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
                [0, self.parameters['thickness'], self.parameters['height']],
                [0, self.parameters['thickness'], 0]
                ]
        self.faces = [
                [0,3,2,1],
                [1,2,5,6],
                [6,5,4,7],
                [7,4,3,0],
                [0,7,6,1],
                [2,3,4,5]
                ]

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        if x.parameters['width'] + x.parameters['position'][0] <= self.parameters['position'][0]+self.parameters['width']:
            if x.parameters['height'] + x.parameters['position'][2] <= self.parameters['position'][2] + self.parameters['height']:
                return True
        return False

    # Creates the new sections for the object x
    def createNewSections(self, x):
        if self.canCreateOpening(x) :
          sections = []
          if x.parameters['position'][0] - self.parameters['position'][0] > 0:
              s1 = Section({'position': self.parameters['position'], \
                            'width': x.parameters['position'][0] - self.parameters['position'][0], \
                            'height': self.parameters['height'], \
                            'thickness': self.parameters['thickness'],\
                            'color' :self.parameters['color']})
          sections.append(s1)


          if self.parameters['position'][2] + self.parameters['height'] - x.parameters['position'][2] - x.parameters['height'] > 0:
              s2 = Section({'position': [x.parameters['position'][0],self.parameters['position'][1], x.parameters['position'][2]], \
                            'width': x.parameters['width'], \
                            'height': self.parameters['height'] - x.parameters['height'] - x.parameters['position'][2], \
                            'thickness': self.parameters['thickness'], \
                            'color' :[0, 1, 0]})
              sections.append(s2)


          if x.parameters['position'][2] - self.parameters['position'][2] > 0:
              s3 = Section({'position': [x.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2]], \
                            'width': x.parameters['width'], \
                            'height': x.parameters['position'][2] - self.parameters['position'][2],\
                            'thickness': self.parameters['thickness'], \
                            'color' :[0, 0, 1]})
              sections.append(s3)


          if self.parameters['position'][0] + self.parameters['width'] - x.parameters['position'][0] - x.parameters['width'] > 0:
              s4 = Section({'position': [x.parameters['position'][0] + x.parameters['width'], self.parameters['position'][1], self.parameters['position'][2]], \
                            'width': self.parameters['width'] - s1.parameters['width'] - x.parameters['width'], \
                            'height': self.parameters['height'] - x.parameters['height'] - x.parameters['position'][2],\
                            'thickness': self.parameters['thickness'], \
                            'color':[self.parameters['color']]})
              sections.append(s4)

          return sections


    # Draws the edges
    def drawEdges(self):
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][1], self.parameters['position'][0], self.parameters['position'][2])

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE) # on trace les lignes : GL_LINE

        for faces in self.faces:
            gl.glBegin(gl.GL_QUADS) # Tracé d='un quadrilatère
            gl.glColor3fv([0.1, 0.1, 0.1]) # Couleur gris moyen
            for vertice in faces:
                gl.glVertex3fv(self.vertices[vertice])
            gl.glEnd()
        gl.glPopMatrix()

    # Draws the faces
    def draw(self):
        gl.glPushMatrix()
        self.drawEdges()
        gl.glTranslatef(self.parameters['position'][1], self.parameters['position'][0], self.parameters['position'][2])

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL

        for faces in self.faces:
            gl.glBegin(gl.GL_QUADS) # Tracé d'un quadrilatère
            gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
            for vertice in faces:
                gl.glVertex3fv(self.vertices[vertice])
            gl.glEnd()
        gl.glPopMatrix()
