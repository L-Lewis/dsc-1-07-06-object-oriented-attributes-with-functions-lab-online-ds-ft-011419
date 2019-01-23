class School:
    
    def __init__(self, name):
        self.name = name
        self.roster = {}
        
    def roster(self):
        return self.roster
    
    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = []
            self.roster[grade].append(name)
            
    def grade(self, grade):
        return self.roster[grade]
    
