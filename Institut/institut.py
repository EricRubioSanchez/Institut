from datetime import *
import re
#Variables Globals
#alumnes és un diccionari que tindrà com a Key el codi de l'alumne, i com a Value al propi alumne
alumnes={}
#materies és un diccionari que tindrà com a Key el codi de la materia i com a value la pròpia matèria
materies={}


#Classes
class Alumne:
    def __init__(self,Codi:str,Nom:str,Cognom:str,DataNaixement:date):
        self.Codi=Codi
        self.Nom=Nom
        self.Cognom=Cognom
        self.DataNaixement=DataNaixement
        #self.Materies és un diccionari que tindrà com a Key el codi de MAtèria, i com a value la nota que ha tret l'alumnes de la matèria
        self.Materies={}
class Materia:
    def __init__(self,Codi:str,Nom:str):
        self.Codi=Codi
        self.Nom=Nom
        #self.Alumnes és una llista que contindrà els alumnes que estan matriculats de cada matèria. Han de ser els alumnes(Clss Alumne), no els codis d'alumnes
        self.Alumnes=[]

#Funcions que heu de programar
def nouAlumne():
    #Ha de demanar les dades d'un alumne, crea-lo i retornar una variable de la classe Alumne
    ahora=(datetime.now()).date()
    patroNom = "^[ a-zA-ZÀ-ȗ]{3,}$"
    patroCodi = "^[A-Z]{1}[0-9]{1}$"
    Codi = input("Codi: ").upper()
    Nom = input("Nom: ")
    Cognom = input("Cognom: ")
    DataNaixement = input("Data Naixement (d/m/a): ")
    if re.search(patroCodi,Codi):
        if re.search(patroNom,Nom) and re.search(patroNom,Cognom):
            try:
            
                DataNaixement = (datetime.strptime(DataNaixement, '%d/%m/%Y')).date()
                if ahora < DataNaixement:
                    a= 1/0
            except:
                print("La data es incorrecte")
                print("L'Alumne no es guardara")
                return None
        else:
            print("El nom i el cognom han de ser minim de 3 lletres")
            print("L'Alumne no es guardara")
            return None
    else:
        print("El codi del Alumne ha de amb una lletra i un numero")
        return None
    segur = input("Vols guardar l'alumne(s/n)? ").lower()
    while segur=="s" and segur=="n":
        print("La reposta nómes pot ser o s o n")
        segur=input("Vols guardar l'alumne?(s/n) ").lower()
    if segur=="s":
        a1 = Alumne(Codi,Nom,Cognom,DataNaixement)
        afegirAlumne(a1)
        print("Alumne guardat")
    if segur=="n":
        print("Alumne no creat")
        return None
    return a1

def novaMateria():
    #Ídem anterior però amb materia
    patroNom = "^[ a-zA-ZÀ-ȗ]{3,}$"
    patroCodi = "^[A-Z]{1}[0-9]{1}$"
    Codi = input("Codi: ").upper()
    Nom = input("Nom: ")
    if re.search(patroCodi,Codi):
        if re.search(patroNom,Nom):
            segur = input("Vols guardar la materia(s/n)? ").lower()
            while segur=="s" and segur=="n":
                print("La reposta nómes pot ser o s o n")
                segur=input("Vols guardar la materia?(s/n) ").lower()
            if segur=="s":
                m1 = Materia(Codi,Nom)
                afegirMateria(m1)
                print("Materia guardada")
            if segur=="n":
                print("Materia no creada")
        else:
            print("El nom ha de ser minim de 3 lletres")
            print("La materia no es guardara")
            return None
    else:
        print("El codi de la Materia ha de amb una lletra i un numero")
        return None
    return m1

def afegirAlumne(a:Alumne):
    #Afegirà l'alumne a al diccionari alumnes
    alumnes[a.Codi] = a

def afegirMateria(m:Materia):
    #Afegirà la materia m al diccionaru materies
    materies[m.Codi] = m


def eliminarAlumne(codiAlumne:str):
    #Elimina del diccionary alumnes, l'alumne que té com a codi codiAlumne
    #Ha de eliminar-lo també de totes les materies que estigui matriculat
    try:
        alumne = alumnes[codiAlumne]
    except:
        print("No existeix l'alumne")
        return None
    for m in alumne.Materies:
        materia = materies[m]
        materia.Alumnes.remove(alumne)
    alumnes.pop(alumne.Codi)
    print("Alumne eliminat")
        

def eliminarMateria(codiMateria:str):
    #Eliminar la materia amb codiMateria del diccionari materies,
    #i també del diccionari a.materies de tots els alumnes que estaven matriculats d'aquella matèria
    try:
        materia = materies[codiMateria]
    except:
        print("No existeix la materia")
        return None
    for a in materia.Alumnes:
        a.Materies.pop(materia.Codi)
    materies.pop(materia.Codi)
    print("Materia eliminada")
    


def matriculaAlumne(codiAlumne:str,codiMateria:str):
    #agafarà l'alumne a, que té com a codi codiAlumne del dicc alumnes
    #agafarà la materia m, que té com a codi codiMateria del dicc materies
    #afegirà el coidiMateria a alumne a, per tant, l'afegirà al diccionai a.Materies, amb value buit, el value serà la nota
    #afegirà l'alumne a la materia m, l'afegirà a la llista m.Alumnes
    #Tot l'anterior sempre comprovant que existeixen l'alumne i la materia
    try:
        alumne = alumnes[codiAlumne]
    except:
        print("No existeix l'alumne")
        return None
    try:
        materia = materies[codiMateria]
    except:
        print("No existeix la materia")
        return None
    try:
        a = alumne.Materies[materia.Codi]
        print("L'alumne ja estava matriculat")
        return None
    except:        
        alumne.Materies[materia.Codi] = "--"
        materia.Alumnes.append(alumne)
        print("Alumne Matriculat")
def desmatriculaAlumne(codiAlumne:str,codiMateria:str):
    #Ha de fer el contrari que el métode anterior
    try:
        alumne = alumnes[codiAlumne]
    except:
        print("No existeix l'alumne")
        return None
    try:
        materia = materies[codiMateria]
    except:
        print("No existeix la materia")
        return None
    try:
        alumne.Materies.pop(materia.Codi)
        materia.Alumnes.remove(alumne)
        print("Alumne desmatriculat")
    except:
        print("L'alumne no estava matriculat")

def estaMatriculat(Alumne,Materia):
    #retornarà True si l'alumne ja està matriculat de la materia i false sinó està matriculat
    if Materia.Codi in Alumne.Materies:
        return True
    else:
        return False

def matriculadesAlumne(codiAlumne:str):
    #retornara totes les materies i en las que estigui matriculat posara True
    try:
        alumne = alumnes[codiAlumne]
    except:
        print("No existeix l'alumne")
        return None
    print(f"Alumne {alumne.Cognom} {alumne.Nom}")
    for m,i in materies.items():
        if estaMatriculat(alumne,i):
            print(f"{m:5} {i.Nom:10} {'Matriculat':20}")
        else:
            print(f"{m:5} {i.Nom:10} {'No Matriculat':20}")
    

def posarNota(codiAlumne:str,codiMateria:str,nota:int):
    #Servirà per posar nota a l'alumne a
    #Comprovarà que l'alumne està matriculat de la materia, i després li possarà nota
    # a[codiMateria]=nota
    try:
        alumne = alumnes[codiAlumne]
    except:
        print("No existeix l'alumne")
        return None
    try:
        materia = materies[codiMateria]
    except:
        print("No existeix la materia")
        return None
    if nota>10 or nota<0:
        print("La nota nómes pot estar entre el 10 i el 0")
        return None
    if estaMatriculat(alumne,materia):
        alumne.Materies[materia.Codi] = nota
        print("Nota posada")
    else:
        print("No es pot posar la nota perquè l'alumne no esta matriculat")

def mostrarNotesMateria(codiMateria:str):
    #Li passarem el codi d'una Matèria i ens mostrarà per pantalla un llistat amb les següents columnes:
    #Nom Materia    CodiAlumne  NomAlumne Nota
    #Si l'alumne no té nota, mostrarà 2 guionets --
    try:
        materia = materies[codiMateria]
    except:
        print("No existeix la materia")
        return None
    for a in materia.Alumnes:
        print(f"{materia.Nom:20}{a.Codi:20}{a.Nom:20}{a.Materies[materia.Codi]:>4}")
        

def mostrarNotesAlumne(codiAlumne:str):
    #Li passarem el codi d'un alumne i ens mostrarà per pantalla un llistat amb les següents columnes:
    #Nom Materia  Nota
    #Si l'alumne no té nota, mostrarà 2 guionets --
    try:
        alumne = alumnes[codiAlumne]
    except:
        print("No existeix l'alumne")
        return None
    for m,n in alumne.Materies.items():
        materia = materies[m]
        print(f"{materia.Nom:20}{n:>20}")

def mostrarTotsAlumnes():
    print(f"{'Cognom':20}{'Nom':20}{'Nota Mitjana':20}{'Materies Avaluades':20}")
    print("-"*80)
    for c,a in alumnes.items():
        contador=0
        nota = 0
        for m,i in a.Materies.items():
            if i!="--":
                nota = nota + i
                contador = contador +1
        if contador > 0:
            nota=nota/contador
        print(f"{a.Cognom:20}{a.Nom:20}{nota:<20}{contador:<20}")

def mostrarToTesMateries():
    print(f"{'Nom':20}{'Alumnes avaluats':20}{'Nota mitjana':20}")
    print("-"*60)
    for c,m in materies.items():
        alum = 0
        nota = 0
        for a in m.Alumnes:
            if a.Materies[m.Codi]!="--":
                nota = nota + a.Materies[m.Codi]
                alum=alum+1
        if alum > 0:
            nota = nota / alum
        print(f"{m.Nom:20}{alum:<20}{nota:<20}")

def mostrarMenu(opcions):
     for i,opcio in enumerate(opcions):
        print(f"{i+1:2}. {opcio}")
        
def escullOpcio(n):
    patro = "^\d{1,}$"
    while True:
        o = input("Opció: ")
        if re.search(patro,o):
            if n>=int(o) and int(o)!=0:
                return o
def sortir():
    print("Sortint del programa")
