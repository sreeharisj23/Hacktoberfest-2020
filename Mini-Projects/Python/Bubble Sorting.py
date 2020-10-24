'''
Implementation of Binary Search Algorithm in Python
'''

# defining a function for bubble sort
def bubble_sort(myList):

                # len() to find total no of elements in list
                length   =  len(myList)
                print(f"Original List : {myList}")

                # traversing through the list with for loop
                for i in range(length - 1): 
                        for j in range(length - i - 1):
                                #  checking and swapping values if the element is found larger
                                if myList[j] > myList[j+1]:
                                        myList[j],  myList[j+1] = myList[j+1],  myList[j]

                print(f"After sorting list is :  {myList}")

# creating a list through user input
myList = []
num = int(input("Enter total no of elements =  "))
for i in range(num):
        x = int(input("Enter no :  "))
        myList.append(x)

# function call
bubble_sort(myList)
