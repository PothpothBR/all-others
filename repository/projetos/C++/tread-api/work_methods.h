#ifndef WORK_METHOS_H_INCLUDED
#define WORK_METHOS_H_INCLUDED

#include "workspace_needs.h"

// create an work using only parameters and insert in the queue
void add_work(Workflow* self, int id, void* object, bool (*manipulator)(void*), void (*releaser)(Work*)) {
	// error test
	if (!self || !object || !manipulator) cout << "<add_job> null pointer as obrigatory parameter.\n\n";

	// create the work
	Work* tmp = new Work();
	tmp->id = id;
	tmp->object = object;
	tmp->moder = manipulator;
	tmp->releaser = releaser;

	// insert in queue
	self->header->before = tmp;
	tmp->next = self->header;
	self->header = tmp;

	// update the queue size counter
	self->size++;
}

// the function moder of footer work
// only return if the programs stop or none
static bool work_loop(void* self) {
	return RT(Work_master, self)->flow;
}

void work_start(Workflow* self) {
	for (Work* ptr = self->header; ptr; ptr = ptr->next) {

		// verify 0 return to work moder function
		if (!(*ptr->moder)(ptr->object)) {

			// if releaser existis run this
			if (ptr->releaser) ptr->releaser(ptr);
		}
	}
} 

Workflow* create_workflow(int id) {
	Workflow* self = new Workflow;

	self->header = new Work;
	self->header->object = new Work_master;
	self->header->moder = &work_loop;
	self->footer = self->header;
	self->size = 1;
	self->id = id;

	return self;
}

// creates a workspace with a pre-loaded size of workflows
Workspace* create_workspace(Workspace_info* info) {
	if (!info) cout << "<create_workspace> null pointer at parameter.\n\n";
	Workspace* self = new Workspace;

	self->workflow = (Workflow**)calloc(sizeof(Workflow), info->initial_size);
	if (!self->workflow) cout << "<create_workspace> error to alloc resources.\n\n";

	self->size = info->initial_size;

	for (register uint i = 0; i < info->initial_size; i++) {
		self->workflow[i] = create_workflow(info->id_list[i]);
	}
	delete info;
	return self;
}

#endif // !WORK_METHOS_H_INCLUDED
