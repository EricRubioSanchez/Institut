from omplir import *
opcions=("Afegir Nou Alumne","Afegir Nova Materia","Eliminar Alumne","Eliminar Materia","Matricular Alumne","Desmatricular Alumne","Materies Matriculades del Alumne","Posar Nota","Mostrar Notes per Materia","Mostrar Notes per Alumne","Mostrar totes les Materies","Mostrar tots els Alumnes","Sortir")

fi=False
while not fi:
    
    mostrarMenu(opcions)
    print("")
    opcio=escullOpcio(len(opcions))
    print("")
    
    #Afegir Nou Alumne
    if opcio=="1":
        nouAlumne()
        
    #Afegir Nova Materia
    elif opcio=="2":
        novaMateria()

    #Eliminar Alumne
    elif opcio=="3":
        codiAlumne = input("Codi del alumne: ").upper()
        eliminarAlumne(codiAlumne)

    #Eliminar Materia
    elif opcio=="4":
        codiMateria = input("Codi de la materia: ").upper()
        eliminarMateria(codiMateria)

    #Matricular Alumne
    elif opcio=="5":
        codiAlumne = input("Codi del alumne: ").upper()
        codiMateria = input("Codi de la materia: ").upper()
        matriculaAlumne(codiAlumne,codiMateria)

    #Desmatricular Alumne
    elif opcio=="6":
        codiAlumne = input("Codi del alumne: ").upper()
        codiMateria = input("Codi de la materia: ").upper()
        desmatriculaAlumne(codiAlumne,codiMateria)

    #Materies Matriculades del Alumne
    elif opcio=="7":
        codiAlumne = input("Codi del alumne: ").upper()
        matriculadesAlumne(codiAlumne)

    #Posar nota
    elif opcio=="8":
        codiAlumne = input("Codi del alumne: ").upper()
        codiMateria = input("Codi de la materia: ").upper()
        nota = input("Nota: ")
        llave=False
        try:
            nota = int(nota)
            llave=True
        except:
            print("La nota no pot tenir decimals ni caracters")
        if llave:
            posarNota(codiAlumne,codiMateria,nota)

    #Mostrar Nota per Materia
    elif opcio=="9":
        codiMateria = input("Codi de la materia: ").upper()
        mostrarNotesMateria(codiMateria)

    #Mostrar Nota per Alumne
    elif opcio=="10":
        codiAlumne = input("Codi del alumne: ").upper()
        mostrarNotesAlumne(codiAlumne)

    #Motrar Totes les Materies
    elif opcio =="11":
        mostrarToTesMateries()

    #Mostrar Tots els alumnes
    elif opcio == "12":
        mostrarTotsAlumnes()

    #Sortir
    elif opcio=="13":
         sortir()
         fi=True
     
    print("")
