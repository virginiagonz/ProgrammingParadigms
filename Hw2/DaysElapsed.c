/*
* This program is designed to gather two inputs from the user and
* return the difference of the two dates. Struct date is used to 
* save the user input. The function daysElapsed takes a struct date
* data type to calculate the number of days for a given date and 
* then returns that number back to main.
*
* Created by Virginia Gonzalez
* October 10, 2022
*/
#include <stdio.h>
#include <stdlib.h>

struct date 
{
    int month, date, year;
} aDate, bDate;

int daysElapsed(struct date xDate) 
{
  // variable to hold number of days
  int nDays;
  
  // to determine which year to use
  if (xDate.month <= 2)
    xDate.year = xDate.year - 1;

  // to determine which month to use
  if (xDate.month <= 2)
    xDate.month = xDate.month + 13;
  else
    xDate.month = xDate.month + 1;

  // formula to return the number of days for a given date
  nDays = 1461 * xDate.year/4 + 153 * xDate.month/5 + xDate.date;

  return nDays;
}

int main(void) 
{
  // variables to hold number of days
  int date1Days, date2Days, daysBetween;

  // initializing structs
  struct date aDate = {0,0,0};
  struct date bDate = {0,0,0};

  // prompt the user to input two dates
  printf("\nThis program provides the number of days between two dates. \n");
  printf("----------------------------------------------------------- \n\n");
  printf("Please enter the first date (mm/dd/yyyy): ");
  scanf("%d/%d/%d", &aDate.month,&aDate.date,&aDate.year);
  printf("Please enter the second date (mm/dd/yyyy): ");
  scanf("%d/%d/%d", &bDate.month,&bDate.date,&bDate.year);

  // calculates days for date1 and date2 and returns the difference
  date1Days = daysElapsed(aDate);
  date2Days = daysElapsed(bDate);
  daysBetween = abs(date1Days-date2Days);

  // output answer
  printf("\nThere are %d between the two dates.", daysBetween);
  
  return 0;
}