import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# --- CONSTANTES ---
STATES = {
    'NORMAL': 0,
    'INFECTE': 1,
    'IMMUNISE': 2,
    'VACCINE': 3
}

class Individu:
    def __init__(self, it_maladie, it_immunise, etat=STATES['NORMAL']):
        self.etat = etat
        self.it_maladie = it_maladie
        self.it_immunise = it_immunise
        self.temps_infection = 0
        self.immunisation_duree = 0

    def infecter(self):
        if self.etat == STATES['NORMAL']:
            self.etat = STATES['INFECTE']
            self.temps_infection = self.it_maladie

    def actualiser(self):
        """Gère le passage du temps pour un individu (maladie ou immunité)"""
        if self.etat == STATES['INFECTE']:
            self.temps_infection -= 1
            if self.temps_infection <= 0:
                self.etat = STATES['IMMUNISE']
                self.immunisation_duree = self.it_immunise
        
        elif self.etat == STATES['IMMUNISE']:
            self.immunisation_duree -= 1
            if self.immunisation_duree <= 0:
                self.etat = STATES['NORMAL']

class EpidemicSimulation:
    def __init__(self, grid_size=50, vaccine_rate=0.01, it_maladie=5, it_immunise=2, threshold=3):
        self.grid_size = grid_size
        self.vaccine_rate = vaccine_rate
        self.threshold = threshold
        self.it_maladie = it_maladie
        self.it_immunise = it_immunise
        
        # Création de la grille d'objets Individu
        self.grid = np.array([[Individu(it_maladie, it_immunise) for _ in range(grid_size)] 
                             for _ in range(grid_size)])

    def seed_infection(self, n_infected):
        """Infecte aléatoirement n individus au départ"""
        coords = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size)]
        indices = np.random.choice(len(coords), n_infected, replace=False)
        for idx in indices:
            self.grid[coords[idx]].infecter()

    def get_neighbor_count(self, r, c, state):
        """Compte les voisins d'un certain état (Voisinage de Moore)"""
        count = 0
        for i in range(max(0, r-1), min(self.grid_size, r+2)):
            for j in range(max(0, c-1), min(self.grid_size, c+2)):
                if (i, j) != (r, c) and self.grid[i, j].etat == state:
                    count += 1
        return count

    def step(self):
        """Exécute une itération complète de la simulation"""
        # On travaille sur une copie pour que les changements soient simultanés
        new_states = np.zeros((self.grid_size, self.grid_size))
        
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                obj = self.grid[r, c]
                
                # Logique de transmission
                if obj.etat == STATES['NORMAL']:
                    if self.get_neighbor_count(r, c, STATES['INFECTE']) >= self.threshold:
                        obj.infecter()
                    elif np.random.rand() < self.vaccine_rate:
                        obj.etat = STATES['VACCINE']
                
                # Logique interne (guérison/immunité)
                obj.actualiser()
                new_states[r, c] = obj.etat
                
        return new_states

# --- CONFIGURATION ET LANCEMENT ---
if __name__ == "__main__":
    sim = EpidemicSimulation(grid_size=50, vaccine_rate=0.01)
    sim.seed_infection(10)

    # Couleurs : Jaune (Normal), Rouge (Infecté), Vert (Immunisé), Blanc (Vacciné)
    cmap = ListedColormap(['yellow', 'red', 'green', 'white'])

    plt.figure(figsize=(8, 8))
    for t in range(100):
        data = sim.step()
        plt.clf()
        plt.imshow(data, cmap=cmap, vmin=0, vmax=3)
        plt.title(f"Simulation Épidémique - Jour {t}")
        
        # Légende
        labels = { 'Normal': 'yellow', 'Infecté': 'red', 'Guéri': 'green', 'Vacciné': 'white' }
        patches = [plt.plot([],[], marker="s", ms=10, ls="", color=c, label=l)[0] for l,c in labels.items()]
        plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.pause(0.1)
