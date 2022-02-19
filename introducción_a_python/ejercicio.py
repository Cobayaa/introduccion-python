




pronombres = ["yo","tu","el","ella","nosotros","ustedes","ellos","ellas"]
verbo = input ("ingrese un verbo:")
conjugacion = {
   "yo":{
       "ar": "o",
       "er": "o",
       "ir": "o"
   },

    "tu":{
       "ar": "as",
       "er": "es",
       "ir": "es"
   },

    "el":{
       "ar": "a",
       "er": "e",
       "ir": "e"
   },

    "ella":{
       "ar": "a",
       "er": "e",
       "ir": "e"
   },

    "nosotros":{
       "ar": "amos",
       "er": "emos",
       "ir": "imos"
   },

    "ustedes":{
       "ar": "an",
       "er": "en",
       "ir": "en"
   },

    "ellos":{
       "ar": "an",
       "er": "en",
       "ir": "en"
   },

    "ellas":{
       "ar": "an",
       "er": "en",
       "ir": "en"
   },

}


terminaciones = verbo[len(verbo) -2] + verbo[len(verbo) -1]
verbosinterminacion = verbo.replace(terminaciones, " ")

for pronombres in conjugacion:
    print(pronombres)
    print(verbosinterminacion)
    print(pronombres[pronombres][conjugacion])
    print(pronombres, verbosinterminacion + pronombres[pronombres][terminaciones])


cobaya = 22
























