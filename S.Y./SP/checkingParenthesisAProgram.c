//Coded by asprazz


#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define fox(a,n) for(a=0;a<n;a++)



/*********************STACK Operations *******************/

int top=-1;
char stack[200];

int stackEmpty() {
	if(top==-1) {
		return 1;
	}
	return 0;
}
void push(char s) {
	stack[top++]=s;
}
char topOfStack() {
	return stack[top-1];
}
char pop() {
	return stack[top--];
}
void printstack() {
		printf("%s",stack);
}
int validChar(char c){ 
	if(c=='(' || c==')' || c=='[' || c==']' || c=='{' || c=='}' )
		return 1;
	return 0;

}

/*********************ended stack operartions *********************/


int main() {
	int t,i,c=1,countLine;
	//int erroLines[1000];
	int
len,stringOk=0,countOpening=0,countClosing=0,openingCurly,closingCurly,openingSquare,closingSquare;
	char string[2000],fileName[20];
	char temp;
	char extra;
	FILE *fp;
	
	printf("\n| Enter no of cases : ");

	scanf("%d",&t);

	while(t--) {

		printf("| Enter the file name :");
		scanf("%s",fileName);
		fp=fopen(fileName,"r");
		//initialization for every test case 		
		stringOk=0;
		countOpening=0;
		countClosing=0;
		openingCurly=0;	
		closingCurly=0;
		openingSquare=0;		
		closingSquare=0;
		countLine=0;
		temp=fgetc(fp);
		i=0;
		while(temp!=EOF) {
			string[i]=temp;
			i++;
			temp=fgetc(fp);

			
		}
		//scanf("%s",string);
		len=strlen(string)-1;
		
		printf("Entered file is : %s",string);

		for(i=0;i<len;i++) {
			if(string[i]=='(')
				countOpening++;
			else if(string[i]==')')	
				countClosing++;
			else if(string[i]=='{')	
				openingCurly++;
			else if(string[i]=='}')	
				closingCurly++;
			else if(string[i]=='[')	
				openingSquare++;
			else if(string[i]==']')	
				closingSquare++;

		}

		if(countOpening == countClosing && openingCurly==closingCurly && openingSquare==closingSquare) 
			stringOk=1;

		
		if(stringOk==1) {

			//printf("**********************%d",len);
			for(i=0;i<len;i++) {

				if(stackEmpty()) {
					if(validChar(string[i]))
						push(string[i]);
				}
				else {
					temp=topOfStack();

					//printf("%c\n",temp);


					if(temp=='(' && string[i]==')') {
						extra=pop();
					}
					else if(temp=='{' && string[i]=='}') {
						extra=pop();
					}
					else if(temp=='[' && string[i]==']') {
						extra=pop();
					}
					else if( validChar(string[i])) {
						push(string[i]);
					}
				}

			}
			if(stackEmpty()) {
				printf("| Test Case %d is Ok with parenthesis \n",c);
			}
			else {
				printf("| Parenthesis are missplaced \n");
			}


		}



		else {	
			printf("\n| Error Report for test case %d.\n", c);
			i=1;
			if(countOpening > countClosing)
				printf("%d. Error: extra '(' parenthesis is their  \n",i++);
			if(countOpening < countClosing) 
				printf("%d. Error: extra ')' parenthesis \n",i++);
			if(openingCurly > closingCurly) 
				printf("%d. Error: extra '{' parenthesis \n",i++);
			if(openingCurly < closingCurly) 
				printf("%d. Error: extra '}' parenthesis \n",i++);
			if(openingSquare > closingSquare) 
				printf("%d. Error: extra '[' parenthesis \n",i++);
			if(openingSquare < closingSquare) 
				printf("%d. Error: extra ']' parenthesis \n",i++);
		}
		c++;
		//printstack();
		fclose(fp);
	}


	return 0;
}
