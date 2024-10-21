import random

class Release_Act:
    max_subjects = 100
    max_searches_per_subject = 50
    subs_to_take = 5
    highest_prisoner = 0

    def prisoner_search_id(self,prisoner, boxes):
        return random.randint(0,1) == 1
    # simuliert mit boxen 
        # for i in range(0,self.max_searches_per_subject):
        #     #print(f"prisioner: {prisoner} searches {i+1}. time")   
        #     drawn_box = random.randint(0, len(boxes)-1)                        
        #     if drawn_box == prisoner:
        #         #print(f"prisioner: {prisoner} found number")
        #         boxes.remove(drawn_box)
        #         return True
        # return False

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
                #self.max_subjects -= self.subs_to_take
                #print(f"Remaining {self.max_subjects} prisoners.")
                return False
            elif self.highest_prisoner < prisoner:
                self.highest_prisoner = prisoner
  
        return True

class King:
    name = "Hardoman der Gerechte"
    age = 42
    act_component = Release_Act()
    max = 42 + 1000 * 10


    def celebrate_birthday(self):
        while self.age < self.max:
            self.age += 1
            print(f"Törröö! The King: {self.name} at age {self.age}. Celebrates. The prisoners choose their destiny the {self.age-42}th time.")
            if self.act_component.release_prisoners():
                print(f"Finally! The King: {self.name} at his {self.age}. birthday released {self.act_component.max_subjects} prisoners. The End.")
                return
                       
        print(f"highest chain: {self.act_component.highest_prisoner}")
                


# TEST
# TODO: Thema noch nicht ganz getroffen es soll dann 10.000 mal geburtstag simuliert werden also immer 100 subs die 100 boxen durchsuchen.
# Das wird dann viel unwahrscheinlicher. 2hoch100
king = King()
king.celebrate_birthday()


