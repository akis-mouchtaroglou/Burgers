import datetime

import json
import os

file_path = os.path.join(os.path.dirname(__file__), "customer.json")
with open(file_path, "r") as f:
    customer = json.load(f)

import json
import os

file_path = os.path.join(os.path.dirname(__file__), "Ending.json")
with open(file_path, "r") as f:
    Ending = json.load(f)

total_cost = 0


def multiplier(num1, num2, total_cost):
    total_cost = total_cost + num1 * num2



twra = datetime.datetime.now()  # <-- If the time is 00:00 (twra = 0 if you want to test it)

if twra == 0:
    print("MACHINE SHUTDOWN - STORE CLOSING")
    SuperSecretAdminCode = input(
        "If you are the store manager, enter the code to view today's statistics: "
    )

    if SuperSecretAdminCode == "9999":
        print(f"Customers today: {Ending[0]}")
        print(f"Today's revenue: {Ending[1]}")

        if Ending[0] != 0:
            print(f"Average order cost: {Ending[1] / Ending[0]}\n")

        Ending[0] = 0
        Ending[1] = 0

        with open(file_path, "w") as f:
            json.dump(Ending, f)

    exit()



print("WELCOME TO BURGER SHOP 🍔")
print("What would you like to order?")
print("---STORE MENU---")

cheeseburger = 6.30
deluxe_burger = 7.60
burger_aplo = 5
xymos = 3
portokalada = 3
votka = 15


print(f"1: Cheeseburger - {cheeseburger:.2f} €")
print(f"2: Deluxe Burger - {deluxe_burger:.2f} €")
print(f"3: Burger - {burger_aplo:.2f} €")
print(f"4: Juice - {xymos:.2f} €")
print(f"5: Orange Soda - {portokalada:.2f} €")
print(f"6: Vodka - {votka:.2f} €")


pelatis_cheeseburger = int(input("How many cheeseburgers would you like? "))
pelatis_deluxe_burger = int(input("How many deluxe burgers would you like? "))
pelatis_burger_aplo = int(input("How many burgers would you like? "))
pelatis_xymos = int(input("How many juices would you like? "))
pelatis_portokalada = int(input("How many orange sodas would you like? "))
pelatis_votka = int(input("How many vodkas would you like? "))



if pelatis_votka >= 1:
    agever = int(input("Scan your ID so we can verify your age before serving vodka: "))

    if agever >= 18:
        print("Since you are 18 or older... Enjoy your drink!!!")

    else:
        print("Nice try... You can drink when you are older!!!")
        pelatis_votka = 0



basket = [pelatis_cheeseburger,pelatis_deluxe_burger,pelatis_burger_aplo,pelatis_xymos,pelatis_portokalada]

list_ctrl = 5


if pelatis_votka >= 1:
    basket = [pelatis_cheeseburger,pelatis_deluxe_burger,pelatis_burger_aplo,pelatis_xymos,pelatis_portokalada,pelatis_votka]

    list_ctrl = 6


multiplier(cheeseburger, pelatis_cheeseburger, total_cost)
multiplier(deluxe_burger, pelatis_deluxe_burger, total_cost)
multiplier(burger_aplo, pelatis_burger_aplo, total_cost)
multiplier(xymos, pelatis_xymos, total_cost)
multiplier(portokalada, pelatis_portokalada, total_cost)
multiplier(votka, pelatis_votka, total_cost)


done = False


while done == False:

    print("Your cart contains:")

    for basket in range(list_ctrl):

        match basket:

            case 0:
                print(f"{pelatis_cheeseburger} cheeseburger")

            case 1:
                print(f"{pelatis_deluxe_burger} deluxe burger")

            case 2:
                print(f"{pelatis_burger_aplo} burger")

            case 3:
                print(f"{pelatis_xymos} juice(s)")

            case 4:
                print(f"{pelatis_portokalada} orange soda(s)")

            case 5:
                print(f"{pelatis_votka} vodka")


    change = input("Would you like to change anything? (Yes = 1, No = 2): ")


    while change not in ["1", "2"]:
        change = input("ONLY YES (1) OR NO (2): ")


    while change == "1":

        item = input("Would you like to change the quantity of a product? (Enter the product number shown above): ")


        while item not in ["1", "2", "3", "4", "5", "6"]:
            mistake = input("Oops, you made a mistake... Try again!!!")
        match item:

            case "1":
                pelatis_cheeseburger = int(input("How many? "))

            case "2":
                pelatis_deluxe_burger = int(input("How many? "))

            case "3":
                pelatis_burger_aplo = int(input("How many? "))

            case "4":
                pelatis_xymos = int(input("How many? "))

            case "5":
                pelatis_portokalada = int(input("How many? "))

            case "6":

                if agever < 18:
                    print("Sorry, this item is not available for you.")

                else:
                    pelatis_votka = int(input("How many? "))


        print("Your cart contains:")

        for basket in range(list_ctrl):

            match basket:

                case 0:
                    print(f"{pelatis_cheeseburger} cheeseburger")

                case 1:
                    print(f"{pelatis_deluxe_burger} deluxe burger")

                case 2:
                    print(f"{pelatis_burger_aplo} regular burger")

                case 3:
                    print(f"{pelatis_xymos} juice")

                case 4:
                    print(f"{pelatis_portokalada} orange soda")

                case 5:
                    print(f"{pelatis_votka} vodka")


        more = input("Would you like to change anything else? (Yes = 1, No = 2): ")


        if more not in ["1", "2"]:
            more = input("ONLY YES (1) OR NO (2): ")


        if more == "2":
            change = "2"



    total_cost = (
        cheeseburger * pelatis_cheeseburger
        + deluxe_burger * pelatis_deluxe_burger
        + burger_aplo * pelatis_burger_aplo
        + xymos * pelatis_xymos
        + portokalada * pelatis_portokalada
        + votka * pelatis_votka
    )


    print(f"Final order price: {total_cost:.2f}€")


    progress = input("Are you finished? (Yes = 1, No = 2): ")


    while progress not in ["1", "2"]:
        progress = input("ONLY YES (1) OR NO (2): ")


    if progress == "2":
        done = False

    else:
        done = True




i = 0

while customer[i] != 0:
    i = i + 1


customer[i] = total_cost



if i == 9:

    print(
        "CONGRATULATIONS! Every 10 customers receive a gift, and you are the 10th customer!"
    )

    print(
        "Here is a 10% discount code for your next order: PYTHONBURGERS#YAY"
    )



i = 0

code = input("Enter a discount code if you have one: ")

is_coupon_valid = (code == "PYTHONBURGERS#YAY")



if is_coupon_valid == True:

    total_cost = total_cost * 0.9

    customer[i] = total_cost

    print(f"Final order price: {total_cost:.2f}€")




plirvmi_metrita = float(input("Insert cash into the machine: "))


while plirvmi_metrita < total_cost:

    total_cost = total_cost - plirvmi_metrita

    plirvmi_metrita = float(
        input(
            f"Incorrect amount, please insert another {total_cost:.2f}€ into the machine: "
        )
    )



resta = float(plirvmi_metrita - total_cost)


print(f"Your change is: {resta:.2f}€")


print("Enjoy your meal!")


print("--- RATE US ---")


rating = int(input("Rate your experience (1 to 5 ⭐⭐⭐⭐⭐): "))
while rating > 5 or rating < 0:

    rating = int(input("ERROR. ENTER A NUMBER FROM 1 TO 5"))


match rating:

    case 5:
        print("Perfect!!! We are happy that you enjoyed your food!!!")

    case 4:
        print("Very good. We will try to get 5 stars next time.")

    case 3:
        print("Average experience. We will inform the staff to improve.")

    case 2:
        print("We are very sorry. Here is a discount coupon for your next visit.")

    case 1 | 0:

        comment = input("We are very sorry. Tell us what went wrong: ")

        print("Thank you for your feedback. We will take it into consideration.")




Ending[0] = Ending[0] + 1

Ending[1] = Ending[1] + total_cost


if not Ending[1] == 0:

    with open(file_path, "w") as f:

        json.dump(Ending, f)




if customer[9] != 0:

    i = 0

    for i in range(10):

        customer[i] = 0




with open(file_path, "w") as f:

    json.dump(customer, f)



with open(file_path, "w") as f:

    json.dump(Ending, f)