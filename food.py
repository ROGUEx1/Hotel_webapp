
# appetizer foods: 

def food():



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


    menu_appetizer=["garlic bread","soup"]
    menu_entree=["pizza","burger","fried chicken fillet"]
    menu_dessert=["caramel panna cotta","nutella cheesecake"]
    menu_drink=["mohito","coca"]

    appetizer_list=[]
    appetizer_quantity=[]

    entree_list=[]
    entree_quantity=[]

    dessert_list=[]
    dessert_quantity=[]

    drink_list=[]
    drink_quantity=[]

    done = False
    while(not done):
        print("Please choose your appetizer. Type none if you want nothing and done when you are done ")
        appetizer = input()

        if (appetizer != "done" and appetizer != "none"):
            order = 0
            quantity = 1
            while (order < len(menu_appetizer)):
        
                    
                if(appetizer == menu_appetizer[order]):
                    
                    while(quantity == 1):
                        print("how many",appetizer,"do you want? ")
                        appetizer_number = input()
                        try:
                            appetizer_number = int(appetizer_number)
                            quantity = 2
                            appetizer_quantity.append(appetizer_number)
                            appetizer_list.append(appetizer)
                            print("Okay",appetizer_number,appetizer,"is added")
                            order = order + len(menu_appetizer)
                            
                        except:
                            print("Invalid input, please enter a number ")
                        
                else:
                    order+=1
                        
            if(quantity == 1):
                print("Please choose from the menue:",menu_appetizer)
                
                
        if(appetizer == "done"):
            done = True
            for count in range (len(appetizer_list)):
                print("You have orderd",appetizer_quantity[count],appetizer_list[count],"for appetizer")
        
        if(appetizer == "none"):
            done = True
            print("Alright")

    #entree order

    done = False
    while(not done):
        print("Please choose your entree. Type none if you want nothing and done when you are done. ")
        entree = input()

        if (entree != "done" and entree != "none"):
            order = 0
            quantity = 1
            while (order < len(menu_entree)):
        
                    
                if(entree == menu_entree[order]):
                    
                    while(quantity == 1):
                        print("How many",entree,"do you want? ")
                        entree_number = input()
                        try:
                            eentree_number = int(entree_number)
                            quantity = 2
                            entree_quantity.append(entree_number)
                            entree_list.append(entree)
                            print("Okay",entree_number,entree,"is added")
                            order = order + len(menu_entree)
                            
                        except:
                            print("Invalid input, please enter a number ")
                        
                else:
                    order+=1
                        
            if(quantity == 1):
                print("Please choose from the menue:",menu_entree)
                
                
        if(entree == "done"):
            done = True
            for count in range (len(entree_list)):
                print("You have orderd",entree_quantity[count],entree_list[count],"for entree")

        if(entree == "none"):
            done = True
            print("Alright")

    #dessert order
    done = False
    while(not done):
        print("Please choose your dessert. Type none if you want nothing and done when you are done. ")
        dessert = input()

        if (dessert != "done" and dessert != "none"):
            order = 0
            quantity = 1
            while (order < len(menu_dessert)):
        
                    
                if(dessert == menu_dessert[order]):
                    
                    while(quantity == 1):
                        print("How many",dessert,"do you want? ")
                        dessert_number = input()
                        try:
                            dessert_number = int(dessert_number)
                            quantity = 2
                            dessert_quantity.append(dessert_number)
                            dessert_list.append(dessert)
                            print("Okay",dessert_number,dessert,"is added")
                            order = order + len(menu_dessert)
                            
                        except:
                            print("Invalid input, please enter a number ")
                        
                else:
                    order+=1
                        
            if(quantity == 1):
                print("Please choose from the menue:",menu_dessert)
                
                
        if(dessert == "done"):
            done = True
            for count in range (len(dessert_list)):
                print("You have orderd",dessert_quantity[count],dessert_list[count],"for desert")
       
        if(dessert == "none"):
            done = True
            print("Alright")


    #drink order

    done = False
    while(not done):
        print("Please choose your drink. Type none if you want nothing and done when you are done. ")
        drink = input()

        if (drink != "done" and drink != "none"):
            order = 0
            quantity = 1
            while (order < len(menu_drink)):
        
                    
                if(drink == menu_drink[order]):
                    
                    while(quantity == 1):
                        print("How many",drink,"do you want? ")
                        drink_number = input()
                        try:
                            drink_number = int(drink_number)
                            quantity = 2
                            drink_quantity.append(drink_number)
                            drink_list.append(drink)
                            print("ok",drink_number,drink,"is added")
                            order = order + len(menu_drink)
                            
                        except:
                            print("Invalid input, please enter a number ")
                        
                else:
                    order+=1
                        
            if(quantity == 1):
                print("Please choose from the menue:",menu_drink)
                
                
        if(drink == "done"):
            done = True
            for count in range (len(drink_list)):
                print("You have orderd",drink_quantity[count],drink_list[count],"for drink")
        
        
        if(dessert == "none"):
            done = True
            print("Alright")


    #order confirmation
    print("For appetizer you have ordered: ")
    if(len(appetizer_quantity) == 0):
        print("nothing")
    for count2 in range (len(appetizer_quantity)):
        print(appetizer_quantity[count2],appetizer_list[count2])

    print("For entree you have ordered: ")
    if(len(entree_quantity) == 0):
        print("nothing")
    for count2 in range (len(entree_quantity)):
        print(entree_quantity[count2],entree_list[count2])

    print("For dessert you have ordered: ")
    if(len(dessert_quantity) == 0):
        print("nothing")
    for count3 in range (len(dessert_quantity)):
        print(dessert_quantity[count3],dessert_list[count3])

    print("For drink you have ordered: ")
    if(len(drink_quantity) == 0):
        print("nothing")
    for count4 in range (len(drink_quantity)):
        print(drink_quantity[count4],drink_list[count4])


    



    print("If you confirm this order type yes")
    orderconfrimation = input()
    if(orderconfrimation == "yes"):
        print("We have sent your order to the catering department. It will be ready soon. Thank you for your order.")
                write = open("food_order_database.txt","a")
        write.write(room_number)
        write.write("\n")
        if(len(appetizer_quantity) == 0):
            write.write("nothing\n")
        for count2 in range (len(appetizer_quantity)):
            write.write(appetizer_quantity[count2],appetizer_list[count2],"\n")

        write.write(room_number)
        write.write("\n")
        if(len(entree_quantity) == 0):
            write.write("nothing\n")
        for count2 in range (len(entree_quantity)):
            write.write(entree_quantity[count2],entree_list[count2],"\n")

        write.write(room_number)
        write.write("\n")
        if(len(dessert_quantity) == 0):
            write.write("nothing\n")
        for count3 in range (len(dessert_quantity)):
            write.write(dessert_quantity[count3],dessert_list[count3],"\n")

        write.write(room_number)
        write.write("\n")
        if(len(drink_quantity) == 0):
            write.write("nothing\n")
        for count4 in range (len(drink_quantity)):
            write.write(drink_quantity[count4],drink_list[count4],"\n") 
        write.close()

    if(orderconfrimation != "yes"):
        print("Alright, let's redo the order")
        food()

food()
