import random

class Release_Act:

    def __init__(self, act_start_at_kings_age ):
        self.max_subjects = 100
        self.max_searches_per_subject = 50
        self.subs_to_take = 5
        self.highest_prisoner = 0
        self.act_start_at_kings_age = act_start_at_kings_age

    def flip_coin(self):
        return random.randbool()

    def prisoner_search_id(self,prisoner, boxes): 
        drawn_boxes = set()   
        for i in range(0,self.max_searches_per_subject): 
            drawn_box = random.randint(0, len(boxes)-1)  

            while drawn_box in drawn_boxes: 
                drawn_box = random.randint(0, len(boxes)-1)  

            drawn_boxes.add(drawn_box)                       
            if drawn_box == prisoner:
                #print(f"prisioner: {prisoner} found number")
                #boxes.remove(drawn_box) #veringert die anzahl boxen wenn ein find
                return True
        return False

    def create_lists(self):
        prisoners = []
        boxes = []   
        for i in range(1,self.max_subjects+1):
            prisoners.append(i)
            boxes.append(i)
        
        shuffeld_boxes = []
        for i in range(1,self.max_subjects+1):
            box = random.randint(0, len(boxes)-1) 
            new_shuffeld_box = boxes[box]
            boxes.remove(new_shuffeld_box)
            shuffeld_boxes.append(new_shuffeld_box) 
        
        return prisoners, shuffeld_boxes

    def release_prisoners(self):
        if self.max_subjects <= 0:
            print("All prisoners aqquired by the King!")
            return False    
        prisoners, boxes = self.create_lists()
        #print(f"Releasing {len(prisoners)} with max: {self.max_subjects}")
        for prisoner in prisoners:
            if not self.prisoner_search_id(prisoner, boxes):
                print(f"Release failed because prisoner #{prisoner} didn't found his id within {self.max_searches_per_subject} trys, hidden in {len(boxes)} boxes:/")
                return False
            elif self.highest_prisoner < prisoner:
                self.highest_prisoner = prisoner 
        return True

class King:

    def __init__(self, name, age, max):
        self.name = name
        self.age = age
        self.max = age + max
        self.act_component = Release_Act(self.age)
        self.celebrate_birthdays()
        
    def celebrate_birthdays(self):
        while self.age < self.max:
            self.age += 1
            print(f"Törröö! The King: {self.name} comes to age {self.age}. Celebrate! The prisoners choose their Fate once again. Now the {self.celebration_counter_to_print()} attempt.")
            if self.act_component.release_prisoners():
                print(f"Finally! The King: {self.name} at his {self.age}. birthday released {self.act_component.max_subjects} prisoners. The End.")
                return                     
        print(f"{self.get_count_attempts()} years have past and the highest sequence where prisoners managed to find their id is {self.act_component.highest_prisoner} in arow.")

    def get_count_attempts(self):
        return self.age - self.act_component.act_start_at_kings_age
    
    def celebration_counter_to_print(self) -> str:
        anu = self.get_count_attempts()
        if (anu == 1):
            return str(anu) + "st"
        elif (anu == 2):
            return str(anu) + "nd"
        elif (anu == 3):
            return str(anu) + "rd"
        else:
            return str(anu) + "th"



# TEST
# 2hoch100
max = 1000 * 1000
king = King("Hardoman der Gerechte", 42, max)


