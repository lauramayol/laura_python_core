'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''
births_secs = 6
deaths_secs = 12
imm_secs = 40
current_population = 380123456

# Get number of seconds in one year (365 days at 24 hrs/day at 60 mins/hr at 60 secs/min)
year_secs = 365 * 24 * 60 * 60


# Get number of births, deaths, immigrants per year
births_year = year_secs // births_secs
deaths_year = year_secs // deaths_secs
imm_year = year_secs // imm_secs


n = 1
new_population = current_population
while n < 4:
    new_population = new_population + births_year + imm_year - deaths_year
    print("The population " + str(n) + " years from now will be " + str(new_population))
    n = n + 1


# Below is my original code without the loop
years_3 = 3 * year_secs

# Get number of births, deaths, immigrants over the next 3 years
births_year3 = years_3 // births_secs
deaths_year3 = years_3 // deaths_secs
imm_year3 = years_3 // imm_secs

new_population = current_population + births_year3 + imm_year3 - deaths_year3
print("The population 3 years from now will be " + str(new_population))
