class car(): 
      
    # init method or constructor 
    def __init__(aaa, model, color): 
        aaa.model = model 
        aaa.color = color 
          
    def show(aaa): 
        print("Model is", aaa.model) 
        print("color is", aaa.color) 
        
          
# both objects have different self which  
# contain their attributes 
audi = car("audi a4", "blue") 
ferrari = car("ferrari 488", "green") 

# print(audi)

audi.show()     # same output as car.show(audi) 
ferrari.show()  # same output as car.show(ferrari) 
  