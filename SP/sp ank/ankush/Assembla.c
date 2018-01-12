#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>


#define ON 1
#define OFF 0
#define NEW_LINE printf("\n")

/* struct opCodes {
	int counter; char name[4]; char opcode[4];
}MOT[20],POT[20];
*/

void printMOT(int,int,char table[20][2][5]);
void printPOT(int,int,char table[20][2][6]);
/* for checking in table */
void checkInMOT(FILE *,char T[20][2][5],char S[20][3][6]);
void generateSymbolTable(FILE *,char T[8][2][6]);


int main() {
	//declaring variables
	char temp,choice,ans; //for reading from the file
	int i=0; int j=0; int k=0;

	char MOT[20][2][5]= { "ADD","M0001",
				"SUB","M0010", "MUL","M0011", "DIV","M0100", "ADC","M0101", "MOV","M0110", "JZ","M0111", "JNZ","M1000", "JNC","M1001",
				"JC","M1010", "CMP","M1011", "INC","M1100", "DEC","M1101", "LOAD","M1110", "DAA","M1111" };
	char POT[8][2][6]= { "USING","P0001",
				"START","P0010",
				"DROP","P0011",
				"DW","P0100",
				"DQ","P0101",
				"DS","P0110",
				"DT","P0111",
				"ASSUME","P1000"
			};
	FILE *pIn;

	char SOT[20][3][6]={0};





	do {
		printf("\n_____________________MENU ____________________________");
		printf("\n1. Read Program");
		printf("\n2. Check In POT");
		printf("\n3. Check In MOT");
		printf("\n4. Display Symbol table");
		printf("\n Enter your choice : ");
		scanf("%s",&choice);
		switch(choice) {
			case '1':pIn = fopen("program.txt","r+");
				if(pIn == NULL) {
					printf("Error opening file");
					exit(0);
				}
				break;
			case '2':generateSymbolTable(pIn,POT);
				break;
			case '3':break;
			case '4':break;
			case '0':exit(0);
			default:printf("\nInvalid Choice");
		}
		printf("\n| Continue or not : ");
		scanf("%s",&ans);


	if(OFF) {
		temp=fgetc(pIn);

		while(temp!=EOF) {
			printf("%c",temp);
			temp=fgetc(pIn);
		}
	}

	if(OFF) {
		printMOT(0,0,MOT);
		printPOT(0,0,POT);
		NEW_LINE;
		checkInMOT(pIn,MOT,SOT);
	}
	}while(ans=='y' || ans=='Y');
	return 0;

}


void printMOT(int i,int j,char table[20][2][5]) {
	printf("OPERATION\tBINARY CODE\n");
	for(i=0;i<20;i++) {
                for(j=0;j<2;j++) {
                                printf("%s\t",table[i][j]);
                }
                printf("\n");
        }
}

void printPOT(int i,int j,char table[8][2][6]) {
	printf("OPERATION\tBINARY CODE\n");
	  for(i=0;i<8;i++) {
                for(j=0;j<2;j++) {
                        printf("%s\t",table[i][j]);
                }
                printf("\n");
        }
}

void generateSymbolTable(FILE *fp,char T[8][2][6]) {
	FILE *pOut;
	int LC=0;
	char label[20],opcode[20],operandOne[20],operandTwo[20],i=0;
	pOut=fopen("symoblTable.txt","w");

	while(fscanf(fp,"%s%s%s%s",label,opcode,operandOne,operandTwo) != EOF) {
		LC+=4;
		if(ON)
			printf("%s %s %s %s\n",label,opcode,operandOne,operandTwo);

		//1check for ** in label field
		//check for opcode
		if(strcmp(label,"**")==0) {

			//perform operations on equal with the **
			//printf("Equal");


		}
		else {

			if( (strcmp(opcode,"EQU") == 0) || (strcmp(opcode,"DC") == 0)) {
				fprintf(pOut,"%s\t%s\t%s\n",label,operandOne,"A");
				printf("%s%s",label,operandOne);

				/*
				S[i][0]=label;
				s[i][1]=operandOne;
				s[i][2]="A";
				i++;
				*/

				printf("write success\n");
			}
			else {
				fprintf(pOut,"%s\t%d\t%s\n",label,LC,"R");
				printf("%s%s",label,operandOne);

				/*
				S[i][0]=label;
				s[i][1]=LC;
				s[i][2]="R";
				i++;
				*/

				printf("write success\n");
			}
		}

	}
}

void checkInMOT(FILE *fp,char T[20][2][5],char S[20][3][6]) {
	  char label[20],opcode[20],operandOne[20],operandTwo[20];

        while(fscanf(fp,"%s%s%s%s",label,opcode,operandOne,operandTwo) != EOF) {

                if(!ON)
                        printf("%s %s %s %s\n",label,opcode,operandOne,operandTwo);

                //1check for ** in label field


                // check for opcode

                if(strcmp(label,"**")==0) {

                       	//printf("EQUAL");
			// perform operations on MOT when **


                }
                else {



                }
        }

}
