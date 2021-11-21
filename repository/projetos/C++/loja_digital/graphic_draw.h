#ifndef GRAPHIC_DRAW_H
#define GRAPHIC_DRAW_H

#include "graphic_constructor.h"
#include "graphic_methods.h"
#include "draw_manager.h"

void drawBox(Box* self);
void drawAllBox(DrawManager* self);

void drawBox(Box* self) {

	// borda de cima
	if (self->style->borderSize[0]) al_draw_line(self->x, self->y - self->style->borderSize[0] / 2, self->x + self->w, self->y - self->style->borderSize[0] / 2, al_map_rgb(self->style->borderColor[0], self->style->borderColor[1], self->style->borderColor[2]), self->style->borderSize[0]);

	// borda da esquerda
	if (self->style->borderSize[1]) al_draw_line(self->x + self->w + self->style->borderSize[1] / 2, self->y - self->style->borderSize[0], self->x + self->w + self->style->borderSize[1] / 2, self->y + self->h + self->style->borderSize[2], al_map_rgb(self->style->borderColor[0], self->style->borderColor[1], self->style->borderColor[2]), self->style->borderSize[1]);

	// borda de baixo
	if (self->style->borderSize[2]) al_draw_line(self->x, self->y + self->h + self->style->borderSize[2] / 2, self->x + self->w, self->y + self->h + self->style->borderSize[2] / 2, al_map_rgb(self->style->borderColor[0], self->style->borderColor[1], self->style->borderColor[2]), self->style->borderSize[2]);

	// borda da esquerda
	if (self->style->borderSize[3]) al_draw_line(self->x - self->style->borderSize[3] / 2, self->y - self->style->borderSize[0], self->x - self->style->borderSize[3] / 2, self->y + self->h + self->style->borderSize[2], al_map_rgb(self->style->borderColor[0], self->style->borderColor[1], self->style->borderColor[2]), self->style->borderSize[3]);

	// background
	al_draw_filled_rectangle(self->x, self->y, self->x + self->w, self->y + self->h,
		al_map_rgb(self->style->backgroundColor[0], self->style->backgroundColor[1], self->style->backgroundColor[2]));
}

void drawAllBox(DrawManager* self) {

	for (Box* ptr = self->boxHeader; ptr; ptr = ptr->next) drawBox(ptr);
}

#endif // GRAPHIC_DRAW_H