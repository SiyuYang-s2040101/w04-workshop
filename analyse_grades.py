import numpy as np
import matplotlib.pyplot as plt

# Task 1
# Read the data into a NumPy array
# grades = np.loadtxt('grades.txt') has a bug, we should delete ','
grades = np.loadtxt('grades.txt', delimiter=',')


# Task 2
# Make some plots
# Set a figure
fig = plt.figure(figsize=(15,6))

# Create a 2x2 matrix for subplots
# Match ax with subplot
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# Adjust the locations of subplots, here we adjusted the vertical distances between subplots 
plt.subplots_adjust(hspace=1)

# Set the limit(0,100) for axis
ax1.set_xlim(0,100)
ax2.set_xlim(0,100)
ax3.set_xlim(0,100)
ax4.set_xlim(0,100)

# Make histgrams and define label names
# Choose all the elements in the first column of the array - grades
x1 = grades[:, 0]
n, bins, patches = ax1.hist(x1)
ax1.set_xlabel('Assignment1')
ax1.set_ylabel('Frequency')

# Choose all the elements in the second column of the array - grades
x2 = grades[:, 1]
n, bins, patches = ax2.hist(x2)
ax2.set_xlabel('Assignment2')
ax2.set_ylabel('Frequency')

# Choose all the elements in the third column of the array - grades
x3 = grades[:, 2]
n, bins, patches = ax3.hist(x3)
ax3.set_xlabel('Assignment3')
ax3.set_ylabel('Frequency')

# Choose all the elements in the forth column of the array - grades
x4 = grades[:, 3]
n, bins, patches = ax4.hist(x4)
ax4.set_xlabel('Assignment4')
ax4.set_ylabel('Frequency')


# Task 3
# Calculate means of the grades in each assignment
mean1 = np.mean(x1)
mean2 = np.mean(x2)
mean3 = np.mean(x3)
mean4 = np.mean(x4)

# Round the results to 2 decimals and print the results 
print('The average grades for assignment 1 is', round(mean1,2))
print('The average grades for assignment 2 is', round(mean2,2))
print('The average grades for assignment 3 is', round(mean3,2))
print('The average grades for assignment 4 is', round(mean4,2))

# Count how many students got A in each assignment
x1_bool = np.array(x1 >= 70)
x1_over_70 = np.sum(x1_bool)

x2_bool = np.array(x2 >= 70)
x2_over_70 = np.sum(x2_bool)

x3_bool = np.array(x3 >= 70)
x3_over_70 = np.sum(x3_bool)

x4_bool = np.array(x4 >= 70)
x4_over_70 = np.sum(x4_bool)

# Print the results
print(x1_over_70, 'students got an A for assignment 1')
print(x2_over_70, 'students got an A for assignment 2')
print(x3_over_70, 'students got an A for assignment 3')
print(x4_over_70, 'students got an A for assignment 4')

# A function to count how many students got A for all the assignments
def A_for_all():
    count = 0
    for i in range(0,300):
        # the variable - row represents all the elements in each row of the array - grades
        row = grades[i,:]
        # if all the elements in row is equal or greater than 70, then count+1
        if row.all() >= 70:
            count += 1
            print(count)
        else:
            continue
    return count

# Print the result
print(A_for_all(),'student(s) got an A for all 4 assignments')

# Write the results from statistical analysis into a new file called 'stats.txt'
with open('stats.txt', 'w') as grades_text:
    
    grades_text.write(f'The average grades for assignment 1 is {round(mean1,2)}.'+'\n')
    grades_text.write(f'The average grades for assignment 2 is {round(mean2,2)}.'+'\n')
    grades_text.write(f'The average grades for assignment 3 is {round(mean3,2)}.'+'\n')
    grades_text.write(f'The average grades for assignment 4 is {round(mean4,2)}.'+'\n')
    
    grades_text.write(f'{x1_over_70} students got an A for assignment 1.'+'\n')
    grades_text.write(f'{x2_over_70} students got an A for assignment 2.'+'\n')
    grades_text.write(f'{x3_over_70} students got an A for assignment 3.'+'\n')
    grades_text.write(f'{x4_over_70} students got an A for assignment 4.'+'\n')
    
    grades_text.write(f'{A_for_all()} student(s) got an A for all 4 assignments.'+'\n')