# PedantixSolver
Programme __simple__ mais __efficace__ qui vous permez de trouver la page _pédantix_ cachée du jour. 

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

En __moyenne__ ce programme finit ces recherches entre __10 et 40 secondes__ (selon votre connexion internet par exemple)

![Imagetop2](https://i.imgur.com/ZXFRIN7.png)

![ImageTerminal](https://i.imgur.com/adu9UfP.png)

`PS: Par malchance le bot peut ne pas vous renvoyer la bonne réponse`

À vous de modifier le dictionnaire pour qu'il soit encore plus performant (celui-ci est d'ailleurs en partie basé sur le travail de [AnthonyJungmann](https://github.com/AnthonyJungmann/pedantix_mots/blob/master/mots_sans_stopwords.txt))

Il peut largement être amélioré, c'est pourquoi je suis ouvert à toute nouvelle proposition de code.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F3GQWPN)