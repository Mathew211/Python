class Timetable:
  def __init__(self, name, arrived, frequency):
    self.name = name
    self.arrived = arrived
    self.frequency = frequency
c1 = Timetable("Poleska",'12 : 45',30)

print('Bus odjeżdza z ', c1.name,'o godzinie', c1.arrived, 'następny będzie za', c1.frequency,'Minut')
class Bus:
  def __init__(self,bus_line):
    self.bus_line = bus_line
line = Bus(123)
class Passenger:
    def __init__(self,discounts):
        self.discounts = discounts
        
d1 = Passenger('Normalny')
d2 = Passenger('Ulgowy')
d3 = Passenger('Studencki')

print('Pasażer wsiadł do linii ',line.bus_line,'posiadał bilet',d3.discounts)

class Ticket:
  def __init__(self,price):
    self.price = price
    
p1 = Ticket(2)
p2 = Ticket(4)
p3 = Ticket(1)

  
print('Pasażer miał bilet', d3.discounts,'zapąłcił za niego',p3.price )
