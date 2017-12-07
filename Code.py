import random



class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Customers_to_be_Served:
    def __init__(self, time):
        '''

        :param time: Customer arrival time
        '''
        self.Customer_arrival_time = time
        self.item = random.randrange(1, 11)

    def getTime(self):
        return self.Customer_arrival_time

    def getItem(self):
        return self.item

    def waitTime(self, Serve_Time):
        return Serve_Time - self.Customer_arrival_time


class Cashier_serving_Customer:
    def __init__(self, itemspm):
        '''

        :param itemspm:Items entered by the cashier per minute
        '''

        self.rate = itemspm
        self.currentCustomer = None
        self.timeRemaining = 0

    def setIdle(self):
        if self.currentCustomer != None:
            self.timeRemaining = self.timeRemaining - 1 #if the customer at the counter takes one second to leave the counter  subtract that 1 second)
            if self.timeRemaining <= 0:
                self.currentCustomer = None

    def busy(self):
        if self.currentCustomer != None:
            return True
        else:
            return False

    def Next(self, newCustomer):
        '''


        :param newCustomer: New customer at the counter
        :return: Returns the serving time of the new customer at the counter
        '''
        self.currentCustomer = newCustomer
        self.timeRemaining = newCustomer.getItem() * 60 / self.rate


def new_Customer():
    Cust = random.randrange(1, 21)
    if Cust == 20:
        return True
    else:
        return False


def simulation(numSec, itemsPermin):
    '''

    :param numSec: Time frame considered for simulation (can be anything)
    :param itemsPermin: Items entered by the cashier per min
    :return: average waiting time and the number of customers
    '''
    restCashier = Cashier_serving_Customer(itemsPermin)
    waitingTimes = []
    q = Queue()

    for currentSec in range(numSec):
        #When the customer has arrived at the restaurant
        if new_Customer():
            serving = Customers_to_be_Served(currentSec)
            q.enqueue(serving)
        #When the customer at the counter has been served
        if (not restCashier.busy()) and (not q.isEmpty()):
            nextCust = q.dequeue()
            waitingTimes.append(nextCust.waitTime(currentSec))
            restCashier.Next(nextCust) #adds the time that the current customer is taking at the counter
        restCashier.setIdle()#current customer has now left and the cashier is available to serve the next customer

    averageWaitingTime = sum(waitingTimes) / len(waitingTimes)


    print("%3d Customers are left for serving and average waiting time for customer is %3.2f secs." %(q.size(),averageWaitingTime))


for i in range(10):
    simulation(600, 5)




