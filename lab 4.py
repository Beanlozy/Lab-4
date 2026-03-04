import random


keep_going = True

while keep_going == True:
    print("")
    print("=== Egyptian Sacred Symbols ===")
    print("1. Display a random shape")
    print("2. Exit")
    print("")
    
    user_choice = input("Enter your choice (1 or 2): ")
    
    if user_choice == "1":
        print("")
        
        
        shape_number = random.randint(1, 4)
        
        if shape_number == 1:
           
            num_rows = random.randint(5, 8)
            
            row = 0
            while row < num_rows:
                col = 0
                while col < 8:
                    if col == 0:
                        print("*", end="")
                    elif col == 1:
                        print("~", end="")
                    elif col == 2:
                        print("*", end="")
                    elif col == 3:
                        print("~", end="")
                    elif col == 4:
                        print("*", end="")
                    elif col == 5:
                        print("~", end="")
                    elif col == 6:
                        print("*", end="")
                    elif col == 7:
                        print("~", end="")
                    col = col + 1
                print()
                row = row + 1
        
        if shape_number == 2:
          
            print("    *")
            print("   ***")
            print("  *****")
            print(" *******")
            print("*********")
            print("    |")
            print("    |")
        
        if shape_number == 3:
            
            print("        *")
            print("       * *")
            print("      * * *")
            print("     * * * *")
            print("    * * * * *")
            print("   * * * * * *")
            print("  * * * * * * *")
            print(" * * * * * * * *")
        
        if shape_number == 4:
           
            num_rows = random.randint(3, 5)
            num_cols = random.randint(6, 10)
            
            row = 0
            while row < num_rows:
                col = 0
                while col < num_cols:
                    print("*", end="")
                    col = col + 1
                print()
                row = row + 1
    
    if user_choice == "2":
        print("The Pharaoh releases you from your duties. Farewell, scribe!")
        keep_going = False
    
    if user_choice != "1" and user_choice != "2":
        print("Invalid choice! Please enter 1 or 2.")
