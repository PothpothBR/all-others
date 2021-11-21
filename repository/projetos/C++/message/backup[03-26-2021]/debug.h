#ifndef DEBUG_H
#define  DEBUG_H

/* para nao necessitar do uso de _s para funcoes i/o */
#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
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
char** _format_text(const char* preform, const char* formated_text) {

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

/* adiciona a lista encadeada */
void _add_to_chain(Message *head, Message self) {

	if (!self) { printf(" [erro] <_add_to_chain()::self> argumento consta como nulo.\n"); getchar(); }

	self->next = *head;
	*head = self;
}

Message _create_message(Message *head, int ID, const char* preform, const char *vals, ...) {
	{
		volatile Message exists = *head;

		for (; exists != NULL && exists->ID != ID; exists = exists->next);
		if (exists) {
			printf(" [aviso] <_create_message()> numero de mensagem ja utilizado, nao criando mensagem.\n");
			return NULL;
		}
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
	message->text = _format_text(preform, buffer);
	message->before_len = (unsigned short int)strlen(*message->text);
	message->after_len = (unsigned short int)strlen(*(message->text + 1));

	/* insere o id da mensagem */
	message->ID = ID;

	/* e pré inicia o encadeamento */
	message->next = NULL;

	_add_to_chain(head, message);

	return message;
}


void _show_message(volatile Message head, int ID, const char* ierarchy) {

	if (!ierarchy) { printf(" [erro] <_show_message()::ierarchy> argumento consta como nulo.\n"); getchar(); }

	for (; head != NULL && head->ID != ID; head = head->next);

	(head != NULL)? printf("%s%s%s\n", *head->text, ierarchy, *(head->text + 1)) : printf(" [aviso] <_show_message()> a mensagem referente ao ID |%d| nao existe.\n", ID);
}

#endif // DEBUG_H