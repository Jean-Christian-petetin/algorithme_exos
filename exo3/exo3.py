#cette algo trouve une lettre defini dans un mot et affiche le nombre de fois ou la lettre apparait dans le mot.

word = "anticonstitutionnellement"
char = "n"
result = 0
#initialisation de l'index donc index 0
i = 0

#tant que index inferieur a la longueur du mot cela exectute le code ci-dessous
while i < len(word):
	#si a l'index ou je me trouve c'est bien un "n" j'incremente de 1
	if word[i] == char:
		result += 1
	#et je passe a l'index suivant
	i += 1

print( "Le nombre de caractereRecherche est : " + str(result))
