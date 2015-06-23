import pylab

class SmartLink(object):
    '''
    Use this to compare different PATH SmartLink plans to get the best value 
    for the number of trips you plan on taking. 
    
    Best used to compare fixed plans like the 40 Pack to the Unlimited plan 
    so you can see how many trips you need to take for it to pay off
    '''
    def __init__(self, name, cost, numberOfTrips):
        self.name = name
        self.cost = cost
        self.numberOfTrips = numberOfTrips
        self.value = cost / numberOfTrips


def createPlot(options):
    #need an x and y for each plan you want to plot
    x1, x2, x3, y1, y2, y3 = ([] for i in range(6))
    
    for i in range(len(options)):  
        if(options[i].name == "Unlimited"):
            x1.append(options[i].numberOfTrips)    
            y1.append(options[i].value)
        elif(options[i].name == "Single Ride"):
            for j in range(len(options)):  
                x2.append(options[j].numberOfTrips)    
                y2.append(options[i].value)   
        elif(options[i].name == "40 Pack"):
            for j in range(len(options)):  
                x3.append(options[j].numberOfTrips)    
                y3.append(options[i].value)  
                     
    pylab.plot(x1,y1,'b')
    pylab.plot(x2,y2,'r')
    pylab.plot(x3,y3,'g')      
    pylab.title("SmartLink Plan Options")
    pylab.xlabel('Number of Trips Taken with Plan', fontsize=10)
    pylab.ylabel('Actual Cost Per Trip')
    pylab.legend(('Unlimited', 'Single Ride (Fixed)', '40 Pack (Fixed)'))
    pylab.show()



#create a list of all possible outcomes...
#e.g. a single ride, a 40 pack, an unlimited used 35 times per month, 
#an unlimed used 52 times per month, etc. 

options = []

for r in range(1,60):
    option = SmartLink('Unlimited', 89.00, r)
    options.append(option)
    if(r == 1): 
        option = SmartLink('Single Ride', 2.75, r)
        options.append(option)
    if(r == 40):
        option = SmartLink('40 Pack', 84.00, r)    
        options.append(option)
        
createPlot(options)






