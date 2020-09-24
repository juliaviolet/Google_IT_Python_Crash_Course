file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

file_counts.keys()
dict_keys(['jpg','txt','csv','py'])

file_counts.values()
dict values ([10, 14 ,2 ,23])

for value in file_counts.values()
    print(value)

10
14
2
23