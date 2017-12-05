#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates

# utilitaire pour ouvrir un file coniguration
"""conf = open('configuration', 'r')
conf = conf.read()
conf = conf.split("\n")
conf = ', '.join(conf)"""

listeglobale = ['00:1A:2B:3C:5E', '00:4A:3B:3C:4B', '00:5A:0B:8C:3C', '00:6A:4B:1C:1C', '00:7A:8B:9C:6F']
listecapteur = open('capteurs','r')
listecapteur = listecapteur.read()
print(listecapteur)
"""listecapteurdict = {}
for line in listecapteur:
	x = line.split(",")
	a = x[0]
	b = x[1]
	listecapteurdict[a]=b

print(listecapteurdict)"""
macorigin = '00:1A:2B:3C:5E'

# utilitaire pour testter si une mac est connue et écrire dans un file filemacteste
f1 = open('filealerte', 'w')
# utilitaire de gestion des dates
date = datetime.datetime.now()
f1.write("[")
for mac in listeglobale:
	if macorigin == mac:
		print('vrai')
		for captor in listecapteur:
			print(captor)
			i = 0
			if captor[i][0] == macorigin:
				print(captor[i][0], captor[i][1])
				i += 1
			#f1.write("'" + macorigin[0] + "'," + macorigin[1] + "'" + ",vrai," + str(date) + ",")
			#f1.write("'" + macorigin[0] + "'," + ",vrai," + str(date) + ",")
			#f1.write("toto")
	# si on ne veut pas écrire le adresse non connue, il faut commenter les lignes else
	"""else:
		print('faux')
		f1.write(mac + ",faux,\n")"""

f1.write("]")
f1.close()