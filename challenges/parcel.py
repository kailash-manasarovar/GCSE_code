
#Task 2 & 3
numberOfParcels = 0
acceptedParcels = 0
rejectedParcels = 0
totalWeight = 0 # to increment the total weight of only accepted parcels
rejected = False # boolean variable to set whether parcel is accepted or not

#create and set the variables via user input
weight = input("Please enter the weight of the package in KGs: ")
height = input("Please enter the length of the box in cm: ")
width = input("Please enter the width of the box in cm: ")
depth = input("Please enter the depth of the box in cm: ")


def checkParcel():
    #if we got here, there's one more parcel, so increment total number of parcels
    global numberOfParcels
    global rejectedParcels
    global acceptedParcels
    global rejected
    
    numberOfParcels += 1

    #check the weight and dimensions are within limits
    if weight <= 2 or weight >= 10:
        print("Sorry, we only deal with weights over 2KG and under 10KG")
        #increment rejected parcels and go to the end
        rejectedParcels = rejectedParcels + 1
        rejected = True
        return;
        
    elif (height > 80 or width > 80 or depth > 80):
        print("Sorry, we only deal with dimensions below 80cm")
        rejectedParcels = rejectedParcels + 1
        rejected = True
        return;
            
    elif ((height + width + depth) > 200):
        print("Sorry, your dimensions are too large for our system.")
        rejectedParcels = rejectedParcels + 1
        rejected = True
        return;
           
    else:
        #print("Your parcel is accepted")
        acceptedParcels = acceptedParcels + 1
        rejected = False
        
#run function
checkParcel()

if (rejected == True):
    print("Your parcel is rejected because it is over weight by...")
    # and you can fill out the required details here...
    
else:
    print("Your parcel is accepted " ) #and all the details here