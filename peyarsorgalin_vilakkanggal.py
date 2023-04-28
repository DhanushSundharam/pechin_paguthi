# அனைத்து 8 வகையான பெயர்ச்சொற்களின் விளக்கம்
vilakkam={
"podhuvaana": { "இடங்கள்":{"bank":"வங்க", "school":"பாடசாலை"},"பொருட்கள்":{"pencil":"பென்சில்","book" :"பொத்தகம்"}},

"vuripitta":{"இடங்கள்":{"California":"கலிபோனியா","London":"இலண்டன்"},
              "மனிதர்கள்":{"Tamilvaanan":"தமிழ்வாணன்","Sarmilan":"சர்மிலன்"},
              "மொழிகள்":{"French":"பிரஞ்சு","Tamil":"தமிழ்"},
              "மதங்கள்":{"Christian":"கிறிஸ்தவம்","Hindu":"இந்து"}},

"kanakkida":{"எடுத்துக்காட்டாக":{"dollar":"டொலர்","apple":"குமழிப்பழம்"}},

"kankkidamudiyadha":{"எடுத்துக்காட்டாக":{"water":"தண்ணீர்","love":"அன்பு / காதல்"}},
"dhidap":{"எடுத்துக்காட்டாக":{"ball":"பந்து","nose":"மூக்கு"}},
"kootu":{"எடுத்துக்காட்டாக":{"army":" இராணுவம் (பல வீரர்களை குறிக்கும் சொல்)","class":"வகுப்பு (பலர் கற்கும் இடம்)"}},
"nuun":{"எடுத்துக்காட்டாக":{"opinion":"கருத்து","skill ":"திறமை"}},
"kalavai":{"எடுத்துக்காட்டாக":{"homeland ":"தாய்நிலம்","blackboard":"கரும்பலகை"}}
}
class peyarsorgalin_vilakkanggal:

        def podhuvaana_peyarsol_vilakkam(self):
            print("பொதுவான பெயர்சொற்கள் எனும் போது மக்கள், இடங்கள், பொருட்கள், உயிரினங்கள் அனைத்தினதும் பெயர்கள், பொதுவான பெயர்ச்சொற்கள் தான். தமிழில் இதனை 'பொதுப் பெயர்ச்சொற்கள்' என அழைப்பதும் உண்டு")
            print()
            for i,j in vilakkam["podhuvaana"].items():print(i,j)

        def  vuripitta_peyarsol_vilakkam(self):
            print("""குறிப்பிட்ட ஒரு பொருள், இடம், மனிதன், மதம், மொழி, மாதம், ஊர், நாடு போன்றவற்றின் உரித்தான பெயர்களையே "உரித்தானப் பெயர்ச்சொற்கள்" என அழைக்கப்படுகின்றன. உரித்தானச்சொற்கள் ஒரு வாக்கியத்தில் எவ்விடத்தில் வந்தாலும் அதன் முதலெழுத்து கெப்பிட்டல் எழுத்திலேயே வரும் என்பதை நினைவில்""")
            print()
            for i,j in vilakkam["vuripitta"].items():print(i,j)

        def kanakkida_peyarsol_vilakkam(self):
            print("""கணக்கிடுப் பெயர்ச்சொற்கள் என்பன எண்ணிக்கையால் எண்ணி கணக்கிடக்கூடிய சொற்கள் ஆகும். அதாவது ஒன்று, இரண்டு, மூன்று என எண்ணி கணக்கிடக்கூடிய சொற்கள் எல்லாம் கணக்கிடுப் பெயர்ச்சொற்கள் தான்.""")
            print()
            for i,j in vilakkam["kanakkida"].items():print(i,j)

        def kanakkidamudiyadha_peyarsol_vilakkam(self):
            print("""எண்ணிக்கையால் எண்ணி கணக்கிட முடியாதச் சொற்கள் எல்லாமே "கணக்கிடாமுடியாப் பெயர்சொற்கள்"  ஆகும்.""")
            print()
            for i,j in vilakkam["kankkidamudiyadha"].items():print(i,j)

        def dhidap_peyarsol_vilakkam(self):
             print("""கண்ணால் பார்க்கவும், கையால் தொடவும் கூடியவற்றை "திடப் பெயர்சொற்கள்" எனலாம். இவை பொதுவானப் பெயர்சொற்களாகவோ உரித்தானப் பெயர்சொற்களாகவோ இருக்கலாம். கணகிடுப் பெயர்சொற்களாகவோ கணக்கிடமுடியாப் பெயர்சொற்களாகவோ இருக்கலாம்.""")
             print()
             for i,j in vilakkam["dhidap"].items():print(i,j)

        def  kootu_peyarsol_vilakkam(self):
            print("""கூட்டம்  அல்லது குழுக்களின் (பலரின் அல்லது பலதின்) கூட்டினை குறிக்கும் பெயர்களை "கூட்டுப் பெயர்சொற்கள்" என்றழைக்கப்படும்.""")
            print()
            for i,j in vilakkam["kootu"].items():print(i,j)

        def    nuun_peyarsol_vilakkam(self):
            print("""நுண் பெயர்ச்சொற்கள் என்பன கண்ணால் பார்க்கவோ, தொட்டுணரவோ முடியாத நுண்மையானவைகளாகும். அதனாலேயே அவற்றை "நுண் பெயர்ச்சொற்கள்" எனப்படுகின்றன""")
            print()
            for i,j in vilakkam["nuun"].items():print(i,j)

        def  kalavai_peyarsol_vilakkam(self):
            print("""இரண்டு அல்லது இரண்டிற்கு மேற்பட்ட சொற்கள் கலந்து இன்னுமொரு தனிச்சொல்லாக பயன்படும் சொற்களை அல்லது பெயர்களை "கலவைப் பெயர்ச்சொற்கள் என்றழைக்கப்படும்.""")
            print()
            for i,j in vilakkam["kalavai"].items():print(i,j)

#x=peyarsorgalin_vilakkanggal()
#x.kalavai_peyarsol_vilakkam()
