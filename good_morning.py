while True:
   print("1 - Add")
   print("2 - Sub")
   print("3 - Multiply")
   print("4 - Divide")
   print("Enter q or Q to exit")
   x = int(input (" Choose an operation  "))
    
   if (x == 'q' or x =='Q'):
     break
         
   num1 = int(input("ENTER YOUR FIRST NUMBER  "))
   num2 = int(input("ENTER YOUR SECOND NUMBER  "))
            
   if(x == 1):
      result = num1+ num2
   elif(x == 2):
      result = num1- num2
   elif (x == 3):
      result = num1* num2
   elif (x == 4):
      result = num1 // num2
   else:
      print("select valid operation")
        
   print("the result is ",result)        
        
        
        
     
        






    



   





    
     
