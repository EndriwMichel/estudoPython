# Selection sort

class SelectionSort(object):

    def sort(self, data):

        for x in range(len(data)):
            for i in range(len(data)):
                if data[x] < data[i]:
                    aux_x = data[i]
                    aux_i = data[x]
                    data[x] = aux_x
                    data[i] = aux_i
        
        return print(data)

new_selection = SelectionSort()

# Dados para o selection
array = [8, 5, 2, 80, 3, 1, 4, 0, 7, 12]

new_selection.sort(array)



