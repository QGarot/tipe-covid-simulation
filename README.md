## Impact des outils numériques sur le contrôle d’une pandémie

### Modèle SIR

**Fichiers contenant la modélisation SIR :**
* [euler_method.py](https://github.com/QGarot/covid-simulation/blob/master/euler_method.py)
* [SIR_model.py](https://github.com/QGarot/covid-simulation/blob/master/SIR_model.py)
* [consts.py](https://github.com/QGarot/covid-simulation/blob/master/consts.py)

Cette modélisation permet d'étudier les variations des trois catégories de personnes (sains, inféctés, rétablis) en
fonction du temps.

---

### Simulation

On considère une région contenant n individus représentés par des points colorés (rouge pour un individu contaminé,
vert pour un individu sain et orange pour un individu rétabli).

Cette simulation a pour objectif de représenter un phénomène de foule.
Pour cela, on représente par un "point attracteur" ce que pourrait être un concert, un marché de Noel, une école ou tout
tout autre lieu/évènement pouvant être à l'origine d'un rassemblement de personnes
conséquent. Ainsi, tous les points se dirigeront vers ce point attracteur, et on mettra en évidence la transmission du
virus par des modification de couleur (par exemple, si un individu sain rentre en contact avec un individu infecté, le
point qui le représente deviendra rouge).

**Dossier contenant la simulation :**

* [Simulation](https://github.com/QGarot/covid-simulation/tree/master/simulation)
    * [Fichier principal (main)](https://github.com/QGarot/covid-simulation/blob/master/simulation/main.py)
    * [Classe Simulation](https://github.com/QGarot/covid-simulation/blob/master/simulation/simulationc.py)
    * [Classe Point](https://github.com/QGarot/covid-simulation/blob/master/simulation/point.py)
    
**Premier aperçu :**
(Ce qu'il reste à faire : transmission du virus => changement de couleur) / contact entre deux points
[![Image from Gyazo](https://i.gyazo.com/ba595fe90a378a2d9b0129515082dc1d.gif)](https://gyazo.com/ba595fe90a378a2d9b0129515082dc1d)

---

### Sauvegarde

Objectif : pouvoir déterminer les tranches de la population les plus exposées aux risques.

Pour cela : créer une base de données grâce à laquelle seront enregistrées tous les contacts qui auront lieu pendant la
simulation.

*A terminer...*

**Dossier concerné :**
* [Serveur](https://github.com/QGarot/covid-simulation/tree/master/server)
* [Base de données](https://github.com/QGarot/covid-simulation/tree/master/database)