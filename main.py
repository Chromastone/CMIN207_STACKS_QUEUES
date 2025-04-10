from stack import Stack
from queue import Queue # type: ignore
from ticket import Ticket

triageOpenTickets  = Queue()
triageClosedTickets = Stack()

def openTicket():
    ticketNumber = input("Ticket Number(ex. 0001): ")
    description = input("Ticket: ")
    newTicket = Ticket(ticketNumber, description)
    triageOpenTickets.enqueue(newTicket)
    print("Ticket opened!")

def mainMenu():
    print("Type the number for the action you wish to perform and then hit Enter.")
    print("1. Open a new ticket")
    print("2. List All Open Tickets")
    print("3. Close ticket")
    print("4. Review All Closed Tickets")
    print("5. Review Previously Closed Ticket")
    print("6. Quit")
    command = input("What do you want to do? ")
    if command == '1':
        openTicket()
        mainMenu()
    elif command == '2':
        #listAllTickets()
        mainMenu()
    elif command == '3':
        #closeTicket()
        mainMenu()
    elif command == '4':
        #reviewAllClosedTickets()
        mainMenu()
    elif command == '5':
        #previouslyClosedTicket()
        mainMenu()
    elif command =='6':
        exit()
    else:
        print("I'm sorry, that is not an appropriate action.")
        mainMenu()
    
def main():
    print("Welcome to Thibodeaux's Tech Triage")
    print("-----------------------------------")
    mainMenu()

if __name__ == "__main__":
    main()
