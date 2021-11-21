#ifndef GROUP_HEADER_H
#define GROUP_HEADER_H

/* aqui vao todas as funcoes e classes de acceso ao usuario
 * tudo o que nao é de manuseio do usuario nao esta definido aqui
 * e sim é definido em seu local de origem
 */

#include <stdio.h>
#include <stdlib.h>

#include "vector4.h"
#include "draw_func.h"
#include "objects.h"

#define UP 0
#define LEFT 1
#define DOWN 2
#define RIGHT 3

/* objeto especifico para o corpo principal*/
typedef struct _Main_container* Main_container;

/* objeto completo*/
typedef struct _Object* Object;

/* inicia a estrutura object*/
#define create_object(x, y, width, height, vector4_padding, vector4_border, vector4_margin) \
	_create_object(x, y, width, height, vector4_padding, vector4_border, vector4_margin)

/* libera a memoria referente ao objeto e a todos os seus dependentes*/
#define delete_object(self) _delete_object(self)

/* argumento de funcao que requer um vetor de 4 posicoes */
#define vector4(top, left, bottom, right) _create_vector4(top, left, bottom, right)

/* cria um vetor virtual(cópia) e retorna-o*/
#define virtual_vector4(vector4) _virtualize_vector4(vector4);

/* se usado externamente essa funcao deve ser usada para liberar a memoria do vector4 */
#define delete_vector4(vector4) _delete_vector4(vector4)

/* desenha e limpa o buffer */
void flip_buffer(char fill);

/* desenha um retangulo */
void draw_rect(int x, int y, int w, int h, char fill[3]);

/* desenha um retangulo simples */
void sdraw_rect(int x, int y, int w, int h, char fill);

/* desenha um retangulo preenchido */
void draw_filled_rect(int x, int y, int w, int h, char fill);

/* inicia o buffer */
void init_buffer(char fill);

#endif