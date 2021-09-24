create table acteur(
    id_acteur integer not NULL primary key autoincrement,
    nom varchar(30) not NULL,
    prenom varchar(30) not NULL,
    date_naiss date not NULL check (date_naiss>='1900-01-01' and date_naiss<='2022-01-01' and date_naiss is strftime('%Y-%m-%d', date_naiss)),
    nationalite varchar(30) not NULL
);

create table utilisateur(
    id_utilisateur integer not NULL primary key autoincrement,
    nom varchar(30) not NULL,
    prenom varchar(30) not NULL,
    date_naiss date not NULL check (date_naiss>='1900-01-01' and date_naiss<='2022-01-01' and date_naiss is strftime('%Y-%m-%d', date_naiss)),
    nationalite varchar(30) not NULL
);

create table realisateur(
    id_realisateur integer not NULL primary key autoincrement,
    nom varchar(30) not NULL,
    prenom varchar(30) not NULL,
    date_naiss date not NULL check (date_naiss>='1900-01-01' and date_naiss<='2022-01-01' and date_naiss is strftime('%Y-%m-%d', date_naiss)),
    nationalite varchar(30) not NULL,
    recompense int not NULL check (recompense in (0, 1))
);

create table oeuvre(
    id_oeuvre integer not NULL primary key autoincrement,
    titre varchar(30) not NULL,
    date_sortie date not NULL check (date_sortie>='1900-01-01' and date_sortie<='2022-01-01' and date_sortie is strftime('%Y-%m-%d', date_sortie)),
    score integer not NULL check (score>=1 and score<=5),
    recompense integer not NULL check (recompense in (0, 1)),
    categorie varchar(30) not NULL,
    id_realisateur integer references realisateur(id_realisateur)
);

create table jouer(
    id_acteur integer not NULL references acteur(id_acteur),
    id_oeuvre integer not NULL references oeuvre(id_oeuvre),
    role varchar(10) not NULL check (role in ('first', 'second', 'antagonist')),
    recompense integer not NULL check (recompense in (0, 1)),
    constraint jouer_pk primary key (id_acteur, id_oeuvre)
);

create table voir(
    id_utilisateur integer not NULL references utilisateur(id_utilisateur),
    id_oeuvre integer not NULL references oeuvre(id_oeuvre),
    note integer not NULL check (note>=1 and note<=5),
    constraint voir_pk primary key (id_utilisateur, id_oeuvre)
);

create table entreprise(
    id_entreprise integer not NULL primary key autoincrement,
    nom varchar(30) not NULL,
    directeur varchar(30) not NULL,
    date_creation date not NULL check (date_creation>='1800-01-01' and date_creation<='2022-01-01' and date_creation is strftime('%Y-%m-%d', date_creation)),
    revenus integer not NULL check (revenus>=0),
    nationalite varchar(30) not NULL
);

create table studio(
    id_studio integer not NULL primary key autoincrement,
    nom varchar(30) not NULL,
    id_entreprise integer not NULL references entreprise(id_entreprise)
);

create table chaine(
    id_chaine integer not NULL primary key autoincrement,
    nom varchar(30) not NULL,
    id_entreprise integer not NULL references entreprise(id_entreprise)
);

create table film(
    id_film integer not NULL primary key autoincrement,
    duree integer not NULL check (duree>=1),
    saga varchar(30),
    budget integer not NULL check (budget>=1),
    box_office integer not NULL check (box_office>=1),
    id_oeuvre integer not NULL references oeuvre(id_oeuvre),
    id_studio integer not NULL references studio(id_studio)
);

create table serie(
    id_serie integer not NULL primary key autoincrement,
    nb_saisons integer not NULL check (nb_saisons>=1),
    nb_episodes integer not NULL check (nb_episodes>=1),
    duree_episode integer not NULL check (duree_episode>=1),
    id_oeuvre integer not NULL references oeuvre(id_oeuvre),
    id_chaine integer not NULL references chaine(id_chaine)
);


