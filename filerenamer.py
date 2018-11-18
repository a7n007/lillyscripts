import os
c = 1
for root, dirs, files in os.walk("."):  
    for filename in files:
    	if(filename[0].isdigit() or filename=='filerenamer.py'):
        	print(filename)
    	else:
        	 os.rename(filename, str(c)) 
        	 c = c + 1