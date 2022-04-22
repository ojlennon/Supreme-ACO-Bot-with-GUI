class UserDetails:
    def __init__(self, name, email, tele, adr, zip, city, state,keywords,colour,size,cardNum,cvv,month,year):
        self.name = name
        self.email = email 
        self.tele = tele
        self.adr = adr
        self.zip = zip
        self.city = city
        self.state = state
        self.keywords = keywords
        self.colour = colour
        self.size = size
        self.cardNum = cardNum
        self.cvv = cvv
        self.month = month
        self.year = year 
        
    def printDetails(self):
        print(vars(self))
    