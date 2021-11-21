#ifndef GLOBAL_DEFINITIONS_H
#define GLOBAL_DEFINITIONS_H

// inclusao em um cabecalho global devido ao uso em divesos lugares
#include <iostream>
using namespace std;

// arquivo para tratamento de erros
#include "C:/Users/bruno/Google Drive/backups/message/lastest/message.h"

// derefinicao de nomeacao
typedef unsigned int uint;
#define message(ID, vals, ...) _show_message(message_manager._message_list, ID, vals, ##__VA_ARGS__)


class Message_manager{
public:
    Message _message_list = nullptr;

    Message_manager(){

        _message_list = (Message) calloc(sizeof(struct _Message), 1);

        _create_message(&_message_list, -1, "error", "estouro de memoria");
    }

}message_manager;


#endif // GLOBAL_DEFINITIONS_H
