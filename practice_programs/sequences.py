# FIT1056
# Week 2 Applied Exercises
# Sequences

# The following lists are defined for you:

months = ["January", "February", "March", "April", "May", "June", "July", 
          "August", "September", "October", "November", "December"]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
                "Saturday", "Sunday"]

# Based on calendar year 2024
num_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

### Indexing
# Exercise 1a: Use indexing to retrieve the current calendar month 
# and assign this to a variable.

index_month = int(input("please enter your desired month index: "))

current_month = months[index_month]


# Exercise 1b: Use indexing to retrieve the total number of days in
# the current calendar month, and assign this to (another) variable.

days_current_month = num_days_in_month[index_month]


### Slicing
# Exercise 2a: Retrieve the first 6 months of the calendar year.

first_six_months = months[0:6]

print(current_month, days_current_month, first_six_months)

# Exercise 2b: Retrieve the weekends of a calendar week.

weekend_days = days_of_week[::]

### Concatenation and Repetition
# Exercise 3a: Using concatenation and slicing, obtain a list of
# each day of the week for the next 7 days, starting from tomorrow.
# For example, if today is Thursday, the list should be:
# ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
school = "Monash University"
print(school[-10:])

print(len(5))

# Exercise 3b: Using repetition, obtain a list of each day of the week
# for the next 21 days, starting from tomorrow.
# You may use any obtained values from previous exercise parts (Hint: 3a).


### Functions involving sequences
# Exercise 4a: Verify that we have correctly identified 12 months in the 
# "months" list and 7 days in the "days_of_week" list.



# Exercise 4b: Verify that the list obtained in Exercise 3a contains 
# exactly 7 elements, and the list obtained in Exercise 3b contains 
# exactly 21 elements.



### Methods involving sequences
# Exercise 5a: Using the given variable below, obtain the index of the 
# current month in the "months" list. Do NOT use the index defined in Exercise 1.
cur_month_str = "July"  # change it to "August" if your Applied class falls on Thursday or Friday this week



# Exercise 5b: Using the given variable above (cur_month_str), return a
# string with the current month in all uppercase
# e.g. "JULY"


# Exercise 5c: Using the list of names defined below, create a name 
# and add this name to the list.
names = ["Adam", "Beth", "Charlie", "Daisy", "Eve"]


### Splitting and Joining Strings
# Exercise 6: Print a proper sentence that tells the reader what the days
# of a calendar week are. Remember to include space(s), comma(s) and 
# full stop(s) where necessary.
# (Optional challenge to include "and" before the last item)
sentence_start = "The months of a calendar year are "