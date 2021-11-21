#ifndef DICTIONARY_H

#include "debug.h"

// classe simples para armazenar um par "chave = valor" e retornar um valor por uma chave
template <class KEY, class VAL>
class Skey_value{

    // buffer de chaves
    KEY* keys = nullptr;
    // buffer de valores
    VAL* values = nullptr;
    //tamanho do buffer (os dois *obrigatoriamente* tem o mesmo tamanho)
    int _size = 0;

public:

    //retorna o tamanho
    int size(){ return _size; }

    // retorna a posicao da chave especifica
    int key_index(KEY ky){
        int i = 0;
        // se o index passar do tamanho maximo do buffer(nao encontrando a chave) retorna "-1"
        for(KEY it; it != ky; it = keys[i], i++)if (i > _size) return -1;
        return i-1;
    }

    // retorna a posicao do valor especifico
    int value_index(VAL vl){
        int i = 0;
        for(VAL it; it != vl; it = values[i], i++)if (i > _size) return -1;
        return i-1;
    }

    // retorna o valor referente a chave
    VAL operator[](KEY ky){
        int i = key_index(ky);
        if (i != -1) return values[i];

        perror<KEY>("Skey_value::operator[]", ky, "don't exists");

        return (VAL) 0;
    }

    // retorna a chave referente ao valor
    KEY inverse(VAL vl){
        int i = value_index(vl);
        if (i != -1) return keys[i];

        perror<VAL>("Skey_value::inverse", vl, "don't exists");

        return (KEY) 0;
    }

    // retorna a chave referente a posicao
    KEY key(int index){
        if ( index < 0 || index > _size - 1){
            perror<int>("Skey_value::key", index, "don't exists");
            return (KEY) 0;
        }

         return keys[index];
    }

    // retorna o valor referente a posicao
    VAL value(int index){
         if ( index < 0 || index > _size - 1){
            perror<int>("Skey_value::value", index, "don't exists");
            return (VAL) 0;
        }
         return values[index];
    }

    // insere um par de "chave = valor"
    void append(KEY ky, VAL vl){

        keys = (KEY*) realloc(keys, sizeof(KEY) * ++_size);
        values = (VAL*) realloc(values, sizeof(VAL) * _size);

        keys[_size - 1] = ky;
        values[_size - 1] = vl;

    }

    // remove um par "chave = valor"
    void remove(KEY ky){

        // posicao da chave a ser removida
        int kindex = key_index(ky);

        // verifica se a chave existe, se nao retorna
        if ( kindex < 0 || kindex > _size - 1){
            perror<KEY>("Skey_value::remove", ky, "don't exists");
            return;
        }

        // buffers para alocar o novo conjunto
        KEY *ktmp = (KEY*) calloc(sizeof(KEY), _size - 1);
        VAL *vtmp = (VAL*) calloc(sizeof(VAL), _size - 1);

        //copia até a chave
        for(int i = 0; i <= kindex; i++){
            ktmp[i] = keys[i];
            vtmp[i] = values[i];
        }
        // pula a chave e copia o resto
        for(int i = kindex + 1; i < _size; i++){
            ktmp[i - 1] = keys[i];
            vtmp[i - 1] = values[i];
        }

        // libera o buffer antigo e insere o novo ja cortado
        free(keys);
        keys = ktmp;
        // libera o buffer antigo e insere o novo ja cortado
        free(values);
        values = vtmp;

        // diminui o tamanho dos buffers
        _size--;

    }

    // libera o buffer
    ~Skey_value(){
        free(keys);
        free(values);
    }
};

#endif // DICTIONARY_H
