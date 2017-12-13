import random
import matplotlib
import matplotlib.pyplot as plt
import math


class Queue:
    def __init__(self):
        """ create an empty queue """
        self.items = []

    def isEmpty(self):
        '''Check if there is passengers in the current waiting queue'''
        return self.items == []

    def enqueue(self, item):
        ''' add new passenger to the end of queue'''
        self.items.insert(0, item)

    def dequeue(self):
        '''remove the passenger from the beginning of the queue'''
        return self.items.pop()

    def size(self):
        '''return the number of items in the queue'''
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
        self.item = random.randrange(1,
                                     11)  # generates a random number between 1 and 10 (customer can order between 1 to 10 items)

    def getTime(self):
        '''returns customer arrival time'''
        return self.Customer_arrival_time

    def getItem(self):
        '''returns the number of items ordered depending on the random number generated'''
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

        self.rate = itemspm  # serving rate(items entered by the cashier per min)
        self.currentCustomer = None
        self.timeRemaining = 0

    def setIdle(self):
        if self.currentCustomer != None:
            self.timeRemaining = self.timeRemaining - 1  # if the customer at the counter takes one second to leave the counter  subtract that 1 second)
            if self.timeRemaining <= 0:  # At this point the customer has been served and the cashier is ready to serve other customer.
                self.currentCustomer = None

    def busy(self):
        '''Returns a boolean True if there is a customer at the counter and cashier is busy with him/her.'''
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
    '''Generates a random number between 1 and 20 and store it in variable Cust. When the random number generated is 20 that means a customer has arrived
     at the restaurant and can either be in the queue or at the counter (if cashier is not busy).
    The function thus returns a boolean True upon customer's arrival.'''
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
    restCashier = Cashier_serving_Customer(itemsPermin)  # creating object of class Cashier_serving_Customer
    waitingTimes = []  # list for storing wait time of each customer
    q = Queue()

    for currentSec in range(numSec):
        # When the customer has arrived at the restaurant and is pushed into the queue
        if new_Customer():
            serving = Customers_to_be_Served(currentSec)
            q.enqueue(serving)
        # When the customer at the counter has been served
        if (not restCashier.busy()) and (not q.isEmpty()):
            nextCust = q.dequeue()
            waitingTimes.append(nextCust.waitTime(
                currentSec))  # calculates the wait time for each customer and appends it to the list of waitingTimes
            restCashier.Next(nextCust)  # calculates the time that the current customer is taking at the counter
        restCashier.setIdle()  # current customer has now left and the cashier is available to serve the next customer

    averageWaitingTime = sum(waitingTimes) / len(waitingTimes)  ##calculates average waiting time

    return averageWaitingTime


def main():
    '''
    taking a fixed time frame of 600 seconds to visualize simulation
    results within this time frame by changing the number of items entered by the cashier (per min).
    '''
    time_frame = 600
    '''storing the outputs in order to make the plot'''
    maxTime = [] #stores the maximum average waiting time among all 10 simulations for each case[items per min in (10,11,12,.....till 50)]
    minTime = [] #stores the minimum average waiting time among all 10 simulations for each case[items per min in (10,11,12,.....till 50)]
    avgTime = [] #stores the average for each case[items per min in (10,11,12,.....till 50)]

    for itemsPerMinute in range(10, 51, 1): #taking items per min in range 10 through 50
        maxWaitTime = 0
        minWaitTime = math.inf
        totalWaitTime = 0
        for i in range(10): #taking 10 simulations
            '''
            running 10 simulations each time (for different number of items per min) and calculating the best, average and the worst case 
            among those 10 simulations everytime.
            '''
            waitingTime = simulation(time_frame, itemsPerMinute)
            maxWaitTime = max(maxWaitTime, waitingTime)
            minWaitTime = min(minWaitTime, waitingTime)
            totalWaitTime += waitingTime
        maxTime.append(maxWaitTime)
        minTime.append(minWaitTime)
        avgTime.append(totalWaitTime / 100)
        print("On running 10 simulations for time frame of 600 seconds and %d items per min (entered by the cashier):" % (itemsPerMinute))
        print("The maximum, minimum and the average case among those 10 simulation outputs are:")
        print("Maximum Average Waiting Time for the customer (in seconds) : %3.2f" % maxWaitTime)
        print("Minimum Average Waiting Time for the customer (in seconds)  : %10.10f " % minWaitTime)
        print("Average of all the outputs from 10 simulations (in seconds) : %3.2f" % (totalWaitTime / 10))
        print("\n")

    #Plot to see the difference in the results of the simulation clearly
    plt.plot(range(10, 51, 1), maxTime, label='Best case (Maximum) Average waiting time')
    plt.plot(range(10, 51, 1), avgTime, label='Average case for the simulation')
    plt.plot(range(10, 51, 1), minTime, label='Worst case (Minimum) Average waiting time')

    plt.legend(loc='upper right')
    #Plot labeling
    plt.xlabel('Items entered by the cashier per min')
    plt.ylabel('Average wait time for the customer (in sec)')
    plt.title("Plot visualizing the comparison between the best, average and worst case of simulation results")
    plt.show()

    # So, the result of this simulation rejects the null hypothesis in favour of alternate hypothesis.

if __name__ == "__main__":
    main()