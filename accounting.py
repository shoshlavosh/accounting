# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
          

def did_customer_underpay(summary):
    """Takes in customer name, what they paid, and what they were /n
    expected to pay to find out if they underpaid for their order"""

    the_file = open(summary)

    for line in the_file: 

        words = line.split('|')
        # #adds a "|" between each word and saves to variable "words"

        melon_cost = 1.00

        customer_name = words[1]

        #assigns variable "melon" to index 1 (second item) of "words"
        melon_quantity = words[2]
        melon_quantity = float(melon_quantity)

        #assigns variable "count" to index 2 (third item) of "words"
        amount_paid = words[3]
        amount_paid = float(amount_paid)

        #assigns variable "amount" to index 3 (fourth item) of "words"

        customer_expected = melon_quantity * melon_cost

        print()
        if customer_expected != amount_paid:
            print(f"{customer_name} paid ${amount_paid:.2f},", f"expected ${customer_expected:.2f}")
        
            if customer_expected < amount_paid:
                print(f"{customer_name} has overpaid for their melons")

            elif customer_expected > amount_paid:
                print(f"{customer_name} has underpaid for their melons")




did_customer_underpay("customer-orders.txt")