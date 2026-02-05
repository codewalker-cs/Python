import random
print("\n"*200)
print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

list_hangman = [
        r'''
        _______
     |/      |
     |         
     |         
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |         
     |        
     |         
     |
 ____|___
 ''', 
 '''
        _______
     |/      |
     |      (_)
     |      \  
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \| 
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /  
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
 ____|___
 '''
    ]

words = [
    # Nature
    "tree", "river", "mountain", "ocean", "forest", "desert", "valley", "waterfall", 
    "island", "volcano", "glacier", "canyon", "sunrise", "sunset", "rainbow", "meadow", 
    "prairie", "savanna", "cliff", "tide", "storm", "thunder", "lightning", "snowflake", 
    "hail", "breeze", "cloud", "dew", "earthquake", "hurricane", "tornado", "whirlpool",

    # Animals
    "lion", "tiger", "elephant", "giraffe", "zebra", "kangaroo", "penguin", "dolphin", 
    "whale", "shark", "octopus", "parrot", "eagle", "hawk", "peacock", "ostrich", "rabbit", 
    "squirrel", "bear", "wolf", "fox", "cheetah", "panda", "crocodile", "snail", "butterfly", 
    "dragonfly", "firefly", "beetle", "ant", "honeybee",

    # Food
    "apple", "banana", "grape", "mango", "watermelon", "pineapple", "strawberry", 
    "blueberry", "cherry", "peach", "orange", "pear", "plum", "kiwi", "avocado", 
    "broccoli", "carrot", "cucumber", "lettuce", "potato", "tomato", "onion", "garlic", 
    "pepper", "spinach", "mushroom", "cabbage", "pumpkin", "bread", "cheese", "butter", 
    "yogurt", "honey", "pasta", "rice", "beans", "chocolate", "coffee", "tea", "juice",

    # Emotions & Feelings
    "happiness", "joy", "sadness", "anger", "love", "fear", "excitement", "relief", 
    "pride", "envy", "compassion", "guilt", "shame", "grief", "courage", "bravery", 
    "hope", "trust", "loyalty", "gratitude", "contentment", "frustration", "disappointment", 
    "boredom", "enthusiasm", "serenity", "peace", "admiration", "melancholy", "jealousy", 
    "affection",

    # Sports & Activities
    "soccer", "basketball", "tennis", "baseball", "golf", "cricket", "volleyball", 
    "badminton", "hockey", "swimming", "surfing", "cycling", "skating", "skiing", 
    "snowboarding", "gymnastics", "wrestling", "boxing", "karate", "yoga", "meditation", 
    "hiking", "camping", "fishing", "running", "jogging", "marathon", "archery", 
    "horseback", "rowing", "canoeing",

    # Everyday Objects
    "table", "chair", "sofa", "bed", "pillow", "blanket", "lamp", "mirror", "clock", 
    "calendar", "curtain", "window", "door", "carpet", "towel", "broom", "bucket", 
    "umbrella", "notebook", "pencil", "pen", "eraser", "ruler", "backpack", "wallet", 
    "key", "shoe", "sock", "hat", "scarf", "gloves", "watch", "sunglasses", "belt",

    # Clothing
    "shirt", "pants", "jeans", "sweater", "jacket", "coat", "dress", "skirt", "shorts", 
    "suit", "tie", "boots", "sandals", "slippers", "blouse", "leggings", "cap", "glasses", 
    "earrings", "necklace", "bracelet", "ring",

    # Music & Art
    "guitar", "piano", "violin", "drum", "flute", "trumpet", "saxophone", "cello", 
    "harp", "accordion", "microphone", "concert", "melody", "harmony", "rhythm", 
    "chorus", "orchestra", "painting", "sculpture", "drawing", "sketch", "mural", 
    "portrait", "self-portrait", "abstract", "watercolor", "oil painting", "canvas", 
    "gallery", "museum", "calligraphy",

    # Travel & Places
    "city", "village", "town", "suburb", "capital", "beach", "resort", "hotel", "hostel", 
    "airport", "train", "subway", "taxi", "bus", "road", "highway", "bridge", "tunnel", 
    "harbor", "lighthouse", "castle", "palace", "temple", "church", "mosque", "monument", 
    "market", "plaza", "square", "fountain", "skyscraper",

    # Weather & Seasons
    "summer", "winter", "autumn", "spring", "rain", "snow", "hailstorm", "fog", "mist", 
    "cloudy", "sunny", "breeze", "humidity", "drought", "frost", "heatwave", "drizzle", 
    "monsoon", "hailstone",

    # Household & Kitchen
    "spoon", "fork", "knife", "plate", "bowl", "cup", "glass", "mug", "tray", "pot", 
    "pan", "stove", "oven", "microwave", "fridge", "freezer", "dishwasher", "blender", 
    "toaster", "kettle", "napkin", "chopping board", "grater", "peeler", "whisk", 
    "ladle", "strainer", "colander", "measuring cup", "rolling pin",

    # Health & Body
    "heart", "lungs", "brain", "liver", "kidneys", "stomach", "skin", "bones", "muscles", 
    "veins", "nerves", "eyes", "ears", "nose", "mouth", "teeth", "tongue", "fingers", 
    "toes", "knees", "elbows", "wrists", "spine", "ribcage",

    # Professions
    "doctor", "nurse", "teacher", "engineer", "artist", "musician", "actor", "writer", 
    "chef", "baker", "pilot", "firefighter", "police", "farmer", "scientist", "lawyer", 
    "judge", "architect", "dentist", "veterinarian", "journalist", "photographer", 
    "electrician", "plumber", "carpenter",

    # Miscellaneous
    "festival", "celebration", "holiday", "weekend", "vacation", "dream", "memory", 
    "story", "legend", "myth", "adventure", "fortune", "luck", "wisdom", "friendship", 
    "family", "kindness", "honesty", "humor", "patience", "forgiveness", "imagination"
]

word=random.choice(words)

placeholder=""

for w in range(len(word)):
    placeholder+="_"
print(placeholder)
display=list(placeholder)

lives=6

while display!=list(word) and lives>0:
    
    letter_gu=input("guess the letter:").lower()
    
    if letter_gu in display:
        print("Letter is already guessed")
        continue
    j=0

    for i in range(len(word)):
        if letter_gu==word[i]:
            display[i]=word[i]
            j+=1
        
    if j==0 and lives-1>0:
        lives-=1
        print("\nIncorrect guess")
        print(f"Only {lives} are remaining\n")
        print(list_hangman[-lives])
        continue
    elif j==0 and lives-1==0:
        print("You lose")
        print(f"your word was {word}")
        exit()
    
    for j in range(len(word)):
        print(display[j],end="")
    
    print("\n")

print("You won")
print(f"your word was {word}")