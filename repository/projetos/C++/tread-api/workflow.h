#ifndef WORKFLOW_H_INCLUDED
#define WORKFLOW_H_INCLUDED

#include "work.h"

// the work flow class, all works have here
class Workflow {
public:
	// work chained queue
	Work* header = nullptr;
	Work* footer = nullptr;
	uint size = 0;

	// workflow data
	int id = 0;

	// free al the works
	~Workflow() {
		for (Work* ptr = header; header;) {
			header = header->next;
			delete ptr;
			ptr = header;
			size--;
		}
		if (size) cout << "<~Workflow> number of works free is different from real queue size.\n\n";
	}
};


#endif // !WORKFLOW_H_INCLUDED
