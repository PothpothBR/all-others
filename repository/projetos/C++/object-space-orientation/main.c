#include <stdio.h>
#include <stdlib.h>
#include "group_header.h"

void flip(double fps);



void main(void) {

	init_buffer(' ');

	for (;;) {

		draw_rect(20, 20, 8, 8, border5);

		flip(0.025);
		break;
	}
	
	//getchar();
}
 
void flip(double fps) {
	system("cls");
	flip_buffer(fill0);
	sleep(fps);
}

