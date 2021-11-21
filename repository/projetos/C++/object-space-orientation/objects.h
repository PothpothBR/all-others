#ifndef	OBJECTS_H
#define OBJECTS_H

#include "erros.h"
#include "primitive_object.h"
#include "object_actions.h"

/* corpo padrao para todo objeto, caixas de texto, divisoes, etc. */
struct _Object {
	Primitive_object body;
	Actions actions;
};

/* corpo padrao da pagina aonde todos os objetos sao inseridos
 * como a pagina é de rolagem, um dos eixos é omitido
 */
struct _Main_container {
	/* n e lenght sao relativos aos eixos:
	 * x e width, ou y e height
	 * o padding é relativo a: lados esquerdo e direito, e o topo
	 */
	float n, lenght, padding[3];
};

/* cria o objeto completo */
struct _Object* _create_object(float x, float y, float width, float height,
	vector4_t padding, vector4_t border, vector4_t margin ) {
	/* verifica a validade dos argumentos*/
	_verify_valid_argue(padding, "_create_object -> padding");
	_verify_valid_argue(border, "_create_object -> border");
	_verify_valid_argue(margin, "_create_object -> margin");

	/* aloca o objeto */
	struct _Object* self = (struct _Object*)calloc(sizeof(struct _Object), 1);
	/* verifica erros de memória*/
	_verify_memory_error(self, "_create_object -> object");

	vector4_t tmpv4 = _virtualize_vector4(padding);

	*(tmpv4 + 3) = x + *(     padding + 3); // direita
	*tmpv4       = y + *      padding;      // cima
	*(tmpv4 + 1) = width - *( padding + 1) - *(padding + 3); // esquerda
	*(tmpv4 + 2) = height - *(padding + 2) - * padding; // baixo
	
	_delete_vector4(padding);
	padding = tmpv4;

	tmpv4 = _virtualize_vector4(margin);

	*(tmpv4 + 3) = x - *(margin + 3) - *(border + 3); // direita
	*tmpv4 = y - *margin - *border;      // cima
	*(tmpv4 + 1) = width + *(margin + 1) + *(margin + 3) + *(border + 1) + *(border + 3); // esquerda
	*(tmpv4 + 2) = height + *(margin + 2) + *margin + *(border + 2) + *border; // baixo

	_delete_vector4(margin);
	margin = tmpv4;

	tmpv4 = _virtualize_vector4(border);

	*(tmpv4 + 3) = x - *(     border + 3); // direita
	*tmpv4       = y - *      border;      // cima
	*(tmpv4 + 1) = width  + *( border + 1) + *(border + 3); // esquerda
	*(tmpv4 + 2) = height + *(border + 2)  + * border; // baixo

	_delete_vector4(border);
	border = tmpv4;



	/* cria o corpo e os objetos dependentes (actions) do objeto*/
	self->body = _create_primitive_object(x, y, width, height, _virtualize_vector4(padding), _virtualize_vector4(border), _virtualize_vector4(margin));
	self->actions = _create_actions(x, y, width, height, padding, border, margin);

	return self;
}


void _delete_object(struct _Object *self) {
	_delete_actions(self->actions);
	self->actions = NULL;

	_delete_primitive_object(self->body);
	self->body = NULL;

	free(self);
	self = NULL;
}
#endif

