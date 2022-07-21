import csv
from tkinter import messagebox

def isunique(id, data):
    if len(data)==1 and len(data[0])==0:
        return True
    for row in data:
        if row[0]==str(id):
            return False
    return True

def writetofile(rows):
    with open('studentsinfo_file.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter='*', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)


class Students:
    def __init__(self, studentID, level, full_name, nationality, gender, faculity, admission_year):
        self.studendID = studentID
        self.level = level
        self.full_name = full_name
        self.nationality = nationality
        self.gender = gender
        self.faculity = faculity
        self.admission_year = admission_year

    def get_fullname(self):
        return self.full_name
    
    def all_data():
        try:
            data = []
            with open('studentsinfo_file.csv', mode='r') as file:
                reader = csv.reader(file, delimiter='*')
                for row in reader:
                    if len(row)!=0:
                        data.append(row)
            return data
        except FileNotFoundError:
            return []
    
    
    def find(id):
        data = Students.all_data()
        if len(data)==0:
            return 1
        
        for row in data:
            if row[0]==str(id):
                return row
            
        return 0
    
    
    def delete(id):
        data = Students.all_data()
        if len(data)==0:
            return 1
        
        for row in data:
            if row[0]==str(id):
                data.remove(row)
                writetofile(data)
                break
        else:
            return 0



class Undergraduate(Students):

    def __init__(self, studentID, level, full_name, nationality, gender, faculity, admission_year, residential_hall):
        super().__init__(studentID, level, full_name, nationality, gender, faculity, admission_year)
        self.residential_hall = residential_hall

    def add(self):
        data = Students.all_data()
        if isunique(self.studendID, data):
            data.append([self.studendID, self.level, self.full_name, self.nationality, self.gender, self.faculity, self.admission_year, self.residential_hall])
            writetofile(data)
        else:
            messagebox.showinfo("Attention!", "There is already a student with this id!")
        



class Postgraduate(Students):
    def __init__(self, studentID, level, full_name, nationality, gender, faculity, admission_year, supervisor_name, research_topic):
        super().__init__(studentID, level, full_name, nationality, gender, faculity, admission_year)
        self.supervisor_name = supervisor_name
        self.research_topic = research_topic
        
    
    def add(self):
        data = Students.all_data()
        if isunique(self.studendID, data):
            data.append([self.studendID, self.level, self.full_name, self.nationality, self.gender, self.faculity, self.admission_year, self.supervisor_name, self.research_topic])
            writetofile(data)
        else:
            messagebox.showinfo("Attention!", "There is already a student with this id!")
        

