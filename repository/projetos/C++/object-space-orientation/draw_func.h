#ifndef DRAW_FUNC_H
#define DRAW_FUNC_H

#include <stdio.h>
#include <stdlib.h>

// pausa o programa
#define clock 650000000
#define sleep(s) for (unsigned long long i = 0; i < clock * ((s > ULLONG_MAX) ? ULLONG_MAX : s) / 2; i++);

/*
#define round_floor(n) (int) n
#define round_up(n) (int) (n+0.99)
#define round(n) (n < round_floor(n) + 0.5) ? (int) n : (int) n+1
*/

// especificacoes do buffer desenhavel
#define buffer_colums 200
#define buffer_lines 100

// opcoes pre-definidas de caracteres para preenchimento
#define black4 '@'
#define black3 '&'
#define black2 '%'
#define black1 '$'
#define black0 '#'

#define fill4 '#'
#define fill3 ';'
#define fill2 ':'
#define fill1 '.'
#define fill0 ' '

#define border0 " .."
#define border1 "..:"
#define border2 ":.:"
#define border3 " .:"
#define border4 "*-|"
#define border5 "=-|"
#define border6 "#-|"
#define border7 "+-|"
#define border8 ".-|"
#define border9 " -|"

#define black_border0 "@##"
#define black_border1 "*##"
#define black_border2 "+##"
#define black_border3 " ##"
#define black_border4 "*%%"
#define black_border5 "x%%"
#define black_border6 "=%%"
#define black_border7 "0@@"
#define black_border8 ".@@"
#define black_border9 " @@"

// o buffer para alocar os desenhos
static char buffer[buffer_lines][buffer_colums];

/* desenha o buffer e o limpa */
void flip_buffer(char fill) {

	register int i = -1, e = -1;
	char *pbuffer = *buffer;

	while (++i < buffer_lines) {
		while (++e < buffer_colums) {
			printf("%c", *(pbuffer + i * buffer_colums + e));
			*(pbuffer + i * buffer_colums + e) = fill;
		}
		e = -1;
		printf("\n");
	}

}

/* desenha um retangulo preenchido no buffer */
void draw_filled_rect(int x, int y, int w, int h, char fill) {

	register int i = y - 1, e = x - 1;

	while (++i < buffer_lines && i < y + h) {
		while ((++e < buffer_colums && e < x + w))
			*(*(buffer + i) + e) = fill;
		e = x - 1;
	}

}

/* desenha um retangulo no buffer */
void draw_rect(int x, int y, int w, int h, char fill[3]) {

	register int i = y-1, e = x-1;

	while (++i < buffer_lines && i < y + h) {
		while ((++e < buffer_colums && e < x + w)) {
			if (i == y || i == y + h - 1)
				*(*(buffer + i) + e) = *(fill+1);
			if (e == x || e == x + w - 1)
				*(*(buffer + i) + e) = *(fill + 2);
			if (i == y && e == x || i == y && e == x + w - 1 || i == y + h - 1 && e == x || i == y + h - 1 && e == x + w - 1)
				*(*(buffer + i) + e) = *(fill + 0);
		}
		e = x - 1;
	}


}

void sdraw_rect(int x, int y, int w, int h, char fill) {

	register int i = y - 1, e = x - 1;

	while (++i < buffer_lines && i < y + h) {
		while ((++e < buffer_colums && e < x + w))
			if (i == y || i == y + h - 1 || e == x || e == x + w - 1)
				*(*(buffer + i) + e) = fill;
		e = x - 1;
	}
}

/* inicia o buffer pela primeira vez
 * nao é obrigatorio usar! */
void init_buffer(char fill) {
	register int i = -1, e = -1;
	while (++i < buffer_lines) {
		while (++e < buffer_colums) {
			*(*(buffer + i) + e) = fill;
		}
		e = -1;
	}
}

#endif
