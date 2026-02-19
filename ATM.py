Balance=5000
Amount=int(input("Enter the amount to widraw:"))
if Amount<=5000:
    Balance=Balance-Amount
    print("Amount withdrawn:", Amount)
    print("Remaining balance:", Balance)
    print("  Thank you for using me !!!")
else:
    print("Insufficient balance or invalid amount.")