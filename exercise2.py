class Park:
     def __init__(self, price):
         self.costs = price

     def park_costs( self, age ):
       if( 10 < age ):
         return self.costs + (self.costs * 0.25)
       else:
         return self.costs
