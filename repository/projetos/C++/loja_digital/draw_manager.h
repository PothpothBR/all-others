#ifndef DRAW_MANAGER_H
#define DRAW_MANAGER_H

#include "vector.h"

class Style {
public:

	Style* next = nullptr;

	char* id = nullptr;

	int *borderColor = nullptr;
	float *borderSize = nullptr;
	float* padding = nullptr;
	float* margin = nullptr;

	int *backgroundColor = nullptr;

	int *fontColor = nullptr;
	char* fontType = nullptr;
	int fontSize = 18;

	Style(const char* id, int borderColor[3], int backgroundColor[3], int fontColor[3],
		const char* fontType, int fontSize, float borderSize[4], float padding[4], float margin[4]) {

		this->id = new char[strlen(id)+1];
		strcpy(this->id, id);

		this->borderColor = borderColor;
		this->backgroundColor = backgroundColor;

		this->fontType = new char[strlen(fontType)+1];
		strcpy(this->fontType, fontType);

		this->fontColor = fontColor;
		this->fontSize = fontSize;

		this->borderSize = borderSize;
		this->padding = padding;
		this->margin = margin;

		cout << " style: " << this->id << endl;
	}

	~Style() {
		cout << " deleting style: " << this->id << endl;
		free(borderColor);
		free(backgroundColor);
		free(fontColor);

		free(padding);
		free(margin);
		free(borderSize);

		delete id;
		delete fontType;
	}
};

class Box {
public:

	Box* next = nullptr;

	Box* master = nullptr;
	Box** inherit = nullptr;

	unsigned int inheritlenght = 0;

	float x = 0, y = 0, w = 0, h = 0,
		*p = nullptr, *m = nullptr, *b = nullptr;

	char* id = nullptr;
	Style* style = nullptr;

	Box(){}

	Box(const char* id, Box* master, Style* style, float x, float y, float width, float height) {

		this->x = x;
		this->y = y;
		w = width;
		h = height;
		p = style->padding;
		m = style->margin;
		b = style->borderSize;
		this->style = style;

		this->master = master;

		this->id = new char[strlen(id) + 1];
		strcpy(this->id, id);

		cout << " box..: " << this->id << endl;
	}

	void addInheritBox(Box* self) {

		Box** verify = (Box**) realloc(inherit, sizeof(Box*) * ++inheritlenght);
		if (!verify) alloc_memory_error();

		verify[inheritlenght - 1] = self;
		inherit = verify;
	}

	~Box(){
		cout << " deleting box..: " << this->id << endl;
		delete id;
	}
};


class StyleManager {
	Style* style = nullptr;
public:
	StyleManager(Style* style = nullptr) {
		this->style = style;
	}

	void setStyle(Style* style) {
		this->style = style;
	}

	void fontColor(int r, int g, int b) {

		style->fontColor[0] = r;
		style->fontColor[1] = g;
		style->fontColor[2] = b;
	}

	void fontColor(int rgb) {

		style->fontColor[0] = rgb;
		style->fontColor[1] = rgb;
		style->fontColor[2] = rgb;
	}

	void fontSize(unsigned int size) {
		style->fontSize = size;
	}

	void fontType(const char* name) {

		delete style->fontType;

		style->fontType = new char[strlen(name) + 1];
		strcpy(style->fontType, name);
	}

	void id(const char* id) {

		delete style->id;

		style->id = new char[strlen(id)];
		strcpy(style->id, id);
	}

	void background(int r, int g, int b) {

		style->backgroundColor[0] = r;
		style->backgroundColor[1] = g;
		style->backgroundColor[2] = b;
	}

	void background(int rgb) {

		style->backgroundColor[0] = rgb;
		style->backgroundColor[1] = rgb;
		style->backgroundColor[2] = rgb;
	}

	void borderColor(int r, int g, int b) {

		style->borderColor[0] = r;
		style->borderColor[1] = g;
		style->borderColor[2] = b;
	}

	void borderColor(int rgb) {

		style->borderColor[0] = rgb;
		style->borderColor[1] = rgb;
		style->borderColor[2] = rgb;
	}

	void borderSize(float up, float left, float down, float right) {

		style->borderSize[0] = up;
		style->borderSize[1] = left;
		style->borderSize[2] = down;
		style->borderSize[3] = right;
	}

	void borderSize(float horizontal, float vertical) {

		style->borderSize[0] = vertical;
		style->borderSize[1] = horizontal;
		style->borderSize[2] = vertical;
		style->borderSize[3] = horizontal;
	}

	void borderSize(float size) {
		style->borderSize[0] = size;
		style->borderSize[1] = size;
		style->borderSize[2] = size;
		style->borderSize[3] = size;
	}

	void padding(float up, float left, float down, float right) {

		style->padding[0] = up;
		style->padding[1] = left;
		style->padding[2] = down;
		style->padding[3] = right;
	}

	void padding(float horizontal, float vertical) {

		style->padding[0] = vertical;
		style->padding[1] = horizontal;
		style->padding[2] = vertical;
		style->padding[3] = horizontal;
	}

	void padding(float size) {
		style->padding[0] = size;
		style->padding[1] = size;
		style->padding[2] = size;
		style->padding[3] = size;
	}

	void margin(float up, float left, float down, float right) {

		style->margin[0] = up;
		style->margin[1] = left;
		style->margin[2] = down;
		style->margin[3] = right;
	}

	void margin(float horizontal, float vertical) {

		style->margin[0] = vertical;
		style->margin[1] = horizontal;
		style->margin[2] = vertical;
		style->margin[3] = horizontal;
	}

	void margin(float size) {
		style->margin[0] = size;
		style->margin[1] = size;
		style->margin[2] = size;
		style->margin[3] = size;
	}
};


class Body {
public:

	Box* box = nullptr;
	Style* style = nullptr;

	Body(Style* style, float width, float height) {

		box = new Box("body", nullptr, style, 0, 0, width, height);
		this->style = style;
		
	}

	~Body() {
		delete box; // talves isso se torne um erro
	}
};

class DrawManager {
public:
	Body* body = nullptr;
	Style* globalStyle = nullptr;

	Box* boxHeader = nullptr;
	Box* boxAnchor = nullptr;

	Style* styleHeader = nullptr;
	Style* styleAnchor = nullptr;

	DrawManager(float width, float height) {
		
		globalStyle = new Style("*", vector3(0), vector3(25), vector3(255), "ArialBlack", 24, vector4<float>(0), vector4<float>(5), vector4<float>(0));
		body = new Body(globalStyle, width, height);

		styleHeader = globalStyle;
		boxHeader = body->box;

		styleAnchor = globalStyle;
		boxAnchor = body->box;
	}

	~DrawManager() {

		for (Style* ptr = styleHeader, *del = styleHeader; ptr; ptr = ptr->next, delete del, del = ptr);
		for (Box* ptr = boxHeader, *del = boxHeader; ptr; ptr = ptr->next, delete del, del = ptr);
	}

	void _addStyle(Style* self) {

		styleAnchor->next = self;
		styleAnchor = self;
	}

	void _addBox(Box* self) {

		boxAnchor->next = self;
		boxAnchor = self;
	}

	Style* _getStyleById(const char* id) {

		for (Style* ptr = styleHeader; ptr; ptr = ptr->next) 
			if (!strcmp(ptr->id, id)) return ptr;

		return nullptr;
	}

	Box* _getBoxById(const char* id) {

		for (Box* ptr = boxHeader; ptr; ptr = ptr->next)
			if (!strcmp(ptr->id, id)) return ptr;

		return nullptr;
	}

	Box* _getBoxByInheritId(const char* id) { // nao testado!!!!!!!!!!!

		for (Box* ptr = boxHeader; ptr; ptr = ptr->next)
			for (register unsigned int i = 0; i < ptr->inheritlenght; i++)
				if (!strcmp(ptr->inherit[i]->id, id)) return ptr;

		return nullptr;
	}
};


#endif // !DRAW_MANAGER_H