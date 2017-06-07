
# Take input of items
# Add items to a list 
# Finalise list with keyword DONE
# print out full list when done 

shopping = []


print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items")

while True:
	new_item = input("> ")

	if new_item == "DONE":
		print("Here's your shopping list:")
		print(shopping)
		break
	else:
		shopping.append(new_item)




