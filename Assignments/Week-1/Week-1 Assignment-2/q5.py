"""
Q5. Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
Example 1
Enter bill amount = 80000
You got 30% discount
Your final bill is Rs. 56000
"""

final_amt: float = float(input("Enter the final Bill amount: "))
final_bill: float = 0.0
discount: float = 0.0
if final_amt >= 50000:
    discount = 0.30 * final_amt
elif 40000 <= final_amt <= 49999:
    discount = 0.25 * final_amt
elif 30000 <= final_amt <= 39999:
    discount = 0.20 * final_amt
elif 10000 <= final_amt <= 29999:
    discount = 0.10 * final_amt
else:
    discount = 0
final_bill = final_amt - discount
print(
    f"Congrats, you got {discount:.2f} rupees discount on your total purchase of {final_amt} rupees.\nYour final Bill after discount is: {final_bill}"
)
