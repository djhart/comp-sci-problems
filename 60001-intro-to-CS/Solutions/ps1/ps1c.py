import numpy
portion_down_payment = 0.25
current_savings = 0
r = 0.04 # annual return

starting_salary = float(input("Starting salary?\n"))
#portion_saved = float(input("savings_rate\n"))
#total_cost = float(input("Total cost of house?\n"))
#raise_rate = float(input("Six month raise as decimal\n"))
raise_rate = 0.07
total_cost = 1000000

down_payment = portion_down_payment*total_cost

goal_months = 36
epsilon = 100
current_savings = 0 

high = 10000
low = 0
n_bisection = 0 
while abs(current_savings - down_payment) >= epsilon:
    portion_saved = (high+low)/2/10000
    current_savings = 0 
    n_months = 0
    annual_salary = starting_salary
    # print("portion saved:", portion_saved,"\n")
    while n_months < goal_months:
        n_months += 1 
        current_savings += current_savings*r/12
        current_savings += portion_saved*annual_salary/12

        if numpy.mod(n_months,6) == 0:
            annual_salary += annual_salary*raise_rate

    if current_savings - down_payment < 0:
        low = (high+low)/2
    else:
        high = (high+low)/2

    #print("diff",current_savings - down_payment,"\n") 
    n_bisection += 1
    if portion_saved >= .99:
        print("It is not possible to pay the down payment in 3 years.")
        break


print("Best savings rate: ", portion_saved,"\n")
print("Steps in bisection search: ", n_bisection,"\n")

