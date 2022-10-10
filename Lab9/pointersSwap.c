/*
* This program 
*
* Created by Virginia Gonzalez
* September 20,2022
*/

#include <stdio.h>

void swap(int *num1Ptr, int *num2Ptr);
int main(void)
{

   int num1, num2;
   
   printf("Please enter an integer \n");
   scanf("%d", &num1);
   printf("Please enter a second integer \n");
   scanf("%d", &num2);
   
   swap(&num1, &num2);
   
   printf("\nAfter swapping: \n");
   printf("The first integer is %d \n", num1);
   printf("The second integer is %d \n", num2);
}

void swap(int *num1Ptr, int *num2Ptr)
{
   int temp = *num1Ptr;
   *num1Ptr = *num2Ptr;
   *num2Ptr = temp;
}


