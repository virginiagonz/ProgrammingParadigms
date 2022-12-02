#include <stdio.h>

int APRGenerator(int creditScore);

int main(void)
{
    int score, apr = 0;

    printf("This program determines the interest rate of a user \n");
    printf("when they take out a loan based on their credit score\n");
    printf("\nPlease enter your credit score: ");
    scanf("%d", &score);
    printf("\nThe interest rate for your loan is %d%%", APRGenerator(score));

    return 0;

}

int APRGenerator(int creditScore)
{
    int APR;
    if (creditScore >= 800)
        APR = 3;
    else if (creditScore >= 700)
        APR = 5;
    else if (creditScore >= 600)
        APR = 8;
    else if (creditScore >= 500)
        APR = 11;
    else
        APR = 23;

    return APR;
}