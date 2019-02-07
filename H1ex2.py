print("This is a notebook")


inputstring = input("You can start adding entries:  ").split(",")  #Add elements to the list/notebook
entrylist = list(inputstring)

print("Now you can:")
print("1.Add entries.")
print("2.Delete entries")

action = input("Please choose the next action:  ")   #the user can choose to add or delete elements

if action == "1":                                     #add elements to the list
    inputaddstring = input().split(", ")
    entrylist.extend(inputaddstring)
    print(entrylist)


elif action == "2":                         #remove elements from the list
    inputremovestring = input().split(",")
    entrylist.remove(inputremovestring)
    print(entrylist)