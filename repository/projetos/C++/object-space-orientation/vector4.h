#ifndef VECTOR4_H
#define VECTOR4_H

/* cabeçalhos padrão*/
#include <stdlib.h>  // calloc, free

/* dependências externas */
#include "erros.h"

/*tipo intrinseco vector4 */
typedef float* vector4_t;

/* aloca e retorna um vetor de 4 posicoes */
vector4_t _create_vector4(float n1, float n2, float n3, float n4) {

	/* aloca o vetor */
	vector4_t vector = (vector4_t)calloc(sizeof(int), 4);
	/* verifica erro de memória */
	_verify_memory_error(vector, "_create_vector4 -> vector");

	/* atribui os valores ao vetor */
	*vector       = n1;
	*(vector + 1) = n2;
	*(vector + 2) = n3;
	*(vector + 3) = n4;

	/* retorna o vetor */
	return vector;
}

/* aloca e retorna uma copia do vetor*/
vector4_t _virtualize_vector4(vector4_t vector) {
	/* verifica a validade do argumento */
	_verify_valid_argue(vector, "_virtualize_vector4 -> vector");

	/* retorna um novo vetor com os mesmos valores*/
	return _create_vector4(*vector, *(vector + 1), *(vector + 2), *(vector + 3));
}

/* desaloca o vetor */
#define _delete_vector4(vector) free(vector); vector = NULL

#endif