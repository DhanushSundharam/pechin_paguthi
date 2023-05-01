import peyarsorgalin_vilakkanggal
import pirathipeyar_vilakkanggal
import inaippu_sorgal_vilakkangal
import re
class pechin_paguthi(peyarsorgalin_vilakkanggal.peyarsorgalin_vilakkanggal,pirathipeyar_vilakkanggal.pirathipeyar,inaippu_sorgal_vilakkangal.inaippu_sorgal_vilakkangal):


    

    def  peyarsol(self, word,type_of_word=False):
        """பெயர்ச்சொற்களை ஆங்கிலத்தில் "nouns” என அழைக்கப்படுகிறது. இச்சொல் இலத்தீன் மொழியில் "nōmen" (பெயர்) என்ற சொல்லில் இருந்து மருவி ஆங்கிலத்தில் பயன்படும் சொல்லாகும்.ஆங்கிலப் பெயர்சொற்கள் (Nouns) என்பன மனிதர்கள், இடங்கள், பொருற்கள், உயிரினங்கள், உணர்வுகள் போன்றவற்றை குறிப்பதற்கான "பெயர்கள்" அல்லது "பெயர்ச்சொற்கள்" ஆகும்."""
        self.word = word
        self.type_word=type_of_word
        self.noun_type = self.peyarsol_vagaigal_perungal()

    def peyarsol_vagaigal_perungal(self):
        if self.word.istitle():
            return "Proper Nouns - உரித்தானப் பெயர்சொற்கள்"
        elif self.type_word in ["people", "animal", "book", "table","thing","fruit","place"] or self.word in ['apple', 'banana', 'car', 'dog', 'cat', 'book', 'phone', 'computer', 'desk', 'chair', 'table', 'window', 'door', 'lamp', 'pen', 'pencil', 'notebook', 'bag', 'shoe', 'shirt', 'pants', 'hat', 'coat', 'jacket', 'socks', 'towel', 'soap', 'toothbrush', 'toothpaste', 'water', 'coffee', 'tea', 'juice', 'milk', 'bread', 'cheese', 'meat', 'vegetables', 'fruit', 'rice', 'noodle', 'soup', 'salad', 'burger', 'pizza', 'fries', 'chicken', 'beef', 'pork', 'fish', 'egg', 'butter', 'oil', 'sugar', 'salt', 'pepper', 'vinegar', 'mustard', 'ketchup', 'mayonnaise', 'honey', 'jam', 'chocolate', 'candy', 'cookie', 'ice cream', 'yogurt', 'cheesecake', 'pie', 'cake', 'candle', 'gift', 'toy', 'game', 'movie', 'music', 'painting', 'sculpture', 'photograph', 'bookshelf', 'paintbrush', 'canvas', 'easel', 'guitar', 'piano', 'drum', 'violin', 'trumpet', 'flute', 'camera', 'telescope', 'microscope', 'binoculars', 'map', 'globe', 'calendar', 'clock']:

            return "Common Nouns - பொதுவான பெயர்சொற்கள்"
        elif self.type_word in ["flock", "herd", "swarm","unit","Pack"] or self.word in ['army', 'audience', 'band', 'board', 'cast', 'choir', 'class', 'club', 'committee', 'crew', 'crowd', 'family', 'flock', 'gang', 'group', 'herd', 'hive', 'jury', 'mob', 'orchestra', 'panel', 'party', 'staff', 'team', 'tribe', 'assembly', 'bunch', 'cabinet', 'camp', 'cast', 'clan', 'colony', 'community', 'congregation', 'council', 'faculty', 'federation', 'fleet', 'gaggle', 'horde', 'household', 'league', 'mass', 'pack', 'parliament', 'posse', 'public', 'school', 'swarm', 'syndicate', 'troop', 'union', 'unit', 'zoo', 'bevy', 'brigade', 'brood', 'covey', 'delegation', 'ensemble', 'gang', 'horde', 'knot', 'muster', 'outfit', 'platoon', 'quiver', 'saga', 'squad', 'squadron', 'troupe', 'youth', 'band', 'batch', 'block', 'cluster', 'collection', 'conglomeration', 'crop', 'drift', 'flock', 'formation', 'host', 'lot', 'mound', 'nest', 'party', 'pod', 'raft', 'set', 'shoal', 'throng', 'tuft', 'batch', 'brood', 'clutch', 'fleet', 'flight', 'gathering', 'herd', 'litter', 'pack', 'school', 'swarm', 'team', 'tidings', 'clique']:

            return "Collective Nouns - கூட்டுப் பெயர்சொற்கள்"
        elif self.type_word in ["love", "happiness", "peace","untouchable","feel","feeling"] or self.word in ['love', 'hate', 'hope', 'fear', 'courage', 'happiness', 'sadness', 'anger', 'peace', 'trust', 'faith', 'patience', 'tolerance', 'compassion', 'joy', 'pain', 'pleasure', 'kindness', 'generosity', 'forgiveness', 'empathy', 'sympathy', 'grace', 'mercy', 'gratitude', 'humility', 'pride', 'envy', 'jealousy', 'justice', 'wisdom', 'knowledge', 'understanding', 'truth', 'reality', 'creativity', 'imagination', 'passion', 'beauty', 'freedom', 'discipline', 'determination', 'perseverance', 'persistence', 'resilience', 'responsibility', 'accountability', 'loyalty', 'integrity', 'respect', 'fairness', 'equity', 'compassion', 'harmony', 'balance', 'moderation', 'patience', 'calm', 'serenity', 'contentment', 'grace', 'generosity', 'humility', 'kindness', 'charity', 'forgiveness', 'gratitude', 'wisdom', 'knowledge', 'curiosity', 'imagination', 'creativity', 'innovation', 'hopefulness', 'optimism', 'bravery', 'courage', 'tenacity', 'determination', 'ambition', 'confidence', 'trustworthiness', 'dependability', 'accountability', 'responsibility', 'honesty', 'loyalty', 'friendship', 'understanding', 'patience', 'compassion', 'empathy', 'tolerance', 'flexibility', 'adventure', 'curiosity', 'passion', 'enthusiasm', 'excitement']:

            return "Abstract Nouns - நுண் பெயர்ச்சொற்கள்"
        elif self.type_word in ["taste","touch","sight","hearing","smell"] or self.word in ['car', 'tree', 'house', 'book', 'computer', 'desk', 'chair', 'phone', 'shoe', 'table', 'dog', 'cat', 'ball', 'bottle', 'cup', 'pen', 'pencil', 'bag', 'hat', 'shirt', 'pants', 'jacket', 'hat', 'socks', 'umbrella', 'lamp', 'clock', 'mirror', 'window', 'door', 'floor', 'ceiling', 'wall', 'roof', 'grass', 'flower', 'rock', 'mountain', 'river', 'ocean', 'lake', 'beach', 'cloud', 'sun', 'moon', 'planet', 'galaxy', 'fish', 'bird', 'insect', 'snake', 'frog', 'lizard', 'elephant', 'lion', 'tiger', 'bear', 'giraffe', 'monkey', 'horse', 'cow', 'sheep', 'chicken', 'pig', 'goat', 'duck', 'boat', 'ship', 'airplane', 'train', 'bus', 'bicycle', 'motorcycle', 'truck', 'bridge', 'building', 'skyscraper', 'street', 'park', 'airport', 'hospital', 'school', 'church', 'museum', 'library', 'store', 'restaurant', 'coffee', 'tea', 'bread', 'cheese', 'meat', 'vegetable', 'fruit', 'candy', 'cookie', 'ice cream']:

            return "Concrete Nouns - திடப் பெயர்சொற்கள்"
        elif " " in self.word:
            return "Compound Nouns - கலவைப் பெயர்சொற்கள்"
        elif self.word.endswith("s") or self.word.isdigit():
            return "Countable Nouns - கணக்கிடுப் பெயர்சொற்கள்"
        else:
            return "Uncountable Nouns - கணக்கிடமுடியாப் பெயர்சொற்கள்"

    def pirathipeyar(self,pronoun):
            """சுட்டுப்பெயர் சொல் என்பது ஒரு பெயரை அல்லது பெயர் சொல்லை குறிப்பிடாமல், அதற்குப் பதிலாக சுட்டிக்காட்டுவதற்கு பயன்படும் சொற்களே "சுட்டுப்பெயர்" என்றழைக்கப்படுகின்றன. இவற்றை தமிழில் "பிரதிப்பெயர்கள்", "பதிலிடுச்சொற்கள்" என்றும் அழைப்பர். ஆங்கிலத்தில் "Pronouns" என அழைக்கப்படும்."""
            pronouns=pronoun.lower()

            
            if pronouns in ["I", "you", "he", "she", "it", "we", "they"]:
                return "எழுவாய் சுட்டுப்பெயர்கள்"

            
            elif pronouns in ["me", "you", "him", "her", "it", "us", "them"]:
                return  "செயப்படுபொருள் சுட்டுப்பெயர்கள்"

            
            elif pronouns in ["myself", "yourself", "himself", "herself", "itself", "ourselves", "themselves"]:
                return "அனிச்சைச் செயல் சுட்டுப்பெயர்கள்"

            
            elif pronouns in ["mine", "yours", "his", "hers", "its", "ours", "theirs","my","your","his","her","its","our","your","their"]:
                return "ஆறாம் வேற்றுமை (உரிமையைக் குறிக்கும்)"

            
            elif pronoun in ["this", "that", "these", "those"]:
                return " குறிப்பிடுச் சுட்டுப்பெயர்கள்"

            
            elif pronouns in ["who", "whom", "whose", "which", "that"]:
                return " உரிச் சுட்டுப்பெயர்கள்"

            
            elif pronouns in ["who", "whom", "whose", "what", "which"]:
                return "கேள்வி சுட்டுப்பெயர்கள்"

            
            elif pronouns in ["anybody", "anyone", "anything", "everybody", "everyone", "everything", "nobody", "no one", "nothing", "somebody", "someone", "something", "all", "any", "both", "each", "either", "neither", "none", "several", "some"]:
                return " இச் சுட்டுப்பெயர்கள் பயன்படுகின்றன"

           
            else:
                return "இந்த வார்த்தை ஒரு பிரதிபெயர் அல்ல"

    def inaippu_sorgal(self,sentence):
                    """ஆங்கில இணைப்புச் சொற்கள் என்றால், ஆங்கில பேச்சின்கூறுகளில் உள்ளடங்கும் எட்டுக் கூறுகளில் ஒன்றாகும். இவை சொற்கள் (words), சொற்றொடர்கள் (Phrases),  மற்றும் வாக்கியக் கூறுகள் (clauses) போன்றவற்றை இணைக்கப் பயன்படும் சிறிய சொற்கள் மற்றும் சொற்றொடர்கள் ஆகும். வாக்கியக் கூறுகளை இணைத்து நீண்ட ஒரு வாக்கியமாக அல்லது வாக்கியத் தொடராக பொருளை உணர்த்த இந்த இணைப்புச்சொற்கள் ஆங்கில இலக்கணப் பயன்பாட்டில் மிக முக்கியமானவைகளாகும்."""
                    coordinating_conjunctions = ["and", "but", "for", "nor", "or", "so", "yet"]
                    subordinating_conjunctions = ["after", "although", "as", "because", "before", "even if", "even though", "if", "in order that", "once", "provided that", "rather than", "since", "so that", "than", "that", "though", "unless", "until", "when", "whenever", "where", "whereas", "wherever", "whether", "while"]
                    correlative_conjunctions = ["both", "either", "neither", "not only", "but also", "whether", "or"]
                    conjunctive_adverbs = ["accordingly", "also", "besides", "consequently", "finally", "further", "furthermore", "hence", "however", "incidentally", "indeed", "instead", "likewise", "meanwhile", "moreover", "namely", "nevertheless", "next", "nonetheless", "otherwise", "similarly", "still", "subsequently", "then", "therefore", "thus"]

                    words = re.findall(r'\b\w+\b', sentence)

                    conjunction_types = []

                    for i in range(len(words)):
                        word = words[i].lower()
                        if word in coordinating_conjunctions:
                            conjunction_types.append("ஒருங்கிணைப்பு இணைப்புச்சொற்கள்")
                        elif word in subordinating_conjunctions:
                            conjunction_types.append("சார்ந்த இணைப்புச்சொற்கள்")
                        elif word in correlative_conjunctions:
                            conjunction_types.append("ஒப்புமை இணைப்புச்சொற்கள்")
                        elif word in conjunctive_adverbs:
                            conjunction_types.append("இணைப்பு வினையெச்சங்கள்")
                    
                    return conjunction_types

           
    def vinaiachingalin_vagaigal_perungal(self,sentence):
            manner_adverbs = ['quickly', 'slowly', 'carefully']
            place_adverbs = ['here', 'there', 'everywhere']
            time_adverbs = ['now', 'yesterday', 'tomorrow']
            frequency_adverbs = ['always', 'often', 'never']
            degree_adverbs = ['very', 'quite', 'extremely']
            """வினெயெச்சங்கள் என்றால் என்ன? வினையெச்சங்கள் என்றால் ஆங்கிலப் பேச்சின் கூறுகளில் ஒன்று என்பதை நாம் ஏற்கெனவே கற்றுள்ளோம். இவை முக்கியமாக ஒரு வினையின் அல்லது வினைச்சொல்லின் தன்மையை விவரித்துக் கூற பயன்படும் சொற்கள் ஆகும். இவற்றை வினையெச்சங்கள், வினையடைகள், வினையுரிச் சொற்கள் என பல்வேறு பெயர்களில் தமிழில் அழைக்கப்படுகின்றது. ஆங்கிலத்தில் "Adverbs" என்றழைப்பர்.ஆங்கிலத்தில் இவற்றை ஐந்து பிரிவுகளாக வகை படுத்தப்பட்டுள்ளன. அவற்றையே "வினையெச்சங்களின் வகைகள்" என்றழைக்கப்படுகின்றன."""
           
            words = sentence.split()
            for word in words:
                
                if re.search(r'\b(' + '|'.join(manner_adverbs) + r')\b', word):
                    return 'மாதிரி வினையெச்சங்கள்'
                
                elif re.search(r'\b(' + '|'.join(place_adverbs) + r')\b', word):
                    return 'இட வினையெச்சங்கள்'
               
                elif re.search(r'\b(' + '|'.join(time_adverbs) + r')\b', word):
                    return 'கால வினையெச்சங்கள்'
                
                elif re.search(r'\b(' + '|'.join(frequency_adverbs) + r')\b', word):
                    return 'நடப்புத்தன்மை வினையெச்சங்கள்'
                
                elif re.search(r'\b(' + '|'.join(degree_adverbs) + r')\b', word):
                    return 'அளவு வினையெச்சங்கள்'
            
            return None
            

    
   
    
    
    

