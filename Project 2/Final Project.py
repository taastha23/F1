#Defining the file names
USERS_FILE ="users.txt"
GRADES_FILE="grades.txt"
ECA_FILE="eca.txt"
PASSWORDS_FILE="password.txt"

#Defining roles
ADMIN_ROLE ="admin"
STUDENT_ROLE="student"
class Student:
    def __init__(self,id,grade,name):
        self.name = name
        self.grade= grade
    def __str__(self):
        return f"{self.name},{self.grade}"
class Login:
    @staticmethod
    def login():
        username= input("Enter your username:")
        password = input("Enter your password:")
        if Login.check_credentials(username, password):
            return True, username
        else:
            return False, None
    @staticmethod       
    def check_credentials(username, password):
        with open(USERS_FILE, "r") as file:
            for line in file:
                values=line.strip().split(",")
                if len(values) ==3:
                    stored_username, stored_password, role = line.strip().split(",")
                    if stored_username == username and stored_password == password:
                        return True
        return False
        

class Admin:

    def __init__(self):
        self.students =[]
    def register_student(self,name,grade):
        student= Student(None,grade,name)
        self.students.append(student)
        print("Student registered successfully.")

    
    def view_students(self):
        print("\nStudents:")
        for i, student in enumerate(self.students, 1):
            print(f"{i}.Name:{student.name}, Grade:{student.grade}")
            
    def update_students(self,index,name,grade):
        if 0<= index<len(self.students):
            self.students[index].name= name
            self.students[index].grade= grade
            print("Student updated successfully.")
        else:
            print("Invalid student index.")
            
    def delete_student(self,index):
        if 0<=index <len(self.students):
            del self.students[index]
            print("Student deleted successfully.")
        else:
            print("Invalid student index.")
    def save_students_to_file(self):
        with open("GRADES_FILE","w") as file:
            for student in self.students:
                file.write(str(student) + "\n")
    def load_students_from_file(self):
        try:
            with open(GRADES_FILE, "r") as file:
                for line in file:
                    values =line.strip().split(",")
                    if len(values) == 2: 
                        name,grade=values
                        self.students.append(Student(None, int(grade), name))
                
                        
        except FileNotFoundError:
            pass
            
    
            
def student_dashboard(admin):
    while True:
        print("\nStudents Dashboard Menu:")
        print("1.View Student Details")
        print("2.Exit")
        choice = input("Enter your choice:")
        if choice =='1':
            admin.view_students()
        elif choice == '2':
            print("Existing the student dashboard.")
            break
        else:
            print("Invalid choice.Please enter a number between 1 and 2.")
def admin_dashboard(admin):
    while True:
        print("\nAdmin Dashboard menu!")
        print("1.Register Students:")
        print("2.Update student")
        print("3.Delete Students")
        print("4.View Students")
        print("5.Exit")
        choice = input("Enter your choice:")
    
        if choice =='1':
            name = input("Enter student name:")
            grade = int(input("Enter Student grade:"))
            admin.register_student(name,grade)
            admin.save_students_to_file()
        elif choice == '2':
            admin.view_students()
            index = int(input("Enter student index to update:"))
            name = input("Enter student name:")
            grade = int(input("Enter Student grade:"))
            admin.update_student(index -1, name, grade)
            admin.save_students_to_file()
        elif choice == '3':
            admin.view_students()
            index = int(input("Enter student index to delete:"))
            admin.delete_student(index -1)
            admin.save_students_to_file()
            
        elif choice =='4':
            admin.view_students()
        elif choice ==  '5':
            print("Existing the admin dashboard.")
            admin.save_students_to_file()
            break
        else:
            print("Invalid choice.Please enter a number between 1 and 5.")
def main():
    admin= Admin()
    admin.load_students_from_file()
    while True:
        print("\nWelcome to the Dashboard!")
        print("1.Student Login")
        print("2.Admin Login:")
        print("3.Exit:")
        choice = input("Enter your choice:")
        if choice =='1':
            success, username = Login.login()
            if success:
                student_dashboard(admin)
        elif choice == '2':
            success, username = Login.login()
            if success:
                admin_dashboard(admin)
        elif choice =='3':
            print("Existing the program.Goodbye!")
            break1
            
        else:
            print("Invalid choice.Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
            