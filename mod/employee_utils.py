def calculate_salary(sal,catg,leave):
    if catg=="coder":
        sal+=(10/100)*sal
    elif catg=="designer":
        sal+=(15/100)*sal
    elif catg=="manager":
        sal+=(5/100)*sal
    
    if leave>15:
        leave-=15
        sal-=100/30*leave
        
    
        

    return sal


    