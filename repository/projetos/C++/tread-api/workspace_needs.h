#ifndef WORKSPACE_INFO_H_INCLUDED
#define WORKSPACE_INFO_H_INCLUDED

#include "workspace.h"

class Workspace_info {
public:
	int* id_list = nullptr;
	uint initial_size = 0;

	Workspace_info(initializer_list<int> id_list) {
		initial_size = id_list.size();
		this->id_list = new int[initial_size];
		initializer_list<int>::iterator i;
		int e = 0;
		for (i = id_list.begin(); i != id_list.end(); i++, e++) {
			this->id_list[e] = (int)*i;
		}
	}
};

class Work_master {
public:
	bool flow = true;
	Workspace* workspace = nullptr;
};

#endif // !WORKSPACE_INFO_H_INCLUDED
