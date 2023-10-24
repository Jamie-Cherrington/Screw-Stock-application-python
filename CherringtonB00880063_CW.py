

master_list = [] #this is the list that code and function will refer back to when its stated.  



def loadlist():
    screw_list= [] # This here defines the empty table
    myfile = open('SCREW_DATA_ENHANCED.txt') #tells the file to open the screw text file. 
    for row in myfile:
        if not row.startswith("#"): #this will remove hastag
            row = row.strip('\n').split(',')
            screw_list.append(row)
    return screw_list


master_list = loadlist() 

def feature1(scwList): #feature 1 list function.
    print('Screw types on sale: \n')
    for i in range(len(scwList)):  #for loop
        print(scwList[i][0],scwList[i][1],scwList[i][2]+'mm') #This line collects the index properties as stated and displays in given format 'mm'.
        unitsStock = (int(scwList[i][3])+ (int(scwList[i][4])*2) + (int(scwList[i][5])*4)) #gathers all the units of stock.
        valuestock = (int(scwList[i][3])*(float(scwList[i][6]))) + (int(scwList[i][4])*(float(scwList[i][6]))*0.9*2) + (int(scwList[i][5])*(float(scwList[i][6]))*0.85*4)
        print(f"{unitsStock} Is the total units of stock and total value of stock with bulk discounts £{valuestock:,.2f}\n")


def feature2(scrw_length):  #basic feature 2 to find total number of units in stock for each length. 
    print('Screw lenth total')
    scrw_total20=0  #delcaring the values of screw lenths as zero as well as giving it a variable.
    scrw_total40=0
    scrw_total60=0
    for item in scrw_length: #creating a for loop screwlenghts.
        if item[2] =="20": #if item in in index '2' = '20' then the following if statement will execute,same is applied to other lengths.
            scrw_total20 += scrw_unitLength(int(item[3]),int(item[4]),int(item[5]))
        if item[2] =="40":
            scrw_total40 += scrw_unitLength(int(item[3]),int(item[4]),int(item[5]))#variable type adds the index value of 
        if item[2] =="60":
            scrw_total60 += scrw_unitLength(int(item[3]),int(item[4]),int(item[5]))
    print("20mm screws currently have", scrw_total20, "units of stock")
    print("40mm screws currently have", scrw_total40, "units of stock") 
    print("60mm screws currently have", scrw_total60, "units of stock") #prints the output data to the user. 

def scrw_unitLength(x,y,z):
    total = (x + (y*2) + (z*4)) 
    return total



def feature3(search):
    screwlength = input("please input/enter a length category to search for eg,[20mm],[40mm],[60mm]") #Gathers input from user. 
    print("Available screws for", screwlength + "mm\n")
    for item in search: #start a for loop,that if an item in index 2= the screw length itll print the material and slot type. 
        if item[2] == screwlength:
            print(item[0],item[1])
            units_of_stock = int(item[3]) + int(item[4]) + int(item[4]) + int(item[5]) + int(item[5]) + int(item[5])+ int(item[5]) #adds the value for all the box variants.
            print("This screw type has", units_of_stock,"units of stock")


def feature4(chnge_stock):

   # option_1 = input("to decrease stock input enter [1] to increase press [2]") #testing options mwnu within 
   #need to implement a memu to display option for increasing or decreasig stock

    option_1 = input("Input option '1' for increasing stock! To decrease stock input option '2'!::")
    if option_1 == "1":
        scrw_mat = input("Please input the screw material [Brass or Steel]: ")
        scrw_head= input("Please input the head type [slot,star,pozidriv]: ")
        scrw_length= input("please input the screw length [20mm,40mm,60mm]: ") #giving all variables an input instructions 
        scrw_type= [scrw_mat,scrw_head,scrw_length]
        for item in chnge_stock:
            sname = (f"{item[0]} {item[1]} {item[2]}")         #For-loop created that matches the input with the index of decsription.
            if scrw_type[0]==item[0]:
                if scrw_type[1]==item[1]:
                    if scrw_type[2]==item[2]:      #with line below if the inputs match the for loop/if statemnts the following is outputted below.
                        option_a = input("item found, what category of box sizes do you wish to update? 50,100,200?: ")
                                                
                        if option_a == "50":
                            increase_amnt = int(input(f"How many units would you like to add?: "))
                            new_amount= (int(item[3]) + increase_amnt)
                            item[3] = new_amount
                            index_item = chnge_stock.index(item)
                            master_list[index_item][3] = new_amount
                            print(f"stock level of {sname} is {master_list[index_item][3]}")
                            #if the inputed value matches this IF statement requirement of "50" itll update the list via finding thru index values.
                        
                        if option_a == "100":
                            increase_amnt = int(input(f"How many units would you like to add?: "))
                            new_amount= (int(item[4]) + increase_amnt)
                            item[4] = new_amount
                            index_item = chnge_stock.index(item)
                            master_list[index_item][4] = new_amount
                            print(f"stock level of {sname} is {master_list[index_item][4]}")
                        
                        if option_a == "200":
                            increase_amnt = int(input(f"How many units would you like to add?: "))
                            new_amount= (int(item[5]) + increase_amnt)
                            item[5] = new_amount
                            index_item = chnge_stock.index(item)
                            master_list[index_item][5] = new_amount
                            print(f"stock level of {sname} is {master_list[index_item][5]}")
    else:
        scrw_mat = input("Please input the screw material [Brass or Steel]: ")
        scrw_head= input("Please input the head type [slot,star,pozidriv]: ")
        scrw_length= input("please input the screw length [20mm,40mm,60mm]: ")
        scrw_type= [scrw_mat,scrw_head,scrw_length]
        for item in chnge_stock:
            sname = (f"{item[0]} {item[1]} {item[2]}")
            if scrw_type[0]==item[0]:
                if scrw_type[1]==item[1]:
                    if scrw_type[2]==item[2]:
                        option_b = input("item found, what category of box sizes do you wish to decrease 50,100,200?: ")

                        if option_b == "50":
                            decrease_amnt = int(input(f"How many units would you like to Decrease?: ")) 
                            check_stock = (int(item[3]) - decrease_amnt)
                            order_cost = int(item[3])
                            if int(check_stock) <= 0:
                                option_b = input(f"This order can only be partially fulfilled: Do you wish to remove {item[3]} ?")
                                if option_b == "yes":
                                    index_item = chnge_stock.index(item)
                                    master_list[index_item][3] = 0
                                    print(f"Action completed! New stock of {sname} is {master_list[index_item][3]}")
                                    final_order_cst = order_cost * float(item[6])
                                    print(f"The final order cost is £{final_order_cst:,.2f}") 
                        
                            else:
                                new_amount = (int(item[3]) - decrease_amnt)
                                final_order_cst = decrease_amnt * float(item[6])
                                index_item = chnge_stock.index(item)
                                master_list[index_item][3]= new_amount
                                print(f"Action completed! New stock of {sname} is {master_list[index_item][3]}")
                                print(f"The final order cost is £{final_order_cst:,.2f}")

                        if option_b == "100":
                            decrease_amnt = int(input(f"How many units would you like to Decrease?: "))  
                            check_stock = (int(item[4]) - decrease_amnt)
                            order_cost = int(item[4])
                            if int(check_stock) <= 0: #if item gets dcreased more than stock records run the following statement
                                option_b = input(f"This order can only be partially fulfilled: Do you wish to remove {item[4]} ?")
                                if option_b == "yes":
                                    index_item = chnge_stock.index(item)
                                    master_list[index_item][4] = 0
                                    print(f"Action completed! New stock of {sname} is {master_list[index_item][4]}")
                                    final_order_cst = order_cost * float(item[6])
                                    print(f"The final order cost is £{final_order_cst:,.2f}") 

                            else:
                                new_amount = (int(item[4]) - decrease_amnt)
                                final_order_cst = decrease_amnt * float(item[6])
                                index_item = chnge_stock.index(item)
                                master_list[index_item][4]= new_amount
                                print(f"Action completed! New stock of {sname} is {master_list[index_item][4]}")
                                print(f"The final order cost is £{final_order_cst:,.2f}")
                        
                        if option_b == "200":
                            decrease_amnt = int(input(f"How many units would you like to Decrease?: "))  
                            check_stock = (int(item[5]) - decrease_amnt)
                            order_cost = int(item[5])
                            if int(check_stock) <= 0:
                                option_b = input(f"This order can only be partially fulfilled: Do you wish to remove {item[5]} ?")
                                if option_b == "yes":
                                    index_item = chnge_stock.index(item)
                                    master_list[index_item][5] = 0
                                    print(f"Action completed! New stock of {sname} is {master_list[index_item][5]}")
                                    final_order_cst = order_cost * float(item[6])
                                    print(f"The final order cost is £{final_order_cst:,.2f}") 


                            else:
                                new_amount = (int(item[5]) - decrease_amnt)
                                final_order_cst = decrease_amnt * float(item[6])
                                index_item = chnge_stock.index(item)
                                master_list[index_item][5]= new_amount
                                print(f"Action completed! New stock of {sname} is {master_list[index_item][5]}")
                                print(f"The final order cost is £{final_order_cst:,.2f}")
                                
                             


def feature5(discount):
    new_list = []
    for i in range(len(discount)):
        unitsStock = (int(discount[i][3])+ (int(discount[i][4])*2) + (int(discount[i][5])*4))#gathers the values from the index list 
        new_list.append(unitsStock)
    maxIndex = new_list.index(max(new_list))
    print(f"{discount[maxIndex][0]} {discount[maxIndex][1]} {discount[maxIndex][2]} mm has the current most stock")

    option_a = input("Do you wish to add 10% discount on this screw category?: ")
    if option_a.lower() == "yes":
        for item in discount:
            if item[7] == " yes":
                option_b = input("There is a sale active do you wish to contiune or stop?")
                previous_sale=  (discount.index(item))
                master_list[previous_sale][7] = " no"
                master_list[maxIndex][7] =  " yes"
            else:
                main() 
    else:
        main() #if user doesnt wish to add discount return them to the menu
        


def feature6(barchart):
    scrw_total20=0  #delcaring the values of screw lenths as zero as well as giving it a variable.
    scrw_total40=0
    scrw_total60=0
    for item in barchart: #creating a for loop screwlenghts.
        if item[2] =="20": #if item in in index '2' = '20' then the following if statement will execute,same is applied to other lengths.
            scrw_total20 += scrw_unitLength(int(item[3]),int(item[4]),int(item[5]))
        if item[2] =="40":
            scrw_total40 += scrw_unitLength(int(item[3]),int(item[4]),int(item[5]))#variable type adds the index value of 
        if item[2] =="60":
           scrw_total60 += scrw_unitLength(int(item[3]),int(item[4]),int(item[5]))



    import matplotlib.pyplot as plt #This tells the inturpetuer to import the matplotlib plug in.
    import numpy as np

    screw_Length=['20mm','40mm','60mm'] #setting the variables  for the bar chart to convert. 
    scrw_lenth_category = [scrw_total20,scrw_total40,scrw_total60]
    pos = np.arange(len(screw_Length))

    plt.bar(pos,scrw_lenth_category,color='red',edgecolor='black') #lets the user set the colour of the bar chart 
    plt.xticks(pos, screw_Length)
    plt.xlabel('length')    #these lines of code are in rleation to the title and fromat the barchart will be presented in. 
    plt.ylabel('units of stock')
    plt.title('units of stock in by length')
    plt.show()




def main():
    print("""1)list of screw types with total stock & Value\n2)Number of units in stock acording to length\n3)List of screws in stock refined by length\n4)Change stock levels\n5)change discount\n6)Bar chart\n7)exit""")
    
    option = input("please input an option ")

    if option == "1":
        feature1(master_list)
        main()
    elif option == "2":
        feature2(master_list)
        main()
    elif option == "3":
        feature3(master_list)
        main()
    elif option == "4":
        feature4(master_list)
        main()
    elif option == "5":
        feature5(master_list)
        main()
    elif option =="6":
        feature6(master_list)
        main()
    elif option =="7":
        quit()
    else:
        print("Invalid option!")
        main() 
if __name__ == "__main__":
    main()



main()

    
 
main()

