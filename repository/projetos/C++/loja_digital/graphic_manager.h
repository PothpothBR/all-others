#ifndef GRAPHIC_MANAGER_H
#define GRAPHIC_MANAGER_H

#include "graphic_draw.h"

// sobrepos
//#define overlap(x, y, w, h, xx, yy, ww, hh) (x < xx + ww && x + w > xx + ww && y < yy + hh && y + h > yy);

// transbordou
//#define overflow(x, y, w, h, xx, yy, ww, hh) (x < xx || x + w > xx + ww || y < yy || y + h > yy + hh); 

class GraphicManager : Allegro_routines, DrawManager{

	File_list* images;
	Font_list* fonts;

	StyleManager styleManager;

	int _invertSide(int side) {

		switch (side) {
		case 0:
			return 2;
			break;
		case 1:
			return 3;
			break;
		case 2:
			return 0;
			break;
		case 3:
			return 1;
			break;
		default:
			cout << " [erro] <_invertSide()> lazarento, coloco o lado maior que 3 ou menor que 0? tu é burro arume ja isso!\n";
		}
	}

	//testa se self1 soberpos self2
	bool _overlap(Box* self1, Box* self2) {

		return (self1->x < self2->x + self2->w && self1->x + self1->w > self2->x + self2->w &&
			self1->y < self2->y + self2->h && self1->y + self1->h > self2->y);
	}

	// testa se self1 saiu fora de self2
	bool _overflow(Box* self1, Box* self2) {

		return (self1->x < self2->x || self1->x + self1->w > self2->x + self2->w ||
			self1->y < self2->y || self1->y + self1->h > self2->y + self2->h);
	}

	// retorna o espaco em branco entre a caixa e sua caixa pai
	int _getMasterSpace(Box* self, int position) {

		return self->style->borderSize[position] + self->style->margin[position] + self->master->style->padding[_invertSide(position)];
	}

	// retorna o espaco em branco entre uma caixa e outra
	int _getSideSpace(Box* self, Box* side, int position) {
		
		int space = self->style->borderSize[position] + self->style->margin[position];
		position = _invertSide(position);
		
		return space + side->style->borderSize[position] + side->style->margin[position];
	}

	// return a espaco em branco que uma caixa usa
	int _getSideSpace(Box* self, int position) {

	}


	void rankBoxes() {

		for (Box* ptr = boxHeader; ptr; ptr = ptr->next) {

			if (!ptr->inherit) continue;

			ptr->inherit[0]->x = ptr->x + _getMasterSpace(ptr->inherit[0], 3);
			ptr->inherit[0]->y = ptr->y + _getMasterSpace(ptr->inherit[0], 0);

			// inserção lado-a-lado, empilhados
			for (register unsigned int i = 1; i < ptr->inheritlenght; i++) {
				Box* self = ptr->inherit[i];
				Box* after = ptr->inherit[i - 1];

				self->x = after->x + after->w + _getSideSpace(self, ptr->inherit[i - 1], 3);

				if (_overflow(self, ptr)) {
					self->x = ptr->x + _getMasterSpace(self, 3);
					self->y = after->y + after->h + _getSideSpace(self, after, 0);
				}
				else
					self->y = after->y ;

			}
		}

	}

public:
	GraphicManager(int dx, int dy, double fps, File_list* images = nullptr, Font_list* fonts = nullptr) :
		DrawManager(dx, dy), Allegro_routines(dx, dy, fps, images, fonts) {
		
		this->images = new File_list;
		this->fonts = new Font_list;
	};

	void loadImages(const char* file, const char* id) {
		images->add(file, id);
	}

	void loadFonts(const char* font, const char* id, unsigned int size, int flags) {
		fonts->add_font(font, id, size, flags);
	}

	void upData() {

		if (fonts->lenght) { 
			_add_fonts(fonts);
			delete fonts; 
			fonts = new Font_list; 
		}
		if (images->lenght) {
			_add_images(images); 
			delete images; 
			images = new File_list;
		}
	}

	bool flip() {

		drawAllBox(this);

		return _flip();
	}

	bool timed() {

		if (_timed()) {
			rankBoxes();
		}

		return _timed();
	}

	void addBox(const char* id, const char* masterId, const char* style, float width, float height) {
		Box* add = new Box(id, _getBoxById(masterId), _getStyleById(style), 0, 0, width, height);

		_addBox(add);
		_getBoxById(masterId)->addInheritBox(add);
	}

	void addStyle(const char* id, int borderColor[3], int backgroundColor[3], int fontColor[3],
		const char* fontType, int fontSize, float borderSize[4], float padding[4], float margin[4]) {

		_addStyle(new Style(id, borderColor, backgroundColor, fontColor,
			fontType, fontSize, borderSize, padding, margin));
	}

	StyleManager& style(const char* id) {

		styleManager.setStyle(_getStyleById(id));

		return styleManager;
	}

	~GraphicManager(){
		delete fonts;
		delete images;
	}
};

#endif // GRAPHIC_MANAGER_H