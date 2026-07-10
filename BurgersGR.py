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

def multiplier(num1 , num2, total_cost ): 
    total_cost = total_cost +  num1 * num2


twra = datetime.datetime.now() #<--  Αν η ωρα ειναι 00:00(twra = 0 <-- αμα θελετε να το τσεκαρετε)

if twra == 0:
   print("ΤΕΡΜΑΤΙΣΜΟΣ ΜΗΧΑΝΗΜΑΤΟΣ - ΚΛΕΙΣΙΜΟ ΚΑΤΑΣΤΗΜΑΤΟΣ")

   SuperSecretAdminCode = input(
       "Εάν είστε ο υπευθυνος του μαγαζιου, βαλτε τον κωδικο ωστε να δειτε τα στατιστικα της ημερας"
   )

   if SuperSecretAdminCode == "9999":

     print(f"Πελάτες σήμερα:  {Ending[0]}")
     print(f"Έσοδα σήμερα:  {Ending[1]}")

     if Ending[0] != 0:
          print(f"Mέσος όρος κόστους παραγγελιών: {Ending[1] / Ending[0]}\n")

     Ending[0] = 0
     Ending[1] = 0

     with open(file_path, "w") as f:
          json.dump(Ending, f)

   exit()



print("ΚΑΛΩΣ ΗΡΘΑΤΕ ΣΤΟ BURGER SHOP 🍔")
print(" Τι θα θέλατε να παραγείλετε?") 
print("---ΚΑΤΑΛΟΓΟΣ ΜΑΓΑΖΙΟΥ---")


cheeseburger = 6.30
deluxe_burger = 7.60
burger_aplo = 5
xymos = 3
portokalada = 3
votka = 15


print(f"1: Cheeseburger - {cheeseburger:.2f} €")
print(f"2: deluxe burger -  {deluxe_burger:.2f} €")
print(f"3: burger  - {burger_aplo:.2f} €")
print(f"4: Χυμός - {xymos:.2f} €")
print(f"5: πορτοκαλαδα - {portokalada:.2f} €")
print(f"6: votka - {votka:.2f} €")


pelatis_cheeseburger = int(input("Πόσα cheeseburger θέλετε?"))
pelatis_deluxe_burger = int(input("Πόσα deluxe burger θέλετε?"))
pelatis_burger_aplo = int(input("Πόσα burger θέλετε?"))
pelatis_xymos = int(input("Πόσους Χυμους θέλετε?"))
pelatis_portokalada = int(input("Πόσες πορτοκαλαδες θέλετε?"))
pelatis_votka = int(input("Πόσες votka θέλετε?"))




if pelatis_votka >= 1:

     agever = int(
         input("Σκαναρετε την ταυτοτητα σας ωστε να μπορουμε να σας προσφερουμε votka: ")
     )

     if agever >= 18:

          print("Αφου εισαι 18 ή πιο μεγαλος... Πιες να το απολαυσεις!!!")

     else:

          print("Μην νομιζεις οτι θα την γλιτωσεις... Θα πιεις οταν μεγαλωσεις!!!")

          pelatis_votka = 0
          basket = [pelatis_cheeseburger , pelatis_deluxe_burger, pelatis_burger_aplo, pelatis_xymos , pelatis_portokalada]

list_ctrl = 5

if pelatis_votka >= 1: 

     basket = [
         pelatis_cheeseburger,
         pelatis_deluxe_burger,
         pelatis_burger_aplo,
         pelatis_xymos,
         pelatis_portokalada,
         pelatis_votka
     ]

     list_ctrl = 6



multiplier(cheeseburger , pelatis_cheeseburger, total_cost)
multiplier(deluxe_burger , pelatis_deluxe_burger, total_cost)
multiplier(burger_aplo , pelatis_burger_aplo, total_cost)
multiplier(xymos , pelatis_xymos, total_cost)
multiplier(portokalada , pelatis_portokalada, total_cost)
multiplier(votka , pelatis_votka, total_cost)



done = False

while done == False:

     print("Το καλαθι σας αποτελειται απο:")

     for basket in range(list_ctrl):

          match basket:

               case 0:
                    print(f"{pelatis_cheeseburger} cheeseburger")

               case 1:
                    print(f"{pelatis_deluxe_burger} deluxe burger")

               case 2:
                    print(f"{pelatis_burger_aplo} burger ")

               case 3:
                    print(f"{pelatis_xymos} χυμο(ους)")

               case 4:
                    print(f"{pelatis_portokalada} πορτοκαλαδα/ες")

               case 5:
                    print(f"{pelatis_votka} votka")


     change = input("Θέλετε να αλλάξετε κάτι;  (ναι = (1) ή οχι(2))")


     while change not in ["1", "2"]:

          change = input("ΜΟΝΟ ναι(1) Ή οχι(2)")


     while change == "1":

          item = input(
              "Θέλετε να αλλάξετε την ποσότητα κάποιου προιόντος? "
              "(Γραψτε τον αριθμο του προιοντος οπως φαινεται παραπανω )"
          )


          while item not in ["1", "2", "3", "4", "5", "6"]:

               mistake = input("Ωχ, μαλλον κάνατε λάθος... Ξαναπροσπαθήστε!!!")



          match item:


               case "1":

                    pelatis_cheeseburger = int(input("Πόσα???"))


               case "2":

                    pelatis_deluxe_burger = int(input("Πόσα???"))


               case "3":

                    pelatis_burger_aplo = int(input("Πόσα???"))


               case "4":

                    pelatis_xymos = int(input("Πόσους"))


               case "5":

                    pelatis_portokalada = int(input("Πόσες???"))


               case "6":

                    if agever < 18:

                         print(
                             "Συγγνώμη, αλλά το αντικείμενο αυτό και η επεξεργασία του "
                             "δεν είναι διαθέσιμο για εσάς"
                         )

                    else:

                         pelatis_votka = int(input("Πόσες???"))
                    print("Το καλαθι σας αποτελειται απο:")

          for basket in range(list_ctrl):

               match basket:

                    case 0:
                         print(f"{pelatis_cheeseburger} cheeseburger")

                    case 1:
                         print(f"{pelatis_deluxe_burger} deluxe burger")

                    case 2:
                         print(f"{pelatis_burger_aplo} burger aplo ")

                    case 3:
                         print(f"{pelatis_xymos} xymos")

                    case 4:
                         print(f"{pelatis_portokalada} portokalada")

                    case 5:
                         print(f"{pelatis_votka} votka")


          more = input("Θα θέλατε να αλλάξετε τίποτα άλλο? (ναι(1) ή οχι(2))")


          if more not in ["1", "2"]:

               more = input("ΜΟΝΟ ΝΑΙ(1) 'Η ΟΧΙ(2)")


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


     print(f"Τελικη τιμη παραγγελιας{total_cost:.2f}€")


     progress = input("Τελειώσατε?(ναι(1) Ή οχι(2))")


     while progress not in ["1", "2"]:

          progress = input("ΜΟΝΟ ναι(1) Ή οχι(2)")


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
         f"ΣΥΓΧΑΡΗΤΗΡΙΑ, κάθε 10 πελάτες δίνουμε ένα δώρο στον 10ο πελάτη "
         f"ο οπόιος, ειστε εσεις"
     )

     print(
         "Ορίστε ενας κωδικος για 10% εκπτωση σε επομενη σας παραγγελια: "
         "PYTHONBURGERS#YAY"
     )



i = 0

code = input("Bαλτε εκπτωτικο κωδικο αν εχετε")


is_coupon_valid = (code == "PYTHONBURGERS#YAY")



if is_coupon_valid == True:

     total_cost = total_cost * 0.9

     customer[i] = total_cost

     print(f"Τελικη τιμη παραγγελιας{total_cost:.2f}€")



plirvmi_metrita = float(input("Προσθέστε μετρητα στο μηχανημα:"))


while plirvmi_metrita < total_cost:

     total_cost = total_cost - plirvmi_metrita

     plirvmi_metrita = float(
         input(
             f"Λάθος ποσό, προσθέστε ακόμα {total_cost:.2f}€ στο μηχανημα:"
         )
     )



resta = float(plirvmi_metrita - total_cost)


print(f"Τα ρέστα σας είναι: {resta:.2f}€")


print("Καλη σας ορεξη")

print("--- AΞΙΟΛΟΓΗΣΤΕ ΜΑΣ---")


rating = int(input("Βαθμολογηστε την εμπειρια σας (1 εως 5⭐⭐⭐⭐⭐)"))



while rating > 5 or rating < 0:

     rating = int(input("ΣΦΑΛΜΑ. ΒΑΛΤΕ ΑΠΟ 1 ΕΩΣ 5"))



match rating:

     case 5:

          print("Τελεια!!! Xαιρομαστε που σας αρεσε το φαγητο σας!!!")


     case 4:

          print(
              "Πολυ καλα, θα προσπαθησουμε να παρουμε "
              "5 αστερια την επομενη φορα"
          )


     case 3:

          print(
              "Μετρια εμπειρια. Θα ενημερωσουμε "
              "το προσωπικο να βελτιωθει"
          )


     case 2:

          print(
              "Λυπουμαστε πολυ. Οριστε ενα κουπονι "
              "εκπτωσης για την επομενη φορα"
          )


     case 1 | 0:

          comment = input(
              "Λυπουμαστε πολυ. Πειτε μας τι πηγε λαθος"
          )

          print(
              "Ευχαριστουμε για το σχολιο, θα το λαβουμε υποψιν"
          )



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