def calculate_tax(tax):
    
    if tax >= 5000000:
        step7 = (tax - 5000000) * 35 / 100
        total_tax = step7 + 7500 + 22500 + 50000 + 75000 + 250000 + 900000
        final_income = tax - step7 - 7500 - 22500 - 50000 - 75000 - 250000 - 900000
        effective_rate = total_tax / tax * 100
        print("เสียภาษีขั้น 5,000,000 ขึ้นไป (35%) เป็นเงิน", step7)
        print("ภาษีรวมทั้งหมด", total_tax)
        print("รายได้หลังหักภาษี",final_income,"บาท")
        print("Effective Tax Rate =", round(effective_rate, 2), "%")
        return total_tax, final_income, effective_rate

    elif tax >= 2000000:
        step6 = (tax - 2000000) * 30 / 100
        total_tax = step6 + 7500 + 22500 + 50000 + 75000 + 250000
        final_income = tax - step6 - 7500 - 22500 - 50000 - 75000 - 250000
        effective_rate = total_tax / tax * 100
        print("เสียภาษีขั้น 2,000,000 - 5,000,000 (30%) เป็นเงิน", step6)
        print("ภาษีรวมทั้งหมด", total_tax)
        print("รายได้หลังหักภาษี",final_income,"บาท")
        print("Effective Tax Rate =",round(effective_rate, 2), "%")
        return total_tax, final_income, effective_rate

    elif tax >= 1000000:
        step5 = (tax - 1000000) * 25 / 100
        total_tax = step5 + 7500 + 22500 + 50000 + 75000
        final_income = tax - step5 - 7500 - 22500 - 50000 - 75000
        effective_rate = total_tax / tax * 100
        print("เสียภาษีขั้น 1,000,000 - 2,000,000 (25%) เป็นเงิน", step5)
        print("ภาษีรวมทั้งหมด", total_tax)
        print("รายได้หลังหักภาษี",final_income,"บาท")
        print("Effective Tax Rate =",round(effective_rate, 2), "%")
        return total_tax, final_income, effective_rate

    elif tax >= 750000:
        step4 = (tax - 750000) * 20 / 100
        total_tax = step4 + 7500 + 22500 + 50000
        final_income = tax - step4 - 7500 - 22500 - 50000
        effective_rate = total_tax / tax * 100
        print("เสียภาษีขั้น 750,000 - 1,000,000 (20%) เป็นเงิน", step4)
        print("ภาษีรวมทั้งหมด", total_tax)
        print("รายได้หลังหักภาษี",final_income,"บาท")
        print("Effective Tax Rate =",round(effective_rate, 2), "%")
        return total_tax, final_income, effective_rate

    elif tax >= 500000:
        step3 = (tax - 500000) * 15 / 100
        total_tax = step3 + 7500 + 22500
        final_income = tax - step3 - 7500 - 22500
        effective_rate = total_tax / tax * 100
        print("เสียภาษีขั้น 500,000 - 750,000 (15%) เป็นเงิน", step3)
        print("ภาษีรวมทั้งหมด", total_tax)
        print("รายได้หลังหักภาษี",final_income,"บาท")
        print("Effective Tax Rate =",round(effective_rate, 2), "%")
        return total_tax, final_income, effective_rate

    elif tax >= 300000:
        step2 = (tax - 300000) * 10 / 100
        total_tax = step2 + 7500
        final_income = tax - step2 - 7500
        effective_rate = total_tax / tax * 100
        print("เสียภาษีขั้น 300,000 - 500,000 (10%) เป็นเงิน", step2)
        print("ภาษีรวมทั้งหมด", total_tax)
        print("รายได้หลังหักภาษี",final_income,"บาท")
        print("Effective Tax Rate =",round(effective_rate, 2), "%")
        return total_tax, final_income, effective_rate

    elif tax >= 150000:
        total_tax = (tax - 150000) * 5 / 100
        final_income = tax - total_tax
        effective_rate = total_tax / tax * 100
        print("เสียภาษีขั้น 150,000 - 300,000 (5%) เป็นเงิน", total_tax)
        print("ภาษีรวมทั้งหมด", total_tax)
        print("รายได้หลังหักภาษี",final_income,"บาท")
        print("Effective Tax Rate =",round(effective_rate, 2), "%")
        return total_tax, final_income, effective_rate

    else:
        total_tax = 0
        print("เสียภาษี 0% เป็นเงิน", total_tax)
        return total_tax, tax, 0

    
tax = float(input("Enter your tax: "))
calculate_tax(tax)


