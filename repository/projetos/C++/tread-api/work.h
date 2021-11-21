#ifndef WORK_H_INCLUDED
#define WORK_H_INCLUDED

#include "work_needs.h"

// work class definition
// the releaser pointer not is required, only use to finish the work use or reference in other jobs 
class Work {
public:
	// next chain work
	Work* before = nullptr;
	Work* next = nullptr;

	// work data
	int id = 0;
	void* object = nullptr;
	bool (*moder)(void*) = nullptr;
	void (*releaser)(Work*) = nullptr;
};

#endif // !WORK_H_INCLUDED
