def main():
    print("Hello World")

def Ex():
    # Ex1
    # Find the all factors of x using a loop and the operator % 
    # % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
    print("\nEx1:")
    x = 52633
    for i in range(x+1):
        if i == 0:
            continue
        if x % i == 0:
            print(i)

    # Ex2
    # Write a function that prints all factors of the given parameter x
    print("\nEx2:")
    def print_factor(x):
        for i in range(x+1):
            if i == 0:
                continue
            if x % i == 0:
                print(i)

    # Ex3
    # Write a program that be able to find all factors of the numbers in the list l
    print("\nEx3:")
    l = [52633, 8137, 1024, 999]
    for num in l:
        print_factor(num)

if __name__ == "__main__":
    main()
    print("\nEx:")
    Ex()
