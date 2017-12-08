import random
import matplotlib
import matplotlib.pyplot as plt




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
        >>> arrival=Customers_to_be_Served(5)
        >>> arrival.waitTime(10)
        5
        '''
        self.Customer_arrival_time = time
        self.item = random.randrange(1, 11)

    def getTime(self):
        return self.Customer_arrival_time

    def getItem(self):
        return self.item

    def waitTime(self, Serve_Time):
        '''
        :param Serve_Time: When customer is at the counter for being served
        :return: Total waiting time for that customer

        '''

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
                '''the time that customer is taking at the counter becomes zero when the random number generating 
                the number of items ordered by the customer becomes zero. And at this point the customer has been served 
                and the cashier is ready to serve other customer.
                '''
                self.currentCustomer = None

    def busy(self):
        if self.currentCustomer != None:
            return True
        else:
            return False

    def Next(self, newCustomer):
        '''
        :param newCustomer: New customer at the counter
        :return: Returns the serving time of the new customer at the counter depending on the number of items ordered

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
            restCashier.Next(nextCust) #calculates the time that the current customer is taking at the counter
        restCashier.setIdle()#current customer has now left and the cashier is available to serve the next customer

    averageWaitingTime = sum(waitingTimes) / len(waitingTimes)

    plt.plot(itemsPermin,averageWaitingTime,'bo')



    print("%3d Customers are left for serving and average waiting time for customer is %3.2f secs." %(q.size(),averageWaitingTime))

print("Simulation output taking time frame of 600 seconds and 10 items per min are entered by the cashier")
for i in range(10):
    simulation(600, 10)
print("Simulation output for same time frame but now taking  50 items per min are entered by the cashier")
for i in range(10):
    simulation(600, 50)

#So, the result of this simulation rejects the null hypothesis in favour of alternate hypothesis.

#Plot to see the difference in the results of the simulation clearly
plt.xlabel('Items entered by the cashier per min')
plt.ylabel('Average wait time for the customer')
plt.title("Plot comparing the two simulation results in more better way")
plt.show()
