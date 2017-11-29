
# Title: Time Minimizing Restaurants

## Team Member(s): Nihali Jain
(Note: Don't put your email addresses here (which is public).  If a student wants their NAME hidden as well, due to optional FERPA regulations, they can be listed purely by their GitHub ID).

# Monte Carlo Simulation Scenario & Purpose:

Fast food restaurants are popular among price-sensitive youths and working adults who runs short of time and expects to receive service quickly. Moreover, the promotional lunch meals attract good response, resulting in occasional long queues and inconvenient waiting times. Thus, a simulation model can be used to analyze the system in a fast-food restaurants. For this project, I have taken a restaurant located on the Green Street (Which Which). The purpose of this simulation is to examine the average waiting time for the customer’s turn and based on the results, determine the serving rate in order to reduce the waiting time. This will help to improve customer service, with reference to reducing waiting time in the queue and shortening queue length by adding one more cashier to improve customer wait time.
### Hypothesis before running the simulation:

With a faster rate of entering the number of items (orders from customer) by the cashier, we should see that more number of customers are served per min. Thus, the conclusion  from this study is that the restaurant should increase the number of cashiers in order to increase the rate of entering the number of items (orders from customer). This will eventually minimize the customer's waiting time. 

### Simulation's variables of uncertainty. 
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). 
For each such variable, how did you decide the range and which probability distribution to use?  
Do you think it's a good representation of reality?

To model this situation, I considered 6 customers served per min on average. This means that on average there will be one customer every 600 seconds. For every second we can simulate the chance that a customer comes by generating a random number between 1 and 600. If the number is 600, this means a customer is at the counter to be served. Also, customers may order from 1 to 10 items. If each item from 1 to 10 is equally likely, then the items taken by each customer can be simulated using a random number between 1 and 10 inclusive. This modeling is based on my observations of people served every minute at Which Which restaurant.  And yes, I think it's a good representation of reality. 
## Instructions on how to use the program:

Run the simulation giving two parameters, first, time frame and second, the number of items (entered by the cashier) per min. By adjusting the number of items per min and running the trials again for the same time frame, with a faster rate of entering the number of items (orders from customer) we will see that more number of customers are served per min.
## Sources Used:
Modeled my own observations.
