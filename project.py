{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# days in month function\n",
    "   def days_in_month(year,month):\n",
    "        if (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <=11):\n",
    "            date1 = datetime.date(year,month,1)\n",
    "            date2 = datetime.date(year,month+1,1)\n",
    "            return (date2 - date1).days\n",
    "        elif (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (month == 12):\n",
    "            date1 = datetime.date(year,month,1)\n",
    "            date2 = datetime.date(year+1,1,1)\n",
    "            return (date2 - date1).days\n",
    "        else:\n",
    "            return False\n",
    "   \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "   def is_valid_date(year, month, day):\n",
    "        days = days_in_month(year, month)\n",
    "        if ((datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1<= month <= 12) and (0 < day <= days)):\n",
    "            return True\n",
    "        else:\n",
    "            return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "   def days_between(year1, month1, day1, year2, month2, day2):\n",
    "        if (is_valid_date(year1, month1, day1)) and (is_valid_date(year2, month2, day2)):\n",
    "            date1 = datetime.date(year1, month1, day1)\n",
    "            date2 = datetime.date(year2, month2, day2)\n",
    "        if (date2 > date1):\n",
    "            number_of_days = date2 - date1\n",
    "            return number_of_days.days\n",
    "        else:\n",
    "            return 0\n",
    "    else:\n",
    "        return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def age_in_days(year, month, day):\n",
    "    if (is_valid_date(year, month, day)):\n",
    "        today = datetime.date.today()\n",
    "        person_bday = datetime.date(year, month, day)\n",
    "        if (person_bday < today):\n",
    "            person_age_in_days = days_between(year, month, day, today.year, today.month, today.day)\n",
    "            return person_age_in_days\n",
    "        else:\n",
    "            return 0\n",
    "    else:\n",
    "        return 0"
   ]
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
