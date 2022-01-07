import food_menu

def room():
    condition = False
    while (not condition):
        try:
            room_number = int(input("Pleas enter your room number "))
            room_number_confirmation = int(input("pleas confrim your room number "))
            if(room_number == room_number_confirmation):
                print("ok your room number is",room_number)
                condition = True
                
            else:
                print("your room number should match the previous one.")
        except:
            print("invalid input, please enter a number")
    food()

menu_apetizer=["garlic bread","soup"]
menu_entree=["pizza","burger","fried chicken fillet"]
menu_dessert=["caramel panna cotta","nutella cheesecake"]
menu_drink=["mohito","coca"]

apetizer_list=[]
apetizer_quantity=[]

entree_list=[]
entree_quantity=[]

dessert_list=[]
dessert_quantity=[]

drink_list=[]
drink_quantity=[]


# apetizer foods: 

def food():
    
    done = False
    while(not done):
        print("Please enter your apetizer from menue. Type done when you are done. ")
        apetizer = input()

        if (apetizer != "done"):
            order = 0
            quantity = 1
            while (order < len(menu_apetizer)):
        
                    
                if(apetizer == menu_apetizer[order]):
                    
                    while(quantity == 1):
                        print("how many",apetizer,"do you want? ")
                        apetizer_number = input()
                        try:
                            apetizer_number = int(apetizer_number)
                            quantity = 2
                            apetizer_quantity.append(apetizer_number)
                            apetizer_list.append(apetizer)
                            print("ok",apetizer_number,apetizer,"added")
                            order = order + len(menu_apetizer)
                            
                        except:
                            print("invalid input, please enter a number ")
                        
                else:
                    order+=1
                        
            if(quantity == 1):
                print("write from menu list and atention to writing",menu_apetizer)
                
                
        if(apetizer == "done"):
            done = True
            for count in range (len(apetizer_list)):
                print("for appetizer you orderd",apetizer_quantity[count],apetizer_list[count])

    #entree order

    done = False
    while(not done):
        print("Please enter your entree from menue. Type done when you are done. ")
        entree = input()

        if (entree != "done"):
            order = 0
            quantity = 1
            while (order < len(menu_entree)):
        
                    
                if(entree == menu_entree[order]):
                    
                    while(quantity == 1):
                        print("how many",entree,"do you want? ")
                        entree_number = input()
                        try:
                            eentree_number = int(entree_number)
                            quantity = 2
                            entree_quantity.append(entree_number)
                            entree_list.append(entree)
                            print("ok",entree_number,entree,"added")
                            order = order + len(menu_entree)
                            
                        except:
                            print("invalid input, please enter a number ")
                        
                else:
                    order+=1
                        
            if(quantity == 1):
                print("write from menu list and atention to writing",menu_entree)
                
                
        if(entree == "done"):
            done = True
            for count in range (len(entree_list)):
                print("for entree you orderd",entree_quantity[count],entree_list[count])

    #dessert order
    done = False
    while(not done):
        print("Please enter your dessert from menue. Type done when you are done. ")
        dessert = input()

        if (dessert != "done"):
            order = 0
            quantity = 1
            while (order < len(menu_dessert)):
        
                    
                if(dessert == menu_dessert[order]):
                    
                    while(quantity == 1):
                        print("how many",dessert,"do you want? ")
                        dessert_number = input()
                        try:
                            dessert_number = int(dessert_number)
                            quantity = 2
                            dessert_quantity.append(dessert_number)
                            dessert_list.append(dessert)
                            print("ok",dessert_number,dessert,"added")
                            order = order + len(menu_dessert)
                            
                        except:
                            print("invalid input, please enter a number ")
                        
                else:
                    order+=1
                        
            if(quantity == 1):
                print("write from menu list and atention to writing",menu_dessert)
                
                
        if(dessert == "done"):
            done = True
            for count in range (len(dessert_list)):
                print("for dessert you orderd",dessert_quantity[count],dessert_list[count])

    #drink order

    done = False
    while(not done):
        print("Please enter your drink from menue. Type done when you are done. ")
        drink = input()

        if (drink != "done"):
            order = 0
            quantity = 1
            while (order < len(menu_drink)):
        
                    
                if(drink == menu_drink[order]):
                    
                    while(quantity == 1):
                        print("how many",drink,"do you want? ")
                        drink_number = input()
                        try:
                            drink_number = int(drink_number)
                            quantity = 2
                            drink_quantity.append(drink_number)
                            drink_list.append(drink)
                            print("ok",drink_number,drink,"added")
                            order = order + len(menu_drink)
                            
                        except:
                            print("invalid input, please enter a number ")
                        
                else:
                    order+=1
                        
            if(quantity == 1):
                print("write from menu list and atention to writing",menu_drink)
                
                
        if(drink == "done"):
            done = True
            for count in range (len(drink_list)):
                print("for drink you orderd",drink_quantity[count],drink_list[count])

    #order confirm 
    print()
room()
