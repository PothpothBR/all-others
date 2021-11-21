/*
  ----------------------------------------------------
  |              Biblioteca feita por                |
  |     [Bruno Dalagnol] [2018] [versao: é...  ]     |
  |--------------------------------------------------|
  |                                                  |
  |			    /\         /\       ___              |
  |			   /--\_______/--\     /  _|             |
  |			   |  Y       Y  |    / /                |
  |			   |    ==T==    |   / /                 |
  |			   \_____________/  / /                  |
  |				  |  _____   \ / /                   |
  |				  |           \ /                    |
  |				  |  |--|  |\  |                     |
  |				  |__||_|__||__|                     |
  ----------------------------------------------------
*/

#ifndef DEBUG_H
#define  DEBUG_H

/* para nao necessitar do uso de _s para funcoes i/o */
#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h> // printf
#include <stdlib.h> // exit()
#include <stdarg.h> // va_list, va_start, ##__VA_ARGS__
#include <string.h> // str

/* estrutura para alocar a descricao do erro */
typedef struct _Message {
	int ID;
	char **text;
	unsigned short int before_len, after_len;
	struct _Message* next;
}*Message;


/* agrupa todas as strings fornecidas em um unico vetor*/
char** __format_text(const char* preform, const char* formated_text) {

	if (!preform) { printf(" [erro] <_format_text()::preform> argumento consta como nulo.\n"); getchar(); }
	if (!formated_text){ printf(" [erro] <_format_text()::formated_text> argumento consta como nulo.\n"); getchar(); }

	/* pega o tamanho total do texto para alocar */
	int full_size_before = strlen(preform) + 6;
	int full_size_after = strlen(formated_text) + 3;
	volatile int index = 0;

	/* aloca o espaco para o texto */
	char** text = (char**)calloc(sizeof(char*), 2);
	*text = (char*)calloc(sizeof(char), full_size_before);
	*(text+1) = (char*)calloc(sizeof(char), full_size_after);

	/* formata-o */
	strcat(*text, " ["); /* " [" */
	strcat(*text , preform); /* " [type" */
	strcat(*text , "] <\0"); /* " [type] <" */
	strcat(*(text + 1) , "> "); /* " [type] <> " */
	strcat(*(text + 1) , formated_text); /* " [type] <ierarchy> other texts" */

	return text;
}

Message _create_message(Message* head, int ID, const char* preform, const char *vals, ...) {
	{   volatile Message exists = *head;
		for (; exists != NULL && exists->ID != ID; exists = exists->next);
		if (exists) { printf(" [aviso] <_create_message()> numero de mensagem ja utilizado, nao criando mensagem.\n"); return NULL; }
	}

	if (!preform) { printf(" [erro] <_create_message()::preform> argumento consta como nulo.\n"); getchar(); }
	if (!vals) { printf(" [erro] <_create_message()::vals> argumento consta como nulo.\n"); getchar(); }

	/* aloca a estrutura message */
	Message message = (Message)calloc(sizeof(struct _Message), 1);

	unsigned short int buffer_lenght = 246;

	/* aloca o buffer com 256 caaracteres */
	char* buffer = (char*)calloc(sizeof(char), buffer_lenght);

	/* coleta e formata as entradas até um limite buffer_lenght */
	va_list va;
	va_start(va, vals);
	vsnprintf(buffer, buffer_lenght, vals, va);

	/* formata e insere a mensagem */
	message->text = __format_text(preform, buffer);
	message->before_len = (unsigned short int)strlen(*message->text);
	message->after_len = (unsigned short int)strlen(*(message->text + 1));

	/* insere o id da mensagem */
	message->ID = ID;

	/* e pré inicia o encadeamento */
	message->next = NULL;

	// adiciona a lista encadeada
	message->next = *head;
	*head = message;

	return message;
}


void _show_message(volatile Message head, int ID, const char* vals, ...) {

	if (!vals) { printf(" [erro] <_show_message()::vals> argumento consta como nulo.\n"); getchar(); }

	unsigned short int buffer_lenght = 246;

	// aloca o buffer com 256 caaracteres
	char* buffer = (char*)calloc(sizeof(char), buffer_lenght);

	// coleta e formata as entradas até um limite buffer_lenght
	va_list va;
	va_start(va, vals);
	vsnprintf(buffer, buffer_lenght, vals, va);

	for (; head != NULL && head->ID != ID; head = head->next);

	(head != NULL)? printf("%s%s%s\n", *head->text, buffer, *(head->text + 1)) : printf(" [aviso] <_show_message()> a mensagem referente ao ID |%d| nao existe.\n", ID);

	// se a mensagem for um erro, encerre o programa
	if (ID < 0) { getchar(); exit(ID); }
}

#endif // DEBUG_H
