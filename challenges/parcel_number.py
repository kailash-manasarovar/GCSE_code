# OUTPUT ‘Write your parcel number’
# parcelNumber ← USERINPUT
# IF LEN(parcelNumber) = 8 THEN
# OUTPUT ‘Valid parcel number’
# ELSE
# OUTPUT ‘Not a valid parcel number’
# ENDIF

parcel_number = input("What is your parcel number?")

if len(parcel_number) == 8:
    print("Valid parcel number.")
else:
   print("Not a valid parcel number.")