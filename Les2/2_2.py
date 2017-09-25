cijferICOR=8
cijferPROG=6
cijferCSN=7

gemiddelde=((cijferICOR+cijferPROG+cijferCSN)/3)
print(gemiddelde)

beloning=(cijferICOR*30)+(cijferPROG*30)+(cijferCSN*30)
print(beloning)

overzicht= 'Mijn cijfers gemiddeld een' + ' ' +str(gemiddelde) + ' ' + 'leveren een beloning van'+ ' ' +str(beloning)+ ' ' + 'euro op!'
print(overzicht)
