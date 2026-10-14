import sys # Access command-line arguments
from collections import Counter # Count occurrences and store it in dictonary

filename=sys.argv[1] # Get the log in variable filename # the second thing after the program name as python 3 
                     #is running the program it isnt counted in the index and summary.py is taken as the first index 
                     # that is 0th index as the value then 1st index value is mylog.log which is the log file name and 
                     # it is stored in the variable filename

with open(filename) as f: #Open the Log file
    lines = f.readlines() # Read all lines and store it as list

print("Total Lines :--> ", len(lines)) #Print total lines

counts = Counter() # Create an empty counter
for line in lines: # Process each line
    fields = line.split() # Split line into fields and store it as lists
    # we are using 7th as the thing we need is on the 8th postion so by indexing it would be on 7th ( comment by me )
    if len(fields) > 7: 
        key = fields[7]
        counts[key] += 1

print("Top 5 most recurring fields at the 7th aka 8th postions are :--> ")
for item, n in counts.most_common(5):
    print(item, n)