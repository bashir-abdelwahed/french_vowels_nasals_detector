vowels='eyuioaéèêùîàâ'
input_file = 'text'
with open(input_file) as f:
        t=f.read()

#Maybe I need to find another elegant solution for this... because nasal rules is complicated
#for example: confinement: comporte 'on' comme nasale mais 'in' ne l'est pas même pour le 'em' et puis 'en' nasale... donc ce n'est pas facile
#nasals=['en', 'un', 'in', 'im', 'on', 'om', 'an', 'am']
#for n in nasals:
#       t=t.replace(n, '<b>'+n+'</b>')

for v in vowels:
        t=t.replace(v, '<b>'+v+'</b>')

print(t)
with open(input_file+'_bold.md', 'w') as f:
        f.write(t)
