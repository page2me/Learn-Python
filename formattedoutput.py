# Formatted output
print("Name", "Marks", "Age")
print("John Doe", 80.67, "27")
print("Bhaskar", 76.908, "27")
print("Mohit", 56.98, "25")

print("Name Marks Age")
print("%s %14.2f %11d" %("John Doe", 80.67, 27))
print("%s %12.2f %11d" %("Bhaskar" ,76.901, 27))
print("%s %3.2f %11d" %("Mohit", 56.98, 25))