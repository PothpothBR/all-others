#ifndef WORK_RELS_H_INCLUDED
#define WORK_RELS_H_INCLUDED

/*
* A classe <work> representa o processo a ser desempenhado
* a variavel <object> armazena todas as informações referentes ao processo
* o vetor <moder> armazena os modificadores quais irão manipular as informações
*
* estruturação
*
* object -> class(only one class pointer)
* moder  -> manipulate function(first position containing the function pointer and receiving the class pointer as parameter)
* releaser -> deleting function(one use in deleting object, reciving the himself work pointer as parameter)
*
* add_job() -> create an work and insert in queue
*
* work() -> work all the jobs and return to program control
*        +> cycles through all jobs and runs the destructor for the work function that returns 0, if it exists.
*/

#include <iostream>
using namespace std;

// cuting the types
typedef unsigned int uint;

// re-type the void pointer to use
#define RT(type, ptr) ((type*) ptr)

#endif // !WORK_RELS_H_INCLUDED