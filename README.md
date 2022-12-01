# PedantixSolver
Programme __simple__ mais __efficace__ qui vous permet de trouver la page _pédantix_ cachée du jour. 

---
## Dépendances:
Il vous faudra dans un premier temps avoir [python](https://www.python.org/downloads/) installé sur votre machine.

Il vous faudra aussi __installer__ les __modules suivants__: 
- Requests 
- Tqdm 
- Google

Vous pouvez les installer facilement à l'aide de la commande suivante:
```
pip install requests tqdm google
```
`Cela peut prendre quelques minutes`

Et enfin, il est __absolument__ nécessaire d'avoir le fichier "dictionnary.txt" dans __le même__ ficher que "pedantixSolver.py"

---
## Utilisation:
Lancez simplement la commande suivante __après__ avoir installé les dépendances:
```
python pedantixSolver.py [nb](option)
```
ou alors:
```
python3 pedantixSolver.py [nb](option)
```
__nb__ est optionnel et correspond au nombre de lettre du __premier mot__ de la page wikipédia accessible en cliquant sur la case noir, cela peut permettre de grandement améliorer les résultats.

---
## Performances:

En __moyenne__ ce programme finit ces recherches entre __25 et 50 secondes__ (selon la configuration de votre pc) 

`PS: Par malchance le bot peut ne pas vous renvoyer la bonne réponse`

À vous de modifier le dictionnaire pour qu'il soit encore plus performant (celui-ci est d'ailleurs en partie basé sur le travail de [AnthonyJungmann](https://github.com/AnthonyJungmann/pedantix_mots/blob/master/mots_sans_stopwords.txt))

Il peut largement être amélioré, c'est pourquoi je suis ouvert à toute nouvelle proposition de code.