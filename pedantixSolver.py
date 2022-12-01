"""
Ce programme permet de trouver rapidement la page wikipédia pédantix du jour
Il prend en moyenne entre 15 et 30 secondes pour proposer 3 pages wikipédia potentielles
parmis lequels se trouve peut être la page du jour

Il utilise un dictionaire simple des mots et verbes les plus courants et des méthodes
de recherches Google afin de proposer le résultat le plus pertinent possible

Pour l'utiliser, il faut avoir installé les modules requests, tqdm et google

Pour installer les modules, il suffit de lancer la commande suivante dans un terminal:
pip install requests tqdm google

Pour lancer le programme, il suffit de lancer la commande suivante dans un terminal:
python pedantixSolver.py

Réalisé par @DragonSlyme
"""

import requests
import sys
from googlesearch import search
from urllib.parse import unquote
from tqdm import tqdm

# Fonction pour envoyer une requête à l'API de pédantix
def send_word(word):
    payload = {"word": word, "answer": [word, word, word]}
    response = requests.post(url, headers=headers,json=payload).json()
    return response


# Dictionnaire des mots trouver sur la page sans doublons
def get_list_words(word, list_words):
    response = send_word(word)
    for words in response["score"].items():
        word = words[1]
        if isinstance(word, str):
            if word.lower() not in list_words.values():
                list_words[int(words[0])] = word.lower()
    return list_words


# Fonction pour tester le dictionnaire
def test_dictionnary(dictionnary, list_words):
    for word in tqdm(dictionnary):
        get_list_words(word, list_words)
    return list_words


# Fonction pour convertir la liste des mots en une chaine de caractère utilisant les bonnes pratiques de recherches Google
def convert_list_to_search(list_words):
    search = ""
    number_of_words = 0
    for key in sorted(list_words.keys()):
        if number_of_words < MAX:
            search += f"\"{list_words[key]}\" "
            number_of_words += 1
        else:
            break  
    search += "site:https://fr.wikipedia.org/"
    return search

# Fonction pour récupérer les urls des pages wikipédia et n'en garder que la fin
def get_wikipedia_url(query):
    list_possible_words = []
    as_argument = len(sys.argv) > 1
    ban_extension = [".pdf", ".html", ".fr", "/", ".htm", "#"]
    nb_search = 10
    nb_max_search = 3
    for url in search(query, stop=nb_search, pause=0.1):
        clean_word = unquote(url)[30:].replace("_", " ")
        if as_argument:
            if nb_max_search > 0 and nb_search > 0:
                if all([extension not in clean_word for extension in ban_extension]) and int(sys.argv[1]) == len(clean_word.split(" ")[0]):
                    list_possible_words.append(clean_word)
                    nb_max_search -= 1
            else:
                break
        else:
            if nb_max_search > 0 and nb_search > 0:
                if all([extension not in clean_word for extension in ban_extension]):
                    list_possible_words.append(clean_word)
                    nb_max_search -= 1
            else:
                break
        nb_search -= 1
    return list_possible_words

# Programme principal
def main():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("|            Pédantix Solver              |")
    print("|            by @DragonSlyme              |")
    print("|             Version 1.1.0               |")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

    dictionnary = open("dictionnary.txt", "r").readlines()
    print("En recherche:")
    list_word = test_dictionnary(dictionnary, {})
    list_to_search = convert_list_to_search(list_word)
    results = get_wikipedia_url(list_to_search)

    i = 1

    print("\nListe des mots pédantix potentiel aujourd'hui:\n")
    for result in results:
        print("\033[92m" + f"[+{i}+]" + "\033[0m" + f" {result}\n")
        i += 1


if __name__ == "__main__":
    MAX = 31

    url = "https://cemantix.certitudes.org/pedantix/score"

    headers = {
        "authority" : "cemantix.certitudes.org",
        "method" : "POST",
        "path" : "/pedantix/score",
        "scheme" : "https",
        "accept" : "*/*",
        "accept-encoding" : "gzip, deflate, br",
        "accept-language" : "fr-FR,fr;q=0.7",
        "content-length" : "43",
        "content-type" : "application/json",
        "origin" : "https://cemantix.certitudes.org",
        "referer" : "https://cemantix.certitudes.org/pedantix",
        "sec-fetch-dest" : "empty",
        "sec-fetch-mode" : "cors",
        "sec-fetch-site" : "same-origin",
        "sec-gpc" : "1",
        "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    main()