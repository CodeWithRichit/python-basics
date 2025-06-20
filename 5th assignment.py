#Task1: Create a dictionary of student marks
try:
  name=input('Enter the name of Child: ')
  Marks_dict={'Alice':85,'James':90,'Suresh':97}
  print('Marks: ',Marks_dict[name])
except Exception as e:
    print('Student not found',e)

#Task2: Demonstrate list slicing
list1=[1,2,3,4,5,6,7,8,9,10]
print("Original list: ",list1)
list2=(list1[0:6])
print("Extracted list",list2)
list2.reverse()
print("Reversed list: ",list2)

