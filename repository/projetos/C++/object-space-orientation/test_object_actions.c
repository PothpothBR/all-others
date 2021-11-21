#include <stdio.h>
#include "group_header.h"


void main(void) {

	Object ac = create_object(35, 35, 35, 35, vector4(2, 2, 2, 2), vector4(1, 1, 1, 1), vector4(10, 10, 10, 10));
	
	printf("        x : %.f\n", ac->body->x);
	printf("        y : %.f\n", ac->body->y);
	printf("    width : %.f\n", ac->body->width);
	printf("   height : %.f\n", ac->body->height);
	for (int i = 0; i < 4; i++) {
		printf(" %d margin : %.f  ", i, ac->body->margin[i] );
		printf("padding : %.f  ", ac->body->padding[i]);
		printf(" border : %.f\n", ac->body->border[i] );
	}

	delete_object(ac);
	
	printf("\n");
	system("pause");
}