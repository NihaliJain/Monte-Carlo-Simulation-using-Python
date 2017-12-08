
# Title: Time Minimizing Restaurants

## Team Member(s): Nihali Jain
(Note: Don't put your email addresses here (which is public).  If a student wants their NAME hidden as well, due to optional FERPA regulations, they can be listed purely by their GitHub ID).

# Monte Carlo Simulation Scenario & Purpose:

Fast food restaurants are popular among price-sensitive youths and working adults who runs short of time and expects to receive service quickly. Moreover, the promotional lunch meals attract good response, resulting in occasional long queues and inconvenient waiting times. Thus, a simulation model can be used to analyze the system in a fast-food restaurant. For this project, I have taken a restaurant located on the Green Street (Which Which). The purpose of this simulation is to examine the average waiting time for the customer’s turn and based on the results, determine the serving rate in order to reduce the waiting time. This will help to improve customer service, with reference to reducing waiting time in the queue and shortening queue length by adding one more cashier to improve customer wait time.

### Hypothesis before running the simulation:

Null Hypothesis: There is no association between the customer's waiting time and the rate of number of items entered by the cashier.
Alternate Hypothesis:  There is an association between the customer's waiting time and the rate of number of items entered by the cashier.
 

### Simulation's variables of uncertainty. 
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). 
For each such variable, how did you decide the range and which probability distribution to use?  
Do you think it's a good representation of reality?

To model this situation, I considered 3 customers arriving per min on average (either at the counter if cashier is free or in the queue if cashier is busy). This means that on average there will be one customer every 20 seconds. For every second we can simulate the chance that a customer comes by generating a random number between 1 and 20. If the number is 20, this means a customer is in the queue. Also, customers may order from 1 to 10 items. If each item from 1 to 10 is equally likely, then the items taken by each customer can be simulated using a random number between 1 and 10 inclusive.  
## Instructions on how to use the program:

Run the simulation giving two parameters, first parameter is the time frame for the simulation and the second parameter is the number of items (entered by the cashier) per min. By adjusting the number of items entered per min and running the trials again for the same time frame, we can observe how the simulation result changes according to the rate of number of items entered by the cashier.

## Results Obtained:
The simulation result rejects the null hypothesis in favour of alternate hypothesis and confirms that there is an association between the customer's waiting time and the rate of number of items entered by the cashier. As we increase the number of items entered per min for a given time frame, we can observe that more number of customers are being served and the average time for the customer has been reduced. Hence, we can conclude that the restaurant should increase the number of cashiers in order to increase the serving rate (items entered) and to eventually minimize the customer's wait time. Also, for robust simulation results we can take the real data.
## Sources Used:
1. https://docs.python.org/2/library/queue.html
2. https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
3. https://docs.python.org/2/library/random.html#module-random