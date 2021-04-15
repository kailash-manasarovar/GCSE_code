# i = "hello"
#
# if i.isupper():
#     pass
#
#
#
# car_array = ["car1", "car2", "car3", "...", "car20"] # more memory
#
# car1 = "car1"
# car2 = "car2"
# car3 =
# ...


cat_box = 0
dog_box_small = 0
dog_box_medium = 0
dog_box_large = 0

order = input("what type of box?")
order_amount = input("how many?")

if order == cat_box:
    cat_box = cat_box + order_amount

total_boxes = cat_box + dog_box_large

print(total_boxes)