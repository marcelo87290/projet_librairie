     
print('         Bien venu au projet API Librairie')
print('')
print('         Appuyer sur <<Entrée>> pour commencer>>')
input()
print('')


import requests 
import json

r = requests.get("https://demo.api-platform.com/books?order[publicationDate]=desc&page=1")

r.json()
dico={}
dico = json.loads(r.text)
dico

lista=[]

lista=dico['hydra:member']

print('')
print('la Liste des 10 derniers livres par leur date de publication') 
print('')  

n=10 
for i in range(n):
   # if ((lista[i]['publicationDate'])[0:4]) in lista1:
        print('Title : '+ lista[i]['title'])
        print('Auteur : '+ lista[i]['author'])
        print('Année de Publication:'+ ((lista[i]['publicationDate'])[0:4]))
        print(' ')

###----------------EXO 2   
print('')
print('Appuyer sur <<Entrée>> ')
input()
print('')
import requests 
import json
r = requests.get("https://demo.api-platform.com/books?author=Dr.%20Kaitlyn%20Ratke&page=1")

dico={}
dico = r.json()

dico

lista=[]

lista=dico['hydra:member']

n=len(lista)

for i in range(n):
    #print (lista[i]['author'])
    if (lista[i]['author']) == 'Dr. Kaitlyn Ratke':
            print('Auteur : Dr. Kaitlyn Ratke')
            print('le title du livre : '+lista[i]['title'])
            print('Année de Publication :'+ ((lista[i]['publicationDate'])[0:4]))
    


###------------EXO3

print('')
print('Appuyer sur <<Entrée>>')
input()
print('')
import requests 
import json

r = requests.get("https://demo.api-platform.com/books/1d52ba85-97c8-4cc3-b81a-40582f3aff64")

dico={}
dico = r.json()
dico.keys()
lista=[]
lista=dico['reviews']
print(' ')
print('Liste des commentaires concernant le livre de')
print('l'+'ID = 1d52ba85-97c8-4cc3-b81a-40582f3aff64')
print('')
print('Titre du Livre :'+(dico['title']))
print('Auteur :'+(dico['author']))
print('Année de Publication :'+ ((dico['publicationDate'])[0:4]))
print(' ')
n=len(lista)
c=0
for i in range(n):
    c+=1
    print(str(c)+'°) '+lista[i]['body'])
    print('')
###------------Exo 4
print('')
print('Appuyer sur <<Entrée>>')
input()
print('')
print(' Le Commentaire avec le texte et la note de votre choix pour le livre')
#print('avec le texte et la note de votre choix pour le livre')
print('dont le id est « 1b08c9ab-6254-4015-ad14-bac3e5c008df.')
print('')



import requests 
import json

commentaire = {"body": "La représentation de la maximisation des espaces modulaires",
      "rating": 2,
      "author": "M.CORBOUSIER",
      "book": "books/1b08c9ab-6254-4015-ad14-bac3e5c008df"}
#commentaire=json.dumps(commentaire)
r_post = requests.post("https://demo.api-platform.com/reviews", json=commentaire)
dico=r_post.json()
dico
print(dico['body'])
print('')
print('La note :'+str(dico['rating']))
var_id=dico['@id']

print(var_id)

###------Exo 5
print('')
print('Appuyer sur <<Entrée>>')
input('')
print(' ')
print('Modification du nouveau commentaire en utilisant l’id qui')
print('a été fourni lors de sa création')
print('')
print('')


import requests 
import json
var_alt={"body": "La représentation de la minimisation des espaces modulaires"}
r_patch = requests.patch("https://demo.api-platform.com"+var_id, json = var_alt,headers={'Content-Type': 'application/merge-patch+json'})
dico=r_patch.json()
print('')
print('modification :')
print('')
print(dico['body'])
print(' ')

print('<----------------FIN----------------------->')
