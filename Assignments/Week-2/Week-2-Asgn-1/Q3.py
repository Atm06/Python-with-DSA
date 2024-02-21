"""
Q3. Attempt the same bill calculator question (Week 1 - Assignment 2 -

Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.

50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount

Print the discount and the final amount to be paid.

Example 1
Enter bill amount = 80000You got 30% discountYour final bill is Rs. 56000
"""


def bill_calculation(final_amt: int):
    if final_amt >= 50000:
        discount = final_amt * 0.3
    elif 40000 <= final_amt <= 49999:
        discount = final_amt * 0.25
    elif 30000 <= final_amt <= 39999:
        discount = final_amt * 0.20
    elif 10000 <= final_amt <= 29999:
        discount = final_amt * 0.10
    else:
        discount = 0
    discounted_purchase_amt = final_amt - discount
    print(f"Discount received on {final_amt} is {discount} rupees.")
    print(f"Final discounted price of purchase is: {discounted_purchase_amt}")


final_amt: int = int(input("Enter the final amount: "))
bill_calculation(final_amt)
