#ifndef PRIMITIVE_OBJECT_H
#define	PRIMITIVE_OBJECT_H

/* cabeçalhos padrão */
#include <stdlib.h> // calloc, free

/* dependencias externas */
#include "erros.h"
#include "vector4.h"

/* objeto primitivo, somente com coordenadas basicas */
typedef struct _Primitive_object {
	float x, y, width, height,
		border[4], margin[4], padding[4];

}*Primitive_object;

/* cria e retorna uma estrutura de objeto primitivo */
Primitive_object _create_primitive_object(float x, float y, float width, float height,
	vector4_t padding, vector4_t border, vector4_t margin) {

	/* verifica a validade dos argumentos que sao alocados no heap*/
	_verify_valid_argue(padding, "_create_primitive_object -> padding");
	_verify_valid_argue(border, "_create_primitive_object -> border");
	_verify_valid_argue(margin, "_create_primitive_object -> margin");

	/* aloca o objeto primitivo */
	Primitive_object self = (Primitive_object) calloc(sizeof(struct _Primitive_object),1);

	/* verifica a alocação de memória */
	_verify_memory_error(self, "_create_primitive_object -> self");

	/* inicia os valoes básicos */
	self->x = x, self->y = y;
	self->width = width, self->height = height;

	/* inicia os valores de vetores*/
	register int i = -1;
	while (++i < 4) {
		*(self->padding + i) = *(padding + i);
		*(self->border + i) = *(border + i);
		*(self->margin + i) = *(margin + i);
	}

	/* deleta os argumentos vetores pois nao sao main necessarios*/
	_delete_vector4(padding);
	_delete_vector4(border);
	_delete_vector4(margin);

	/* retorna o objeto pronto*/
	return self;
}

/* destroi uma estrutura primitiva anteriormente alocada */
#define _delete_primitive_object(self) free(self); self = NULL
#endif

