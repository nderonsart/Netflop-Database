create view films_netflop as
    
    select titre 
    from oeuvre natural join film natural join studio
    where id_entreprise=1
    
    order by titre
;

create view series_netflop as
    
    select titre 
    from oeuvre natural join serie natural join chaine
    where id_entreprise=1
    
    order by titre
;

create view top_films as
    select titre 
    from film natural join oeuvre
    where score=5
    order by titre
;

create view flop_films as
    select titre 
    from film natural join oeuvre
    where score<=2
    order by titre
;

create view top_series as
    select titre 
    from serie natural join oeuvre
    where score=5
    order by titre
;

create view flop_series as
    select titre 
    from serie natural join oeuvre
    where score<=2
    order by titre
;

create view acteur_recompense_pour as
    select nom, prenom, titre
    from acteur natural join jouer natural join oeuvre
    where jouer.recompense=1
    order by nom
;

create view film_prefere_utilisateurs as
    select titre 
    from oeuvre 
    where id_oeuvre= (
        select id_oeuvre 
        from ( 
            select id_oeuvre, max(cpt) 
            from ( 
                select id_oeuvre, count(*) as cpt 
                from film natural join oeuvre natural join voir 
                where note=5 group by id_oeuvre 
            ) 
        )
    )
; 

create view serie_preferee_utilisateurs as
    select titre 
    from oeuvre 
    where id_oeuvre= (
        select id_oeuvre 
        from ( 
            select id_oeuvre, max(cpt) 
            from ( 
                select id_oeuvre, count(*) as cpt 
                from serie natural join oeuvre natural join voir 
                where note=5 group by id_oeuvre 
            ) 
        )
    )
; 
                

