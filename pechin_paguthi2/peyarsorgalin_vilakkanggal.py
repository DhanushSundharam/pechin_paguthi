
# அனைத்து 8 வகையான பெயர்ச்சொற்களின் விளக்கம்
vilakkam={
"podhuvaana": { "இடங்கள்":{"bank":"வங்க", "school":"பாடசாலை"},"பொருட்கள்":{"pencil":"பென்சில்","book" :"பொத்தகம்"},
"Villakkam":"""பொதுவான பெயர்சொற்கள் எனும் போது மக்கள், இடங்கள், பொருட்கள், உயிரினங்கள் அனைத்தினதும் பெயர்கள், பொதுவான பெயர்ச்சொற்கள் தான். தமிழில் இதனை 'பொதுப் பெயர்ச்சொற்கள்' என அழைப்பதும் உண்டு"""},

"vuripitta":{"இடங்கள்":{"California":"கலிபோனியா","London":"இலண்டன்"},
              "மனிதர்கள்":{"Tamilvaanan":"தமிழ்வாணன்","Sarmilan":"சர்மிலன்"},
              "மொழிகள்":{"French":"பிரஞ்சு","Tamil":"தமிழ்"},
              "மதங்கள்":{"Christian":"கிறிஸ்தவம்","Hindu":"இந்து"},
             "Villakkam":"""குறிப்பிட்ட ஒரு பொருள், இடம், மனிதன், மதம், மொழி, மாதம், ஊர், நாடு போன்றவற்றின் உரித்தான பெயர்களையே "உரித்தானப் பெயர்ச்சொற்கள்" என அழைக்கப்படுகின்றன. உரித்தானச்சொற்கள் ஒரு வாக்கியத்தில் எவ்விடத்தில் வந்தாலும் அதன் முதலெழுத்து கெப்பிட்டல் எழுத்திலேயே வரும் என்பதை நினைவில்"""},

"kanakkida":{"எடுத்துக்காட்டாக":{"dollar":"டொலர்","apple":"குமழிப்பழம்"},
             "Villakkam":"""கணக்கிடுப் பெயர்ச்சொற்கள் என்பன எண்ணிக்கையால் எண்ணி கணக்கிடக்கூடிய சொற்கள் ஆகும். அதாவது ஒன்று, இரண்டு, மூன்று என எண்ணி கணக்கிடக்கூடிய சொற்கள் எல்லாம் கணக்கிடுப் பெயர்ச்சொற்கள் தான்."""},

"kankkidamudiyadha":{"எடுத்துக்காட்டாக":{"water":"தண்ணீர்","love":"அன்பு / காதல்"},
                     "Villakkam":"""எண்ணிக்கையால் எண்ணி கணக்கிட முடியாதச் சொற்கள் எல்லாமே "கணக்கிடாமுடியாப் பெயர்சொற்கள்"  ஆகும்."""},
"dhidap":{"எடுத்துக்காட்டாக":{"ball":"பந்து","nose":"மூக்கு"},
          "Villakkam":"""கண்ணால் பார்க்கவும், கையால் தொடவும் கூடியவற்றை "திடப் பெயர்சொற்கள்" எனலாம். இவை பொதுவானப் பெயர்சொற்களாகவோ உரித்தானப் பெயர்சொற்களாகவோ இருக்கலாம். கணகிடுப் பெயர்சொற்களாகவோ கணக்கிடமுடியாப் பெயர்சொற்களாகவோ இருக்கலாம்."""},
"kootu":{"எடுத்துக்காட்டாக":{"army":" இராணுவம் (பல வீரர்களை குறிக்கும் சொல்)","class":"வகுப்பு (பலர் கற்கும் இடம்)"},
            "Villakkam":"""கூட்டம்  அல்லது குழுக்களின் (பலரின் அல்லது பலதின்) கூட்டினை குறிக்கும் பெயர்களை "கூட்டுப் பெயர்சொற்கள்" என்றழைக்கப்படும்."""
},
"nuun":{"எடுத்துக்காட்டாக":{"opinion":"கருத்து","skill ":"திறமை"},
        "Villakkam": """நுண் பெயர்ச்சொற்கள் என்பன கண்ணால் பார்க்கவோ, தொட்டுணரவோ முடியாத நுண்மையானவைகளாகும். அதனாலேயே அவற்றை "நுண் பெயர்ச்சொற்கள்" எனப்படுகின்றன"""
},
"kalavai":{"எடுத்துக்காட்டாக":{"homeland ":"தாய்நிலம்","blackboard":"கரும்பலகை"},
           "Villakkam":"""இரண்டு அல்லது இரண்டிற்கு மேற்பட்ட சொற்கள் கலந்து இன்னுமொரு தனிச்சொல்லாக பயன்படும் சொற்களை அல்லது பெயர்களை "கலவைப் பெயர்ச்சொற்கள் என்றழைக்கப்படும்."""
}
}

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

x=peyarsorgalin_vilakkanggal()
x.podhuvaana_peyarsol_vilakkam()
x.vuripitta_peyarsol_vilakkam()
x.kanakkida_peyarsol_vilakkam()
x.kanakkidamudiyadha_peyarsol_vilakkam()
x.dhidap_peyarsol_vilakkam()
x.kootu_peyarsol_vilakkam()
x.nuun_peyarsol_vilakkam()
x.kalavai_peyarsol_vilakkam()
