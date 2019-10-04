# #variables for name, melons, and paid defined for each customer
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

# #code is copied for each added customer and variable names are changed 

# #defining amount for expected payment (melons * cost of melons)
# customer1_expected = customer1_melons * melon_cost
# #conditional, if expected is not what was paid 
# if customer1_expected != customer1_paid:
#     #print customer information if expected was not == paid
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
#           )

def customer_payment_error(customer_file):
    """Read customer file and print customers with payment error."""

    the_file = open(customer_file) #open the file 

    #counts set for underpayment and overpayment to keep track 
    under_count = 0 
    over_count = 0
    #iterate through customer file line by line
    for line in the_file:
        #remove whitespace and new lines
        line = line.rstrip()
        #split each line by "|"
        info = line.split("|")
        #unpack information assigning values for customer number,
        ##name, melon count, and customer payment. 
        cus_number, cus_name, melon_count, cus_paid = info
        #define melon cost once inside function- can be easily changed later
        melon_cost = 1
        #define expected payment amount using melon cost
        pay_expected = melon_count * melon_cost
        #conditional if customer underpaid 
        if cus_paid < pay_expected:
          #increment underpayment count 
          under_count += 1
          #print out customer information who underpaid
          print(f"{cus_name}, UNDERPAID ${cus_paid},",
                f"expected amount is ${pay_expected}."
                )
        #conditional if customer overpaid 
        elif cus_paid > pay_expected:
          #increment overpayment count 
          over_count += 1 
          #print out customer information who overpaid 
          print(f"{cus_name}, OVERPAID ${cus_paid},",
                f"expected amount is ${pay_expected}."
                )
    #print out underpayment and overpayment information at end
    print("__________")      
    print("Number of UNDERPAID customers:")
    print(under_count)
    print("__________")      
    print("Number of OVERPAID customers:")
    print(over_count)
    print("__________")
    #close the open file
    the_file.close()
    

customer_payment_error("customer-orders.txt")


