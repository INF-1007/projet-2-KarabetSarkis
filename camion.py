from vehicule import Vehicule
from roue import Roue
from moteur import Moteur
from chassis import Chassis
from specifications import CamionSpecs

class Camion(Vehicule): 
    
    def __init__(self, nom, position_dep, image_path):
        
        
        self.specs = CamionSpecs()
        
        self.roues = [
            Roue(self.specs.roue_nom, self.specs.roue_poids, self.specs.roue_friction, self.specs.roue_support),
            Roue(self.specs.roue_nom, self.specs.roue_poids, self.specs.roue_friction, self.specs.roue_support),
            Roue(self.specs.roue_nom, self.specs.roue_poids, self.specs.roue_friction, self.specs.roue_support),
            Roue(self.specs.roue_nom, self.specs.roue_poids, self.specs.roue_friction, self.specs.roue_support),
            Roue(self.specs.roue_nom, self.specs.roue_poids, self.specs.roue_friction, self.specs.roue_support),
            Roue(self.specs.roue_nom, self.specs.roue_poids, self.specs.roue_friction, self.specs.roue_support)
        ]
        
        
        self.moteur = Moteur(self.specs.moteur_nom, self.specs.moteur_poids, self.specs.moteur_acceleration) 
        
        self.chassis = Chassis(self.specs.chassis_nom, self.specs.chassis_poids, self.specs.chassis_aire, self.specs.chassis_trainee)
        
        super().__init__(nom, position_dep, self.roues, self.moteur, self.chassis, self.specs, image_path)
   