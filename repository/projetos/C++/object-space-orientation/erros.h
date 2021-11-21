#ifndef ERRORS_H
#define	ERRORS_H

/* cabe�alhos padr�o */
#include <stdio.h> // printf
#include <stdlib.h> // system, exit


/* se ocorrer erro de aloca��o de mem�ria, gere uma mensagem apropriada e encerre o programa*/
#define _verify_memory_error(self, hierachy) \
	if (!self) { \
		printf("\nerro em |%s| ao alocar memoria, encerrando.\n", hierachy); \
		system("pause"); \
		exit(-1); \
	}

/* se o argumento fornecido for nulo, gere uma mensagem apropriada e encerre o programa
 * observe que um inteiro contendo 0 sera considerado erro
 * essa fun�ao serve somente para verificar a validade de ponteiros!*/
#define _verify_valid_argue(self, hierachy) \
	if (!self){ \
		printf("\nargumento em |%s| consta como nulo, encerrando.\n", hierachy); \
		system("pause"); \
		exit(-2); \
	} 


#endif // !