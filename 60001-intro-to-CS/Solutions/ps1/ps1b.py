import numpy
portion_down_payment = 0.25
current_savings = 0
r = 0.04 # annual return

annual_salary = float(input("Starting salary?\n"))
portion_saved = float(input("savings_rate\n"))
total_cost = float(input("Total cost of house?\n"))
raise_rate = float(input("Six month raise as decimal\n"))

n_months = 0
while current_savings < portion_down_payment*total_cost:
    n_months += 1 
    current_savings += current_savings*r/12
    current_savings += portion_saved*annual_salary/12

    if numpy.mod(n_months,6) == 0:
        annual_salary += annual_salary*raise_rate

print("Months to save for down payment\n", n_months)
