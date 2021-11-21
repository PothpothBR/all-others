#include <iostream> // para debug - remover quando finalizado
#include <cstdlib>
using namespace std;

#include "graphic.h"

#include "lomeb.h"

//arquivo de cabecalho para coleta de letras
#include "C:/Users//bd88//Google Drive/backup lomeo(old moblib)/lastest/timing.h"

/*
	erros:
		nenhum bb


*/




// desenha uma classe do tipo Box ..**borda nao implementada**..
void draw_box_debug(Box* box_name) {
	
	// margem
	al_draw_filled_rectangle(box_name->X(), box_name->Y(), box_name->x() + box_name->width(), box_name->y(), al_map_rgb(220, 80, 80));
	al_draw_filled_rectangle(box_name->X(), box_name->Y(), box_name->x(), box_name->y() + box_name->height(), al_map_rgb(220, 80, 80));
	al_draw_filled_rectangle(box_name->x() + box_name->width(), box_name->Y(), box_name->X() + box_name->WIDTH(), box_name->y() + box_name->height(), al_map_rgb(220, 80, 80));
	al_draw_filled_rectangle(box_name->X(), box_name->y() + box_name->height(), box_name->X() + box_name->WIDTH(), box_name->Y() + box_name->HEIGHT(), al_map_rgb(220, 80, 80));

	// espacamento interno
	al_draw_filled_rectangle(box_name->x(), box_name->y(), box_name->x() + box_name->width(), box_name->y() + box_name->_padding[box_name->up], al_map_rgb(80, 220, 80));
	al_draw_filled_rectangle(box_name->x(), box_name->y(), box_name->x() + box_name->_padding[box_name->left], box_name->y() + box_name->height(), al_map_rgb(80, 220, 80));
	al_draw_filled_rectangle(box_name->x() + box_name->width(), box_name->y(), box_name->x() + box_name->width() - box_name->_padding[box_name->right], box_name->y() + box_name->height(), al_map_rgb(80, 220, 80));
	al_draw_filled_rectangle(box_name->x() , box_name->y() + box_name->height(), box_name->x() + box_name->width() , box_name->y() + box_name->height() - box_name->_padding[box_name->down], al_map_rgb(80, 220, 80));
	
}

void draw_box(Box* box_name) {

	al_draw_rectangle(box_name->x(),
		box_name->y(),
		box_name->x() + box_name->width(),
		box_name->y() + box_name->height(),
		al_map_rgb(0, 0, 0), 1);
}

void draw_box_global(Box* box_name) {
	for (int i = 0; i < box_name->_global_size; i++) {
		box_name = box_name->_global[i];
		al_draw_rectangle(box_name->x(),
			box_name->y(),
			box_name->x() + box_name->width(),
			box_name->y() + box_name->height(),
			al_map_rgb(0, 0, 0), 1);
	}
}


int main() {
	
	Box body(1040, 680);
	body.inherit();
	body.margin(20);

	Box div(400, body.height());
	div.inherit(&body);

	Box button(45, 45);
	button.inherit(&div);

	Box subdiv(div.width() - 45, 45);
	subdiv.inherit(&div);

	Box ficha(div.width() - 40, 120);
	ficha.inherit(&div);
	ficha.margin(20);

	cout << box._global_size;

	while (graphic.flip()) {

		if (graphic.timed()) {
			
			if (colid_out(graphic.mouse_x(), graphic.mouse_y(), 1, 1, subdiv.x(), subdiv.y(), subdiv.x() + subdiv.width() - 20, subdiv.height())) {
				
				writebox.write(graphic.keyboard_input(), graphic.keyboard_press());
				
			}

		}

		draw_box_global(&box);

		al_draw_text(graphic.text, al_map_rgb(250, 250, 250), subdiv._x + 10, subdiv.y()*1.5 + 2.5, NULL, writebox.buffer);
		
	}

	return 0;
}