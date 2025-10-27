# Drew Crockett
#10/26/25
# Module 1.3

def countdown(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            bottles -= 1
            print(f"Take one down and pass it around, {bottles} bottle{'s' if bottles > 1 else ''} of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
            bottles -= 1
    print("Time to buy more beer!")

def main():
    try:
        bottles = int(input("Enter number of bottles: "))
        if bottles <= 0:
            print("You need at least one bottle to start singing.")
        else:
            countdown(bottles)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
