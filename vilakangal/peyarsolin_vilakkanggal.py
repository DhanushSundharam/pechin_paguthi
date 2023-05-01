import json
Peyarsol=open("vilakkanggalin_paguthi.json","r")
vilakkam=json.load(Peyarsol)



class peyarsorgalin_vilakkanggal:

        def podhuvaana_peyarsol_vilakkam(self):
            print(vilakkam["podhuvaana"]["Villakkam"],"\n\n")
            for i,j in vilakkam["podhuvaana"].items():print(i,j);print()

        def  vuripitta_peyarsol_vilakkam(self):
            
            print(vilakkam["vuripitta"]["Villakkam"],"\n\n")
            for i,j in vilakkam["vuripitta"].items():print(i,":",j);print()

        def kanakkida_peyarsol_vilakkam(self):
            
            print(vilakkam["kanakkida"]["Villakkam"],"\n\n")
            for i,j in vilakkam["kanakkida"]["எடுத்துக்காட்டாக"].items():print(i,":",j);print()

        def kanakkidamudiyadha_peyarsol_vilakkam(self):
           
            print(vilakkam["kankkidamudiyadha"]["Villakkam"],"\n\n")
            for i,j in vilakkam["kankkidamudiyadha"]["எடுத்துக்காட்டாக"].items():print(i,":",j);print()

        def dhidap_peyarsol_vilakkam(self):
             
             print(vilakkam["dhidap"]["Villakkam"],"\n\n")
             for i,j in vilakkam["dhidap"]["எடுத்துக்காட்டாக"].items():print(i,":",j);print()

        def  kootu_peyarsol_vilakkam(self):
            
            print(vilakkam["kootu"]["Villakkam"],"\n\n")
            for i,j in vilakkam["kootu"]["எடுத்துக்காட்டாக"].items():print(i,":",j);print()

        def    nuun_peyarsol_vilakkam(self):
            
            print(vilakkam["nuun"]["Villakkam"],"\n\n")
            for i,j in vilakkam["nuun"]["எடுத்துக்காட்டாக"].items():print(i,":",j);print()

        def  kalavai_peyarsol_vilakkam(self):
           
            print(vilakkam["kalavai"]["Villakkam"],"\n\n")
            for i,j in vilakkam["kalavai"]["எடுத்துக்காட்டாக"].items():print(i,":",j);print()

