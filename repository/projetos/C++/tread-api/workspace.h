#ifndef WORKSPACE_H_INCLUDED
#define WORKSPACE_H_INCLUDED

#include "workflow.h"

// sort the works by type
class Workspace {
public:
	// dynamic pointer vector
	Workflow** workflow = nullptr;
	uint size = 0;

	// free all the workflows
	~Workspace() {
		if (!workflow) cout << "<~Workspace> deallocate null pointer.\n\n";
		free(workflow);
	}
};

#endif // !WORKSPACE_H_INCLUDED

