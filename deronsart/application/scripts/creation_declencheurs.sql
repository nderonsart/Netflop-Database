create trigger suppression_voir
    after delete on utilisateur for each row
    begin
        delete from voir where id_utilisateur=old.id_utilisateur;

end;


create trigger suppression_jouer
    after delete on acteur
    begin
        delete from jouer where id_acteur=old.id_acteur;

end;


create trigger maj_recompense_oeuvre
    after insert on jouer
    begin
        update oeuvre set recompense=new.recompense where recompense=0 and id_oeuvre=new.id_oeuvre;
end;


create trigger supprime_film_serie
    after delete on oeuvre
    begin
        delete from film where id_oeuvre=old.id_oeuvre;
        delete from serie where id_oeuvre=old.id_oeuvre;
end;    


create trigger realisateur_inconnu
    after delete on realisateur
    begin
        update oeuvre set id_realisateur=0 where id_realisateur=old.id_realisateur;
end;



