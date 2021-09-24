#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet de base de données : Netflop

@author: Nicolas Deronsart
"""

import os

import sqlite3
import pandas 

import interfaceBD


# Si la base de données a déjà été crée

if (os.path.isfile('netflop_database.db')):
    conn=sqlite3.connect('netflop_database.db')
    cur=conn.cursor()
    
    
#Sinon
else:
    
    # Creation de la base de données
    conn=sqlite3.connect('netflop_database.db')
    cur=conn.cursor()

    ## Ajout des tables
    creation_tables=open('scripts/creation_tables.sql')
    creation_tables=creation_tables.read()
    cur.executescript(creation_tables)

    ## Ajout des vues
    creation_vues=open('scripts/creation_vues.sql')
    creation_vues=creation_vues.read()
    cur.executescript(creation_vues)
    
    ## Ajout des déclencheurs
    creation_declencheurs=open('scripts/creation_declencheurs.sql')
    creation_declencheurs=creation_declencheurs.read()
    cur.executescript(creation_declencheurs)


    ## Ajout des données
    dataframes=['acteur',
                'utilisateur',
                'realisateur',
                'oeuvre',
                'jouer',
                'voir',
                'entreprise',
                'studio',
                'chaine',
                'film',
                'serie']
    for i in range(len(dataframes)):
        data = pandas.read_csv('data/'+dataframes[i]+'.csv')
        data.to_sql(dataframes[i], conn, if_exists='append', index=False)


# Lancement de l'interface

if __name__=='__main__':
    interfaceBD.InterfaceNetflop(conn, cur)
    
    conn.close()


