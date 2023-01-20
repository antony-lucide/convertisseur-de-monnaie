from tkinter import *
import tkinter as tk 





OPTION = { #List de deux argumets afin de convertir
    "Euro":77.85,
    "Us Dollar":69.32
        }






def transition(): #Fonction permettant de convertir
    somme = (equation.get())#Récupération des deux valeurs, somme et taux
    taux =  (résultat.get())
    dict = OPTION.get(résultat,None)#Récuperation du dictionnaire
    converti = float(dict)*(somme)#Calcule
    résult1.insert(INSERT, "le prix en", INSERT, résultat,INSERT," = ",converti)#Réponse
    if equation !="":
            try:
                result = eval(converti) #évalue l'équation
            except:
                result = "error"
                equation = ""
            résult1.config(text=converti)


    
        


gui = tk.Tk() #créer une nouvelle fenêtre sur linux ou window/mac
gui.configure (background="dark blue")
gui.title("Convertisseur de monnaie")
gui.geometry("600x400")
résult1 = LabelFrame(gui, text="Taux",borderwidth=80, relief=SUNKEN, width=60, height=60)
résult1.pack( fill=X, side=TOP, expand=True)
equation = StringVar()
résult2 = Entry(gui, textvariable=equation,width=60).place(x=50, y=100) 
résult3 = LabelFrame(gui, text="somme",borderwidth=80, relief=SUNKEN, width=70, height=70)
résultat = StringVar
résult3.pack(fill=X, side=BOTTOM, expand=True)
result3 = Entry(gui, textvariable=résultat,width=70)
Button(gui, text="calcule", command=transition,width=20).place(x=9, y=130)
result3 = Entry(gui, textvariable=résultat,width=60).place(x=40,y=300)
résultat = LabelFrame(gui, text='',borderwidth=80, relief=SUNKEN, width=70, height=70).place(x=9, y=500)

gui.mainloop()
