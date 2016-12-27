$word = "tacos sauce blanche"
$carac = "a"
$resultat = 0
#initialisation de l'index donc index 0
$i = 0

#tant que index inferieur a la longueur du mot cela exectute le code ci-dessous
while $i < $word.length
	#si a l'index ou je me trouve c'est bien un "n" j'incremente de 1
	if $word[$i] == $carac
		$resultat += 1
	end
#et je passe a l'index suivant
$i += 1
end
print "Le nombre de caractereRecherche est : #{$resultat}\r\n"
