number_of_students = int(input("Please enter the number of students: "))
mylist_lb = []
mylist_kg = []
LB_TO_KG = 0.453592
for i in range(number_of_students):
    mylist_lb.append(float(input(f"Enter the {i + 1} student's weight in lb: ")))
    mylist_kg.append(float("%.2f" % (mylist_lb[i] * LB_TO_KG)))

print(f"Students weights in lb {mylist_lb}")
print(f"Students weights in kg {mylist_kg}")
