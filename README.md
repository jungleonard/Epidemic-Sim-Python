# 🦠 Modeling Herd Immunity & Viral Propagation

Ce projet est une simulation de la propagation d'une maladie au sein d'une population dynamique utilisant un modèle d'automate cellulaire. L'objectif est d'étudier l'impact des politiques de vaccination et de l'immunité collective sur l'évolution d'une épidémie.

---

## 🔬 Objectifs Scientifiques

L'étude repose sur deux hypothèses majeures :
1. **Thèse Principale :** Si 50% de la population est vaccinée, la maladie disparaît du système (Seuil d'immunité collective).
2. **Thèse Secondaire :** Si 50% de la population est infectée initialement, la contamination devient totale.

Le projet évalue l'efficacité des interventions de santé publique en faisant varier des paramètres tels que le taux de transmission, la durée d'incubation et la cinétique de vaccination.

---

## 🛠️ Architecture du Projet

Le simulateur est développé en **Python 3** en utilisant le paradigme de la **Programmation Orientée Objet (POO)**.

*   **Modélisation spatiale :** La population est représentée par une matrice 2D où chaque cellule contient un objet `Individu`.
*   **Voisinage :** Utilisation du modèle de Moore (carré de 8 voisins).
*   **États des individus :**
    *   ⚪ `Normal` : Susceptible d'être infecté.
    *   🔴 `Infecté` : Porteur et transmetteur de la maladie.
    *   🛡️ `Immunisé` : Guéri après infection (protection temporaire).
    *   💉 `Vacciné` : Protection permanente contre la maladie.

---

## ⚙️ Paramètres de Simulation

Le système est hautement configurable via les variables suivantes :
- **Taille de l'espace :** Dimensions de la matrice de simulation.
- **Taux de transmission :** Probabilité de contagion selon le nombre de voisins infectés (seuil par défaut : 3).
- **Durée de maladie :** Nombre d'itérations avant la guérison (défaut : 5).
- **Durée d'immunisation :** Temps pendant lequel un individu guéri ne peut pas être réinfecté.
- **Vaccination temps réel :** Probabilité pour un individu normal de se faire vacciner à chaque étape.

---

## 📚 Références & Inspirations
- **Modèles de complexité :** [Complexity Explorables](https://www.complexity-explorables.org/explorables/i-herd-you/)
- **Concepts épidémiologiques :** [Institut Pasteur - Immunité collective](https://www.pasteur.fr/fr/espace-presse/documents-presse/qu-est-ce-que-immunite-collective)
- **Données de santé :** [OMS (WHO) - COVID-19 & Herd Immunity](https://www.who.int/fr/news-room/questions-and-answers/item/herd-immunity-lockdowns-and-covid-19)

---
**Auteur :** Léonard Jung - Étudiant en Double Licence Mathématiques & Informatique à Sorbonne Université.
