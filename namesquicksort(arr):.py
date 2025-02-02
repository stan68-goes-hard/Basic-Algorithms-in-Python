def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    names = []
    print("Enter names and surnames (type 'done' to finish):")
    while True:
        name = input()
        if name.lower() == 'done':
            break
        names.append(name)
    
    sorted_names = quicksort(names)
    print("Sorted names and surnames:")
    for name in sorted_names:
        print(name)

if __name__ == "__main__":
    main()