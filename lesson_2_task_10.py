def bank(x,y):
    total_contribution = x
    for i in range(y):
        total_contribution = total_contribution*0.1 + total_contribution
    print(total_contribution)
        
       
bank (5,4)