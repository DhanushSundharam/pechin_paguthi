from textblob import TextBlob
import json
file=open("vilakkam1.json","r")
vilakkam=json.load(file)
file.close()
def about_pechin_paguthiPOS():
                        print("""நாம் பள்ளியில் இருக்கும்போது அல்லது ஆங்கில மொழி கற்றல் செயல்முறையைத் தொடங்கும் போது நாம் கற்றுக் கொள்ளும் முதல் இலக்கண தலைப்புகளில் பேச்சின் பகுதிகளும் அடங்கும். பேச்சின் பகுதிகளை ஒரு வாக்கியத்தில் வெவ்வேறு பாத்திரங்களைச் செய்யும் வார்த்தைகளாக வரையறுக்கலாம். பேச்சின் சில பகுதிகள் பேச்சின் மற்ற பகுதிகளின் செயல்பாடுகளையும் செய்ய முடியும்\n\n\n""")

                        print("பேச்சு வரையறைகள் மற்றும் எடுத்துக்காட்டுகளின் 8 பகுதிகள்:\n\n")
                        data = [
                            ["பெயர்ச்சொல்", "Nouns", "Peyarsol"],
                            ["சுட்டுபெயர்கள்", "Pronouns", "suttuppeyargal"],
                            ["இணைப்புகள்", "Conjunctions", "innaippu_sorgal"],
                            ["வினையுரிச்சொற்கள்", "Adverbs", "vinaiachanggal"],
                            ["வினைச்சொற்கள்", "Verbs", "vinaichsol"],
                            ["பெயரடைகள்", "Adjectives", "vurichsorgal"],
                            ["முன்மொழிவுகள்", "Prepositions", "idaichsol"],
                            ["இடையிடல்கள்", "Interjections", "viyappusol"]
                        ]

                        headers = ["Tamil", "English", "Tanglish"]

                        
                        max_widths = [max(len(str(row[i])) for row in data) for i in range(len(headers))]

                        
                        table = "|".join(header.ljust(max_widths[i]) for i, header in enumerate(headers))
                        print(table)
                        print('-' * len(table))

                        
                        for row in data:
                            row_str = "|".join(str(cell).ljust(max_widths[i]) for i, cell in enumerate(row))
                            print(row_str)

                            
        

  
class peyarsol_vilakkanggal(object):
            def __init__(self,objects=None):
                      self.__objects=objects
            def about_peyarsol(self):
                print("""பெயர்ச்சொல் என்பது ஒரு நபர், இடம், பொருள் அல்லது யோசனை போன்ற ஒன்றைப் பெயரிடும் சொல். ஒரு வாக்கியத்தில், பெயர்ச்சொற்கள் பொருள், நேரடி பொருள், மறைமுக பொருள், பொருள் நிரப்புதல், பொருள் நிரப்புதல், அபோசிட்டிவ் அல்லது மாற்றியமைக்கும் பாத்திரத்தை வகிக்க முடியும்.பெயர்ச்சொல் மற்றும் அதன் வகைப்பாடு
                              பெயர்ச்சொற்களில் மேலும் இரண்டு வகைப்பாடுகள் உள்ளன, அவை ஒருமை பெயர்ச்சொற்கள் மற்றும் பன்மை பெயர்ச்சொற்கள்.

                            ஒருமை பெயர்ச்சொல்
                            1) ஒருமை பெயர்ச்சொல் - சொற்றொடரில் ஒரு பொருள் அல்லது ஒரு நபர் குறிக்கப்பட்டால் அது ஒருமை பெயர்ச்சொல் என்று அழைக்கப்படுகிறது.

                            Ex. பெண், புத்தகம், நாய், மேசை போன்றவை.

                            எங்கள் வகுப்பில் உள்ள பையன் போர்டு தேர்வில் முதலிடம் பிடித்தான்.

                            2) பன்மை பெயர்ச்சொல் - ஒரு சொற்றொடரில் உள்ள பெயர்ச்சொல் ஒன்றுக்கு மேற்பட்ட நபர்கள் அல்லது பொருள் அல்லது பொருட்களைக் குறிக்கும் போது அது பன்மை பெயர்ச்சொல் என்று அழைக்கப்படுகிறது.

                            Ex. மொபைல்கள், சிறுவர்கள், மேஜைகள், பொறியாளர்கள் போன்றவை.

                            இன்றைக்கு எத்தனையோ பொறியாளர்கள் வேலையில்லாமல் இருக்கிறார்கள்.


                                                  """)
                                            
            def vagaigal(self):
                
                
                    z=[]
                    x={"common_nouns":"பொதுவான பெயர்சொற்கள்","proper_nouns":"உரித்தானப் பெயர்சொற்கள்","countable_Nouns":"கணக்கிடுப் பெயர்சொற்கள்","uncountable_nouns":"கணக்கிடமுடியாப் பெயர்சொற்கள்","Concrete_nouns":"கணக்கிடமுடியாப் பெயர்சொற்கள்","collective_nouns":"கூட்டுப் பெயர்சொற்கள்","abstract_nouns":"நுண் பெயர்ச்சொற்கள்","compound_nouns":"கலவைப் பெயர்சொற்கள்"}
                    for i,j in x.items():
                             z.append((i,j))
                    return z        
                           
            def ta_to_en(self):
                    
                           word=TextBlob("""பெயர்ச்சொற்களை ஆங்கிலத்தில் "nouns” என அழைக்கப்படுகிறது. இச்சொல் இலத்தீன் மொழியில் "nōmen" (பெயர்) என்ற சொல்லில் இருந்து மருவி ஆங்கிலத்தில் பயன்படும் சொல்லாகும்.ஆங்கிலப் பெயர்சொற்கள் (Nouns) என்பன மனிதர்கள், இடங்கள், பொருற்கள், உயிரினங்கள், உணர்வுகள் போன்றவற்றை குறிப்பதற்கான "பெயர்கள்" அல்லது "பெயர்ச்சொற்கள்" ஆகும்.""")
                           z=word.translate(from_lang="ta",to="en")
                           print(z)
            def vagaigalin_vilakkam(self):
                     if self.__objects==None:
                         print("""பெயர்ச்சொற்களை ஆங்கிலத்தில் "nouns” என அழைக்கப்படுகிறது. இச்சொல் இலத்தீன் மொழியில் "nōmen" (பெயர்) என்ற சொல்லில் இருந்து மருவி ஆங்கிலத்தில் பயன்படும் சொல்லாகும்.ஆங்கிலப் பெயர்சொற்கள் (Nouns) என்பன மனிதர்கள், இடங்கள், பொருற்கள், உயிரினங்கள், உணர்வுகள் போன்றவற்றை குறிப்பதற்கான "பெயர்கள்" அல்லது "பெயர்ச்சொற்கள்" ஆகும்.""")

                     else:
                            print(vilakkam[self.__objects]["Villakkam"],"\n\n")
                            for i,j in vilakkam[self.__objects]["example"].items():print(i,j);print()
                      


             
             
        
       

class suttuppeyar_vilakkanggal:
    
         def __init__(self,objects=None):
                      self.__objects=objects

         
              
                      
         def vagaigal(self):
                    z=[]
                    x={"subject_pronouns":"எழுவாய்_சுட்டுப்பெயர்கள்","object_pronouns":"செயப்படுபொருள்_சுட்டுப்பெயர்கள்","reflexive_pronouns":"அனிச்சைச்_செயல்_சுட்டுப்பெயர்கள்","possessive_pronouns":"ஆறாம்_வேற்றுமை","demonstrative_pronouns":"குறிப்பிடுச்_சுட்டுப்பெயர்கள்","relative_pronouns":"உரிச்_சுட்டுப்பெயர்கள்","interrogative_pronouns":"கேள்வி_சுட்டுப்பெயர்கள்","indefinite_pronouns":"காலவரையற்ற_சுட்டுப்பெயர்கள்"}
                    for i,j in x.items():
                        z.append((i,j))
                    return z

         def ta_to_en(self):
                 word=TextBlob("""சுட்டுப்பெயர் சொல் என்பது ஒரு பெயரை அல்லது பெயர் சொல்லை குறிப்பிடாமல், அதற்குப் பதிலாக சுட்டிக்காட்டுவதற்கு பயன்படும் சொற்களே "சுட்டுப்பெயர்" என்றழைக்கப்படுகின்றன. இவற்றை தமிழில் "பிரதிப்பெயர்கள்", "பதிலிடுச்சொற்கள்" என்றும் அழைப்பர். ஆங்கிலத்தில் "Pronouns" என அழைக்கப்படும்.""")    
                 z=word.translate(from_lang="ta",to="en")
                 print(z)
                
         def vagaigalin_vilakkam(self):
              if self.__objects==None:
                  print("""சுட்டுப்பெயர் சொல் என்பது ஒரு பெயரை அல்லது பெயர் சொல்லை குறிப்பிடாமல், அதற்குப் பதிலாக சுட்டிக்காட்டுவதற்கு பயன்படும் சொற்களே "சுட்டுப்பெயர்" என்றழைக்கப்படுகின்றன. இவற்றை தமிழில் "பிரதிப்பெயர்கள்", "பதிலிடுச்சொற்கள்" என்றும் அழைப்பர். ஆங்கிலத்தில் "Pronouns" என அழைக்கப்படும்.""")    
              else:
                  print(vilakkam[self.__objects]["Villakkam"]);print()
                  for i,j in vilakkam[self.__objects]["example"].items():print(i,j);print()
                  print(vilakkam[self.__objects]["forexample"]);print()
                  

        

class innaippu_vilakkanggal():
            def __init__(self,objects=None):
                          self.__objects=objects

            def vagaigal(self):
                   z=[]
                   x={"Adverbs_of_manner":"மாதிரி_வினையெச்சங்கள்","Adverbs_of_place":"இட_வினையெச்சங்கள்","Adverbs_of_time":"கால_வினையெச்சங்கள்","Adverbs_of_frequency":"நடப்புத்தன்மை_வினையெச்சங்கள்","Adverbs_of_degree":"அளவு_வினையெச்சங்கள்"}
                   for i,j in x.items():
                         z.append((i,j))
                   return z

            def ta_to_en(self):
                   word=TextBlob("""இணைப்புச்சொற்கள் எவ்வாறு எத்தனை முறைகளில் பயன்படுகின்றன?இவை இரண்டு அல்லது இரண்டிற்கு மேற்பட்ட வாக்கியக் கூறுகளை இணைக்க தனித்த ஒற்றை சொல், கூட்டுச்சொற்கள், இடமாறி பயன்படும் சொற்கள் என மூன்று முறைகளில் பயன்படுகின்றன""")    
                   z=word.translate(from_lang="ta",to="en")
                   print(z)
                  

            def vagaigalin_vilakkam(self):
                 print(vilakkam[self.__objects]["Villakkam"])
                 for i,j in vilakkam[self.__objects]["example"].items():print(i,j);print()
                 print(vilakkam[self.__objects]["example_sentence"],"\n\n",vilakkam[objects]["Note"])
               

           

class vinaiachanggal_vilakkanggal:
            def __init__(self,objects=None):
                              self.__objects=objects

            def vagaigal(self):
                    z=[]
                    x={"Adverbs_of_manner":"மாதிரி_வினையெச்சங்கள்","Adverbs_of_place":"இட_வினையெச்சங்கள்","Adverbs_of_time":"கால_வினையெச்சங்கள்","Adverbs_of_frequency":"நடப்புத்தன்மை_வினையெச்சங்கள்","Adverbs_of_degree":"அளவு_வினையெச்சங்கள்"}
                    for i,j in x.items():
                             z.append((i,j))
                    return z

            def ta_to_en(self):
                 word=TextBlob("""வினெயெச்சங்கள் என்றால் என்ன? வினையெச்சங்கள் என்றால் ஆங்கிலப் பேச்சின் கூறுகளில் ஒன்று என்பதை நாம் ஏற்கெனவே கற்றுள்ளோம். இவை முக்கியமாக ஒரு வினையின் அல்லது வினைச்சொல்லின் தன்மையை விவரித்துக் கூற பயன்படும் சொற்கள் ஆகும். இவற்றை வினையெச்சங்கள், வினையடைகள், வினையுரிச் சொற்கள் என பல்வேறு பெயர்களில் தமிழில் அழைக்கப்படுகின்றது. ஆங்கிலத்தில் "Adverbs" என்றழைப்பர்""")
                 z=word.translate(from_lang="ta",to="en")
                 print(z)

            def vagaigalin_vilakkam(self,__objects):
                 print(vilakkam[self.__objects]["Villakkam"])
                 for i,j in vilakkam[self.__objects]["example_sentence"].items():print(i,":",j);print()
                 
                              
class munmozhigal():
    def __init__(self,objects=None):
        self.__objects=objects

    def vagaigal(self):
         z=[]
         x={"Preposition for Place":"இடத்திற்கான முன்மொழிவு","இடத்திற்கான முன்மொழிவு":"நேரத்திற்கான முன்மொழிவு","preposition for Agent or Instrument":"முகவர் அல்லது கருவிக்கான முன்மொழிவு","preposition for Manner":"முறைக்கான முன்மொழிவு","preposition for Cause,Reason,Purpose":"காரணம், காரணம், நோக்கம் ஆகியவற்றிற்கான முன்மொழிவு","preposition for Possession":"முறைக்கான முன்மொழிவு"}
         for i,j in x.items():
                        z.append((i,j))
         return z

    def ta_to_en(self):
        word=TextBlob("முன்மொழிவு என்பது ஒரு குறுகிய வார்த்தையாகும், இது அந்தந்த வாக்கியங்களுக்குள் உள்ள பிற பகுதிகளுடன் உள்ள உறவு பெயர்ச்சொற்கள், பிரதிபெயர்கள் அல்லது சொற்றொடர்களைக் காட்ட வாக்கியங்களில் பயன்படுத்தப்படுகிறது. முன்மொழிவுகள் பொதுவாக வாக்கியத்தின் பிற்பகுதியில் அமைந்துள்ளன, ஆனால் பெயர்ச்சொல் அல்லது பிரதிபெயருக்கு முன்.")
        z=word.translate(from_lang="ta",to="en")
        print(z)

    def vagaigalin_vilakkam(self):
         if self.objects==None:
             print("""முன்மொழிவு என்பது ஒரு குறுகிய வார்த்தையாகும், இது அந்தந்த வாக்கியங்களுக்குள் உள்ள பிற பகுதிகளுடன் உள்ள உறவு பெயர்ச்சொற்கள், பிரதிபெயர்கள் அல்லது சொற்றொடர்களைக் காட்ட வாக்கியங்களில் பயன்படுத்தப்படுகிறது. முன்மொழிவுகள் பொதுவாக வாக்கியத்தின் பிற்பகுதியில் அமைந்துள்ளன, ஆனால் பெயர்ச்சொல் அல்லது பிரதிபெயருக்கு முன்.""")
         else:
             print(vilakkam[self.__objects]["Villakkam"]);print()
             for i,j in vilakkam[self.__objects]["example"].items():print(i,j);print()

class idaichsol():
    def __init__(self,objects=None):
        self.__objects=objects

    def vagaigal(self):
        z=[]
        x={"Interjections of joy":"மகிழ்ச்சியின் இடைச் சொற்கள்","Interjections of Sorrow":"சோகத்தின் இடைச் சொற்கள்","Interjections of Greeting":"வாழ்த்து என்பதன் இடைச் சொற்கள்","Interjections of Attention":"கவனத்தின் குறுக்கீடுகள்","Interjections of Approval":"ஒப்புதலின் குறுக்கீடுகள்","Interjections of Suprise":"ஆச்சரியத்தின் இடைச் சொற்கள்","Interjections of Anger":"கோபத்தின் இடைச் சொற்கள்","Interjections of Shock":"அதிர்ச்சியின் இடைச் சொற்கள்"}
        for i,j in x.items():
            z.append((i,j))
        return z

    def ta_to_en(self):
        word=TextBlob("இடைச்சொல் என்பது பேச்சின் எட்டு பகுதிகளில் ஒன்றாகும், இது வாக்கியத்தின் தெளிவான பொருளைப் பெற பொதுவாகத் தேவையில்லை, எனவே இது முறையான எழுத்து அல்லது பேச்சைக் காட்டிலும் முறைசாரா மொழியில் பொதுவாகப் பயன்படுத்தப்படுகிறது மற்றும் ஒரு வாக்கியத்தில் ஆச்சரியத்தை சேர்க்க முக்கியமாகப் பயன்படுத்தப்படுகிறது.")
        z=word.translate(from_lang="ta",to="en")
        print(z)

    def vagaigalin_vilakkam(self):
         if self.objects==None:
            print("""இடைச்சொல் என்பது பேச்சின் எட்டு பகுதிகளில் ஒன்றாகும், இது வாக்கியத்தின் தெளிவான பொருளைப் பெற பொதுவாகத் தேவையில்லை, எனவே இது முறையான எழுத்து அல்லது பேச்சைக் காட்டிலும் முறைசாரா மொழியில் பொதுவாகப் பயன்படுத்தப்படுகிறது மற்றும் ஒரு வாக்கியத்தில் ஆச்சரியத்தை சேர்க்க முக்கியமாகப் பயன்படுத்தப்படுகிறது.""")
         else:
             print(vilakkam[self.__objects]["Villakkam"]);print()
             for i,j in vilakkam[self.__objects]["example"].items():print(i,j);print()

class vurichsol():
    def __init__(self,objects=None):
        self.__objects=objects

    def vagaigal(self):
        z=[]
        x={"Descriptive Adjective":"விளக்கப் பெயரடை","Numeral Adjective":"எண் உரிச்சொல்","Quantitative Adjective":"அளவு உரிச்சொல்","Demonstrative Adjective":"ஆர்ப்பாட்ட உரிச்சொல்","Interrogative Adjective":"வினவு உரிச்சொல்","Possessive Adjective":"உடைமை உரிச்சொல்","Proper Adjective":"சரியான பெயரடை","Exclamatory Adjective":"ஆச்சரியமூட்டும் உரிச்சொல்"}
        for i,j in x.items():
            z.append((i,j))
        return z

    def ta_to_en(self):
        word=TextBlob("""பெயரடை என்பது பெயர்ச்சொல் அல்லது பெயர்ச்சொல் சொற்றொடரை விவரிக்கும் ஒரு சொல். அதன் சொற்பொருள் பங்கு பெயர்ச்சொல் மூலம் கொடுக்கப்பட்ட தகவலை மாற்றுவதாகும். பாரம்பரியமாக, உரிச்சொற்கள் ஆங்கில மொழியின் பேச்சின் முக்கிய பகுதிகளில் ஒன்றாகக் கருதப்பட்டன, இருப்பினும் வரலாற்று ரீதியாக அவை பெயர்ச்சொற்களுடன் ஒன்றாக வகைப்படுத்தப்பட்டுள்ளன.""")
        z=word.translate(from_lang="ta",to="en")
        print(z)

    def vagaigalin_vilakkam(self):
         if self.objects==None:
            print("""பெயரடை என்பது பெயர்ச்சொல் அல்லது பெயர்ச்சொல் சொற்றொடரை விவரிக்கும் ஒரு சொல். அதன் சொற்பொருள் பங்கு பெயர்ச்சொல் மூலம் கொடுக்கப்பட்ட தகவலை மாற்றுவதாகும். பாரம்பரியமாக, உரிச்சொற்கள் ஆங்கில மொழியின் பேச்சின் முக்கிய பகுதிகளில் ஒன்றாகக் கருதப்பட்டன, இருப்பினும் வரலாற்று ரீதியாக அவை பெயர்ச்சொற்களுடன் ஒன்றாக வகைப்படுத்தப்பட்டுள்ளன.""")
         else:
             print(vilakkam[self.__objects]["Villakkam"]);print()
             for i,j in vilakkam[self.__objects]["example"].items():print(i,j);print()
             
class vinaichsol():
   def __init__(self,objects=None):
        self.__objects=objects

   def vagaigal(self):
        z=[]
        x={"Action verbs":"செயல் வினைகள்","stative verbs":"நிலையான வினைச்சொற்கள்","Transitive verbs":"இடைநிலை வினைச்சொற்கள்","Intransitive verbs":"மாறாத வினைச்சொற்கள்","Linking verbs":"வினைச்சொற்களை இணைத்தல்","Helping verbs":"உதவும் வினைச்சொற்கள்","Modal verbs":"மாதிரி வினைச்சொற்கள்","Regular verbs":"வழக்கமான வினைச்சொல்","irregular verbs":"ஒழுங்கற்ற வினைச்சொற்கள்","Phrasal verbs":"சொற்றொடர் வினைச்சொற்கள்","infinitives verbs":"முடிவிலி வினைச்சொற்கள்"}
        for i,j in x.items():
            z.append((i,j))
        return z

   def ta_to_en(self):
        word=TextBlob("""பெயர்ச்சொல் என்பது பொதுவாக உயிரினங்கள், இடங்கள், செயல்கள், குணங்கள், இருப்பு நிலைகள் அல்லது யோசனைகள் போன்ற ஒரு குறிப்பிட்ட பொருள் அல்லது பொருட்களின் தொகுப்பின் பெயராக செயல்படும் ஒரு சொல். லெக்சிகல் பிரிவுகள் அவற்றின் உறுப்பினர்கள் மற்ற வகையான வெளிப்பாடுகளுடன் இணைக்கும் வழிகளின் அடிப்படையில் வரையறுக்கப்படுகின்றன""")
        z=word.translate(from_lang="ta",to="en")
        print(z)

   def vagaigalin_vilakkam(self):
         if self.objects==None:
            print("""பெயர்ச்சொல் என்பது பொதுவாக உயிரினங்கள், இடங்கள், செயல்கள், குணங்கள், இருப்பு நிலைகள் அல்லது யோசனைகள் போன்ற ஒரு குறிப்பிட்ட பொருள் அல்லது பொருட்களின் தொகுப்பின் பெயராக செயல்படும் ஒரு சொல். லெக்சிகல் பிரிவுகள் அவற்றின் உறுப்பினர்கள் மற்ற வகையான வெளிப்பாடுகளுடன் இணைக்கும் வழிகளின் அடிப்படையில் வரையறுக்கப்படுகின்றன""")
         else:
             print(vilakkam[self.__objects]["Villakkam"]);print()
             for i,j in vilakkam[self.__objects]["example"].items():print(i,j);print()
             

    
    
               
               
                   
       
                



