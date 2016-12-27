<?php
$word = "le tacos sauce blance est anticonstitutionnel";
$carac = "t";
$resultat = 0;
#initialisation de l'index donc index 0
$i = 0;

#tant que index inferieur a la longueur du mot cela exectute le code ci-dessous
while($i < strlen($word)){
	#si a l'index ou je me trouve c'est bien un "n" j'incremente de 1
	if($word[$i] == $carac){
		$resultat++;
	}
#et je passe a l'index suivant
$i++;
}
echo "Le nombre de caractereRecherche est : " .$resultat."\r"."\n";
?>
