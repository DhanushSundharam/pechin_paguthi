import json
innaippu=open("vilakkanggalin_paguthi.json","r")
conjunctions=json.load(innaippu)




class inaippu_sorgal_vilakkangal:
    def oorunginaipu_inaippusorgal(self):
        print(conjunctions["Coordinating"]["Villakkam"])
        for i,j in conjunctions["Coordinating"]["அவைகளாவன"].items():print(i,j);print()
        print(conjunctions["Coordinating"]["எடுத்துக்காட்டு_வாக்கியங்கள்"],"\n\n",conjunctions["Coordinating"]["குறிப்பு"])

    def saarntha_inaippusorgal(self):    
        print(conjunctions["subordinating"]["Villakkam"])
        for i in conjunctions["subordinating"]["சொற்கள்"]:print(i);print()
        print(conjunctions["subordinating"]["எடுத்துக்காட்டு_வாக்கியங்கள்"],"\n\n",conjunctions["subordinating"]["குறிப்பு"])

    def  opumai_inaippusorgal(self):
       print(conjunctions["correlative"]["Villakkam"])
       for i in conjunctions["correlative"]["சொற்கள்"]:print(i);print()
       for i,j in conjunctions["correlative"]["எடுத்துக்காட்டு_வாக்கியங்கள்"].items():print(i,j)

    def inaippu_vinaiachinggal(self):
        print(conjunctions["conjunctive"]["Villakkam"]) 
        for i in conjunctions["conjunctive"]["சொற்கள்"]:print(i);print()
        print(conjunctions["conjunctive"]["எடுத்துக்காட்டு_வாக்கியங்கள்"],"\n\n",conjunctions["conjunctive"]["குறிப்பு"])

x=inaippu_sorgal_vilakkangal()
x.oorunginaipu_inaippusorgal()
#x.saarntha_inaippusorgal()
#x.opumai_inaippusorgal()
#x.inaippu_vinaiachinggal()



