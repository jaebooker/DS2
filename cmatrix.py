def accuracy(confusion_matrix):
    new_array = []
    new_array.append((confusion_matrix[0]+confusion_matrix[1])/len(confusion_matrix))
    new_array.append(confusion_matrix[0]/(confusion_matrix[0]+confusion_matrix[3]))
    new_array.append((confusion_matrix[0])/(confusion_matrix[4]+confusion_matrix[0]))
    new_array.append(2**(new_array[1]*new_array[3])/(new_array[1]*new_array[3]))
    return new_array
