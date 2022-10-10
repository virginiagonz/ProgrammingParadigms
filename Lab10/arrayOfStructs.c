/*
* This program stores student information using struct arrays
* Created by Virginia Gonzalez
* September 23, 2022
*/

#include <stdio.h>
#include <stdlib.h>

struct Student
{
   char name[15];
   int age;
   float gpa;
};

int main(void)
{
   struct Student structArray[5];
   
  // studentsPtr = malloc(sizeof(struct Student));

   for (int i=0 ; i<5 ; i++)
   {
     printf("Please enter student's first name: ");
     scanf("%s", structArray[i].name);  
     printf("Enter %s's age: ", structArray[i].name);   
     scanf("%d", &structArray[i].age);
     printf("Enter %s's GPA: ", structArray[i].name);
     scanf("%f", &structArray[i].gpa);
   }
  
   printf("\n");
   
   for(int i=1; i <+ 5; i++)
   {
      printf("Student Record #%d: \n", i);
      printf("%s\n", structArray[i].name);
      printf("%d\n", structArray[i].age);
      printf("%.2f\n\n", structArray[i].gpa);
   }
   

}
