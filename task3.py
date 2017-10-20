with open('running-config.cfg','r') as current:
 with open('replace here.cfg','r') as updated:
    for line in current:
        updated.write(line.replace('172','192'))
    updated.close()

