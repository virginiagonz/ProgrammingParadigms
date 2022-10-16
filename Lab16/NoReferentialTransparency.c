#include <stdio.h>

int x = 1; // global variable

// This function accepts a pointer variable to the global 
// variable as a parameter and returns the pointer variable 
int MyFunction(int *x)
{
    *x += 1; // Increments the value of the pointer variable by 1
    return *x;
}

int main(void)
{
    // Assign a pointer variable to the global variable
    int *ptrGlobal = &x;

    // Output statements to reflect that the global variable 
    // has been updated when passed by reference to MyFunction
    printf("Observing no referential transparency \n");
    printf("where the global int variable is equal to 1\n");
    printf("\nFirst call to MyFunction\n");
    printf("%d\n", MyFunction(&x));
    printf("Second call to MyFunction\n");
    printf("%d", MyFunction(&x));

}