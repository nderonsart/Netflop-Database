#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creation de l'interface pour la base de données de Netflop

@author: Nicolas Deronsart
"""

import tkinter
import tkinter.font as font
from tkinter import messagebox

import sqlite3


class InterfaceNetflop:
    ''' Classe qui permet d'interagir avec la base de données de Netflop '''
    
    
    def __init__(self, conn, cur):
        ''' Constructeur de la classe InterfaceBD '''
        
        self.conn=conn
        self.cur=cur
        
        self.fenetre=tkinter.Tk()
        self.fenetre.title('Netflop Database')
        self.fenetre.configure(bg='white')
        
        self.fontStyle = font.Font(family="Times", size=15)
        
        
        
        
        frame0 = tkinter.Frame(self.fenetre, borderwidth=2, bg='white')
        
        tkinter.Label(frame0, text='Bienvenue', font=self.fontStyle, relief=tkinter.RIDGE).pack(side=tkinter.BOTTOM, padx=300)
        
        image_quitter=tkinter.PhotoImage(master=self.fenetre, file='img/exit.gif')
        tkinter.Button(frame0, image=image_quitter, command=self.quitter, relief=tkinter.SUNKEN).pack(side=tkinter.RIGHT)
        
        frame0.pack(pady=10)
        
        
        
        
        frame1_2 = tkinter.Frame(self.fenetre, borderwidth=2, bg='white')
        
        
        
        frame1 = tkinter.Frame(frame1_2, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame1, text="Parcourir...", font=self.fontStyle).pack(padx=5, pady=10)
        
        tkinter.Button(frame1, text='Utilisateurs', command=self.parcourir_utilisateur, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame1, text='Films', command=self.parcourir_film, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame1, text='Series', command=self.parcourir_serie, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame1, text='Acteurs', command=self.parcourir_acteur, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame1, text='Realisateurs', command=self.parcourir_realisateur, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame1, text='Entreprises', command=self.parcourir_entreprise, font=self.fontStyle).pack(padx=5, pady=5)
        
        frame1.pack(side=tkinter.LEFT, padx=50, pady=20)
        
        
        
        frame2 = tkinter.Frame(frame1_2, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame2, text="Modification", font=self.fontStyle).pack(padx=5, pady=10)
        
        tkinter.Button(frame2, text='Utilisateur', command=self.modification_utilisateur, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame2, text='Visionnage', command=self.modification_visionnage, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame2, text='Oeuvre', command=self.modification_oeuvre, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame2, text='Acteur', command=self.modification_acteur, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame2, text='Jouer', command=self.modification_jouer, font=self.fontStyle).pack(padx=5, pady=5)
        tkinter.Button(frame2, text='Realisateur', command=self.modification_realisateur, font=self.fontStyle).pack(padx=5, pady=5)
        
        frame2.pack(side=tkinter.RIGHT, padx=50, pady=10)
        


        frame1_2.pack(padx=100, pady=10)
        
        
        
        
        self.frame3 = tkinter.Frame(self.fenetre, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(self.frame3, text="Recommandation", font=self.fontStyle).pack(padx=5, pady=10)
        
        self.cur.execute('select id_utilisateur from utilisateur')
        requete=self.cur.fetchall()
        
        self.liste_boutons_utilisateurs=[]
        for i in range (len(requete)):
            btn=tkinter.Button(self.frame3, text='User '+str(requete[i][0]), command=self.creer_recommandation(requete[i][0]), font=self.fontStyle)
            btn.pack(padx=5, pady=5)
            self.liste_boutons_utilisateurs.append(btn)
        
        self.frame3.pack(side=tkinter.BOTTOM, padx=100, pady=20)
        
        
        self.fenetre.mainloop()
    
    
    
    
    def parcourir_utilisateur(self):
        ''' Affiche une fenetre présentant les utilisateurs et leur age '''
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        tkinter.Label(top_level, text='Nom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=0, padx=10, pady=10)
        tkinter.Label(top_level, text='Prenom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=1, padx=10, pady=10)
        tkinter.Label(top_level, text='Age', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=2, padx=10, pady=10)
        
        self.cur.execute('select nom, prenom, date(\'now\')-date_naiss from utilisateur order by nom')
        requete=self.cur.fetchall()
        
        for i in range(len(requete)):
            for j in range(len(requete[i])):
                tkinter.Label(top_level, text=requete[i][j], font=self.fontStyle).grid(row=i+1, column=j, padx=10, pady=10)
        
        
        
    
    
    def parcourir_film(self):
        ''' Affiche une fenetre présentant les films de la plateforme '''
        
        def film_prefere_utilisateurs():
            ''' Gère le cas où l'on souhaite faire apparaître le film préféré des utilisateurs '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Film préféré de la plateforme')  
            
            self.cur.execute('select * from film_prefere_utilisateurs')
            requete=self.cur.fetchall()
            
            tkinter.Label(top_level2, text=requete[0][0], font=self.fontStyle).pack(padx=10, pady=10)
            
        
        def netflop_films():
            ''' Gère le cas où l'on souhaite faire apparaitre les films Netflop '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Films Netflop')  
            
            self.cur.execute('select * from films_netflop')
            requete=self.cur.fetchall()
            
            cpt=0
            lig=0
            col=0
            for i in range(len(requete)):
                if (cpt%15==0):
                    lig=0
                    col+=1
                tkinter.Label(top_level2, text=requete[i][0], font=self.fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                lig+=1
                cpt+=1
        
        
        def top_films():
            ''' Gère le cas où l'on souhaite faire apparaitre les meilleurs films de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Top Films')    
            
            self.cur.execute('select * from top_films')
            requete=self.cur.fetchall()
        
            cpt=0
            lig=0
            col=0
            for i in range(len(requete)):
                if (cpt%15==0):
                    lig=0
                    col+=1
                tkinter.Label(top_level2, text=requete[i][0], font=self.fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                lig+=1
                cpt+=1
            
        
        def flop_films():
            ''' Gère le cas où l'on souhaite faire apparaitre les pires films de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Flop Films')      
            
            self.cur.execute('select * from flop_films')
            requete=self.cur.fetchall()
        
            cpt=0
            lig=0
            col=0
            for i in range(len(requete)):
                if (cpt%15==0):
                    lig=0
                    col+=1
                tkinter.Label(top_level2, text=requete[i][0], font=self.fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                lig+=1
                cpt+=1
            
        
        def tous_films():
            ''' Gère le cas où l'on souhaite faire apparaitre tous les films de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Tous les Films')    
            
            self.cur.execute('select titre from film natural join oeuvre order by titre')
            requete=self.cur.fetchall()
        
            new_fontStyle = font.Font(family="Times", size=10)
        
            cpt=0
            lig=1
            col=0
            for i in range(len(requete)):
                if (cpt%20==0 and cpt!=0):
                    lig=1
                    col+=len(requete[i])
                    for j in range(20):
                        tkinter.Label(top_level2, text='|', font=new_fontStyle).grid(row=lig+j, column=col, padx=10, pady=10)
                    col+=1
                tkinter.Label(top_level2, text=requete[i][0], font=new_fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                lig+=1
                cpt+=1
            
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame_choix, text="Films", font=self.fontStyle).pack(padx=20, pady=10)
        
        tkinter.Button(frame_choix, text='Film préféré', command=film_prefere_utilisateurs, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Films Netflop', command=netflop_films, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Top films', command=top_films, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Flop films', command=flop_films, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Tous', command=tous_films, font=self.fontStyle).pack(padx=20, pady=5)
        
        frame_choix.pack(padx=10, pady=10)
        
        
    
    
    def parcourir_serie(self):
        ''' Affiche une fenetre présentant les séries de la plateforme '''
        
        def serie_preferee_utilisateurs():
            ''' Gère le cas où l'on souhaite faire apparaître la série préférée des utilisateurs '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Série préférée de la plateforme')  
            
            self.cur.execute('select * from serie_preferee_utilisateurs')
            requete=self.cur.fetchall()
            
            tkinter.Label(top_level2, text=requete[0][0], font=self.fontStyle).pack(padx=10, pady=10)
            
        
        def netflop_series():
            ''' Gère le cas où l'on souhaite faire apparaitre les séries Netflop '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Séries Netflop')     
            
            self.cur.execute('select * from series_netflop')
            requete=self.cur.fetchall()
            
            cpt=0
            lig=0
            col=0
            for i in range(len(requete)):
                if (cpt%15==0):
                    lig=0
                    col+=1
                tkinter.Label(top_level2, text=requete[i][0], font=self.fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                lig+=1
                cpt+=1
        
        
        def top_series():
            ''' Gère le cas où l'on souhaite faire apparaitre les meilleures séries de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Top Séries')   
            
            self.cur.execute('select * from top_series')
            requete=self.cur.fetchall()
        
            cpt=0
            lig=0
            col=0
            for i in range(len(requete)):
                if (cpt%15==0):
                    lig=0
                    col+=1
                tkinter.Label(top_level2, text=requete[i][0], font=self.fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                lig+=1
                cpt+=1
            
        
        def flop_series():
            ''' Gère le cas où l'on souhaite faire apparaitre les pires séries de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Flop Séries')     
            
            self.cur.execute('select * from flop_series')
            requete=self.cur.fetchall()
        
            cpt=0
            lig=0
            col=0
            for i in range(len(requete)):
                if (cpt%15==0):
                    lig=0
                    col+=1
                tkinter.Label(top_level2, text=requete[i][0], font=self.fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                lig+=1
                cpt+=1
            
        
        def toutes_series():
            ''' Gère le cas où l'on souhaite faire apparaitre toutes les séries de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Toutes les Séries')  
            
            self.cur.execute('select titre from serie natural join oeuvre order by titre')
            requete=self.cur.fetchall()
        
            new_fontStyle = font.Font(family="Times", size=10)
        
            cpt=0
            lig=1
            col=0
            for i in range(len(requete)):
                if (cpt%20==0 and cpt!=0):
                    lig=1
                    col+=len(requete[i])
                    for j in range(20):
                        tkinter.Label(top_level2, text='|', font=new_fontStyle).grid(row=lig+j, column=col, padx=10, pady=10)
                    col+=1
                tkinter.Label(top_level2, text=requete[i][0], font=new_fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                lig+=1
                cpt+=1
            
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame_choix, text="Séries", font=self.fontStyle).pack(padx=20, pady=10)
        
        tkinter.Button(frame_choix, text='Série préférée', command=serie_preferee_utilisateurs, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Séries Netflop', command=netflop_series, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Top séries', command=top_series, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Flop séries', command=flop_series, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Toutes', command=toutes_series, font=self.fontStyle).pack(padx=20, pady=5)
        
        frame_choix.pack(padx=10, pady=10)
    
    
    
    def parcourir_acteur(self):
        ''' Affiche une fenetre présentant les acteurs des oeuvres de la plateforme '''
        
        def recompenses():
            ''' Gère le cas où l'on souhaite faire apparaitre les acteurs ayant reçu des récompenses pour les oeuvres de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Acteurs récompensés')  
            
            tkinter.Label(top_level2, text='Nom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=0, padx=10, pady=10)
            tkinter.Label(top_level2, text='Prenom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=1, padx=10, pady=10)
            tkinter.Label(top_level2, text='Oeuvre', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=2, padx=10, pady=10)
        
            self.cur.execute('select * from acteur_recompense_pour')
            requete=self.cur.fetchall()
            
            for i in range(len(requete)):
                for j in range(len(requete[i])):
                    tkinter.Label(top_level2, text=requete[i][j], font=self.fontStyle).grid(row=i+1, column=j, padx=10, pady=10)
                
        
        def tous_acteurs():
            ''' Gère le cas où l'on souhaite faire apparaitre tous les acteurs d'oeuvres de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Tous les Acteurs')
        
            tkinter.Label(top_level2, text='Nom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=0, padx=10, pady=10)
            tkinter.Label(top_level2, text='Prenom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=1, padx=10, pady=10)
            
            self.cur.execute('select nom, prenom from acteur order by nom')
            requete=self.cur.fetchall()
            
            
            new_fontStyle = font.Font(family="Times", size=10)
        
            cpt=0
            lig=1
            col=0
            for i in range(len(requete)):
                if (cpt%20==0 and cpt!=0):
                    lig=1
                    col+=len(requete[i])
                    for j in range(20):
                        tkinter.Label(top_level2, text='|', font=new_fontStyle).grid(row=lig+j, column=col, padx=10, pady=10)
                    col+=1
                    
                for j in range(len(requete[i])):
                    tkinter.Label(top_level2, text=requete[i][j], font=new_fontStyle).grid(row=lig, column=col+j, padx=10, pady=10)
                lig+=1
                cpt+=1
                
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame_choix, text="Acteurs", font=self.fontStyle).pack(padx=20, pady=10)
        
        tkinter.Button(frame_choix, text='Récompensés', command=recompenses, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Tous', command=tous_acteurs, font=self.fontStyle).pack(padx=20, pady=5)
        
        frame_choix.pack(padx=10, pady=10)
        
        
        
        
    def parcourir_realisateur(self):
        ''' Affiche une fenetre présentant les réalisateurs des oeuvres de la plateforme '''
        
        def recompenses():
            ''' Gère le cas où l'on souhaite faire apparaitre les réalisateurs ayant reçu des récompenses '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Réalisateurs récompensés')  
            
            tkinter.Label(top_level2, text='Nom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=0, padx=10, pady=10)
            tkinter.Label(top_level2, text='Prenom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=1, padx=10, pady=10)
            
            self.cur.execute('select nom, prenom from realisateur where recompense=1 order by nom')
            requete=self.cur.fetchall()
            
            new_fontStyle = font.Font(family="Times", size=10)
        
            cpt=0
            lig=1
            col=0
            for i in range(len(requete)):
                if (cpt%20==0 and cpt!=0):
                    lig=1
                    col+=len(requete[i])
                    for j in range(20):
                        tkinter.Label(top_level2, text='|', font=new_fontStyle).grid(row=lig+j, column=col, padx=10, pady=10)
                    col+=1
                    
                for j in range(len(requete[i])):
                    tkinter.Label(top_level2, text=requete[i][j], font=new_fontStyle).grid(row=lig, column=col+j, padx=10, pady=10)
                lig+=1
                cpt+=1
                
        
        def tous_realisateurs():
            ''' Gère le cas où l'on souhaite faire apparaitre tous les réalisateurs d'oeuvres de la plateforme '''
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Tous les Acteurs')
        
            tkinter.Label(top_level2, text='Nom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=0, padx=10, pady=10)
            tkinter.Label(top_level2, text='Prenom', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=1, padx=10, pady=10)
            
            self.cur.execute('select nom, prenom from realisateur order by nom')
            requete=self.cur.fetchall()
            
            
            new_fontStyle = font.Font(family="Times", size=10)
        
            cpt=0
            lig=1
            col=0
            for i in range(len(requete)):
                if (cpt%20==0 and cpt!=0):
                    lig=1
                    col+=len(requete[i])
                    for j in range(20):
                        tkinter.Label(top_level2, text='|', font=new_fontStyle).grid(row=lig+j, column=col, padx=10, pady=10)
                    col+=1
                    
                for j in range(len(requete[i])):
                    tkinter.Label(top_level2, text=requete[i][j], font=new_fontStyle).grid(row=lig, column=col+j, padx=10, pady=10)
                lig+=1
                cpt+=1
                
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame_choix, text="Réalisateurs", font=self.fontStyle).pack(padx=20, pady=10)
        
        tkinter.Button(frame_choix, text='Récompensés', command=recompenses, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Tous', command=tous_realisateurs, font=self.fontStyle).pack(padx=20, pady=5)
        
        frame_choix.pack(padx=10, pady=10)
        
        
        
        
    def parcourir_entreprise(self):
        ''' Affiche une fenetre présentant les entreprises et les studios et/ou chaînes qu'ils possèdent '''
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        tkinter.Label(top_level, text='Entreprise', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=0, padx=10, pady=10)
        tkinter.Label(top_level, text='Studios', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=1, padx=10, pady=10)
        tkinter.Label(top_level, text='Chaînes', font=self.fontStyle, relief=tkinter.RAISED).grid(row=0, column=2, padx=10, pady=10)
        
        self.cur.execute('select nom, id_entreprise from entreprise order by nom')
        requete=self.cur.fetchall()
        
        new_fontStyle = font.Font(family="Times", size=10)
        
        cpt=0
        lig=1
        col=0
        for i in range(len(requete)):
            if (cpt>4):
                cpt=0
                lig=1
                col+=3
                for j in range(20):
                    tkinter.Label(top_level, text='|', font=new_fontStyle).grid(row=lig+j, column=col, padx=10, pady=10)
                lig=1-i
                col+=1
            
            tkinter.Label(top_level, text=requete[i][0], font=new_fontStyle).grid(row=i+lig, column=col, padx=10, pady=10)
            lig+=1
            
            lig_chaine=lig
            
            self.cur.execute('select nom from studio where id_entreprise=\''+str(requete[i][1])+'\' order by nom')
            requete_studio=self.cur.fetchall()
            for j in range(len(requete_studio)):
                tkinter.Label(top_level, text=requete_studio[j][0], font=new_fontStyle).grid(row=i+lig, column=col+1, padx=10, pady=10)
                lig+=1
            
            self.cur.execute('select nom from chaine where id_entreprise=\''+str(requete[i][1])+'\' order by nom')
            requete_chaine=self.cur.fetchall()
            for j in range(len(requete_chaine)):
                tkinter.Label(top_level, text=requete_chaine[j][0], font=new_fontStyle).grid(row=i+lig_chaine, column=col+2, padx=10, pady=10)
                lig_chaine+=1
            
            lig=max(lig, lig_chaine)
            
            tkinter.Label(top_level, text='_______________', font=new_fontStyle).grid(row=i+lig, column=col, padx=10, pady=10)
            tkinter.Label(top_level, text='_______________', font=new_fontStyle).grid(row=i+lig, column=col+1, padx=10, pady=10)
            tkinter.Label(top_level, text='_______________', font=new_fontStyle).grid(row=i+lig, column=col+2, padx=10, pady=10)
            
            lig+=1
            cpt+=1
            
    
    
    
    def modification_utilisateur(self): 
        ''' Affiche une fenetre permettant de gérer l'ajout ou la suppression d'utilisateur dans la base de données '''
        
        def ajout():
            ''' Gère le cas où l'on souhaite ajouter un profil utilisateur '''
            
            def get_formulaire():
                ''' Récupère les informations entrées dans le formulaire pour les ajouter dans la base de données '''
                
                self.cur.execute('select * from utilisateur where nom=\''+entry_nom.get()+'\' and prenom=\''+entry_prenom.get()+'\' and date_naiss=\''+entry_date_naiss.get()+'\' and nationalite=\''+entry_nationalite.get()+'\'')
                if (self.cur.fetchall()==[]):
                    try:
                        valeurs=''
                        if (entry_nom.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_nom.get()+'\', '
                        if (entry_prenom.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_prenom.get()+'\', '
                        valeurs+='\''+entry_date_naiss.get()+'\', '
                        if (entry_nationalite.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_nationalite.get()+'\''
                            
                        self.cur.execute('insert into utilisateur(nom, prenom, date_naiss, nationalite) values('+valeurs+')')
                
                    except sqlite3.Error :
                        messagebox.showwarning('Erreur', 'Attention données invalides !')
                
                    else:
                        
                        self.cur.execute('select max(id_utilisateur) from utilisateur')
                        requete=self.cur.fetchall()
                        
                        btn=tkinter.Button(self.frame3, text='User '+str(requete[0][0]), command=self.creer_recommandation(requete[0][0]), font=self.fontStyle)
                        btn.pack(padx=5, pady=5)
                        self.liste_boutons_utilisateurs.append(btn)
                else:
                    messagebox.showwarning('Erreur', 'Attention cet utilisateur existe déjà !')
            
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Ajout d\'utilisateur')  
            
            tkinter.Label(top_level2, text = "Nom :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_nom=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_nom.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Prenom :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_prenom=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_prenom.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Date de naissance :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_date_naiss=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_date_naiss.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Nationalité :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_nationalite=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_nationalite.pack(padx=20, pady=10)
            
            tkinter.Button(top_level2 ,text="Ajout", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
            
        
        def suppression():
            ''' Gère le cas où l'on souhaite supprimer un profil utilisateur '''
            
            def get_formulaire():
                ''' Récupère les informations entrées dans le formulaire pour savoir l'utilisateur à supprimer de la base de données '''
                
                nom=var_utilisateur.get()
                if (nom=='-'):
                    messagebox.showwarning('Erreur', 'Attention il n\'y a pas d\'utilisateur à supprimer !')
                else:
                    for i in range(len(nom)):
                        if (nom[i]==' '):
                            valeur_nom=nom[0:i]
                            valeur_prenom=nom[i+1:]
                    
                    self.cur.execute('select id_utilisateur from utilisateur where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\'')
                    requete=self.cur.fetchall()
                    self.liste_boutons_utilisateurs[requete[0][0]-1].destroy()
                            
                    self.cur.execute('delete from utilisateur where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\'')
                
                    
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Suppression d\'utilisateur')
            
            self.cur.execute('select nom, prenom from utilisateur')
            requete_utilisateur=self.cur.fetchall()
            
            utilisateurs=[]
            
            if (len(requete_utilisateur)==0):
                utilisateurs=['-']
            else:
                for i in range(len(requete_utilisateur)):
                    utilisateurs+=[requete_utilisateur[i][0]+' '+requete_utilisateur[i][1]]
                
            var_utilisateur=tkinter.StringVar()
            var_utilisateur.set('Utilisateur ')
            
            choix_utilisateur = tkinter.OptionMenu(top_level2, var_utilisateur, *utilisateurs)
            choix_utilisateur.configure(font=self.fontStyle)
            choix_utilisateur.pack(padx=20, pady=10)
            
            tkinter.Button(top_level2, text="Suppression", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
        
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame_choix, text="Utilisateurs", font=self.fontStyle).pack(padx=20, pady=10)
        
        tkinter.Button(frame_choix, text='Ajout', command=ajout, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Suppression', command=suppression, font=self.fontStyle).pack(padx=20, pady=5)
        
        frame_choix.pack(padx=10, pady=10)


    

    def modification_visionnage(self):
        ''' Affiche une fenetre permettant de gérer l'ajout d'un visionnage dans la base de données '''
        
        def get_formulaire():
            ''' Récupère les informations entrées dans le formulaire pour les ajouter dans la base de données '''
            
            nom=var_utilisateur.get()
            for i in range(len(nom)):
                if (nom[i]==' '):
                    valeur_nom=nom[0:i]
                    valeur_prenom=nom[i+1:]
            
            self.cur.execute('select * from voir natural join utilisateur natural join oeuvre where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\' and titre=\''+var_oeuvre.get()+'\'')
            if (self.cur.fetchall()==[]):
                try:
                    valeurs=''
                    if (valeur_nom=='Utilisateur'):
                        valeurs+='NULL, '
                    else:
                        self.cur.execute('select id_utilisateur from utilisateur where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\'')
                        new_requete=self.cur.fetchall()
                        valeurs+=str(new_requete[0][0])+', '
                    if (var_oeuvre.get()=='Oeuvre'):
                        valeurs+='NULL, '
                    else:
                        self.cur.execute('select id_oeuvre from oeuvre where titre=\''+var_oeuvre.get()+'\'')
                        new_requete=self.cur.fetchall()
                        valeurs+=str(new_requete[0][0])+', '
                    if (entry_note.get()==''):
                        valeurs+='NULL, '
                    else:
                        valeurs+=str(entry_note.get())
                        
                    self.cur.execute('insert into voir(id_utilisateur, id_oeuvre, note) values('+valeurs+')')
            
                except sqlite3.Error :
                    messagebox.showwarning('Erreur', 'Attention données invalides !')
                    
            else:
                messagebox.showwarning('Erreur', 'Attention cet utilisateur a déjà vu ce film !')
            
        
        
        top_level=tkinter.Toplevel(self.fenetre)
        top_level.title('Ajout de visionnage')  
        
        
        
        self.cur.execute('select nom, prenom from utilisateur')
        requete_utilisateur=self.cur.fetchall()
        
        utilisateurs=[]
        for i in range(len(requete_utilisateur)):
            utilisateurs+=[requete_utilisateur[i][0]+' '+requete_utilisateur[i][1]]
        
        var_utilisateur=tkinter.StringVar()
        var_utilisateur.set('Utilisateur ')
        
        choix_utilisateur = tkinter.OptionMenu(top_level, var_utilisateur, *utilisateurs)
        choix_utilisateur.configure(font=self.fontStyle)
        choix_utilisateur.pack(padx=20, pady=10)
        
        
        
        self.cur.execute('select titre from oeuvre order by titre')
        requete_oeuvre=self.cur.fetchall()
        
        oeuvres=[]
        for i in range(len(requete_oeuvre)):
            oeuvres+=[requete_oeuvre[i][0]]
        
        var_oeuvre=tkinter.StringVar()
        var_oeuvre.set('Oeuvre')
        
        choix_oeuvre = tkinter.OptionMenu(top_level, var_oeuvre, *oeuvres)
        choix_oeuvre.configure(font=self.fontStyle)
        choix_oeuvre.pack(padx=20, pady=10)
        
        
        
        tkinter.Label(top_level, text = "Note :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
        entry_note=tkinter.Entry(top_level, font=self.fontStyle, relief=tkinter.RIDGE)
        entry_note.pack(padx=20, pady=10)
        
        tkinter.Button(top_level, text="Ajout", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
        
    
    
    
    def modification_oeuvre(self): 
        ''' Affiche une fenetre permettant de gérer l'ajout ou la suppression d'oeuvre dans la base de données '''
        
        def ajout():
            ''' Gère le cas où l'on souhaite ajouter une oeuvre de la base de données '''
            
            def get_formulaire():
                ''' Récupère les informations entrées dans le formulaire pour les ajouter dans la base de données '''
                
                if (var_f_s.get()=='Film'):
                    
                    nom=var_realisateur.get()
                    if (nom=='Autre'):
                        valeur_nom='Doe'
                        valeur_prenom='John'
                    else:
                        for i in range(len(nom)):
                            if (nom[i]==' '):
                                valeur_nom=nom[0:i]
                                valeur_prenom=nom[i+1:]
                
                    self.cur.execute('select * from realisateur where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\'')
                    requete=self.cur.fetchall()
                    if (requete==[]):
                        self.cur.execute('select max(id_realisateur) from realisateur')
                        requete=self.cur.fetchall()
                        id_realisateur=requete[0][0]+1
                    else:
                        id_realisateur=requete[0][0]
                        
            
                    self.cur.execute('select * from oeuvre natural join film where titre=\''+entry_titre.get()+'\' and id_realisateur='+str(id_realisateur))
                    if (self.cur.fetchall()==[]):
                        try:
                            
                            valeurs_oeuvre=''
                            if (entry_titre.get()==''):
                                valeurs_oeuvre+='NULL, '
                            else:
                                valeurs_oeuvre+='\''+entry_titre.get()+'\', '
                                
                            if (entry_date_sortie.get()==''):
                                valeurs_oeuvre+='NULL, '
                            else:
                                valeurs_oeuvre+='\''+entry_date_sortie.get()+'\', '
                            
                            if (entry_score.get()==''):
                                valeurs_oeuvre+='NULL, '
                            else:
                                valeurs_oeuvre+=str(entry_score.get())+', '
                            
                            if (var_recompense.get()=='Oui'):
                                valeurs_oeuvre+='1, '
                            else:
                                valeurs_oeuvre+='0, '
                            
                            if (entry_categorie.get()==''):
                                valeurs_oeuvre+='NULL, '
                            else:
                                valeurs_oeuvre+='\''+entry_categorie.get()+'\', '
                            
                            valeurs_oeuvre+=str(id_realisateur)
                            
                            self.cur.execute('insert into oeuvre(titre, date_sortie, score, recompense, categorie, id_realisateur) values('+valeurs_oeuvre+')')
                
                
                
                            valeurs_film=''
                            if (entry_duree.get()==''):
                                valeurs_film+='NULL, '
                            else:
                                valeurs_film+='\''+entry_duree.get()+'\', '
                                
                            if (entry_budget.get()==''):
                                valeurs_film+='NULL, '
                            else:
                                valeurs_film+=str(entry_budget.get())+', '
                            
                            if (entry_box_office.get()==''):
                                valeurs_film+='NULL, '
                            else:
                                valeurs_film+=str(entry_box_office.get())+', '
                            
                            self.cur.execute('select max(id_oeuvre) from oeuvre')
                            requete=self.cur.fetchall()
                            valeurs_film+=str(requete[0][0])+', '
                            
                            if (var_studio.get()=='Autre' or var_studio.get()=='Studio (Si film) :'):
                                valeurs_film+='NULL'
                            else:
                                self.cur.execute('select id_studio from studio where nom=\''+var_studio.get()+'\'')
                                requete=self.cur.fetchall()
                                valeurs_film+=str(requete[0][0])
                            
                            self.cur.execute('insert into film(duree, budget, box_office, id_oeuvre, id_studio) values('+valeurs_film+')')
                            
                
                        except sqlite3.Error :
                            self.cur.execute('delete from oeuvre where titre=\''+entry_titre.get()+'\' and id_realisateur='+str(id_realisateur))
                            messagebox.showwarning('Erreur', 'Attention données invalides !')
                    
                    else:
                        messagebox.showwarning('Erreur', 'Attention film déjà dans la base de données !')
                    
                    
                    
                
                elif (var_f_s.get()=='Serie'):
                    
                    nom=var_realisateur.get()
                    if (nom=='Autre'):
                        valeur_nom=' '
                        valeur_prenom=' '
                    else:
                        for i in range(len(nom)):
                            if (nom[i]==' '):
                                valeur_nom=nom[0:i]
                                valeur_prenom=nom[i+1:]
                
                    self.cur.execute('select * from realisateur where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\'')
                    requete=self.cur.fetchall()
                    if (requete==[]):
                        self.cur.execute('select max(id_realisateur) from realisateur')
                        requete=self.cur.fetchall()
                        id_realisateur=requete[0][0]+1
                    else:
                        id_realisateur=requete[0][0]
                        
            
                    self.cur.execute('select * from oeuvre natural join serie where titre=\''+entry_titre.get()+'\' and id_realisateur='+str(id_realisateur))
                    if (self.cur.fetchall()==[]):
                        try:
                            
                            valeurs_oeuvre=''
                            if (entry_titre.get()==''):
                                valeurs_oeuvre+='NULL, '
                            else:
                                valeurs_oeuvre+='\''+entry_titre.get()+'\', '
                                
                            if (entry_date_sortie.get()==''):
                                valeurs_oeuvre+='NULL, '
                            else:
                                valeurs_oeuvre+='\''+entry_date_sortie.get()+'\', '
                            
                            if (entry_score.get()==''):
                                valeurs_oeuvre+='NULL, '
                            else:
                                valeurs_oeuvre+=str(entry_score.get())+', '
                            
                            if (var_recompense.get()=='Oui'):
                                valeurs_oeuvre+='1, '
                            else:
                                valeurs_oeuvre+='0, '
                            
                            if (entry_categorie.get()==''):
                                valeurs_oeuvre+='NULL, '
                            else:
                                valeurs_oeuvre+='\''+entry_categorie.get()+'\', '
                            
                            valeurs_oeuvre+=str(id_realisateur)
                            
                            self.cur.execute('insert into oeuvre(titre, date_sortie, score, recompense, categorie, id_realisateur) values('+valeurs_oeuvre+')')
                
                
                
                            valeurs_serie=''
                            if (entry_saisons.get()==''):
                                valeurs_serie+='NULL, '
                            else:
                                valeurs_serie+='\''+entry_saisons.get()+'\', '
                                
                            if (entry_episodes.get()==''):
                                valeurs_serie+='NULL, '
                            else:
                                valeurs_serie+='\''+entry_episodes.get()+'\', '
                                
                            if (entry_duree.get()==''):
                                valeurs_serie+='NULL, '
                            else:
                                valeurs_serie+='\''+entry_duree.get()+'\', '
                            
                            self.cur.execute('select max(id_oeuvre) from oeuvre')
                            requete=self.cur.fetchall()
                            valeurs_serie+=str(requete[0][0])+', '
                            
                            if (var_chaine.get()=='Autre' or var_chaine.get()=='Chaine (Si série) :'):
                                valeurs_serie+='NULL'
                            else:
                                self.cur.execute('select id_chaine from chaine where nom=\''+var_chaine.get()+'\'')
                                requete=self.cur.fetchall()
                                valeurs_serie+=str(requete[0][0])
                            
                            self.cur.execute('insert into serie(nb_saisons, nb_episodes, duree_episode, id_oeuvre, id_chaine) values('+valeurs_serie+')')
                            
                
                        except sqlite3.Error :
                            self.cur.execute('delete from oeuvre where titre=\''+entry_titre.get()+'\' and id_realisateur='+str(id_realisateur))
                            messagebox.showwarning('Erreur', 'Attention données invalides !')
                    
                    else:
                        messagebox.showwarning('Erreur', 'Attention série déjà dans la base de données !')
                
                
            
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Ajout d\'oeuvre')  
            
            
        
            frame_choix2 = tkinter.Frame(top_level2, borderwidth=2)
        
            
            film_serie=['Film', 'Serie']
            var_f_s=tkinter.StringVar()
            var_f_s.set('Film ou Série ?')
            choix_f_s = tkinter.OptionMenu(frame_choix2, var_f_s, *film_serie)
            choix_f_s.configure(font=self.fontStyle)
            choix_f_s.pack(padx=20, pady=10)
            
            tkinter.Label(frame_choix2, text = "Titre :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_titre=tkinter.Entry(frame_choix2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_titre.pack(padx=20, pady=10)
            
            tkinter.Label(frame_choix2, text = "Date de sortie :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_date_sortie=tkinter.Entry(frame_choix2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_date_sortie.pack(padx=20, pady=10)
            
            tkinter.Label(frame_choix2, text = "Score :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_score=tkinter.Entry(frame_choix2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_score.pack(padx=20, pady=10)
        
            true_false=['Oui', 'Non']
            var_recompense=tkinter.StringVar()
            var_recompense.set('Recompense')
            choix_recompense = tkinter.OptionMenu(frame_choix2, var_recompense, *true_false)
            choix_recompense.configure(font=self.fontStyle)
            choix_recompense.pack(padx=20, pady=10)
            
            tkinter.Label(frame_choix2, text = "Catégorie :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_categorie=tkinter.Entry(frame_choix2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_categorie.pack(padx=20, pady=10)
            
            tkinter.Label(frame_choix2, text = "Durée :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_duree=tkinter.Entry(frame_choix2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_duree.pack(padx=20, pady=10)
            
            self.cur.execute('select nom, prenom from realisateur order by nom')
            requete_realisateur=self.cur.fetchall()
            realisateurs=[]
            for i in range(len(requete_realisateur)):
                realisateurs+=[requete_realisateur[i][0]+' '+requete_realisateur[i][1]]
            realisateurs+=['Autre']
            var_realisateur=tkinter.StringVar()
            var_realisateur.set('Realisateur ')
            choix_realisateur = tkinter.OptionMenu(frame_choix2, var_realisateur, *realisateurs)
            choix_realisateur.configure(font=self.fontStyle)
            choix_realisateur.pack(padx=20, pady=10)
            
            
            frame_choix2.pack(side=tkinter.LEFT, padx=10, pady=10)
            
            
            frame_choix3 = tkinter.Frame(top_level2, borderwidth=2)
            
            
            tkinter.Label(frame_choix3, text = "Budget (Si film) :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_budget=tkinter.Entry(frame_choix3, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_budget.pack(padx=20, pady=10)
            
            tkinter.Label(frame_choix3, text = "Box-Office (Si film) :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_box_office=tkinter.Entry(frame_choix3, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_box_office.pack(padx=20, pady=10)
            
            self.cur.execute('select nom from studio order by nom')
            requete_studio=self.cur.fetchall()
            studios=[]
            for i in range(len(requete_studio)):
                studios+=[requete_studio[i][0]]
            studios+=['Autre']
            var_studio=tkinter.StringVar()
            var_studio.set('Studio (Si film) :')
            choix_studio = tkinter.OptionMenu(frame_choix3, var_studio, *studios)
            choix_studio.configure(font=self.fontStyle)
            choix_studio.pack(padx=20, pady=10)
            
            tkinter.Label(frame_choix3, text = "Nombre de saisons (Si série) :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_saisons=tkinter.Entry(frame_choix3, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_saisons.pack(padx=20, pady=10)
            
            tkinter.Label(frame_choix3, text = "Nombre d'épisodes (Si série) :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_episodes=tkinter.Entry(frame_choix3, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_episodes.pack(padx=20, pady=10)
            
            self.cur.execute('select nom from chaine order by nom')
            requete_chaine=self.cur.fetchall()
            chaines=[]
            for i in range(len(requete_chaine)):
                chaines+=[requete_chaine[i][0]]
            chaines+=['Autre']
            var_chaine=tkinter.StringVar()
            var_chaine.set('Chaine (Si série) :')
            choix_chaine = tkinter.OptionMenu(frame_choix3, var_chaine, *chaines)
            choix_chaine.configure(font=self.fontStyle)
            choix_chaine.pack(padx=20, pady=10)
            
            tkinter.Button(top_level2 ,text="Ajout", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
            
            
            frame_choix3.pack(side=tkinter.RIGHT, padx=10, pady=10)
            
            
            
            
            
        def suppression():
            ''' Gère le cas où l'on souhaite supprimer une oeuvre de la base de données '''
            
            def get_formulaire():
                ''' Récupère les informations entrées dans le formulaire pour savoir l'oeuvre à supprimer de la base de données '''
                
                titre=var_oeuvre.get()
                if (titre=='-'):
                    messagebox.showwarning('Erreur', 'Attention il n\'y a pas d\'oeuvre à supprimer !')
                elif (titre=='Oeuvre '):
                    messagebox.showwarning('Erreur', 'Attention il n\'y a pas d\'oeuvre selectionnée !')
                else:
                    for i in range(len(titre)):
                        if (titre[i]==' '):
                            valeur_titre=titre[0:i]
                            valeur_real=titre[i+1:]
                    self.cur.execute('delete from oeuvre where titre=\''+valeur_titre+'\' and id_realisateur=(select id_realisateur from oeuvre natural join realisateur where titre=\''+valeur_titre+'\' and nom=\''+valeur_real+'\')')
                    
                    
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Suppression d\'oeuvre')
            
            self.cur.execute('select titre, nom from oeuvre natural join realisateur order by titre')
            requete_oeuvres=self.cur.fetchall()
            
            oeuvres=[]
            
            if (len(requete_oeuvres)==0):
                oeuvres=['-']
            else:
                for i in range(len(requete_oeuvres)):
                    oeuvres+=[requete_oeuvres[i][0]+' '+requete_oeuvres[i][1]]
                
            var_oeuvre=tkinter.StringVar()
            var_oeuvre.set('Oeuvre ')
            
            choix_oeuvre = tkinter.OptionMenu(top_level2, var_oeuvre, *oeuvres)
            choix_oeuvre.configure(font=self.fontStyle)
            choix_oeuvre.pack(padx=20, pady=10)
            
            tkinter.Button(top_level2, text="Suppression", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
        
        
        
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame_choix, text="Oeuvres", font=self.fontStyle).pack(padx=20, pady=10)
        
        tkinter.Button(frame_choix, text='Ajout', command=ajout, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Suppression', command=suppression, font=self.fontStyle).pack(padx=20, pady=5)
        
        frame_choix.pack(padx=10, pady=10)
        
        
        
        
        
    def modification_acteur(self): 
        ''' Affiche une fenetre permettant de gérer l'ajout ou la suppression d'acteur dans la base de données '''
        
        def ajout():
            ''' Gère le cas où l'on souhaite ajouter un acteur '''
            
            def get_formulaire():
                ''' Récupère les informations entrées dans le formulaire pour les ajouter dans la base de données '''
                
                self.cur.execute('select * from acteur where nom=\''+entry_nom.get()+'\' and prenom=\''+entry_prenom.get()+'\' and date_naiss=\''+entry_date_naiss.get()+'\' and nationalite=\''+entry_nationalite.get()+'\'')
                if (self.cur.fetchall()==[]):
                    try:
                        valeurs=''
                        if (entry_nom.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_nom.get()+'\', '
                        if (entry_prenom.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_prenom.get()+'\', '
                        valeurs+='\''+entry_date_naiss.get()+'\', '
                        if (entry_nationalite.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_nationalite.get()+'\''
                            
                        self.cur.execute('insert into acteur(nom, prenom, date_naiss, nationalite) values('+valeurs+')')
                
                    except sqlite3.Error :
                        messagebox.showwarning('Erreur', 'Attention données invalides !')
                        
                else:
                    messagebox.showwarning('Erreur', 'Attention cet acteur est déjà dans la base de données !')
                
            
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Ajout d\'acteur')  
            
            tkinter.Label(top_level2, text = "Nom :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_nom=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_nom.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Prenom :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_prenom=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_prenom.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Date de naissance :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_date_naiss=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_date_naiss.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Nationalité :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_nationalite=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_nationalite.pack(padx=20, pady=10)
            
            tkinter.Button(top_level2 ,text="Ajout", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
            
        
        def suppression():
            ''' Gère le cas où l'on souhaite supprimer un acteur '''
            
            def get_formulaire():
                ''' Récupère les informations entrées dans le formulaire pour savoir l'acteur à supprimer de la base de données '''
                
                nom=var_acteur.get()
                if (nom=='-'):
                    messagebox.showwarning('Erreur', 'Attention il n\'y a pas d\'acteur à supprimer !')
                else:
                    for i in range(len(nom)):
                        if (nom[i]==' '):
                            valeur_nom=nom[0:i]
                            valeur_prenom=nom[i+1:]
                            
                    self.cur.execute('delete from acteur where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\'')
                
                    
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Suppression d\'acteur')
            
            self.cur.execute('select nom, prenom from acteur')
            requete_acteur=self.cur.fetchall()
            
            acteurs=[]
            
            if (len(requete_acteur)==0):
                acteurs=['-']
            else:
                for i in range(len(requete_acteur)):
                    acteurs+=[requete_acteur[i][0]+' '+requete_acteur[i][1]]
                
            var_acteur=tkinter.StringVar()
            var_acteur.set('Acteur ')
            
            choix_acteur = tkinter.OptionMenu(top_level2, var_acteur, *acteurs)
            choix_acteur.configure(font=self.fontStyle)
            choix_acteur.pack(padx=20, pady=10)
            
            tkinter.Button(top_level2, text="Suppression", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
        
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame_choix, text="Acteurs", font=self.fontStyle).pack(padx=20, pady=10)
        
        tkinter.Button(frame_choix, text='Ajout', command=ajout, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Suppression', command=suppression, font=self.fontStyle).pack(padx=20, pady=5)
        
        frame_choix.pack(padx=10, pady=10)
        
        
        
        
        
    def modification_jouer(self):
        ''' Affiche une fenetre permettant d'indiquer à la base de données qu'un acteur a joué dans une oeuvre '''
        
        def get_formulaire():
            ''' Récupère les informations entrées dans le formulaire pour les ajouter dans la base de données '''
            
            nom=var_acteur.get()
            for i in range(len(nom)):
                if (nom[i]==' '):
                    valeur_nom=nom[0:i]
                    valeur_prenom=nom[i+1:]
            
            self.cur.execute('select * from jouer natural join acteur natural join oeuvre where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\' and titre=\''+var_oeuvre.get()+'\'')
            if (self.cur.fetchall()==[]):
                try:
                    valeurs=''
                    if (valeur_nom=='Acteur'):
                        valeurs+='NULL, '
                    else:
                        self.cur.execute('select id_acteur from acteur where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\'')
                        new_requete=self.cur.fetchall()
                        valeurs+=str(new_requete[0][0])+', '
                    if (var_oeuvre.get()=='Oeuvre'):
                        valeurs+='NULL, '
                    else:
                        self.cur.execute('select id_oeuvre from oeuvre where titre=\''+var_oeuvre.get()+'\'')
                        new_requete=self.cur.fetchall()
                        valeurs+=str(new_requete[0][0])+', '
                    if (var_role.get()=='Role'):
                        valeurs+='NULL, '
                    else:
                        valeurs+='\''+var_role.get()+'\', '
                    if (var_recompense.get()=='Oui'):
                        valeurs+='1'
                    else:
                        valeurs+='0'
                        
                        
                    self.cur.execute('insert into jouer(id_acteur, id_oeuvre, role, recompense) values('+valeurs+')')
            
                except sqlite3.Error :
                    messagebox.showwarning('Erreur', 'Attention données invalides !')
                    
            else:
                messagebox.showwarning('Erreur', 'Attention cet acteur a déjà joué dans ce film !')
            
            
        
        
        top_level=tkinter.Toplevel(self.fenetre)
        top_level.title('Quel acteur a joué dans quel film ?')  
                        
            
        self.cur.execute('select nom, prenom from acteur order by nom')
        requete_acteur=self.cur.fetchall()
        
        acteurs=[]
        for i in range(len(requete_acteur)):
            acteurs+=[requete_acteur[i][0]+' '+requete_acteur[i][1]]
        
        var_acteur=tkinter.StringVar()
        var_acteur.set('Acteur ')
        
        choix_acteur = tkinter.OptionMenu(top_level, var_acteur, *acteurs)
        choix_acteur.configure(font=self.fontStyle)
        choix_acteur.pack(padx=20, pady=10)
        
        
        
        self.cur.execute('select titre from oeuvre order by titre')
        requete_oeuvre=self.cur.fetchall()
        
        oeuvres=[]
        for i in range(len(requete_oeuvre)):
            oeuvres+=[requete_oeuvre[i][0]]
        
        var_oeuvre=tkinter.StringVar()
        var_oeuvre.set('Oeuvre')
        
        choix_oeuvre = tkinter.OptionMenu(top_level, var_oeuvre, *oeuvres)
        choix_oeuvre.configure(font=self.fontStyle)
        choix_oeuvre.pack(padx=20, pady=10)
        
        
        
        roles=['first', 'second', 'antagonist']
        
        var_role=tkinter.StringVar()
        var_role.set('Role')
        
        choix_role = tkinter.OptionMenu(top_level, var_role, *roles)
        choix_role.configure(font=self.fontStyle)
        choix_role.pack(padx=20, pady=10)
        
        
        
        recompenses=['Oui', 'Non']
        
        var_recompense=tkinter.StringVar()
        var_recompense.set('Recompensé')
        
        choix_recompense = tkinter.OptionMenu(top_level, var_recompense, *recompenses)
        choix_recompense.configure(font=self.fontStyle)
        choix_recompense.pack(padx=20, pady=10)
        
        
        
        tkinter.Button(top_level, text="Ajout", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
    
    
    
    
    
    def modification_realisateur(self): 
        ''' Affiche une fenetre permettant de gérer l'ajout ou la suppression de réalisateur dans la base de données '''
        
        def ajout():
            ''' Gère le cas où l'on souhaite ajouter un réalisateur '''
            
            def get_formulaire():
                ''' Récupère les informations entrées dans le formulaire pour les ajouter dans la base de données '''
                
                self.cur.execute('select * from realisateur where nom=\''+entry_nom.get()+'\' and prenom=\''+entry_prenom.get()+'\' and date_naiss=\''+entry_date_naiss.get()+'\' and nationalite=\''+entry_nationalite.get()+'\'')
                if (self.cur.fetchall()==[]):
                    try:
                        valeurs=''
                        if (entry_nom.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_nom.get()+'\', '
                        if (entry_prenom.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_prenom.get()+'\', '
                        valeurs+='\''+entry_date_naiss.get()+'\', '
                        if (entry_nationalite.get()==''):
                            valeurs+='NULL, '
                        else:
                            valeurs+='\''+entry_nationalite.get()+'\', '
                        if (var_recompense.get()=='Oui'):
                            valeurs+='1'
                        else:
                            valeurs+='0'
                            
                        self.cur.execute('insert into realisateur(nom, prenom, date_naiss, nationalite, recompense) values('+valeurs+')')
                
                    except sqlite3.Error :
                        messagebox.showwarning('Erreur', 'Attention données invalides !')
                        
                else:
                    messagebox.showwarning('Erreur', 'Attention ce réalisateur est déjà dans la base de données !')
                
            
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Ajout de réalisateur')  
            
            tkinter.Label(top_level2, text = "Nom :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_nom=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_nom.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Prenom :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_prenom=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_prenom.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Date de naissance :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_date_naiss=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_date_naiss.pack(padx=20, pady=10)
            
            tkinter.Label(top_level2, text = "Nationalité :", font=self.fontStyle, relief=tkinter.RIDGE).pack(padx=20, pady=10)
            entry_nationalite=tkinter.Entry(top_level2, font=self.fontStyle, relief=tkinter.RIDGE)
            entry_nationalite.pack(padx=20, pady=10)
            
            recompenses=['Oui', 'Non']
            var_recompense=tkinter.StringVar()
            var_recompense.set('Recompensé')
            choix_recompense = tkinter.OptionMenu(top_level2, var_recompense, *recompenses)
            choix_recompense.configure(font=self.fontStyle)
            choix_recompense.pack(padx=20, pady=10)
            
            tkinter.Button(top_level2 ,text="Ajout", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
            
        
        def suppression():
            ''' Gère le cas où l'on souhaite supprimer un réalisateur '''
            
            def get_formulaire():
                ''' Récupère les informations entrées dans le formulaire pour savoir l'acteur à supprimer de la base de données '''
                
                nom=var_realisateur.get()
                if (nom=='-'):
                    messagebox.showwarning('Erreur', 'Attention il n\'y a pas de realisateur à supprimer !')
                else:
                    for i in range(len(nom)):
                        if (nom[i]==' '):
                            valeur_nom=nom[0:i]
                            valeur_prenom=nom[i+1:]
                            
                    self.cur.execute('delete from realisateur where nom=\''+valeur_nom+'\' and prenom=\''+valeur_prenom+'\'')
                                    
                    
            
            top_level2=tkinter.Toplevel(self.fenetre)
            top_level2.title('Suppression de réalisateur')
            
            self.cur.execute('select nom, prenom from realisateur order by nom')
            requete_realisateur=self.cur.fetchall()
            
            realisateurs=[]
            
            if (len(requete_realisateur)==0):
                realisateurs=['-']
            else:
                for i in range(len(requete_realisateur)):
                    realisateurs+=[requete_realisateur[i][0]+' '+requete_realisateur[i][1]]
                
            var_realisateur=tkinter.StringVar()
            var_realisateur.set('Réalisateur ')
            
            choix_realisateur = tkinter.OptionMenu(top_level2, var_realisateur, *realisateurs)
            choix_realisateur.configure(font=self.fontStyle)
            choix_realisateur.pack(padx=20, pady=10)
            
            tkinter.Button(top_level2, text="Suppression", command=get_formulaire, font=self.fontStyle, relief=tkinter.RAISED).pack(padx=20, pady=10)
        
        
        top_level=tkinter.Toplevel(self.fenetre)
        
        frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
        tkinter.Label(frame_choix, text="Réalisateurs", font=self.fontStyle).pack(padx=20, pady=10)
        
        tkinter.Button(frame_choix, text='Ajout', command=ajout, font=self.fontStyle).pack(padx=20, pady=5)
        tkinter.Button(frame_choix, text='Suppression', command=suppression, font=self.fontStyle).pack(padx=20, pady=5)
        
        frame_choix.pack(padx=10, pady=10)
    
    
    
    
    
    def creer_recommandation(self, id_utilisateur):
        
        def commande_recommandation():
            ''' Fonction qui affiche une fenêtre de recommandation pour l'utilisateur avec l'id en paramètre '''
            
            def gout():
                ''' Affiche les oeuvres aimées par l'utilisateur '''
            
                top_level2=tkinter.Toplevel(self.fenetre)
                top_level2.title('Oeuvres vues')    
                
                self.cur.execute('select titre, note from utilisateur natural join voir natural join oeuvre where id_utilisateur='+str(id_utilisateur)+' order by note desc')
                requete=self.cur.fetchall()
                
                cpt=0
                lig=0
                col=0
                for i in range(len(requete)):
                    if (cpt%15==0):
                        lig=0
                        col+=1
                    tkinter.Label(top_level2, text=requete[i][0], font=self.fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                    tkinter.Label(top_level2, text=requete[i][1], font=self.fontStyle).grid(row=lig, column=col+1, padx=10, pady=10)
                    lig+=1
                    cpt+=1
                    
                    
            def recommandation():
                ''' Affiche les oeuvres recommandées pour l'utilisateur selon ses gouts '''
                
                top_level2=tkinter.Toplevel(self.fenetre)
                top_level2.title('Oeuvres recommandées') 
                
                commande='select titre from oeuvre where categorie= ( select categorie from ( select categorie, max(cpt) from ( select categorie, count(*) as cpt from voir natural join oeuvre where id_utilisateur='+str(id_utilisateur)+' and note>=4 group by categorie ) )) ' 
                commande+='union '
                commande+='select titre from oeuvre where id_realisateur= ( select id_realisateur from ( select id_realisateur, max(cpt) from ( select id_realisateur, count(*) as cpt from voir natural join oeuvre where id_utilisateur='+str(id_utilisateur)+' and note>=4 group by id_realisateur ) )) ' 
                commande+='union '
                commande+='select titre from oeuvre natural join jouer where id_acteur= ( select id_acteur from ( select id_acteur, max(cpt) from ( select id_acteur, count(*) as cpt from voir natural join oeuvre natural join jouer where id_utilisateur='+str(id_utilisateur)+' and note>=4 group by id_realisateur ) )) ' 
                commande+='union '
                commande+='select titre from oeuvre natural join film where saga= ( select saga from film natural join oeuvre natural join voir where id_utilisateur='+str(id_utilisateur)+' and note>=4) ' 
                commande+='except ' 
                commande+='select titre from oeuvre natural join voir where id_utilisateur='+str(id_utilisateur)+' '
                
                commande+='order by titre'

                self.cur.execute(commande)
                requete=self.cur.fetchall()
                
                cpt=0
                lig=0
                col=0
                for i in range(len(requete)):
                    if (cpt%15==0):
                        lig=0
                        col+=1
                    tkinter.Label(top_level2, text=requete[i][0], font=self.fontStyle).grid(row=lig, column=col, padx=10, pady=10)
                    lig+=1
                    cpt+=1
                
            
            top_level=tkinter.Toplevel(self.fenetre)
        
            frame_choix = tkinter.Frame(top_level, borderwidth=2, relief=tkinter.GROOVE)
        
            tkinter.Label(frame_choix, text="Utilisateur "+str(id_utilisateur), font=self.fontStyle).pack(padx=20, pady=10)
        
            tkinter.Button(frame_choix, text='Liste oeuvres vues', command=gout, font=self.fontStyle).pack(padx=20, pady=5)
            tkinter.Button(frame_choix, text='Recommandations', command=recommandation, font=self.fontStyle).pack(padx=20, pady=5)
        
            frame_choix.pack(padx=10, pady=10)
        
        return commande_recommandation
    
    
    
    
    
    def quitter(self):
        ''' Méthode qui sauvegarde les données entrées et ferme la connection à la base de données ainsi que toutes les fenetres'''
        
        self.conn.commit()
        self.conn.close()
        
        
        self.fenetre.destroy()


