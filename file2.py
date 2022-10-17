A function that uses command line arguments. This function will print two variables used, the script and then the script AND variables:
  
#!/usr/bin/env python3

#importing the sys module in script
import sys

#defining the command line argument in which we have two main variables which are further defined. Apart from these variables, we have four print statements
#which are printing the value of those variables. 
def cmd_args():
        name = str()
        section = str()
      
        name = sys.argv[1]
        section = sys.argv[2]
        
        print(f"Element1 = {name}")
        print(f"Element2 = {section}")
        print(f"Script: {sys.argv[0]}")
        print("Script and variables are : ", sys.argv[0], name, section)
        
   if __name__ == "__main__":
     cmd_args()
