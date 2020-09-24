file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
file_counts["txt"]
14
"jpg" in file_counts
True
"html" in file_counts
False
file_counts["cfg"] = 8
print file_counts
{"jpg":10, "txt":14, "csv":2, "py":23, "cfg" = 8 }
file_counts["csv"]= 17
print file_counts
{"jpg":10, "txt":14, "csv":17, "py":23, "cfg" = 8 }
