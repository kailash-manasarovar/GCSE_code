#SET list TO [5,9,2,5,13]
#RECEIVE item FROM (INTEGER) KEYBOARD
#SET found TO false
#FOR search FROM 0 to LENGTH(list) DO
#   IF item = list[search] THEN
#   found = true
#   END IF
#END FOR
#IF found = true THEN
#SEND 'the item is in the list' TO DISPLAY
#ELSE
#SEND 'the item is not in the list' TO DISPLAY
#END IF



