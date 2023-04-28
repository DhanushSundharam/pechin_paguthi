import peyarsorgalin_vilakkanggal

class pechin_paguthi(peyarsorgalin_vilakkanggal.peyarsorgalin_vilakkanggal):
    """பெயர்ச்சொற்களை ஆங்கிலத்தில் "nouns” என அழைக்கப்படுகிறது. இச்சொல் இலத்தீன் மொழியில் "nōmen" (பெயர்) என்ற சொல்லில் இருந்து மருவி ஆங்கிலத்தில் பயன்படும் சொல்லாகும்.

ஆங்கிலப் பெயர்சொற்கள் (Nouns) என்பன மனிதர்கள், இடங்கள், பொருற்கள், உயிரினங்கள், உணர்வுகள் போன்றவற்றை குறிப்பதற்கான "பெயர்கள்" அல்லது "பெயர்ச்சொற்கள்" ஆகும்.
"""
    def  __init__(self, word,type_of_word=False):
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

    
   
    
    
    

#if __name__=="__main__"  :
            #x=peyarsol("madurai")
            #z=peyarsol("madurais")
            #print(z.peyarsol_vagaigal_perungal())
            #z.peyarsol_vagaigal()
            #help(peyarsol)
            #print(x.peyarsol_vagaigal_perungal())
            #x.peyarsol_vagaigal()
