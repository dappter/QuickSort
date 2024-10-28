def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] 
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    lista_desordenada = [3, 6, 8, 10, 1, 2, 1]
    print("Lista desordenada:", lista_desordenada)
    lista_ordenada = quick_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada) 