def part_1():
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))
    bmi = (weight * 703) / ( (height ** 2))
    print("Your BMI is: ", round(bmi, 2))
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

def part_2():
    even_list = []
    even_total = 0
    for i in range(2, 101, 2):
        even_list.append(i)
    for x in even_list:
        even_total += x
    print("\nThe sum of all even numbers from 0 to 100 is:", even_total)

def part_3():
    odd_start = int(input("Enter your starting number: "))
    odd_end = int(input("Enter your ending number: "))
    odd_list = []
    odd_total = 0
    if odd_start % 2 == 0:
        odd_start + 1
        odd_list.append(odd_start)
    else:
        odd_list.append(odd_start)
    if odd_end % 2 == 0:
        odd_end -= 1
        odd_list.append(odd_end)
    else:
        odd_list.append(odd_end)
    for i in range(odd_start, odd_end, 2):
        odd_list.append(i)
    for x in odd_list:
        odd_total += x
    print("\nThe sum of all odd numbers from", odd_start, "to", odd_end, "is:", odd_total - 1)

def part_4():
    target_price = float(input("Enter the target price: "))
    current_price = 0
    while True:
        if current_price < target_price:
            current_price = float(input("Enter the current price: "))
        elif current_price >= target_price:
            print("The the target price has been met. \nThe shares can be sold now.")
            break
        else:
            print("Invalid input.")

def part_5():
    tuition = 8000.00
    i = 0
    print("\nThe tuition for year 1 is: $", tuition)
    while i <= 4:
        tuition = tuition * 1.03
        i += 1
        print("The tuition for year" ,i + 1, "is: $", round(tuition,2))

def main():
    print("Would you like to run part 1, 2, 3, 4, or 5 of the assignment?")
    print("You can also type view to get an overview of all parts, or exit to quit the program.")
    usr_input = input("Enter 1, 2, 3, 4, 5, view, or exit: ").lower()
    if usr_input == "1":
        part_1()
        main()
    elif usr_input == "2":
        part_2()
        main() 
    elif usr_input == "3":
        part_3()
        main()  
    elif usr_input == "4":
        part_4()
        main()
    elif usr_input == "5":
        part_5()
        main()
    elif usr_input == "view":
        print("\nPart 1: Calculate BMI and determine weight category."
              "\nPart 2: Calculate the sum of all even numbers from 0 to 100."
              "\nPart 3: Calculate the sum of all odd numbers within a user-defined range."
              "\nPart 4: Monitor stock price until it meets or exceeds a target price."
              "\nPart 5: Calculate and display tuition increase over 5 years with a 3% annual increase.")
        main()
    else:
        print("Exiting the program. Goodbye!")
        exit()
main()
    

    

    