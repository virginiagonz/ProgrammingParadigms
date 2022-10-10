#include <stdio.h>

void Fibonacci(int nthInt);
void FibonacciTriangle(int nthInt);

int main( void )
{
   int nth = 0;
   
   printf("Enter an nth integer: ");
   scanf("%d", &nth);
   
   Fibonacci(nth);
   FibonacciTriangle(nth);
   
} // end function main

void Fibonacci (int nthInt) 
{
	unsigned long long int prevTerm, newTerm = 0;
   	unsigned long long int currTerm = 1;
   	int counter = 1;
   	
	while ( counter <= nthInt)  
	{
		printf("%lld ", prevTerm);
		
		newTerm = prevTerm + currTerm;
		prevTerm = currTerm;
		currTerm = newTerm; 
		
		counter++;
	}
} 

void FibonacciTriangle (int nthInt) 
{
	printf("\n\n\n");
	
	for(int i = 0; i <= nthInt; i++)
	{
		Fibonacci(i);
		printf( "\n" );
   
	}
}

