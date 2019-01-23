class School:
    
    def __init__(self, name):
        self.name = name
        self._roster = {}
        
    def roster(self):
        return self._roster
        
    def add_student(self, name, grade):
        if grade in self._roster:
            self._roster[grade].append(name)
        else:
            self._roster[grade] = []
            self._roster[grade].append(name)
            
    def grade(self, grade):
        return self._roster[grade]
    
    def sort_roster(self):
        sorted_roster = self._roster
        for x in sorted_roster:
            sorted_roster[x].sort()
        return sorted_roster