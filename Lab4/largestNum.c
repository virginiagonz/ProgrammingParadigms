/*
* This program returns the largest and second largest number from a list of
* 10 inputs provided by the user.
* Written by Virginia Gonzalez
* September 1, 2022
*/
#include <stdio.h>

/*function main begins program execution*/
int main( void )
{
    int num = 0;
    int counter = 0; // to increment within the while loop
    int size = 10; // the size of the max input
    int max, max2 = 0; // max variable to hold the largest number
    
    // a while loop to save the inputs into an array of size 10
    while (counter < size) 
    {
    	printf("Enter an integer: "); //promt user to input integer
    	scanf("%d", &num ); //read the integer and put into an array
    	
    	if ( num > max ) 
    	{
    	//	max2 = max; // max2 will hold the previous largest integer
    		max = num; // max variable will hold the largest integer
    	}
    	if ( num < max && num >= max2)
    	{
    		max2 = num;
    	}
    
    	
    	counter++; // increases the value of counter
    }
    
    // Outputs the largest number
    printf("The largest integer is %d\n", max); 
    // Outputs the second largest number
    printf("The second largest integer is %d\n", max2); 

    return 0; //we return 0 if the program ends succesfully
} //end function main
