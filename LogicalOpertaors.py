#has_good_income = True
has_credit_record =True
has_criminal_record = False

if has_credit_record and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")