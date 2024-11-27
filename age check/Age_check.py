#--Find Age ?
#EX
#Enter Your Birth Year : 1992
#Enter Your Birth Month : 4
#Enter Your Birth Day : 16

#-- Current Date

#Enter Your Current Year : 2023
#Enter Your Current Month : 7
#Enter Your Current Day : 26

#- output

#30 years 3 months 10 days
#or 363 months 10 days
#or 1579 weeks 5 days
#or 11,058 days
#3or 265,392 hours

birthyear=int(input('Enter your birth year: '))
birthmonth=int(input('Enter your birth month: '))
birthdate=int(input('Enter your birth date: '))

print('-----------------------------------------')

currentyear=int(input('Enter current  year: '))
currentmonth=int(input('Enter current  month: '))
currentdate=int(input('Enter current  date: '))

print('-----------------------------------------')

years = 365
if birthmonth == 1 or birthmonth ==3 or birthmonth ==5 or birthmonth ==7 or birthmonth ==8 or birthmonth ==10 or birthmonth ==12 :
   days = 31
elif birthmonth == 4 or birthmonth ==6 or birthmonth ==9 or birthmonth ==11 :
   days = 30
elif ((birthmonth==2) and (birthyear%4==0)) :
    days = 29
else :
   days = 28

total_year = abs(birthyear - currentyear )
print(f"Total Year = {total_year}")

totalmonth = birthmonth - currentmonth
print(f"Total month = {totalmonth}")

day = birthdate - currentdate
print(f"total day live you in month  = {day}")

age=(total_year * 365 ) + (totalmonth * days) + day
print(f"Over all day live you = {age}")