{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def days_in_month(year,month):\n",
    "    \"\"\"\n",
    "    This function takes two integers: a year and a month that return the number\n",
    "    of days in that given month.\n",
    "    \"\"\"\n",
    "\n",
    "    #computing number of days in a month\n",
    "    if (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <=11):\n",
    "        date1 = datetime.date(year,month,1)\n",
    "        date2 = datetime.date(year,month+1,1)\n",
    "        return (date2 - date1).days\n",
    "    elif (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (month == 12):\n",
    "        date1 = datetime.date(year,month,1)\n",
    "        date2 = datetime.date(year+1,1,1)\n",
    "        return (date2 - date1).days\n",
    "    else:\n",
    "        return False\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please write the year which number of days you want to calculate1000\n",
      "Please give the number of the month31\n",
      "Total Days in Month is : False\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#date is valid function\n",
    "def is_valid_date(year, month, day):\n",
    "    \"\"\"\n",
    "    This function takes three integers: a year, a month, and a day. and return\n",
    "    True if the date is valid and False otherwise.\n",
    "    \"\"\"\n",
    "\n",
    "    #computing date is valid or not\n",
    "    days = days_in_month(year, month)\n",
    "    if ((datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1<= month <= 12) and (0 < day <= days)):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#computing number of days between two dates\n",
    "def days_between(year1, month1, day1, year2, month2, day2):\n",
    "    \"\"\"\n",
    "    Takes six integers (year1, month1, day1, year2, month2, day2) and returns\n",
    "    the number of days from an earlier to a later date and if either date is\n",
    "    invalid the function return 0.\n",
    "    \"\"\"\n",
    "\n",
    "    #computing the number between days\n",
    "    #conditions and computation of days between two dates\n",
    "    if (is_valid_date(year1, month1, day1)) and (is_valid_date(year2, month2, day2)):\n",
    "\n",
    "        date1 = datetime.date(year1, month1, day1)\n",
    "        date2 = datetime.date(year2, month2, day2)\n",
    "\n",
    "        if (date2 > date1):\n",
    "            number_of_days = date2 - date1\n",
    "            return number_of_days.days\n",
    "        else:\n",
    "            return 0\n",
    "    else:\n",
    "        return 0\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#computing person's age in days\n",
    "def age_in_days(year, month, day):\n",
    "    \"\"\"\n",
    "    Takes three integers as input(year,month,day) of a persons\n",
    "    birthday and return that person's age in days as of today.\n",
    "    \"\"\"\n",
    "\n",
    "    #conditions and calculations of person's age in days\n",
    "\n",
    "    if (is_valid_date(year, month, day)):\n",
    "        today = datetime.date.today()\n",
    "        person_bday = datetime.date(year, month, day)\n",
    "        if (person_bday < today):\n",
    "            person_age_in_days = days_between(year, month, day, today.year, today.month, today.day)\n",
    "            return person_age_in_days\n",
    "        else:\n",
    "            return 0\n",
    "    else:\n",
    "        return 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please write the year which you want to check1998\n",
      "Please give the number of the month for finalise checking10\n",
      "Please give the date for Checking10\n",
      "Given date is : True\n",
      "Please write the year from where you want to calculate1000\n",
      "Please write the month from where you want to calculate10\n",
      "Please write the date from where you want to calculate10\n",
      "Please write the end year where to you want to calculate999\n",
      "Please write the end month where to you want to calculate10\n",
      "Please write the end date where to you want to calculate10\n",
      "Distance Between The Given Dates : 0\n",
      "Please write the year of birth10\n",
      "Please write the month of birth10\n",
      "Please write the date of birth101\n",
      "Persons age in days  : 0\n"
     ]
    }
   ],
   "source": [
    "year_input = int(input(\"Please write the year which number of days you want to calculate\"))\n",
    "month_input = int(input(\"Please give the number of the month\"))\n",
    "print(\"Total Days in Month is :\", days_in_month(year_input,month_input))\n",
    "\n",
    "year_input1 = int(input(\"Please write the year which you want to check\"))\n",
    "month_input1 = int(input(\"Please give the number of the month for finalise checking\"))\n",
    "day_input1 = int(input(\"Please give the date for Checking\"))\n",
    "print(\"Given date is :\",is_valid_date(year_input1,month_input1,day_input1))\n",
    "\n",
    "year_input2 = int(input(\"Please write the year from where you want to calculate\"))\n",
    "month_input2 = int(input(\"Please write the month from where you want to calculate\"))\n",
    "day_input2 = int(input(\"Please write the date from where you want to calculate\"))\n",
    "\n",
    "year_input3 = int(input(\"Please write the end year where to you want to calculate\"))\n",
    "month_input3 = int(input(\"Please write the end month where to you want to calculate\"))\n",
    "day_input3 = int(input(\"Please write the end date where to you want to calculate\"))\n",
    "print(\"Distance Between The Given Dates :\",days_between(year_input2,month_input2,day_input2,year_input3,month_input3,day_input3))\n",
    "\n",
    "year_input4 = int(input(\"Please write the year of birth\"))\n",
    "month_input4 = int(input(\"Please write the month of birth\"))\n",
    "day_input4 = int(input(\"Please write the date of birth\"))\n",
    "print(\"Persons age in days  :\",age_in_days(year_input4,month_input4,day_input4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
