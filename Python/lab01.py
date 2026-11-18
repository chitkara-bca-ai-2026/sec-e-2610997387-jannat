tuition_fee = float(input("Enter Tuition Fee: "))
lab_fee = float(input("Enter Lab Fee: "))
library_fee = float(input("Enter Library Fee: "))
exam_fee = float(input("Enter Exam Fee: "))
discount = float(input("Enter Discount Amount: "))

total_fee = tuition_fee + lab_fee + library_fee + exam_fee
fee_after_discount = total_fee - discount
annual_fee = fee_after_discount * 2
monthly_installment = annual_fee / 12

print("\nTotal Fee:", total_fee)
print("Fee After Discount:", fee_after_discount)
print("Annual Fee:", annual_fee)
print("Monthly Installment:", monthly_installment)