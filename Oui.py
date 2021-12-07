import pygame
import OpenGL.GL as gl
import OpenGL.GLU as glu

if __name__ == '__main__':
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    # Sets the screen color (white)
    gl.glClearColor(1, 1, 1, 1)
    # Clears the buffers and sets DEPTH_TEST to remove hidden surfaces
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glEnable(gl.GL_DEPTH_TEST)

    # Placer ici l'utilisation de gluPerspective.
    glu.gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    gl.glTranslatef(0.0, 2, -5)
    gl.glRotatef(-90, 1, 0, 0)
   
    gl.glBegin(gl.GL_LINES)  # Indique que l'on va commencer un trace en mode lignes (segments)
    
    
    gl.glColor3fv([1, 0, 0])  # Indique la couleur du prochian segment en RGB
    gl.glVertex3fv((0, 0, -2))  # Premier vertice : départ de la ligne
    gl.glVertex3fv((1, 0, -2))  # Deuxième vertice : fin de la ligne
   
    gl.glColor3fv([0, 1, 0])  # Indique la couleur du prochian segment en RGB
    gl.glVertex3fv((0, 0, -2))  # Premier vertice : départ de la ligne
    gl.glVertex3fv((0, 0, 2))  # Deuxième vertice : fin de la ligne
    
    gl.glColor3fv([0, 0, 1])  # Indique la couleur du prochian segment en RGB
    gl.glVertex3fv((0, 0, -2))  # Premier vertice : départ de la ligne
    gl.glVertex3fv((-1, 0, -2))  # Deuxième vertice : fin de la ligne
    
    gl.glEnd()  # Find du tracé
    pygame.display.flip()  # Met à jour l'affichage de la fenêtre graphique
   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

