#ifndef GRAPHIC_CONSTRUCTOR_H
#define GRAPHIC_CONSTRUCTOR_H

#include "graphic.h"

Allegro_routines::Allegro_routines(int display_x, int display_y, double fps, File_list* image_file_list, Font_list* font_file_list) {

	display_size[0] = display_x;
	display_size[1] = display_y;

	this->fps = fps;

	if (!al_init()) {
		al_show_native_message_box(display, "Erro", "", "Falha ao iniciar recurso -> al_init()", "", 2); exit(-1);
	}
	if (!al_init_font_addon()) {
		al_show_native_message_box(display, "Erro", "", "Falha ao iniciar recurso -> al_init_font_addon()", "", 2); exit(-1);
	}
	if (!al_init_image_addon()) {
		al_show_native_message_box(display, "Erro", "", "Falha ao iniciar recurso -> al_init_image_addon()", "", 2); exit(-1);
	}
	if (!al_init_primitives_addon()) {
		al_show_native_message_box(display, "Erro", "", "Falha ao iniciar recurso -> al_init_primitives_addon()", "", 2); exit(-1);
	}
	if (!al_init_ttf_addon()) {
		al_show_native_message_box(display, "Erro", "", "Falha ao iniciar recurso -> al_init_ttf_addon()", "", 2); exit(-1);
	}

	if (image_file_list) _add_images(image_file_list);
	if (font_file_list) _add_fonts(font_file_list);

	display = al_create_display(display_x, display_y);

	timer = al_create_timer(1 / fps);

	if (!al_install_keyboard()) {
		al_show_native_message_box(display, "Erro", "", "Falha ao iniciar recurso -> al_install_keyboard()", "", 2); exit(-1);
	}
	if (!al_install_mouse()) {
		al_show_native_message_box(display, "Erro", "", "Falha ao iniciar recurso -> al_install_mouse()", "", 2); exit(-1);
	}

	event_queue = al_create_event_queue();
	mouse_event_queue = al_create_event_queue();

	al_register_event_source(event_queue, al_get_keyboard_event_source());
	al_register_event_source(event_queue, al_get_display_event_source(display));
	al_register_event_source(event_queue, al_get_timer_event_source(timer));
	al_register_event_source(mouse_event_queue, al_get_mouse_event_source());

	al_start_timer(timer);
}

#endif // !GRAPHIC_CONSTRUCTOR_H