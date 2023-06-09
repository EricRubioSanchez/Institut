from institut import *
#Crear alumne
a1= Alumne("A1","Pep","Garcia",date(2000,10,5))
alumnes["A1"] = a1
a2= Alumne("A2","Marta","Perez",date(2002,5,1))
alumnes["A2"] = a2
a3= Alumne("A3","Pere","Pi",date(1998,4,20))
alumnes["A3"] = a3
a4= Alumne("A4","Joana","Matas",date(2004,6,1))
alumnes["A4"] = a4

#Crear Materias
m1=Materia("M1","Mates")
materies["M1"] = m1
m2=Materia("M2","Socials")
materies["M2"] = m2
m3=Materia("M3","Francès")
materies["M3"] = m3

#Matricular
a1.Materies["M1"] = "--"
m1.Alumnes.append(a1)

a1.Materies["M2"] = "--"
m2.Alumnes.append(a1)

a2.Materies["M1"] = "--"
m1.Alumnes.append(a2)

a2.Materies["M2"] = "--"
m2.Alumnes.append(a2)

a3.Materies["M1"] = "--"
m1.Alumnes.append(a3)

a3.Materies["M3"] = "--"
m3.Alumnes.append(a3)

a4.Materies["M1"] = "--"
m1.Alumnes.append(a4)

a4.Materies["M2"] = "--"
m2.Alumnes.append(a4)

a4.Materies["M3"] = "--"
m3.Alumnes.append(a4)

#Posar nota
a1.Materies["M1"] = 3
a2.Materies["M1"] = 7
a3.Materies["M3"] = 2
a3.Materies["M1"] = 8
a4.Materies["M1"] = 5
a4.Materies["M2"] = 3
a4.Materies["M1"] = 8

if "__main__"==__name__:

    for alumne in m1.Alumnes:
        print(f"{m1.Nom:20}{alumne.Nom:20}{alumne.Cognom:20}{alumne.Materies[m1.Codi]:>4}")
    for alumne in m2.Alumnes:
        print(f"{m2.Nom:20}{alumne.Nom:20}{alumne.Cognom:20}{alumne.Materies[m2.Codi]:>4}")
    for alumne in m3.Alumnes:
        print(f"{m3.Nom:20}{alumne.Nom:20}{alumne.Cognom:20}{alumne.Materies[m3.Codi]:>4}")
