#ifndef FILE_LIST_H
#define FILE_LIST_H

#include "alloc_functions.h"

class File_list {
public:

	char** files = nullptr;
	char** ids = nullptr;
	unsigned int lenght = 0;

	void add(const char* file, const char* id) {
		alloc_str_vector(&files, lenght, file);
		alloc_str_vector(&this->ids, lenght, id);
		lenght++;
	}

	~File_list() {
		if (files) {
			for (register unsigned int i = 0; i < lenght; i++) free(files[i]);
			free(files);
		}
		/*if (ids) {
			for (register unsigned int i = 0; i < lenght; i++) free(ids[i]);
			free(ids);
		}*/
	}
};

class Font_list : public File_list {
public:
	unsigned int* sizes = nullptr;
	int* flags = nullptr;

	void add_font(const char* font, const char* id, unsigned int size, int flags) {

		alloc_vector<unsigned int>(&this->sizes, lenght, size);
		alloc_vector<int>(&this->flags, lenght, flags);
		add(font, id);
	}

	~Font_list() {
		if (sizes) {
			free(sizes);
		}
		if (flags) {
			free(flags);
		}
	}
};

#endif // !FILE_LIST_H
