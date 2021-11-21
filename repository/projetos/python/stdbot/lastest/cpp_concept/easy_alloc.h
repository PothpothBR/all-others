#ifndef EASY_ALLOC_H
#define EASY_ALLOC_H

#include "global_definitions.h"
#include <string.h>

char* easy_alloc_string(const char* string){

    char* temporary = calloc(sizeof(char), lenght);

    if (temporary){
        message(-1, "char* easy_alloc_string::temporary")
    }



}

#endif // EASY_ALLOC_H
