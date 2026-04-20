import numpy as np
import pygame
from specifications import DENSITE_AIR

class Vehicule:
    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, roues, moteur, chassis, Specs, image_path):

        # TODO : ajouter les attributs
        self.__nom = nom
        self.__position = np.array(position_dep, dtype=float)
        self.__roues = roues 
        self.__moteur = moteur 
        self.__chassis = chassis
        self.__Specs = Specs 
        self.__vitesse = np.array([0.0, 0.0])
        
        self.__poids_total = self.__chassis.get_poids() + self.__moteur.get_poids() + sum(roue.get_poids() for roue in roues)

        # TODO : ajouter un attribut pour l'image du véhicule
        self.image = pygame.transform.scale(pygame.image.load(image_path),(self.__Specs.image_width, self.__Specs.image_height)) 
        
   

    
    def affichage_vehicule(self, screen):
        # TODO : compléter la méthode 
        x, y = self.__position
        ima = self.image.get_rect()
        ima.topright = (x,y)
        screen.blit(self.image, ima)

        
    
    def calculer_poids_total(self):
       poids_tot = self.__chassis.get_poids() + self.__moteur.get_poids() + sum(roue.get_poids() for roue in roues)
       return poids_tot
        
       

    def calculer_traction(self):
        # TODO : compléter la méthode 
        trac = self.__poids_total * self.__moteur.get_acceleration()
        return trac 


    def calculer_friction(self):
        # TODO : compléter la méthode 
        friction = self.__roues.coefficient_friction * self.__vitesse
        return friction
        

    def calculer_trainee(self):
        trainee = (1/2 * self.__chassis.coefficient_trainee * self.__chassis.aire_frontale * DENSITE_AIR * self.__vitesse**2)
        return trainee 
        
        

    def accelerer(self, dt):
        # TODO : compléter la méthode 
        frottement_total = sum(roue.get_coefficient_friction() for roue in self.__roues)
        acceleration = (self.__poids_total * self.__moteur.get_acceleration() - (1/2 * self.__chassis.get_coefficient_trainee() * frottement_total * DENSITE_AIR * self.__vitesse**2)  - sum(roue.get_coefficient_friction() for roue in self.__roues) * self.__vitesse) / self.__poids_total
       
        self.__vitesse += self.__moteur.get_acceleration() * dt    
        self.__position[0] += self.__vitesse[0] * dt
        
        

    def celebrer(self):
        # TODO : compléter la méthode 
        return f"{self.__nom} remporte la course !"
        
    def get_position(self):
        return self.__position