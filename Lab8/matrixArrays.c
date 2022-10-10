/*
* This program takes two 3x3 matrices to return their addition and subtraction.
* It also takes the transpose of any 3x3 matrix
*
* Created by Virginia Gonzalez
* September 19, 2022
*/

#include<stdio.h>

void matrixAdd(int a[3][3], int b[3][3], int sum[3][3]);
void matrixSubtract(int a[3][3], int b[3][3], int diff[3][3]);
void matrixTranspose(int a[3][3], int trans[3][3]);
//void matrixMultiply(int a[3][3], int b[3][3], int prod[3][3]);

int main(void)
{

   int a[3][3] = { {1,2,3}, {4,5,6}, {7,8,9} };
   int b[3][3] = { {3,5,7}, {7,3,2}, {0,2,6} };
   int sum[3][3];
   int diff[3][3];
   int trans[3][3];
   int prod[3][3];
   
   matrixAdd(a, b, sum);
   matrixSubtract(a, b, diff);
   matrixTranspose(a, trans);
  // matrixMultiply(a, b, prod);

}

void matrixAdd(int a[3][3], int b[3][3], int sum[3][3])
{
   printf("Matrix addition: \n");
   
   for (int i = 0; i < 3 ; i++)
   {
      for (int j = 0; j < 3 ; j++)
      {
         sum[i][j] = a[i][j] + b[i][j];
         printf("%d ", sum[i][j]);
      }
   	 
   	 printf("\n");
   
   }
   
   printf("\n\n");
}


void matrixSubtract(int a[3][3], int b[3][3], int diff[3][3])
{
   printf("Matrix subrtaction: \n");
   
   for (int i = 0; i < 3 ; i++)
   {
      for (int j = 0; j < 3 ; j++)
      {
         diff[i][j] = a[i][j] - b[i][j];
         printf("%d ", diff[i][j]);
      }
   	 
   	 printf("\n");
   
   }
   
   printf("\n\n");
}

void matrixTranspose(int a[3][3], int trans[3][3])
{
   printf("Matrix transpose: \n");
   for (int i = 0; i < 3 ; i++)
   {
      for (int j = 0; j < 3 ; j++)
      {
         if ( i == j )
         {
         	trans[i][j] = a[i][j];
         	printf("%d ", trans[i][j]);
         }
         else
         {
       	 	trans[j][i] = a[i][j];
      	 	trans[i][j] = a[j][i];
         	printf("%d ", trans[i][j]);
         }
         
      }
   	 
   	 printf("\n");
   	 
   }
   
   printf("\n\n");
}

/*void matrixMultiply(int a[3][3], int b[3][3], int prod[3][3])
{
   for (int i = 0; i < 3 ; i++)
   {
      for (int j = 0; j < 3 ; j++)
      {
         prod[i][j] = a[i][j] - b[i][j];
         printf("%d ", prod[i][j]);
      }
   	 
   	 printf("\n");
   
   }
   
   printf("\n");
}
*/
