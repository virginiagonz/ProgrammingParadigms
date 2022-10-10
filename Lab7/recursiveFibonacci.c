/*
* This program returns the largest and second largest number from a list of
* 10 inputs provided by the user.
* Written by Virginia Gonzalez
* September 1, 2022
*/
#include <stdio.h>
int long long Fibonacci(int nthInt);
int main( void )
{
   int long long nth = 0;
   printf("Enter an nth integer: ");
   scanf("%lld", &nth);
   
   printf("%lld", Fibonacci(nth));
   printf("\n");

    return 0; //we return 0 if the program ends succesfully
} //end function main

int long long Fibonacci (int index)
{
	if (index == 1)
		return 0;
	else if (index == 2)
		return 1;
	else
		return Fibonacci(index-1) + Fibonacci(index-2);
		
}
