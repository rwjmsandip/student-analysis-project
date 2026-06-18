import statistics 
import matplotlib.pyplot as plt

students = {
    "Amit": 78,
    "Priya": 92,
    "Rahul": 65,
    "Sneha": 88,
    "Vikas": 55,
    "Neha": 74,
    "Arjun": 96,
    "Kiran": 82,
    "Riya": 69,
    "Ankit": 90
}   

subjects = ("Math", "Science", "English")
def display_subjects():
    print("Subjects:")
    for subject in subjects:
        print(subject)

class Person:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print(f"Student Name: {self.name}")


class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.__marks = marks
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        self.__marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.__marks}")


def add_student():
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    students[name] = marks
    print("Student Added Successfully")


def update_student():
    name = input("Enter Name to Update: ")
    if name in students:
        marks = int(input("Enter New Marks: "))
        students[name] = marks
        print("Updated Successfully")
    else:
        print("Student Not Found")


def delete_student():
    name = input("Enter Name to Delete: ")
    if name in students:
        del students[name]
        print("Deleted Successfully")
    else:
        print("Student Not Found")


def display_students(): 
    for name, marks in students.items():
        print(name, ":", marks)


def statistics_report():
    marks = list(students.values())
    mean = statistics.mean(marks)
    median = statistics.median(marks)
    mode = statistics.mode(marks)
    data_range = max(marks) - min(marks)
    variance = statistics.variance(marks)
    std_dev = statistics.stdev(marks)

    sorted_marks = sorted(marks)
    q1 = sorted_marks[len(sorted_marks)//4]
    q3 = sorted_marks[(3*len(sorted_marks))//4]

    iqr = q3 - q1
    print("Mean =", mean)
    print("Median =", median)
    print("Mode =", mode)
    print("Range =", data_range)
    print("Variance =", variance)
    print("Standard Deviation =", std_dev)
    print("Q1 =", q1)
    print("Q3 =", q3)
    print("IQR =", iqr)

def probability_analysis():
    marks = list(students.values())
    total = len(marks)

    above80 = 0
    for m in marks:
        if m >= 80:
            above80 += 1
    prob_above80 = above80 / total
    print("Probability of scoring above 80:", prob_above80)

    above70 = 0
    for m in marks:
        if m >= 70:
            above70 += 1
    prob_above70 = above70 / total
    print("Probability of scoring above 70:", prob_above70)

    conditional = above80 / above70
    print("Conditional Probability of scoring above 80 given above 70:", conditional)

def visualize_data():
    names = list(students.keys())
    marks = list(students.values())

    plt.hist(marks)
    plt.title("Histogram")
    plt.savefig("screenshots/histogram.png")
    plt.close()

    plt.bar(names, marks)
    plt.title("Bar Chart")
    plt.savefig("screenshots/barchart.png")
    plt.close()

    plt.boxplot(marks)
    plt.title("Box Plot")
    plt.savefig("screenshots/boxplot.png")
    plt.close()

    plt.scatter(range(len(marks)), marks)
    plt.title("Scatter Plot")
    plt.savefig("screenshots/scatterplot.png")
    plt.close()

    plt.plot(names, marks)
    plt.title("Line Chart")
    plt.savefig("screenshots/linechart.png")
    plt.close()

    print("Charts Saved Successfully")



while True:
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Statistics Report")
    print("6. Probability Analysis")
    print("7. Data Visualization")
    print("8. Display Subjects")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_student()

    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_students()

    elif choice == "5":
        statistics_report()

    elif choice == "6":
        probability_analysis()

    elif choice == "7":
        visualize_data()

    elif choice == "8":
        display_subjects()

    elif choice == "9":
        print("Thank You")
        break
    else:
        print("Invalid Choice")