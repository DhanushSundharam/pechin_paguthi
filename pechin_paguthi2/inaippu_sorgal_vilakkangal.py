conjunctions={"Coordinating":{"அவைகளாவன":{"F":"For","A":"And","N":"Nor","B":"But","O":"Or","Y":"Yet","S":"So"},
                             "எடுத்துக்காட்டு_வாக்கியங்கள்":{"I like bread and butter.":"நான் உரொட்டியும் வெண்ணையும் விரும்புகிறேன்","I like tea, but I don't like coffee":"நான் தேனீர் விரும்புகிறேன், ஆனால் நான் காப்பி(க்கு) விருப்பமில்லை."},
                             "குறிப்பு":"""ஆங்கிலத்தில் ஒருங்கிணைப்புச் சொற்கள் 7 மட்டுமே உள்ளன. இவற்றை எளிதாக மனதில் இருத்திக்கொள்வதற்கு இச்சொற்களின் முதலெழுத்துக்களை இணைத்து FANBOYS என ஒரு சுருக்கப்பெயராக (Acronyms) அழைப்பர். நீங்களும் இச்சுருக்கப்பெயரை மனதில் இருத்திக்கொள்ளலாம்.""",
                              "Villakkam":"""ஒருங்கிணைப்பு இணைப்புச்சொற்கள், வாக்கியங்களில் ஒரே சமனிடையான "சொற்கள்”, "சொற்றொடர்கள்”, "வாக்கியக்கூறுகள் " போன்றவற்றை ஒருங்கே இணைக்கப் பயன்படும் சிறிய சொற்கள் ஆகும். இதனை "ஒருங்கிணைப்புச் சொற்கள்" என சுருக்கமாகவும் கூறலாம்."""},



"subordinating":{"சொற்கள்":["after","although","as long as","as soon as","even though","before","if","how","since","than","that","when","where","whether","while","whenever"],
    "எடுத்துக்காட்டு_வாக்கியங்கள்":{"If I do a job, I will get experience":"நான் ஒரு வேலை செய்தால் எனக்கு கிடைக்கும் அனுபவம்","I will get experience if I do a job":"எனக்கு கிடைக்கும் அனுபவம் நான் செய்தால் ஒரு வேலை"},
    "குறிப்பு":" சார்ந்த இணைப்புச்சொற்கள் எப்போதும் சார்ந்த வாக்கிய கூற்றின் (Subordinate Clause) முன்னாலேயே பயன்படும்.",
     "Villakkam":""""சார்ந்த இணைப்புச்சொற்கள்" எப்போதும் பிரதான வாக்கியக் கூற்றையும் (Independent Clause) சார்ந்த வாக்கியக் கூற்றையும் (Dependent Clause) தொடர்புபடுத்தும் வகையில் பயன்படுபவைகள் ஆகும். இவை ஆங்கிலத்தில் நூற்றுக்கணக்கானவைகள் உள்ளன."""},


"correlative":{"சொற்கள்":["both ... and","so ... as","not ... but","not only ... but also","either ... or","neither ... nor","whether ... or"],
               "எடுத்துக்காட்டு_வாக்கியங்கள்":{"Neither cats nor dogs are my favorite animals":"பூனைகள் நாய்கள் இரண்டுமே எனது விருப்பு மிருகங்கள் அல்ல","I want both a computer and a iPad":"கணனி மற்றும்  ஐபேட் இரண்டும் எனக்கு வேண்டும்"},
               "Villakkam":"""ஒப்புமை இணைப்புச்சொற்கள் இரண்டு சமனிடையான வாக்கியங்களை ஒப்புமையுடன் இணைக்கும் சொற்களாகும். இவ்விணைப்புச்சொற்கள் சோடிகளாகவே பயன்படும்."""},
               

"conjunctive":{"சொற்கள்":["accordingly","consequently","finally","furthermore","however","similarly","therefore"],
                "எடுத்துக்காட்டு_வாக்கியங்கள்":{"I wanted to buy a shirt; however, It was too expensive":"எனக்கு ஒரு சட்டை வாங்க வேண்டும்; எனினும், அதன் விலை மிகவும் அதிகமாக இருந்தது","David went to market; however, he didn't buy anything":"டேவிட் சந்தைக்கு சென்றார்; இருப்பினும், அவர் எதனையும் வாங்கவில்லை."},
               "குறிப்பு":""": இனைப்பு வினையெச்சங்கள் என்பவை ஒருவகையில் வினையெச்சங்கள் தான். இருப்பினும் அவை வாக்கியக் கூறுகளை இணைக்கப் பயன்படுவதால் "இணைப்பு வினையெச்சங்கள்" என்றழைக்கப்படுகின்றன.""",
               "Villakkam": """இணைப்பு வினையெச்சங்கள் இரண்டு பிரதான வாக்கியக் கூறுகளை (Main Clauses) இணைப்பவைகளாகவே, அதாவது "ஒருங்கிணைப்புச் சொற்கள்" போன்றதாகவே பயன்படும். ஆனாலும் சற்று வேறுபட்டது.அதாவது தமிழில்  "அதனால்", எப்படியானாலும்", "இதுதொடர்பாக" போன்ற சொற்களை பயன்படுத்தி இரண்டு வாக்கியங்களை இணைக்கும் முறைக்கு ஒத்ததாகவே இவை இருக்கும்."""},        
}


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

#x=inaippu_sorgal_vilakkangal()
#x.oorunginaipu_inaippusorgal()
#x.saarntha_inaippusorgal()
#x.opumai_inaippusorgal()
#x.inaippu_vinaiachinggal()



