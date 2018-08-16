#PROBLEM ONE
#You will be given a list named our_list
#Print True if our_list is longer than 2 elements AND 
#the first and last elements are the same. 
#If the list is 2 elements OR shorter OR the first and
#last elements are not the same, print False. 
#Hint: to test your code, define an example value for 
#our_list at the top of your code.

#my_list = [1,1,1,1,1,1]
#if len(my_list) > 2 and my_list[0] == my_list[len(my_list)-1]:
#    print(True)
#else:
#    print(False)

#PROBLEM TWO
#It may be helpful to comment out the code from 
#problem one while you are working on this section.list_one and list_two. 
#Print a list containing elements for which the same 
#index in both lists has the same element.
list_one = [1,2,3]
list_two = [3,2,1]
i = 0
while i<len(list_one):
    if list_one[i] == list_two[i]:
        print(list_one[i])
        i+=1
    else:
        print("No same numbers in index " + str(i))
        i+=1
