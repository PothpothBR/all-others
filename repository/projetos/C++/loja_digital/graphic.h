#ifndef GRAPHIC_STARTUP_H
#define GRAPHIC_STARTUP_H

#include <allegro5/allegro.h>
#include <allegro5/allegro_native_dialog.h>
#include <allegro5/allegro_primitives.h>
#include <allegro5/allegro_ttf.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_color.h>
#include <allegro5/allegro_image.h>

#include "file_list.h"

class Allegro_routines {
public:
	int display_size[2] = { 0, 0 };
	int fps = 0;
	bool runing = true;

	ALLEGRO_DISPLAY* display = nullptr;

	ALLEGRO_EVENT evnt;
	ALLEGRO_EVENT_QUEUE* event_queue = nullptr;
	ALLEGRO_EVENT mouse_evnt;
	ALLEGRO_EVENT_QUEUE* mouse_event_queue = nullptr;

	ALLEGRO_TIMER* timer = nullptr;

	ALLEGRO_BITMAP** image = nullptr;
	char** image_id = nullptr;
	unsigned int image_lenght = 0;

	ALLEGRO_FONT** font = nullptr;
	char** font_id = nullptr;
	unsigned int font_lenght = 0;

	Allegro_routines(int display_x, int display_y, double fps,
		File_list* image_file_list = nullptr, Font_list* font_file_list = nullptr);

	~Allegro_routines() {
		al_destroy_display(display);
		al_destroy_event_queue(event_queue);
		al_destroy_event_queue(mouse_event_queue);
		al_destroy_timer(timer);

		
		for (register unsigned int i = 0; i < image_lenght; i++) {
			cout << " deleting file..: " << image_id[i] << endl;
			al_destroy_bitmap(image[i]);
			free(image_id[i]);
		}
		
		for (register unsigned int i = 0; i < font_lenght; i++) {
			cout << " deleting file..: " << font_id[i] << endl;
			al_destroy_font(font[i]);
			free(font_id[i]);
		}

		free(font_id);
		free(image_id);
	}

	bool _flip();
	bool _timed();
	void _add_images(File_list* file_list);
	void _add_fonts(Font_list* file_list);

	};

#endif // !GRAPHIC_STARTUP_H
