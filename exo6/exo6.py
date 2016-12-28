#Ce code sert a repeter un mot ou une phrase que l'utilisateur a entrer.
#JesuScript
#beweb

quitter = False
oui = "o"
non = "n"
reponse = ""
flag = False

while quitter == False:
	print("Bienvenue chez le perroquet du capitaine")
	perroquet = raw_input("entrez une phrase ou un mot: ")
	print(str(perroquet))
	flag = True

	while flag == True:
		reponse = raw_input("Voulez vous quitter o/n ?")

		if oui == reponse.lower():
			quitter = True
			flag = False
		elif non == reponse.lower():
			print("non")
			flag = False
		else:
			print("Moi y a na pas comprendre ce que toi vouloir me dire")

