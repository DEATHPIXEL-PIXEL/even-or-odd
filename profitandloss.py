sp=int(input("enter the selling price "))
cp=int(input("enter the cost price "))
if(sp>cp):
    print("its a profit")
    profit=sp-cp
    print("your profit is " , profit)     
    profitperc=profit/cp*100 
    print("your profit percentage is " , profitperc)       
else:       
    print("its a loss")
    loss=cp-sp
    print("your loss is " , loss)     
    lossperc=loss/cp*100 
    print("your loss percentage is " , lossperc)                                                                