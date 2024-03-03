mylist = []

#Append the following elements to my_list: 10, 20, 30, 40.
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)

print(mylist)
#Insert the value 15 at the second position in the list
mylist.insert(1,15)
print(mylist)
#Extend my_list with another list: [50, 60, 70]
list2 =[50,60,70]
mylist = mylist + list2
print(mylist)
#Remove the last element from my_list.
mylist.pop()
print(mylist)
#Sort my_list in ascending order.
mylist.sort()
print(mylist)
#Find and print the index of the value 30 in my_list.
if 30 in mylist:
  index = mylist.index(30)
  print(f'The no. 30 is in index {index}')
else:
  print("There is no 30 in your list")
