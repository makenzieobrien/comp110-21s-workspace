"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population = int(input("Population:"))
doses_administered = int(input("Doses Administered:"))
doses_per_day = int(input("Doses Per Day:"))
target_percent_vacc = int(input("Target % Vaccinated:"))


# Calculate how many doses you need, considering you need 2 per person
num_doses = population * (target_percent_vacc / 100) * 2
still_needed = num_doses - doses_administered
days_passed = still_needed / doses_per_day

# To find days passed, use timedelta()
done_date = datetime.today() + timedelta(days_passed)
# Convert this day into a string!
printable_done_date = done_date.strftime("%B %d, %Y")

# Combine it all into a final print statement
target_vacc_string = str(target_percent_vacc) + "%"

print("We will reach " + target_vacc_string + " vaccination in " + str(int(days_passed)) + 
" days, which falls on " + printable_done_date + ".")