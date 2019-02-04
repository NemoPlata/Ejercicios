class Park:
	 def __init__(self, price):
		 self.costs = price

	 def park_costs( self ):
	 	print ("Ingresa la edad de la persona: ")
	 	age = int(input())
	   if(10>age):
	   	 return self.costs + (self.costs * 0.25)
	   else:
	   	 return self.costs

	 def show_data (self):
	 	print(":: Estos son los datos ::")
	 	print("La edad de la persona es: ", age)
		print("El costo del juego es de: ", self.park_costs())
