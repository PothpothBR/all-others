#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
using namespace std;

#include "graphic_manager.h"

int main() {
	GraphicManager gfc(1080, 720, 40);

	gfc.loadImages("pictures/pc1.jpg", "pc1");
	gfc.loadImages("pictures/pc2.jpg", "pc2");
	gfc.loadImages("pictures/pc3.jpg", "pc3");
	gfc.loadImages("pictures/pc4.jpg", "pc4");
	gfc.loadImages("pictures/pc5.jpg", "pc5");
	gfc.loadImages("pictures/pc6.jpg", "pc6");
	gfc.loadImages("pictures/pc7.jpg", "pc7");
	gfc.loadImages("pictures/pc8.jpg", "pc8");

	gfc.loadFonts("fonts/arial-black.ttf", "ArialBlack", 24, 0);
	gfc.loadFonts("fonts/GeosansLight.ttf", "GeosansLight", 24, 0);
	gfc.loadFonts("fonts/GeosansLight-Oblique.ttf", "GeosansLight-Oblique", 24, 0);

	gfc.upData();

	gfc.style("*").fontColor(210, 220, 228);
	gfc.style("*").background(40, 46, 48);
	gfc.style("*").padding(5);

	gfc.addStyle("header", vector3(210, 220, 228), vector3(40, 46, 48), vector3(210, 220, 228), "GeosansLight", 24, vector4<float>(0,0,2,0), vector4<float>(5), vector4<float>(10));
	gfc.addStyle("menu-item", vector3(210, 220, 228), vector3(60, 66,68), vector3(210, 220, 228), "GeosansLight", 24, vector4<float>(0,0,0,0), vector4<float>(0), vector4<float>(5));

	gfc.addBox("header", "body", "header", 1080 - 10 - 20 - 5, 64*2);

	gfc.addBox("inicio", "header", "menu-item", 64, 64);
	gfc.addBox("agenda", "header", "menu-item", 64, 64);
	gfc.addBox("financeiro", "header", "menu-item", 64, 64);
	gfc.addBox("pedido", "header", "menu-item", 64, 64);
	gfc.addBox("emissão", "header", "menu-item", 64, 64);
	gfc.addBox("cliente", "header", "menu-item", 64, 64);
	gfc.addBox("produtos", "header", "menu-item", 64, 64);
	gfc.addBox("usuario", "header", "menu-item", 64, 64);
	gfc.addBox("configurações", "header", "menu-item", 64, 64);
	

	while (gfc.flip()) if (gfc.timed());



	return 0;
}

