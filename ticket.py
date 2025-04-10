class Ticket():
    def __init__(self, ticketNumber, description):
        self.ticketNumber = "#"+ticketNumber
        self.description = description
    
    def __str__(self):
        ticketStr = self.ticketNumber+" "+self.description
        return ticketStr