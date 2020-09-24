wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key,values in wardrobe.items():
	for v in values:
	  print("{} {}".format(v,key))
