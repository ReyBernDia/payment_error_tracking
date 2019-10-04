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


