 # L'algoritmo seleziona di volta in volta il numero maggiore nella sequenza di partenza
 # e lo sposta nella sequenza ordinata; di fatto la sequenza viene suddivisa in due parti:
 # la sottosequenza ordinata, che occupa le prime posizioni dell'array,
 # e la sottosequenza da ordinare, che costituisce la parte restante dell'array. nel main si inserisce un array lungo 20
   
from random import random

LIST_LENGTH = 20  

def biggest(array, index):
    #trova l'indice dell'elemento più grande dell'array di interi 
    big = 0
    for i in range(index+1):
        if array[i] > array[big]:
            big = i
    return big

def swap(array, num1, num2):
    #swap l'elemento di posto num2 con quello di posto num1 
    tmp = array[num1]
    array[num1] = array[num2]
    array[num2] = tmp
    return array

def check_sort(numbers, index):
    #controllo se l'array è ordinato
    for i in range(index+1):
        if numbers[i] > numbers[i+1]:  #  voglio l'ordine crescente
            return True  # cioè non è in ordine 
    return False

def selection_sort(array):
    passes = 0
    index = len(array) - 1
    while check_sort(array, index):
        num = biggest(array, index)
        array = swap(array, index, num)
        index -= 1
        passes += 1
        print("List: %s, Passes: %s" % (array, passes))
    
    return array
#test della selection_sort su un array random 
def main():
    to_sort = []

    for i in range(LIST_LENGTH):
        to_sort.append(int(input("Enter a number: ")))
    print("Unsorted: %s\n" % (to_sort))

    sort = selection_sort(to_sort)
    print("\nSorted: %s" % (sort))



if __name__ == "__main__":
    main()   
