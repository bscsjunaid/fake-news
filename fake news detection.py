print(" ***** Unit Calculator Program ***** ")
print(" "," ")
def meter_To_Kilometer(meter):
    return (meter/1000)
def kilometer_To_Meter(kilometer):
    return (kilometer*1000)
def centimeter_To_Meter(centimeter):
    return (centimeter/100)
def centimeter_To_Millimeter(centimeter):
    return (centimeter*10)

def Menu():
    while True:
        print(" ")
        print(" ")
        print(" **** Select Operation **** ")
        print("1.Meter_To_Kilometer ")
        print("2.Kilometer_To_Meter ")
        print("3.Centimeter_To_Meter ")
        print("4.centimeter_To_Millimeter ")
        print("5.Exit")

        choice=input(" Enter any number to select operation (1/2/3/4/5) : ")

        if choice in('1','2','3','4','5'):
            print(" "," ")
            if choice == '1':
                print(" **** Meter_To_Kilometer **** ")
                meter = float(input("How many meter : "))
                print(meter,"/",1000,"=",meter_To_Kilometer(meter))
            elif choice == '2':
                print(" **** Kilometer_To_Meter **** ")
                kilometer = float(input("How many kilometer : "))
                print(meter,"*",1000,"=",kilometer_To_Meter(kilometer))
            elif choice == '3':
                print(" **** Centimeter_To_Meter **** ")
                centimeter = float(input("How many centimeter : "))
                print(centimeter,"/",100,"=",centimeter_To_Meter(centimeter))
            elif choice == '4':
                print(" **** centimeter_To_Millimeter **** ")
                centimeter = float(input("How many centimeter : "))
                print(centimeter,"*",1000,"=",centimeter_To_Millimeter(centimeter))    
            if choice == '5':
                break

while True:
    print(" **** Select Operation **** ")
    print("1.Menu")
    print("2.Exit ")

    choice=input(" Enter any number to select operation (1/2) : ")

    if choice in('1','2'):
        if choice == '1':
            print(Menu()," "," ")
        elif choice == '2':
            break  
