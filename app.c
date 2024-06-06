#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int *generateBirthdays(int numBirthdays){
    /*
    Generates int between 1-365 and stores it in a list.
    */
   int *birthdayList = malloc(numBirthdays * sizeof(int));

   if(!birthdayList){
       return NULL;
   }

   for (int i = 0; i < numBirthdays; i++){
       int randomNum = rand() % 365 + 1;
       birthdayList[i] = randomNum;
   }

   return birthdayList;
}

int main(){
    srand(time(NULL));

    printf("How many birthdays shall I generate? (Max 100): ");
    
    int numBirthdays;
    scanf("%d", &numBirthdays);

    // Check for valid number of birthdays
    if(numBirthdays < 1 || numBirthdays > 100) {
        printf("Please enter a number between 1 and 100.\n");
        return 1;
    }

    int *birthdays = generateBirthdays(numBirthdays);

    if (!birthdays) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    printf("Here are %d birthdays: ", numBirthdays);
    for (int i = 0; i < numBirthdays; i++) {
        printf("%d ", birthdays[i]);
    }
    printf("\n");

    free(birthdays);
    return 0;
}