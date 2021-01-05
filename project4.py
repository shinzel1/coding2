{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unit test  False\n",
      "Unit test  2\n",
      "Unit test  1884\n"
     ]
    }
   ],
   "source": [
    "import calendar\n",
    "import datetime\n",
    "def days_in_month(year, month):\n",
    "    \"\"\"\n",
    "    Inputs:\n",
    "      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR\n",
    "              representing the year\n",
    "      month - an integer between 1 and 12 representing the month\n",
    "    Returns:\n",
    "      The number of days in the input month.\n",
    "    \"\"\"\n",
    "    #return calendar.monthrange(year, month) [1] #returns Tuplet\n",
    "    if month==4 or month==6 or month==9 or month==11:\n",
    "        return int(30)\n",
    "    elif month==1 or month==3 or month==5:\n",
    "        return int(31)\n",
    "    elif month==7 or month==8 or month==10 or month==12:\n",
    "        return int(31)\n",
    "    elif calendar.isleap(year) is True:\n",
    "        return int(29)\n",
    "    \n",
    "def  is_valid_date(year, month, day):\n",
    "    \"\"\"\n",
    "      Inputs:\n",
    "        year  - an integer representing the year\n",
    "        month - an integer representing the month\n",
    "        day   - an integer representing the day\n",
    "      Returns:\n",
    "        True if year-month-day is a valid date and\n",
    "        False otherwise\n",
    "      \"\"\"\n",
    "    days=days_in_month(year,month)\n",
    "    if (datetime.MINYEAR <= year <= datetime.MAXYEAR ):\n",
    "        if (month>=1 and month<=12):\n",
    "            if(day>=1 and day<=days):\n",
    "                return True\n",
    "            else:\n",
    "                return False\n",
    "        return False\n",
    "    return False\n",
    "\n",
    "print(\"Unit test \", is_valid_date(200000, 1, 1))\n",
    "\n",
    "\n",
    "def days_between(year1, month1, day1, year2, month2, day2):\n",
    "    if is_valid_date(year1,month1,day1) is False or is_valid_date(year2,month2,day2) is False:\n",
    "        return 0\n",
    "    elif datetime.date(year1,month1,day1)>datetime.date(year2,month2,day2):\n",
    "        return 0\n",
    "    else:\n",
    "        return (datetime.date(year2,month2,day2)-datetime.date(year1,month1,day1)).days\n",
    "\n",
    "print(\"Unit test \", days_between(2016,5,7,2016,5,9))\n",
    "\n",
    "\n",
    "def age_in_days(year, month, day):\n",
    "    if is_valid_date(year,month,day) is False:\n",
    "        return 0\n",
    "    elif datetime.date.today() < datetime.date(year, month, day):\n",
    "        return 0\n",
    "    else:\n",
    "        return (datetime.date.today() - datetime.date(year, month, day)).days\n",
    "\n",
    "print(\"Unit test \", age_in_days(2015, 11, 1))"
   ]
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
