class traveler():
    
  def __init__(self,traveler_id,traveler_name,baggage_weight,expiry_year,noc_status):
    self.traveler_id=traveler_id
    self.traveler_name=traveler_name
    self.baggage_weight=baggage_weight
    self.expiry_year=expiry_year
    self.noc_status=noc_status

    
  def check_baggage(self):
    if self.baggage_weight >=0 and self.baggage_weight <=40:
        return True
    else:
        return False

    
  def check_immigration(self):
    if self.expiry_year >= 2030 and self.expiry_year<=2050:
        return True
    else:
        return False


    
  def check_security(self):
    
    if self.noc_status.lower()=="valid":
        return True

    else:        
        return False

  def display(self):
   
    if (bool(trav.check_baggage())) and (bool(trav.check_immigration())) and (bool(trav.check_security()))  :     
        print("Traveler id: " ,self.traveler_id)
        print("Traveler name: ",self.traveler_name)
        print("Allow traveler to fly ")
    else:
        print("Traveler id: " ,self.traveler_id)
        print("Traveler name: ",self.traveler_name)
        print("Detain Traveler for Re-checking! ")

trav=traveler(1001,"jim",35,2019,"VALID")
trav.display()

