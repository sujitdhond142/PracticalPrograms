// We Code Here --> T.Y.B.Tech Computer
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


//definations here 
#define ON 1
#define OFF 0
#define DEBUG 1



//functions declaratins here







//starting of the main program
int main() {

    // assembla designing and developement by tybtech computer 
    
    //declaring variables 
    char choice,continueChoice;


    do {
        printf("________________MENU__________________");
        printf("1. Enter the program here");
        printf("2. Search in POT");
        printf("3. Search in MOT");
        printf("4. Create Symbol Table");
        printf("5. Create the literal Table");
        printf("Enter your chioce");
        scanf("%s",&choice);

        switch(choice) {
            

            case '1':break;
            case '2':break;
            case '3':break;
            case '4':break;
            case '5':break;
            default: printf("Invalid chocie");

        }
        printf("Do you want to continue ? ");
        scanf("%s",&continueChoice);
    
    }while(continueChoice == 'y' || continueChoice ==  'Y');

    return 0;
}

//definations of functions 





