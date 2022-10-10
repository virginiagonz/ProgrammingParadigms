// This program prints out 4 sets of patterns
// Created by Virginia Gonzalez
// September 6, 2022

#include <stdio.h>

// function main begins program execution
int main( void )
{
   // ------------------------------------------- //
   // Part A
   
   for (int i = 0; i <= 10; i++) 
   {
   	for (int j = 0; j <= 10; j++ )
   	{
   		printf("*");
   	}
   	printf("\n");
   }
   printf("\n\n\n");
   
   // ------------------------------------------- //
   // Part B
   
   for (int i = 0; i <= 10; i++) 
   {
   	for (int j = 0; j <= i; j++ )
   	{
   		printf("*");
   	}
   	printf("\n");
   }
   printf("\n\n\n");
   
   // ------------------------------------------- //
   // Part C

   
   for (int i = 0; i <= 10; i++) 
   {	
   	for (int j = 0; j <= 10; j++ )
   	{
   		if (i <= j ) 
   			printf("*");
   			
   		else
   			printf(" ");
   	}
   	
   	printf("\n");
   }
   printf("\n\n\n");
   
   // ------------------------------------------- //
   // Part D 
   
   for (int i = 1; i <= 10; i++) 
   {
   	
   	for (int j = 1; j <= 10 - i; j++ )
   		printf(" ");
   	
   	for (int k = 1; k <= i*2 - 1; k++)
   		printf("*");
   		
   	printf("\n");
   }
   printf("\n\n\n");
   
   
} // end function main*");
   
