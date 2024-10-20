import random


class King:
    name = "Hardoman der Gerechte"
    age = 42
    

class Release_Act:
    max_searches = 50
    max_subjects = 100
    subs_to_take = 5

    def prisoner_search_id(self,prisoner, boxes):
        
        for i in range(0,self.max_searches):
            #print(f"prisioner: {prisoner} searches {i+1}. time")
            drawn_box = boxes[random.randint(0, len(boxes)-1)]
            if drawn_box == prisoner:
                print(f"prisioner: {prisoner} found number")
                boxes.remove(drawn_box)
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
        #print(prisoners)
        #print(sorted(boxes))
        print(f"Releasing {len(prisoners)} with max: {self.max_subjects}")
        for prisoner in prisoners:
            if not self.prisoner_search_id(prisoner, boxes):
                print(f"Release failed because prisoner #{prisoner} didn't found his id with {self.max_searches} trys, hidden in {len(boxes)} boxes:/")
                self.max_subjects -= self.subs_to_take
                print(f"Remaining {self.max_subjects} prisoners.")
                return False
        return True
# TEST

king = King()
act = Release_Act()

while True:
    if act.release_prisoners():
        print(f"Finally {act.max_subjects} prisoners released. The End.")
        break
