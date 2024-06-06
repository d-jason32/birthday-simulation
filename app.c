#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h> 

char *generateBirthdays(int numBirthdays){
    /*
    Generates birthdays and stores it in a list.
    */
   char *birthdayList = malloc(numBirthdays);

   if(!birthdayList){
    return NULL;
   }

   for (int i = 0; i < numBirthdays; i++){
    int randomNum = rand() % (366);
    birthdayList[i] = randomNum;
   }

   return birthdayList;
}

int main(){
    srand(time(NULL));

    printf("How many birthdays shall I generate? (Max 100): ");
    
    int numBirthdays;
    scanf("%d", &numBirthdays);

    printf("Here are %d birthdays: ", numBirthdays);
    
    char *list = generateBirthdays(numBirthdays);

    for (int i = 0; i < numBirthdays; i++){
    printf("%d",list[i]);
    }


}
