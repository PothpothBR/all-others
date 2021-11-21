#ifndef	OBJECT_ACTIONS_H
#define	OBJECT_ACTIONS_H

/* cabeçalhos padrão */
#include <stdlib.h> // calloc, free

/* dependencias externas*/
#include "erros.h"
#include "vector4.h"
#include "primitive_object.h"

/* objeto de acao que representa o objeto verdadeiro quando esta em um estado especifico */
typedef struct _Action {
	Primitive_object body;
	short int active; /*c nao tem bool?*/
}*Action;

/* estrutura para modificar o objeto quando o mouse estiver sobreposto */
typedef struct _Actions {
	/* quando o mouse estiver em cima*/
	Action hover;
	/* quando for cicado no objeto*/
	Action pressed;
	/* somente no momento em que for soltado*/
	Action in_relase;
}*Actions;

/* cria e retorna uma estrutura de acao */
Action _create_action(float x, float y, float width, float height,
	vector4_t padding, vector4_t border, vector4_t margin) {

	/* verifica a validade dos argumentos */
	_verify_valid_argue(*border, "_create_action -> border");
	_verify_valid_argue(*margin, "_create_action -> margin");
	_verify_valid_argue(*padding, "_create_action -> padding");

	/* cria o objeto */
	Action self = (Action)calloc(sizeof(struct _Action), 1);
	/* verifica falha na alocação de memória*/
	_verify_memory_error(self, "_create_action -> self");

	/* atribui os valores*/
	self->active = 0;
	/* e cria o objeto primitivo*/
	self->body = _create_primitive_object(x, y, width, height, padding, border, margin);

	/* como os valores de vector sao usados por _create_primitive_object()
	 * nao é nessesario liberalos pois a funcao ja o faz*/

	/* retorna o objeto action completo*/
	return self;
}

/* cria e retorna uma estrutura que contem multiplas acoes */
Actions _create_actions(float x, float y, float width, float height,
	vector4_t padding, vector4_t border, vector4_t margin) {

	/* verifica a validade dos argumentos */
	_verify_valid_argue(border, "_create_actions -> border");
	_verify_valid_argue(margin, "_create_actions -> margin");
	_verify_valid_argue(padding, "_create_actions -> padding");

	/* cria o objeto */
	Actions self = (Actions)calloc(sizeof (struct _Actions), 1);
	/* verifica falha na alocação de memória*/
	_verify_memory_error(self, "_create_actions -> self");

	/* cria as acoes isoladas */
	/* as primeiras duas instanciascoes sao virtualizadas pois cada uma delas libera a memoria do vector4
	 * a ultima nao necessita pois é necessario deslocar os recursos do vector4*/
	self->hover = _create_action(x, y, width, height, _virtualize_vector4(padding), _virtualize_vector4(border), _virtualize_vector4(margin));
	self->pressed = _create_action(x, y, width, height, _virtualize_vector4(padding), _virtualize_vector4(border), _virtualize_vector4(margin));
	self->in_relase = _create_action(x, y, width, height, padding, border, margin);

	/* como os valores de vector sao usados por _create_action -> _create_primitive_object()
	 * nao é nessesario liberalos pois a funcao ja o faz*/

	/* retorna o objeto actions completo*/
	return self;
}

/* modifica a estrutura action dentro de actions */
void _reload_action(Action self, float x, float y, float width, float height,
	vector4_t padding, vector4_t border, vector4_t margin) {

	/* verifica a validade dos argumentos */
	_verify_valid_argue(padding, "_reload_action -> padding");
	_verify_valid_argue(border, "_reload_action -> border");
	_verify_valid_argue(margin, "_reload_action -> margin");

	/* substitui os valoes simples*/
	self->active = 0;
	self->body->x = x;
	self->body->y = y;
	self->body->width = width;
	self->body->height = height;

	/* substitui os valores vetoriais*/
	register int i;
	for (i = 0; i < 4; i++){
		*(self->body->padding + i) = *(padding + i);
		*(self->body->border + i) = *(border + i);
		*(self->body->margin + i) = *(margin + i);
	}

	/* libera os vetores pois não são mais necessarios*/
	_delete_vector4(padding);
	_delete_vector4(border);
	_delete_vector4(margin);
}

/* deleta um objeto action e todas as suas dependências*/
void _delete_action(Action self) {
	_delete_primitive_object(self->body);

	free(self);
	self = NULL;
}

/* deleta um objeto actions e todas as suas dependências*/
void _delete_actions(Actions self) {

	_delete_action(self->hover);
	_delete_action(self->pressed);
	_delete_action(self->in_relase);


	free(self);
	self = NULL;
}
#endif