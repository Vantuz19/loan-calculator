import math
import sys

init_dict = {"principal": 0, "payment": 0, "periods": 0, "interest": 0}
init_dict.update([i.strip("--").split("=") for i in sys.argv[2:]])
try:
    for key in init_dict:
        init_dict[key] = float(init_dict[key])
except TypeError:
    print("Incorrect parameters")
    exit()

for key in init_dict:
    if init_dict[key] < 0:
        print("Incorrect parameters")
        exit()
if "interest" not in init_dict:
    print("Incorrect parameters")
    exit()

if sys.argv[1] not in ("--type=annuity", "--type=diff") or len(sys.argv) != 5:
    print("Incorrect parameters")
    exit()

if sys.argv[1] == "--type=diff" and init_dict["payment"] != 0 and init_dict["periods"] == 0 and \
        init_dict["interest"] == 0 and init_dict["principal"] == 0:
    print("Incorrect parameters")
    exit()

periods = init_dict["periods"]
mp = init_dict["payment"]
loan_interest = init_dict["interest"] / 1200
loan = init_dict["principal"]

if sys.argv[1] == "--type=annuity":
    if periods == 0:
        res = math.ceil(math.log(mp / (mp - loan_interest * loan), 1 + loan_interest))
        years = f" {res // 12} year{('s', '')[res // 12 == 1]}" if res // 12 != 0 else ""
        months = f" {res % 12} month{('s', '')[res % 12 == 1]}" if res % 12 != 0 else ""
        overpay = res * mp - loan
        print(f"It will take{years}{months} to repay the loan!")
    elif mp == 0:
        res = loan * loan_interest * (1 + loan_interest) ** periods / ((1 + loan_interest) ** periods - 1)
        print(f"Your monthly payment = {math.ceil(res)}!")
        overpay = math.ceil(res) * periods - loan
    elif loan == 0:
        res = mp / (loan_interest * (1 + loan_interest) ** periods / ((1 + loan_interest) ** periods - 1))
        print(f"Your loan principal = {math.ceil(res)}!")
        overpay = mp * periods - res
    print(f"Overpayment = {int(overpay)}")
else:
    summa = 0
    for i in range(int(periods)):
        mp = math.ceil(loan / periods + loan_interest * (loan - loan * i / periods))
        print(f"Month {i+1}: payment is {mp}")
        summa += mp
    print(f"Overpayment = {math.ceil(summa) - int(loan)}")
