# procedure sort_it(data_array, last_index)
#   for x = 1 to last_index
#       current_data = data_array[x]
#       position = x
#       while (position > 0 AND data_array[x – 1] > current_data)
#           data_array[position] = data_array[position-1]
#           position = position – 1
#       endwhile
#       dataArray[position] = currentData
#   next x
# endprocedure