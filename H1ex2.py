print("This is a notebook")


inputstring = input("You can start adding entries:  ").split(",")
entrylist = list(inputstring)

print("Now you can:")
print("1.Add entries.")
print("2.Delete entries")

action = input("Please choose the next action:  ")

if action == "1":
    inputaddstring = input().split(", ")
    entrylist.extend(inputaddstring)
    print(entrylist)


elif action == "2":
    inputremovestring = input().split(",")
    entrylist.remove(inputremovestring)
    print(entrylist)