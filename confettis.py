import random
import pygame

class Confetti: 

    def __init__(self, largeur_ecran):
        self.x = random.randint(0, largeur_ecran)
        self.y = random.randint(0, 30)
        self.taille = random.randint(4, 10)
        self.vitesse = random.randint(3, 5)
        self.couleur = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0),(128, 0, 128)])

    def tomber(self):
        self.y += self.vitesse

    def afficher(self, screen):
        pygame.draw.rect(screen, self.couleur, (self.x, self.y, self.taille, self.taille))

  

    