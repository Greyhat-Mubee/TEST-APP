import pandas as pd
import numpy as np

#############################
# THIS WAS A GIT REPO TEST ##
##############################

name = ['Mubarak', 'Jida', 'Jude', 'Eddie', 'Zamani']
department = ['NOC', 'Management', 'Data', 'Security', 'Tourism']
state = ['Kwara', 'Lagos', 'Benue', 'Akwa ibom', 'Plateau']
staff_ind =['MU', 'JI', 'JU', 'ED', 'ZA']

staff_dict = {'name':name, 'department':department, 'state':state}
staff = pd.DataFrame(staff_dict)
staff.index = staff_ind

# print(staff)

# print(staff['name'])

# print(staff[['name']]) 

# print(staff[['name', 'state']]) 

# print(staff[0:4])

# print(type(staff[0:4][0:2]))

# print(staff[0:4][0:2])

# To import data from file, use the code below
# variable = pd.read_csv('path/to/csv'/file)

# below is a more robust way of using indexing and selecting data from a panda data frame
# - loc  - (label oriented)
# - iloc - (index position oriented)

cars = pd.read_csv('cars.csv', index_col=0)
print(cars)

# Print out observation for Japan
print(cars.loc['JPN'])
print(cars.loc[['JPN']])
# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])
#print(cars.iloc[[4,5], [1,2]])

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])
#print(type(cars.loc[:,'drives_right']))

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])
#print(type(cars.loc[:,['drives_right']]))


# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap', 'drives_right']])
# Extract drives_right column as Series: dr
dr = cars['drives_right']

####################################################
# Code for loop that adds COUNTRY column
for l, r in cars.iterrows():
    cars.loc[l, "COUNTRY"] = r['country'].upper()

# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print (sel)
# Print out observations for Australia and Egypt
# print(cars.loc['AUS', 'EG'])
# print(cars.loc[['AUS', 'EG']])

# print(staff.iloc[:,[2]])

#COMPARISON

#NUMPY Comparison functions
#==> logical_and()
#==> logical_or()
#==> logical_not()

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(my_house >= 18)
print(my_house < your_house)
# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

#CONTROL-FLOW
#If-elif-else

room = "Kitchen"
area = 20

if room == 'Kitchen' and area < 20:
    print('This is not the perfect Kitchen for the house')
elif room == 'bed' and area >= 20:
    print('This a perfect sized bedroom!')
else:
    print('This is a perfect kitchen')
    
    
#loop
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index,a in enumerate(areas):
    print('room ' + str(index) + ': ' + str(a))
    
#Looping with dictionaries
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k, v in europe.items():
    print('the capital of ' + k + ' is ' + v)
    
    # For loop over np_height
for no in np_height:
    print(str(no) + " inches")

# For loop over np_baseball
for bo in np.nditer(np_baseball):
    print(bo)
    
    # Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ': ' + str(row['cars_per_cap']))
    
    
####################################################
#RANDOM
####################################################

np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice > 2 and dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)


# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)



# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)


# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()



# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
