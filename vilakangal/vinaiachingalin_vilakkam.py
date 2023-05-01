import json
vinaiachingal=open("vilakkanggalin_paguthi.json","r")
vinaiachingal=json.load(vinaiachingal)


class vinnaiachingalin_vilakkam:
    
    def madhiri_vinnaiachingal(self):
         print(vinaiachingal["Adverbs_of_manner"])
         for i,j in vinaiachingal["Adverbs_of_manner"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
         print( vinaiachingal["Adverbs_of_manner"]["கவனிக்கவும்"]);print();print(vinaiachingal["Adverbs_of_manner"]["குறிப்பு"])
         
    
    def  iida_vinnaiachingal(self):
        print(vinaiachingal["Adverbs_of_place"]["Villakkam"])
        for i,j in vinaiachingal["Adverbs_of_place"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
        print(vinaiachingal["Adverbs_of_place"]["குறிப்பு"])

    def kaala_vinnaiachingal(self):
        print(vinaiachingal["Adverbs_of_time"]["Villakkam"])
        for i,j in vinaiachingal["Adverbs_of_time"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
        print(vinaiachingal["Adverbs_of_time"]["குறிப்பு"])

    def natputhanmai_vinnaiachingal(self):
       print(vinaiachingal["Adverbs_of_frequency"]["Villakkam"])
       for i,j in vinaiachingal["Adverbs_of_frequency"]["எடுத்துக்காட்டாக"].items():print(i,j);print()

    def  aalavu_vinnaiachingal(self):
        print(vinaiachingal["Adverbs_of_degree"]["Villakkam"])
        for i,j in vinaiachingal["Adverbs_of_degree"]["எடுத்துக்காட்டாக"].items():print(i,j);print()

        
x=vinnaiachingalin_vilakkam()        
x.madhiri_vinnaiachingal()
#x.Adverbs_of_place()
#x.Adverbs_of_time()
#x.Adverbs_of_frequency()
#x.Adverbs_of_degree()
