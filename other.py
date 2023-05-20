## Short Story 1:
story_1 = 'The dog ran home, and the cat followed to play. They arrived and the house was empty. The dog whined, and the cat meowed in response. They searched every room but found no sign of the owner. Feeling worried and confused, they decided to sit by the door and wait. Hours passed, and as the sun began to set, they started to give up hope. They heard the sound of a car that was pulling into the driveway. They rushed to the door, wagging their tails and meowing excitedly. The owner walked in and scooped both of them up, giving each a pat on the head. "I am sorry I was gone for a long walk and came back late today," the owner said. "I did not mind because I am so happy to be back and see you both, waiting for me."'
story_2 = 'The dog ran home. The cat followed. They arrived. The house was empty. The dog whined. The cat meowed. They searched every room. There was no sign of the owner. Feeling worried, they decided to sit by the door. Hours passed. The sun began to set. They heard the sound of a car pulling into the driveway. They rushed. They wagged their tails. The cat was meowing excitedly. The owner walked in and scooped them up. The owner gave them a pat on the head. "I am sorry that I was gone for a long walk," the owner said. "I am back and so happy to see you both."'
story_3 = 'They searched every room, pulling curtains and drawers. They saw no sign of the owner. They were confused and worried, but they decided to sit and wait by the door. Hours passed and it was sunset. They heard a sound. A car was pulling into the driveway. They rushed wagging their tails to the door. The owner arrived, late but happily. They scooped the dog and cat, giving each a pat on the head. "Sorry for the wait," the owner said. The dog and cat meowed in response because they were happy to see their owner.'


story_1_words = story_1.split()
story_2_words = story_2.split()
story_3_words = story_3.split()

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

