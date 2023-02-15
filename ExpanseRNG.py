import random

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#abilities
#stats = {
   # "Accuracy": random.randint(-2,4),
  #  "Constitution": random.randint(-2,4),
 #   "Fighting": random.randint(-2,4),
  #  "Communication": random.randint(-2,4),
 #   "Dexterity": random.randint(-2,4),
 #   "Intelligence": random.randint(-2,4),
 #   "Perception": random.randint(-2,4),
 #   "Strength": random.randint(-2,4),
 #   "Willpower": random.randint(-2,4),
    


  #  }

#Generate Stats
AccRand = random.randint(3,18)
ConRand = random.randint(3,18)
FigRand = random.randint(3,18)
ComRand = random.randint(3,18)
DexRand = random.randint(3,18)
IntRand = random.randint(3,18)
PerRand = random.randint(3,18)
StrRand = random.randint(3,18)
WilRand = random.randint(3,18)

#Converting Accuracy roll to a stat value
if AccRand == 3:
    AccValue = "-2"
elif AccRand == 4:
    AccValue = "-1"
elif AccRand == 5:
    AccValue = "-1"
elif AccRand == 6:
    AccValue = "0"
elif AccRand == 7:
    AccValue = "0"
elif AccRand == 8:
    AccValue = "0"
elif AccRand == 9:
    AccValue = "1"
elif AccRand == 10:
    AccValue = "1"
elif AccRand == 11:
    AccValue = "1"
elif AccRand == 12:
    AccValue = "2"
elif AccRand == 13:
    AccValue = "2"
elif AccRand == 14:
    AccValue = "2"
elif AccRand == 15:
    AccValue = "3"
elif AccRand == 16:
    AccValue = "3"
elif AccRand == 17:
    AccValue = "3"
elif AccRand == 18:
    AccValue = "4"


#Converting Constitution roll to a stat value
if ConRand == 3:
    ConValue = "-2"
elif ConRand == 4:
    ConValue = "-1"
elif ConRand == 5:
    ConValue = "-1"
elif ConRand == 6:
    ConValue = "0"
elif ConRand == 7:
    ConValue = "0"
elif ConRand == 8:
    ConValue = "0"
elif ConRand == 9:
    ConValue = "1"
elif ConRand == 10:
    ConValue = "1"
elif ConRand == 11:
    ConValue = "1"
elif ConRand == 12:
    ConValue = "2"
elif ConRand == 13:
    ConValue = "2"
elif ConRand == 14:
    ConValue = "2"
elif ConRand == 15:
    ConValue = "3"
elif ConRand == 16:
    ConValue = "3"
elif ConRand == 17:
    ConValue = "3"
elif ConRand == 18:
    ConValue = "4"

#Converting Fighting roll to a stat value
if FigRand == 3:
    FigValue = "-2"
elif FigRand == 4:
    FigValue = "-1"
elif FigRand == 5:
    FigValue = "-1"
elif FigRand == 6:
    FigValue = "0"
elif FigRand == 7:
    FigValue = "0"
elif FigRand == 8:
    FigValue = "0"
elif FigRand == 9:
    FigValue = "1"
elif FigRand == 10:
    FigValue = "1"
elif FigRand == 11:
    FigValue = "1"
elif FigRand == 12:
    FigValue = "2"
elif FigRand == 13:
    FigValue = "2"
elif FigRand == 14:
    FigValue = "2"
elif FigRand == 15:
    FigValue = "3"
elif FigRand == 16:
    FigValue = "3"
elif FigRand == 17:
    FigValue = "3"
elif FigRand == 18:
    FigValue = "4"

#Converting Communication roll to a stat value
if ComRand == 3:
    ComValue = "-2"
elif ComRand == 4:
    ComValue = "-1"
elif ComRand == 5:
    ComValue = "-1"
elif ComRand == 6:
    ComValue = "0"
elif ComRand == 7:
    ComValue = "0"
elif ComRand == 8:
    ComValue = "0"
elif ComRand == 9:
    ComValue = "1"
elif ComRand == 10:
    ComValue = "1"
elif ComRand == 11:
    ComValue = "1"
elif ComRand == 12:
    ComValue = "2"
elif ComRand == 13:
    ComValue = "2"
elif ComRand == 14:
    ComValue = "2"
elif ComRand == 15:
    ComValue = "3"
elif ComRand == 16:
    ComValue = "3"
elif ComRand == 17:
    ComValue = "3"
elif ComRand == 18:
    ComValue = "4"

#Converting Dexterity roll to a stat value
if DexRand == 3:
    DexValue = "-2"
elif DexRand == 4:
    DexValue = "-1"
elif DexRand == 5:
    DexValue = "-1"
elif DexRand == 6:
    DexValue = "0"
elif DexRand == 7:
    DexValue = "0"
elif DexRand == 8:
    DexValue = "0"
elif DexRand == 9:
    DexValue = "1"
elif DexRand == 10:
    DexValue = "1"
elif DexRand == 11:
    DexValue = "1"
elif DexRand == 12:
    DexValue = "2"
elif DexRand == 13:
    DexValue = "2"
elif DexRand == 14:
    DexValue = "2"
elif DexRand == 15:
    DexValue = "3"
elif DexRand == 16:
    DexValue = "3"
elif DexRand == 17:
    DexValue = "3"
elif DexRand == 18:
    DexValue = "4"

#Converting Intelligence roll to a stat value
if IntRand == 3:
    IntValue = "-2"
elif IntRand == 4:
    IntValue = "-1"
elif IntRand == 5:
    IntValue = "-1"
elif IntRand == 6:
    IntValue = "0"
elif IntRand == 7:
    IntValue = "0"
elif IntRand == 8:
    IntValue = "0"
elif IntRand == 9:
    IntValue = "1"
elif IntRand == 10:
    IntValue = "1"
elif IntRand == 11:
    IntValue = "1"
elif IntRand == 12:
    IntValue = "2"
elif IntRand == 13:
    IntValue = "2"
elif IntRand == 14:
    IntValue = "2"
elif IntRand == 15:
    IntValue = "3"
elif IntRand == 16:
    IntValue = "3"
elif IntRand == 17:
    IntValue = "3"
elif IntRand == 18:
    IntValue = "4"

#Converting Perception roll to a stat value
if PerRand == 3:
    PerValue = "-2"
elif PerRand == 4:
    PerValue = "-1"
elif PerRand == 5:
    PerValue = "-1"
elif PerRand == 6:
    PerValue = "0"
elif PerRand == 7:
    PerValue = "0"
elif PerRand == 8:
    PerValue = "0"
elif PerRand == 9:
    PerValue = "1"
elif PerRand == 10:
    PerValue = "1"
elif PerRand == 11:
    PerValue = "1"
elif PerRand == 12:
    PerValue = "2"
elif PerRand == 13:
    PerValue = "2"
elif PerRand == 14:
    PerValue = "2"
elif PerRand == 15:
    PerValue = "3"
elif PerRand == 16:
    PerValue = "3"
elif PerRand == 17:
    PerValue = "3"
elif PerRand == 18:
    PerValue = "4"

#Converting Strength roll to a stat value
if StrRand == 3:
    StrValue = "-2"
elif StrRand == 4:
    StrValue = "-1"
elif StrRand == 5:
    StrValue = "-1"
elif StrRand == 6:
    StrValue = "0"
elif StrRand == 7:
    StrValue = "0"
elif StrRand == 8:
    StrValue = "0"
elif StrRand == 9:
    StrValue = "1"
elif StrRand == 10:
    StrValue = "1"
elif StrRand == 11:
    StrValue = "1"
elif StrRand == 12:
    StrValue = "2"
elif StrRand == 13:
    StrValue = "2"
elif StrRand == 14:
    StrValue = "2"
elif StrRand == 15:
    StrValue = "3"
elif StrRand == 16:
    StrValue = "3"
elif StrRand == 17:
    StrValue = "3"
elif StrRand == 18:
    StrValue = "4"

#Converting Willpower roll to a stat value
if WilRand == 3:
    WilValue = "-2"
elif WilRand == 4:
    WilValue = "-1"
elif WilRand == 5:
    WilValue = "-1"
elif WilRand == 6:
    WilValue = "0"
elif WilRand == 7:
    WilValue = "0"
elif WilRand == 8:
    WilValue = "0"
elif WilRand == 9:
    WilValue = "1"
elif WilRand == 10:
    WilValue = "1"
elif WilRand == 11:
    WilValue = "1"
elif WilRand == 12:
    WilValue = "2"
elif WilRand == 13:
    WilValue = "2"
elif WilRand == 14:
    WilValue = "2"
elif WilRand == 15:
    WilValue = "3"
elif WilRand == 16:
    WilValue = "3"
elif WilRand == 17:
    WilValue = "3"
elif WilRand == 18:
    WilValue = "4"


#Shows the Character ability scores
print(color.BOLD + "Accuracy: " + color.END + AccValue)
print(color.BOLD + "Constitution: " + color.END + ConValue)
print(color.BOLD + "Fighting: " + color.END + FigValue)
print(color.BOLD + "Communication: " + color.END + ComValue)
print(color.BOLD + "Dexterity: " + color.END + DexValue)
print(color.BOLD + "Intelligence: " + color.END + IntValue)
print(color.BOLD + "Perception: " + color.END + PerValue)
print(color.BOLD + "Strength: " + color.END + StrValue)
print(color.BOLD + "Willpower: " + color.END + WilValue)



#origins = ("Belter,Earther,Martain")
#Origin generator
origins = ("Belter","Earther","Martian")
origin = random.choices(origins)
print(f"Your origin is {origin}")



#Social Class generator for Belters
SocialRand = random.randint(2,12)
if 'Belter' in origin and SocialRand <= (5):
    print("Social Class is Outsider")
    SocialClassVal = "Outsider"
elif 'Belter' in origin and (SocialRand >= (6) and SocialRand <= (8)):
    print("Social Class is Lower Class")
    SocialClassVal = "Lower Class"
elif 'Belter' in origin and (SocialRand >= (9) and SocialRand <= (11)):
    print("Social Class is Middle Class")
    SocialClassVal = "Middle Class"
elif 'Belter' in origin and (SocialRand == (12)):
    print("Social Class is Upper Class")
    SocialClassVal = "Upper Class"

#Social Class generator for Martians
if 'Martian' in origin and SocialRand <= (2):
    print("Social Class is Outsider")
    SocialClassVal = "Outsider"
elif 'Martian' in origin and (SocialRand >= (3) and SocialRand <= (6)):
    print("Social Class is Lower Class")
    SocialClassVal = "Lower Class"
elif 'Martian' in origin and (SocialRand >= (7) and SocialRand <= (11)):
    print("Social Class is Middle Class")
    SocialClassVal = "Middle Class"
elif 'Martian' in origin and (SocialRand == (12)):
    print("Social Class is Upper Class")
    SocialClassVal = "Upper Class"

#Social Class generator for Earthers
if 'Earther' in origin and SocialRand <= (3):
    print("Social Class is Outsider")
    SocialClassVal = "Outsider"
elif 'Earther' in origin and (SocialRand >= (4) and SocialRand <= (6)):
    print("Social Class is Lower Class")
    SocialClassVal = "Lower Class"
elif 'Earther' in origin and (SocialRand >= (7) and SocialRand <= (10)):
    print("Social Class is Middle Class")
    SocialClassVal = "Middle Class"
elif 'Earther' in origin and (SocialRand >= (11)):
    print(f"Social Class is Upper Class")
    SocialClassVal = "Upper Class"

#Background Generator for Belter Outsiders
BackgroundRand = random.randint(1,6)
if 'Belter' in origin and 'Outsider' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Bohemian")
    BackgroundVal = "Bohemian"
elif 'Belter' in origin and 'Outsider' in SocialClassVal and BackgroundRand <= (4):
    print("Your Background is Exile")
    BackgroundVal = "Exile"
elif 'Belter' in origin and 'Outsider' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Outcast")
    BackgroundVal = "Outcast"

#Background Generator for Martian Outsiders
if 'Martian' in origin and 'Outsider' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Bohemian")
    BackgroundVal = "Bohemian"
elif 'Martian' in origin and 'Outsider' in SocialClassVal and BackgroundRand >=3 and BackgroundRand <= (4):
    print("Your Background is Exile")
    BackgroundVal = "Exile"
elif 'Martian' in origin and 'Outsider' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Outcast")
    BackgroundVal = "Outcast"

#Background Generator for Earther Outsiders
if 'Earther' in origin and 'Outsider' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Bohemian")
    BackgroundVal = "Bohemian"
elif 'Earther' in origin and 'Outsider' in SocialClassVal and BackgroundRand >=3 and BackgroundRand <= (4):
    print("Your Background is Exile")
    BackgroundVal = "Exile"
elif 'Earther' in origin and 'Outsider' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Outcast")
    BackgroundVal = "Outcast"

#Background Generator for Belter Lower Class
if 'Belter' in origin and 'Lower Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Military")
    BackgroundVal = "Military"
elif 'Belter' in origin and 'Lower Class' in SocialClassVal and BackgroundRand >=3 and BackgroundRand <= (4):
    print("Your Background is Laborer")
    BackgroundVal = "Laborer"
elif 'Belter' in origin and 'Lower Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Urban")
    BackgroundVal = "Urban"

#Background Generator for Martian Lower Class
if 'Martian' in origin and 'Lower Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Military")
    BackgroundVal = "Military"
elif 'Martian' in origin and 'Lower Class' in SocialClassVal and BackgroundRand <= (4):
    print("Your Background is Laborer")
    BackgroundVal = "Laborer"
elif 'Martian' in origin and 'Lower Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Urban")
    BackgroundVal = "Urban"

#Background Generator for Earther Lower Class
if 'Earther' in origin and 'Lower Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Military")
    BackgroundVal = "Military"
elif 'Earther' in origin and 'Lower Class' in SocialClassVal and BackgroundRand <= (4):
    print("Your Background is Laborer")
    BackgroundVal = "Laborer"
elif 'Earther' in origin and 'Lower Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Urban")
    BackgroundVal = "Urban"

#Background Generator for Belter Middle Class
if 'Belter' in origin and 'Middle Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Academic")
    BackgroundVal = "Academic"
elif 'Belter' in origin and 'Middle Class' in SocialClassVal and BackgroundRand >=3 and BackgroundRand <= (4):
    print("Your Background is Suburban")
    BackgroundVal = "Suburban"
elif 'Belter' in origin and 'Middle Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Trade")
    BackgroundVal = "Trade"

#Background Generator for Martian Middle Class
if 'Martian' in origin and 'Middle Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Academic")
    BackgroundVal = "Academic"
elif 'Martian' in origin and 'Middle Class' in SocialClassVal and BackgroundRand <= (4):
    print("Your Background is Suburban")
    BackgroundVal = "Suburban"
elif 'Martian' in origin and 'Middle Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Trade")
    BackgroundVal = "Trade"

#Background Generator for Earther Middle Class
if 'Earther' in origin and 'Middle Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Academic")
    BackgroundVal = "Academic"
elif 'Earther' in origin and 'Middle Class' in SocialClassVal and BackgroundRand <= (4):
    print("Your Background is Suburban")
    BackgroundVal = "Suburban"
elif 'Earther' in origin and 'Middle Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Trade")
    BackgroundVal = "Trade"

#Background Generator for Belter Upper Class
if 'Belter' in origin and 'Upper Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Aristocratic")
    BackgroundVal = "Aristocratic"
elif 'Belter' in origin and 'Upper Class' in SocialClassVal and BackgroundRand >=3 and BackgroundRand <= (4):
    print("Your Background is Corporate")
    BackgroundVal = "Corporate"
elif 'Belter' in origin and 'Upper Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Cosmopolitan")
    BackgroundVal = "Cosmopolitan"

#Background Generator for Martian Upper Class
if 'Martian' in origin and 'Upper Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Aristocratic")
    BackgroundVal = "Aristocratic"
elif 'Martian' in origin and 'Upper Class' in SocialClassVal and BackgroundRand <= (4):
    print("Your Background is Corporate")
    BackgroundVal = "Corporate"
elif 'Martian' in origin and 'Upper Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Cosmopolitan")
    BackgroundVal = "Cosmopolitan"

#Background Generator for Earther Upper Class
if 'Earther' in origin and 'Upper Class' in SocialClassVal and BackgroundRand <=2:
    print("Your Background is Aristocratic")
    BackgroundVal = "Aristocratic"
elif 'Earther' in origin and 'Upper Class' in SocialClassVal and BackgroundRand <= (4):
    print("Your Background is Corporate")
    BackgroundVal = "Corporate"
elif 'Earther' in origin and 'Upper Class' in SocialClassVal and BackgroundRand >= (5):
    print("Your Background is Cosmopolitan")
    BackgroundVal = "Cosmopolitan"

#Background Descriptions
BackgroundBenefitRand = random.randint(2,12)

#Academic Background Defined
if "Academic" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Intelligence
  Focus: Intelligence (choose one)
 Talent: Knowledge OR Linguistics""")
    
if BackgroundBenefitRand == 2 and 'Academic' in BackgroundVal:
    print("You also gain +1 Communication")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Academic' in BackgroundVal:
    print("You also gain Focus: Intelligence(Research)")
elif BackgroundBenefitRand == 5 and 'Academic' in BackgroundVal:
    print("You also gain a +2 to your Income")
elif BackgroundBenefitRand == 6 and 'Academic' in BackgroundVal:
    print("You also gain Focus: Intelligence(History")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Academic' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand == 9 and 'Academic' in BackgroundVal:
    print("You also gain Focus: Willpower(Self-Discipline)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Academic' in BackgroundVal:
    print("You also gain Focus: Intelligence(choose one)")
elif BackgroundBenefitRand == 12 and 'Academic' in BackgroundVal:
    print("You also gain +1 Willpower")

#Aristocratic Background Defined
if "Aristocratic" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Communication
  Focus: Communication(Etiquette) or Intelligence(History)
 Talent: Affluent or Contacts""")
    
if BackgroundBenefitRand == 2 and 'Aristocratic' in BackgroundVal:
    print("You also gain +1 Accuracy")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Aristocratic' in BackgroundVal:
    print("You also gain +2 Income")
elif BackgroundBenefitRand == 5 and 'Aristocratic' in BackgroundVal:
    print("You also gain Focus: Communication(Persuasion)")
elif BackgroundBenefitRand == 6 and 'Aristocratic' in BackgroundVal:
    print("You also gain Focus: Dexterity(Piloting)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Aristocratic' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand == 9 and 'Aristocratic' in BackgroundVal:
    print("You also gain Focus: Communication(Gambling)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Aristocratic' in BackgroundVal:
    print("You also gain Focus: Communication(Leadership)")
elif BackgroundBenefitRand == 12 and 'Aristocratic' in BackgroundVal:
    print("You also gain +1 Willpower")

#Bohemian Background Defined
if "Bohemian" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Communication
  Focus: Communication(Performing) or Intelligence(choose one)
 Talent: Carousing or Performance""")
    
if BackgroundBenefitRand == 2 and 'Bohemian' in BackgroundVal:
    print("You also gain +1 Dexterity")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Bohemian' in BackgroundVal:
    print("You also gain Focus: Perception(Empathy)")
elif BackgroundBenefitRand == 5 and 'Bohemian' in BackgroundVal:
    print("You also gain Focus: Willpower(Courage or Faith)")
elif BackgroundBenefitRand == 6 and 'Bohemian' in BackgroundVal:
    print("You also gain Focus: Communication(choose one)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Bohemian' in BackgroundVal:
    print("You also gain +1 Constitution")
elif BackgroundBenefitRand == 9 and 'Bohemian' in BackgroundVal:
    print("You also gain Focus: Dexterity (Acrobatics or Free-fall)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Bohemian' in BackgroundVal:
    print("You also gain Focus: Communication(Persuasion)")
elif BackgroundBenefitRand == 12 and 'Bohemian' in BackgroundVal:
    print("You also gain +1 Perception")

#Corporate Background Defined
if "Corporate" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Communication
  Focus: Communication(Bargaining) or Intelligence(Business)
 Talent: Contacts or Intrigue""")
    
if BackgroundBenefitRand == 2 and 'Corporate' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Corporate' in BackgroundVal:
    print("You also gain Focus: Communication(Persuasion)")
elif BackgroundBenefitRand == 5 and 'Corporate' in BackgroundVal:
    print("You also gain Focus: Intelligence(Evaluation)")
elif BackgroundBenefitRand == 6 and 'Corporate' in BackgroundVal:
    print("You also gain Focus: Perception(Empathy)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Corporate' in BackgroundVal:
    print("You also gain +1 Intelligence")
elif BackgroundBenefitRand == 9 and 'Corporate' in BackgroundVal:
    print("You also gain Focus: Communication(Expression)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Corporate' in BackgroundVal:
    print("You also gain Focus: Communication(Leadership)")
elif BackgroundBenefitRand == 12 and 'Corporate' in BackgroundVal:
    print("You also gain +1 Accuracy")

#Cosmopolitan Background Defined
if "Cosmopolitan" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Intelligence
  Focus: Communication(Etiquette) or Intelligence(Current Affairs)
 Talent: Knowledge or Observation""")
    
if BackgroundBenefitRand == 2 and 'Cosmopolitan' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Cosmopolitan' in BackgroundVal:
    print("You also gain Focus: Intelligence(choose one)")
elif BackgroundBenefitRand == 5 and 'Cosmopolitan' in BackgroundVal:
    print("You also gain Focus: Communication(Persuasion)")
elif BackgroundBenefitRand == 6 and 'Cosmopolitan' in BackgroundVal:
    print("You also gain Focus: Intelligence(Art)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Cosmopolitan' in BackgroundVal:
    print("You also gain +1 Communication")
elif BackgroundBenefitRand == 9 and 'Cosmopolitan' in BackgroundVal:
    print("You also gain Focus: Communication(Bargaining)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Cosmopolitan' in BackgroundVal:
    print("You also gain Focus: Perception(Seeing)")
elif BackgroundBenefitRand == 12 and 'Cosmopolitan' in BackgroundVal:
    print("You also gain +1 Willpower")
    
#Exile Background Defined
if "Exile" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Constitution
  Focus: Fighting(Brawling) or Willpower(Self-Discipline)
 Talent: Affluent or Fringer
 Additionally you can roll again on the Social Class and Background tables
 to get an idea of your former life, or come up with your own.""")
    
if BackgroundBenefitRand == 2 and 'Exile' in BackgroundVal:
    print("You also gain +1 Fighting")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Exile' in BackgroundVal:
    print("You also gain Focus: Communication(Bargaining)")
elif BackgroundBenefitRand == 5 and 'Exile' in BackgroundVal:
    print("You also gain Focus: Dexterity(Stealth)")
elif BackgroundBenefitRand == 6 and 'Exile' in BackgroundVal:
    print("You also gain Focus: Perception(Searching)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Exile' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand == 9 and 'Exile' in BackgroundVal:
    print("You also gain Focus: Accuracy(Pistols)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Exile' in BackgroundVal:
    print("You also gain Focus: Dexterity(Driving)")
elif BackgroundBenefitRand == 12 and 'Exile' in BackgroundVal:
    print("You also gain +1 Willpower")

#Military Background Defined
if "Military" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Fighting
  Focus: Accuracy(Pistols) or Intelligence(Tactics)
 Talent: One Combat Style or Observation""")
    
if BackgroundBenefitRand == 2 and 'Military' in BackgroundVal:
    print("You also gain +1 Willpower")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Military' in BackgroundVal:
    print("You also gain Focus: Accuracy(Rifles)")
elif BackgroundBenefitRand == 5 and 'Military' in BackgroundVal:
    print("You also gain Focus: Communication(Leadership)")
elif BackgroundBenefitRand == 6 and 'Military' in BackgroundVal:
    print("You also gain Focus: Intelligence(Security)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Military' in BackgroundVal:
    print("You also gain +1 Strength")
elif BackgroundBenefitRand == 9 and 'Military' in BackgroundVal:
    print("You also gain Focus: Perception(Searching)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Military' in BackgroundVal:
    print("You also gain Focus: Fighting(Brawling)")
elif BackgroundBenefitRand == 12 and 'Military' in BackgroundVal:
    print("You also gain +1 Constitution")

#Outcast Background Defined
if "Outcast" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Willpower
  Focus: Communication(Deception) or Dexterity(Stealth)
 Talent: Fringer or Misdirection""")
    
if BackgroundBenefitRand == 2 and 'Outcast' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Outcast' in BackgroundVal:
    print("You also gain Focus: Perception(Seeing)")
elif BackgroundBenefitRand == 5 and 'Outcast' in BackgroundVal:
    print("You also gain Focus: Fighting(Light Weapons)")
elif BackgroundBenefitRand == 6 and 'Outcast' in BackgroundVal:
    print("You also gain Focus: Intelligence(Technology)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Outcast' in BackgroundVal:
    print("You also gain +1 Constitution")
elif BackgroundBenefitRand == 9 and 'Outcast' in BackgroundVal:
    print("You also gain Focus: Dexterity(Sleight of Hand)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Outcast' in BackgroundVal:
    print("You also gain Focus: Willpower(Courage)")
elif BackgroundBenefitRand == 12 and 'Outcast' in BackgroundVal:
    print("You also gain +1 Communication")

#Laborer Background Defined
if "Laborer" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Constitution
  Focus: Dexterity(Crafting) or Strength(Might)
 Talent: One Unarmed Combat Style or Carousing""")
    
if BackgroundBenefitRand == 2 and 'Laborer' in BackgroundVal:
    print("You also gain +1 Fighting")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Laborer' in BackgroundVal:
    print("You also gain Focus: Fighting(Brawling)")
elif BackgroundBenefitRand == 5 and 'Laborer' in BackgroundVal:
    print("You also gain Focus: Intelligence(Engineering)")
elif BackgroundBenefitRand == 6 and 'Laborer' in BackgroundVal:
    print("You also gain Focus: Willpower(Self-Discipline)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Laborer' in BackgroundVal:
    print("You also gain +1 Strength")
elif BackgroundBenefitRand == 9 and 'Laborer' in BackgroundVal:
    print("You also gain Focus: Communication(Gambling)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Laborer' in BackgroundVal:
    print("You also gain Focus: Constitution(Stamina)")
elif BackgroundBenefitRand == 12 and 'Laborer' in BackgroundVal:
    print("You also gain +1 Dexterity")

#Suburban Background Defined
if "Suburban" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Communication
  Focus: Communication(Etiquette) or Intelligence(Current Affairs)
 Talent: Affluent or Contacts""")
    
if BackgroundBenefitRand == 2 and 'Suburban' in BackgroundVal:
    print("You also gain +1 Dexterity")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Suburban' in BackgroundVal:
    print("You also gain Focus: Intelligence(choose one)")
elif BackgroundBenefitRand == 5 and 'Suburban' in BackgroundVal:
    print("You also gain +2 Income")
elif BackgroundBenefitRand == 6 and 'Suburban' in BackgroundVal:
    print("You also gain Focus: Communication(Persuasion)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Suburban' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand == 9 and 'Suburban' in BackgroundVal:
    print("You also gain Focus: Perception(choose one)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Suburban' in BackgroundVal:
    print("You also gain Focus: Dexterity(Driving)")
elif BackgroundBenefitRand == 12 and 'Suburban' in BackgroundVal:
    print("You also gain +1 Intelligence")

#Trade Background Defined
if "Trade" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Dexterity
  Focus: Dexterity(Crafting) or Intelligence(Engineering)
 Talent: Improvisation or Maker""")
    
if BackgroundBenefitRand == 2 and 'Trade' in BackgroundVal:
    print("You also gain +1 Strength")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Trade' in BackgroundVal:
    print("You also gain Focus: Intelligence(Technology)")
elif BackgroundBenefitRand == 5 and 'Trade' in BackgroundVal:
    print("You also gain Focus: Intelligence(Art)")
elif BackgroundBenefitRand == 6 and 'Trade' in BackgroundVal:
    print("You also gain Focus: Constitution(Tolerance)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Trade' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand == 9 and 'Trade' in BackgroundVal:
    print("You also gain Focus: Fighting(Grappling)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Trade' in BackgroundVal:
    print("You also gain Focus: Constitution(Stamina)")
elif BackgroundBenefitRand == 12 and 'Trade' in BackgroundVal:
    print("You also gain +1 Constitution")

#Urban Background Defined
if "Urban" in BackgroundVal:
    print("""Your Background grants you 
Ability: +1 Dexterity
  Focus: Communication(Persuasion) or Constitution(Stamina)
 Talent: Agility or Misdirection""")
    
if BackgroundBenefitRand == 2 and 'Urban' in BackgroundVal:
    print("You also gain +1 Accuracy")
elif BackgroundBenefitRand >= 3 and BackgroundBenefitRand <=4 and 'Urban' in BackgroundVal:
    print("You also gain Focus: Dexterity(Acrobatics)")
elif BackgroundBenefitRand == 5 and 'Urban' in BackgroundVal:
    print("You also gain Focus: Communication(Deception)")
elif BackgroundBenefitRand == 6 and 'Urban' in BackgroundVal:
    print("You also gain Focus: Dexterity(Sleight of Hand)")
elif BackgroundBenefitRand >= 7 and BackgroundBenefitRand <=8 and 'Urban' in BackgroundVal:
    print("You also gain +1 Perception")
elif BackgroundBenefitRand == 9 and 'Urban' in BackgroundVal:
    print("You also gain Focus: Perception(Hearing)")
elif BackgroundBenefitRand >= 10 and BackgroundBenefitRand <= 11 and 'Urban' in BackgroundVal:
    print("You also gain Focus: Strength(Climbing or Jumping)")
elif BackgroundBenefitRand == 12 and 'Urban' in BackgroundVal:
    print("You also gain +1 Fighting")

print("Talents can be found starting on page 49")

#Profession picker
ProfessionsRand = random.randint(1,6)

#Testing Variable Setting
#SocialClassVal = "Outsider"

#Outsider Profession Picker
if ProfessionsRand == 1 and 'Outsider' in SocialClassVal:
    ProfessionsVal = "Brawler"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 2 and 'Outsider' in SocialClassVal:
    ProfessionsVal = "Survivalist"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 3 and 'Outsider' in SocialClassVal:
    ProfessionsVal = "Criminal"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 4 and 'Outsider' in SocialClassVal:
    ProfessionsVal = "Scavenger"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 5 and 'Outsider' in SocialClassVal:
    ProfessionsVal = "Fixer"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 6 and 'Outsider' in SocialClassVal:
    ProfessionsVal = "Artist"
    print(f"Your Profession is {ProfessionsVal}")

#Lower Class Profession Picker
if ProfessionsRand == 1 and 'Lower Class' in SocialClassVal:
    ProfessionsVal = "Athlete"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 2 and 'Lower Class' in SocialClassVal:
    ProfessionsVal = "Soldier"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 3 and 'Lower Class' in SocialClassVal:
    ProfessionsVal = "Investigator"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 4 and 'Lower Class' in SocialClassVal:
    ProfessionsVal = "Technician"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 5 and 'Lower Class' in SocialClassVal:
    ProfessionsVal = "Clergy"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 6 and 'Lower Class' in SocialClassVal:
    ProfessionsVal = "Negotiator"
    print(f"Your Profession is {ProfessionsVal}")

#Middle Class Profession Picker
if ProfessionsRand == 1 and 'Middle Class' in SocialClassVal:
    ProfessionsVal = "Pilot"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 2 and 'Middle Class' in SocialClassVal:
    ProfessionsVal = "Security"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 3 and 'Middle Class' in SocialClassVal:
    ProfessionsVal = "Professional"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 4 and 'Middle Class' in SocialClassVal:
    ProfessionsVal = "Scholar"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 5 and 'Middle Class' in SocialClassVal:
    ProfessionsVal = "Merchant"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 6 and 'Middle Class' in SocialClassVal:
    ProfessionsVal = "Politician"
    print(f"Your Profession is {ProfessionsVal}")

#Upper Class Profession Picker
if ProfessionsRand == 1 and 'Upper Class' in SocialClassVal:
    ProfessionsVal = "Commander"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 2 and 'Upper Class' in SocialClassVal:
    ProfessionsVal = "Explorer"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 3 and 'Upper Class' in SocialClassVal:
    ProfessionsVal = "Dilettante"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 4 and 'Upper Class' in SocialClassVal:
    ProfessionsVal = "Expert"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 5 and 'Upper Class' in SocialClassVal:
    ProfessionsVal = "Executive"
    print(f"Your Profession is {ProfessionsVal}")
elif ProfessionsRand == 6 and 'Upper Class' in SocialClassVal:
    ProfessionsVal = "Socialite"
    print(f"Your Profession is {ProfessionsVal}")

#Profession Descriptions
#Testing Professions
#ProfessionsVal = "Athlete"
if "Artist" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Expression) or Intelligence(Art)
 Talent: Artistry or Performance""")
elif "Athlete" in ProfessionsVal:
    print("""Your Profession grants you
    Focus: Constitution(Running or Swimming), 
    Dexterity(Acrobatics or Free-fall),
    or Strength(Climbing or Jumping)
    Talent: Artistry or Performance""")
elif "Brawler" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Fighting(Brawling) or Fighting(Grappling)
 Talent: Grappling Style or Striking Style""")
elif "Clergy" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Intelligence(Theology) or Willpower(Faith)
 Talent: Inspire or Oratory""")
elif "Commander" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Leadership) or Intelligence(Tactics)
 Talent: Command or Tacticle Awareness""")
elif "Criminal" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Deception) or Dexterity(Forgery, Sleight of Hand, or Stealth)
 Talent: Burglary or Scouting""")
elif "Dilettante" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Intelligence(Research) or Perception(choose one)
 Talent: Improvisation or Know-It-All""")
elif "Executive" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Leadership) or Intelligence(Business)
 Talent: Command or Intrigue""")
elif "Expert" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Intelligence(choose one)
 Talent: Expertise or Know-It-All""")
elif "Explorer" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Intelligence(Navigation) or Perception(choose one)
 Talent: Pilot or Scouting""")
elif "Fixer" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Bargaining) or Intelligence(Evaluation)
 Talent: Fringer or Improvisation""")
elif "Investigator" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Investigation) or Perception(choose one)
 Talent: Intrigue or Observation""")
elif "Merchant" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Bargaining) or Intelligence(Business)
 Talent: Affluent or Contacts""")
elif "Negotiator" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Bargaining or Persuasion) or Perception(Empathy)
 Talent: Intrigue or Oratory""")
elif "Pilot" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Dexterity(Piloting)
 Talent: Pilot""")
elif "Politician" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Deception or Persuasion) or Intelligence(Current Affairs or Law)
 Talent: Contacts or Oratory""")
elif "Professional" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Bargaining or Expression) or Intelligence(Business, Computers, or Research)
 Talent: Affluent or Expertise""")
elif "Scavenger" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Intelligence(Technology) or Perception(Searching)
 Talent: Evaluation or Maker""")
elif "Scholar" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Intelligence(choose one)
 Talent: Expertise or Knowledge""")
elif "Security" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Intelligence(Security) or Perception(Empathy, Intuition, or Seeing)
 Talent: One Fighting Style or Protect""")
elif "Socialite" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Communication(Etiquette or Seduction) or Constitution(Tolerance)
 Talent: Attractive or Contacts""")
elif "Soldier" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Accuracy(Pistols or Rifles) or Fighting(Brawling)
 Talent: One Fighting Style or Tactical Awareness""")
elif "Survivalist" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Accuracy(Bows or Pistols) or Perception(Survival)
 Talent: Fringer or Tactical Awareness""")
elif "Technician" in ProfessionsVal:
    print("""Your Profession grants you
  Focus: Intelligence(Engineering or Technology)
 Talent: Expertise, Hacking, or Maker""")

#Drive picker Randomizer
DriveRand1 = random.randint(1,6)
DriveRand2 = random.randint(1,6)

#Drive Selecting
if DriveRand1 <= 3 and DriveRand2 == 1:
    DriveVal = "Achiever"
elif DriveRand1 <= 3 and DriveRand2 == 2:
    DriveVal = "Builder"
elif DriveRand1 <= 3 and DriveRand2 == 3:
    DriveVal = "Caregiver"
elif DriveRand1 <= 3 and DriveRand2 == 4:
    DriveVal = "Ecstatic"
elif DriveRand1 <= 3 and DriveRand2 == 5:
    DriveVal = "Judge"
elif DriveRand1 <= 3 and DriveRand2 == 6:
    DriveVal = "Leader"
elif DriveRand1 >= 4 and DriveRand2 == 1:
    DriveVal = "Networker"
elif DriveRand1 >= 4 and DriveRand2 == 2:
    DriveVal = "Penitent"
elif DriveRand1 >= 4 and DriveRand2 == 3:
    DriveVal = "Protector"
elif DriveRand1 >= 4 and DriveRand2 == 4:
    DriveVal = "Rebel"
elif DriveRand1 >= 4 and DriveRand2 == 5:
    DriveVal = "Survivor"
elif DriveRand1 >= 4 and DriveRand2 == 6:
    DriveVal = "Visionary"


print("""You also need to select one of the following improvements:
Fortune (+5 Increase,
Membership (rank 1)
Income (+2 Increase),
Relationship (rank1,
or Reputation (rank 1)
For details on Memberships, Relationships, and Reputation, see CHAPTER 14""")

print(f"Your Drive is {DriveVal}")

#Drive Tester 
#DriveVal = "Visionary"

#Drive Descriptions

if DriveVal == "Achiever":
    print(color.BLUE + color.BOLD +"Quality: " + color.END + color.BOLD + "Ambition, " + color.END + "knowing what you want and going after it.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Obsession, " + color.END + "becoming too focused on your goals and unable to see anything (or anyone) else.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Expertise or Inspire")
if DriveVal == "Builder":
    print(color.BLUE + color.BOLD +"Quality: " + color.END + color.BOLD + "Organization, " + color.END + "being able to figure out how to structure things so they work.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Stubbornness, " + color.END + "becoming so caught up in structure that you lose flexibility.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Maker or Oratory")
if DriveVal == "Caregiver":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Compassion, " + color.END + "naturallly feeling and responding to others needs.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Self-sacrifice, " + color.END + "a tendancy to place the needs and even physical safety of others above your own.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Inspire or Medic")
if DriveVal == "Ecstatic":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Zest for life " + color.END + "and a general willingness to find enjoyment in things and try new experiences.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Irresponsibility, " + color.END + "a tendency to overdo enjoyment at the expense of more practical matters.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Attractive or Carousing")
if DriveVal == "Judge":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Discernment, " + color.END + "paying close attention to details and information.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Aloofness, " + color.END + "a tendency to distance yourslef from the world around you to remain objective.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Knowledge or Observation")
if DriveVal == "Leader":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Responsibility, " + color.END + "the ability to take on and make decisions and live with the outcome.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Isolation, " + color.END + "the distance imposed by your role as leader, which can affect relationships and how close you can be with people you lead.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Command or Inspire")
if DriveVal == "Networker":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Gregariousness. " + color.END + "You're good with people and at home in social situations, and tend to seek them out.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Overwrought. " + color.END + "You tend to get caught up in social conflicts, and think finding just the right person is the solution to every problem, making you prone to overly complex schemes.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Contract or Intrigue")
if DriveVal == "Penitent":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Humility. " + color.END + "You have fallen low and learned from it, so you're not quick to judge or to accept accolades.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Guilt, " + color.END + "as you're sometimes haunted by your past mistakes and feel any new missteps heavily.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Fringer or Know-It-All")
if DriveVal == "Protector":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Devoltion " + color.END + "to those under your protection and to your ideals, no matter what challenges lie in your path.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Recklessness " + color.END + "when it comes to putting yourself (and even others) in harm's way to protect your charges.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Misdirection or Protect")
if DriveVal == "Rebel":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Innovation, " + color.END + "the ability to look at things from angles no one else has considered.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Defiance, " + color.END + "a dislike of conformity, conventionality, and doing what you're told.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Expertise or Improvisation")
if DriveVal == "Survivor":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Preparedness. " + color.END + "You survive by being ready for anything and knowing what to do in any situation.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Cynicism. " + color.END + "You are always anticipating and preparing for the worst, such that it's difficult for you to see the good in anything.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Fringer or Tactical Awareness")
if DriveVal == "Visionary":
    print(color.BLUE + color.BOLD + "Quality: " + color.END + color.BOLD + "Faith " + color.END + "in your vision and its ability to reach the right people, given the opportunity.")
    print(color.BLUE + color.BOLD +"Downfall: " + color.END + color.BOLD + "Zealotry, " + color.END + "Your vision becomes confused with absolute truth, which might lead you to offer it where it is unwelcome ot to try and eliminate other visions you see as false or competition.")
    print("Alternatively, your downfall is " + color.BOLD + "Doubt, " + color.END + "where you experience a crisis of faith and are uncertai how to follow your vision-or if you should continue to follow it at all.")
    print(color.BLUE + color.BOLD +"Talent: " + color.END +  "Artistry, Oratory, or Performance")

print(color.BOLD + "Talents can be found starting on page 49" + color.END)
