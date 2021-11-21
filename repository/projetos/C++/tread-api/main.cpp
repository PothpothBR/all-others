#include <iostream>
using namespace std;

#include "work_methods.h"

class tstc{
public:
	int x = 10;
	~tstc() {};
}tst;

bool tstf(void* self) {
	RT(tstc, self)->x--;
	return RT(tstc, self)->x;
}

void tstfr(Work* self) {
	RT(tstc, self->object)->x = 1;
}


int main() {

	Workspace* wks = create_workspace(new Workspace_info{11, 22, 33, 44});
	
	cin.get();
	return 0;
}