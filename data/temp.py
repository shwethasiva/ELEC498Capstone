import os
import csv

directory = '/Users/Mounir/Documents/Documents/Capstone/GeeseLabeling-yolo/data/img'
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        temp = filename
        print(os.path.join(directory, filename))
        with open(temp, 'r') as in_file:
            
            for line in in_file:
                stripped = (line.strip()
            for line in stripped if line)
            
            with open('log.csv', 'w') as out_file:
                
                writer = csv.writer(out_file)
                writer.writerow(('title', 'intro'))
                writer.writerows(lines)
            
        
        
        
    else:
        continue
    