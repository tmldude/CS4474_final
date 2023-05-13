import random

vocabulary = "the, dog, ran, home, cat, followed, play, arrived, house, empty, whined, meowed, response, searched, every, room, sign, owner, feeling, worried, confused, decided, sit, door, wait, hours, passed, sun, began, set, give, hope, heard, sound, car, pulling, driveway, rushed, wagging, tails, meowing, excitedly, walked, scooped, both, up, giving, each, pat, head, sorry, gone, long, walk, late, today, mind, happy, back, just, and, they, was, in, but, found, no, of, to, as, started, i, am, for, came, then, a, into, them, on, am, said, did, not, so, be, because, see, waiting, by, you, me, their, gave, curtains, drawers"
vocabulary_words = vocabulary.split(', ')

# random.shuffle(vocabulary_words)
print(set(vocabulary_words))
print(len(set(vocabulary_words)))


cleaned_vocab_words = []
for word in vocabulary_words:
    word.replace(",", "")
    word.replace(" ", "")
    word.strip()
    # print(word)
    cleaned_vocab_words.append(word)
# print(cleaned_vocab_words)

def words_missing(story):
    not_in = []
    for word in story:
        cleaned = word.strip()
        cleaned = cleaned.replace(",", "")
        cleaned = cleaned.replace(".", "")
        cleaned = cleaned.strip()
        cleaned = cleaned.lower()
        #cleaned = cleaned.replace("'","")
        cleaned = cleaned.replace('"','')
        if cleaned not in vocabulary_words:
            not_in.append(cleaned)
    return not_in


story_1 = 'The dog ran home, and the cat followed to play. They arrived and the house was empty. The dog whined, and the cat meowed in response. They searched every room but found no sign of the owner. Feeling worried and confused, they decided to sit by the door and wait. Hours passed, and as the sun began to set, they started to give up hope. But then they heard the sound of a car pulling into the driveway. They rushed to the door, wagging their tails and meowing excitedly. The owner walked in and scooped both of them up, giving each a pat on the head. "I am sorry I was gone for a long walk and came back late today," the owner said. "But I did not mind because I am so happy to be back and see you both, just waiting for me."'
story_1_words = story_1.split()
# print(story_1_words)

story_2 = 'The dog ran home. The cat followed. They arrived. The house was empty. The dog whined. The cat meowed. They searched every room. No sign of the owner. Feeling worried, they decided to sit by the door. Hours passed. The sun began to set. They heard the sound of a car pulling into the driveway. They rushed. Wagging tails. Meowing excitedly. The owner walked in and scooped them up. The owner gave them a pat on the head. "Sorry, gone for a long walk," the owner said. "But I am back. Happy to see you."'
story_2_words = story_2.split()

story_3 = 'They searched every room, pulling curtains and drawers. No sign of the owner. Confused and worried, they decided to sit and wait by the door. Hours passed, sun set. They heard sound, car pulling into driveway. They rushed, wagging tails. The owner arrived, late but happy. They scooped dog and cat, giving each pat on head. "Sorry, wait," said owner. The dog and cat meowed in response, happy to see their owner.'
story_3_words = story_3.split()

story_4 = 'The dog ran home. The cat followed. They arrived at an empty house. Feeling worried and confused, they searched every room. No sign of the owner. They decided to sit by the door and wait. Hours passed as the sun began to set. They heard a sound—a car pulling into the driveway. They rushed, wagging tails. The owner arrived, late but happy. They scooped both up, giving each a pat on the head. "Sorry, gone for a long walk," said the owner. The dog and cat didn not mind. They were happy to be back, just in time.'
story_4_words = story_4.split()

story_5 = 'The sun set as the worried owner arrived. The house was empty, and the owner felt confused. They decided to search every room, hoping to find their beloved cat. Hours passed, and their hope began to fade. They heard a sound outside—a car pulling into the driveway. Excitedly, they rushed to the door, giving each other a glance. The door opened, and their cat meowed, wagging its tail happily. The owner scooped up the cat, relieved to have found it. "Sorry I am late," the owner said, patting the head of the cat. The cat did not mind. It was just happy to be back home, sitting by the window, watching as the sun rose again'
story_5_words = story_5.split()


print(words_missing(story_1_words))
print(words_missing(story_2_words))
print(words_missing(story_3_words))
print(words_missing(story_4_words))
print(words_missing(story_5_words))




def add_unique(lst, story):
    for word in story:
            cleaned = word.strip()
            cleaned = cleaned.replace(",", "")
            cleaned = cleaned.replace(".", "")
            cleaned = cleaned.strip()
            cleaned = cleaned.lower()
            cleaned = cleaned.replace("-", "")
            #cleaned = cleaned.replace("'","")
            cleaned = cleaned.replace('"','')
            if cleaned not in lst:
                lst.append(cleaned)

all_words = []
add_unique(all_words, story_1_words)
add_unique(all_words, story_2_words)
add_unique(all_words, story_3_words)
print(all_words)
print(len(all_words))


def words_missing_2(story):
    not_in = []
    for word in story:
        cleaned = word.strip()
        cleaned = cleaned.replace(",", "")
        cleaned = cleaned.replace(".", "")
        cleaned = cleaned.strip()
        cleaned = cleaned.lower()
        #cleaned = cleaned.replace("'","")
        cleaned = cleaned.replace('"','')
        if cleaned not in all_words:
            not_in.append(cleaned)
    return not_in

print(words_missing_2(vocabulary_words))

# ['the', 'dog', 'ran', 'home', 'and', 'cat', 'followed', 'to', 'play', 'when', 'they', 'arrived', 
#  'house', 'was', 'empty', 'whined', 'meowed', 'in', 'response', 'searched', 'every', 'room', 'but', 
#  'found', 'no', 'sign', 'of', 'owner', 'feeling', 'worried', 'confused', 'decided', 'sit', 'by', 'door', 'wait', 
#  'hours', 'passed', 'as', 'sun', 'began', 'set', 'started', 'give', 'up', 'hope', 'then', 'heard', 'sound', 'a', 
#  'car', 'pulling', 'into', 'driveway', 'rushed', 'wagging', 'their', 'tails', 'meowing', 'excitedly', 'walked', 
#  'scooped', 'both', 'them', 'giving', 'each', 'pat', 'on', 'head', 'i', 'am', 'sorry', 'gone', 'for', 'long', 'walk', 
#  'came', 'back', 'late', 'today', 'said', 'did', 'not', 'mind', 'because', 'so', 'happy', 'be', 'see', 'you', 'here', 
#  'just', 'waiting', 'me', 'were', 'got', 'curtains', 'opening', 'drawers']

        


