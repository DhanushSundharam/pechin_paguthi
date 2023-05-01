import json
pirathipeyar=open("vilakkanggalin_paguthi.json","r")
vilakkam=json.load(pirathipeyar)



class pirathipeyar:
   def subject_pronouns_description(self):
        print(vilakkam["subject"]["Villakkam"])
        for i,j in vilakkam["subject"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
        print(vilakkam["subject"]["உதாரணம்"]);print()
        print("(“Kennedy” எனும் பெயர்சொல்லுக்குப் பதிலாக “He” எனும் சுட்டுப்பெயர் பயன்படுத்தப்பட்டுள்ளது.)")

   def object_pronouns_description(self):
        print(vilakkam["Object"]["Villakkam"])
        for i,j in vilakkam["Object"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
        print(vilakkam["Object"]["உதாரணம்"]);print()

   def reflexive_pronouns_description(self):
       print(vilakkam["Reflexive"]["Villakkam"])
       for i,j in vilakkam["Reflexive"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
       print(vilakkam["Reflexive"]["உதாரணம்"]);print()
       print("(நான் எனது தலைமயிரை நானே/நானாகவே வெட்டிக்கொண்டேன்.)")

   def possessive_pronouns_description(self):
       print(vilakkam["possessive"]["Villakkam"])
       for i,j in vilakkam["possessive"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
       print(vilakkam["possessive"]["உதாரணம்"]);print()

   def  demonstrative_pronouns_description(self):
       print(vilakkam["Demonstrative"]["Villakkam"])
       for i,j in vilakkam["Demonstrative"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
       print(vilakkam["Demonstrative"]["உதாரணம்"]);print()
       print("(இவற்றில் book books எனும் பெயர் சொற்களை தவிர்த்து சுட்டுப்பெயர்களை மட்டுமே பயன்படுத்தியும் பேசலாம்.)")

   def relative_pronouns_description(self):
       print(vilakkam["relative"]["Villakkam"])
       for i,j in vilakkam["relative"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
       print(vilakkam["relative"]["உதாரணம்"]);print()
       print("மேலும் இதுப்போன்ற இணைப்புச் சொற்களின் பயன்பாடு பற்றி எதிர்வரும் பாடத்தில் விரிவாகப் பார்ப்போம்.")

   def interrogative_pronouns_description(self): 
       print(vilakkam["Interrogative"]["Villakkam"])
       for i,j in vilakkam["Interrogative"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
       print(vilakkam["Interrogative"]["உதாரணம்"]);print()

   def indefinite_pronouns_description(self):
       print(vilakkam["Indefinite"]["Villakkam"])
       for i,j in vilakkam["Indefinite"]["எடுத்துக்காட்டாக"].items():print(i,j);print()
       print(vilakkam["Indefinite"]["உதாரணம்"]);print()

