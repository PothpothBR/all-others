#include <stdio.h>
#include "group_header.h"

void flip();
void draw_object(Object self);


void main(void) {

	Object ac = create_object(15, 15, 12, 14, vector4(4, 4, 4, 4), vector4(4,2,2,2), vector4(10, 10, 10, 10));

	init_buffer(' ');

	for (;;) {

		draw_object(ac);

		flip();
	}

	delete_object(ac);

	printf("\n");
	system("pause");
}

void draw_object(Object self) {
	/*objeto interno*/
	draw_rect(self->body->padding[RIGHT], self->body->padding[UP], self->body->padding[LEFT], self->body->padding[DOWN], border1);
	draw_rect(self->body->margin[RIGHT], self->body->margin[UP], self->body->margin[LEFT], self->body->margin[DOWN], border1);
	draw_rect(self->body->border[RIGHT], self->body->border[UP], self->body->border[LEFT], self->body->border[DOWN], border1);
	draw_rect(self->body->x, self->body->y, self->body->width, self->body->height, black_border7);

}

void flip() {
	system("cls");
	flip_buffer(fill0);
	//system("pause");
	//sleep(fps);
}