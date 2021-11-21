#ifndef DISPLAY_H

// buffer "chave: valor"
#include "dictionary.h"
// formatacao de strings
#include "sformat.h"

// unsigned int
typedef unsigned int uint;

/* o display funciona como um vetor bidimensional (bitmap) para cada caractere
 * é informado a largura e a altura de desenho no console
 * quebra de linha não é usada, e sim é inserido no final da "linha" externamente, na hora de inprimir no console
 **/

// classe principal para gerenciar o desenho no console
class Display{

    /****funcoes internas****/
    // retorna o index para um buffer linear a partir de dados de um bidimensional
    int _index(int x, int y, int width){ return x + y * width; }

public:


    /****buffer principal****/
    // buffer para a saida pronta no console Main BuFFer
    char* mbff = nullptr;
    // tamanho
    uint mbff_size = 0;
    // numero de caracteres ate o fim da linha
    uint mbff_width = 0;
    //numero de caracteres maximos até o fim do console
    uint mbff_height = 0;

    /****funcao linear****/
    // se o buffer sera para escrita linear
    bool linear_draw = false;
    //ultimo caractere escrito linearmente no buffer
    uint mbff_last = 0;

    /****buffers secundarios****/
    // tamanho maximo dos buffers secundarios
    uint sbff_max_size = 0;
    // inicia os buffers secundarios no tamanho maximo
    bool sbff_full_start = false;

    /****construtores****/
    // cria o display
    Display(uint width, uint height){

        mbff_width = width;
        mbff_height = height;

        mbff_size = (width) * height;

        mbff = (char*) calloc(mbff_size + height, sizeof(char)); // "+ height" para os '\n'

        // preenche o buffer com espacos
        for(int i = 0; i < mbff_size; i++) mbff[i] = ' ';
        // insere os '\n' no final
        for (int i = width - 1; i < mbff_size; i += width) mbff[i] = '\n';
    }

    /****funcoes lineares****/
    // insere diretamente no buffer a string até a PRIMEIRA quebra de linha "\n", ou até o fim do buffer
    void to_bff(const char* str, uint _index = 0){

        if (!linear_draw) mbff_last = _index;

        for (int i = 0;
         mbff_last < mbff_size && i < ssize(str);
         mbff_last++, i++){

            // ===criar codigo que verifica quebras de linha e simula uma quebra de linha no buffer===

            mbff[mbff_last] = str[i];
        }
    }

    // insere diretamente no buffer ate o ponto especifico, ou até o fim do buffer
    void to_bff(const char* str, uint _index, uint size){

        if (!linear_draw) mbff_last = _index;

        for (int i = 0;
         mbff_last < mbff_size && i < size;
         mbff_last++, i++){
            cout << mbff_last << '-';
            if (str[i] == '\n') { mbff_last += mbff_width; i++; } // erro aki e eu nao entendi!?!?
            cout << mbff_last << endl;
            mbff[mbff_last] = str[i];
        }
    }

    /****funcoes bidmensionais****/
    // insere uma area no buffer
    void draw_in(char** str, int bx, int by, int sx, int sy, int width, int height){
        // itera bidimensionalmente o buffer
        for (int y = sy; y < height; y++){
            for (int x = sx; x < width; x++){
                // se a largura for maior que o buffer principal, corte-a
                if (x > mbff_width) break;

                // copia o caractere
                mbff[index(bx + x, by + y, mbff_width)] = str[y][x];
            }
            // se a altura for maior que o buffer principal, corte-a
            if (y > mbff_height) break;

        }

    }

    /****controle de execussao****/
    // imprime no console o buffer
    bool flip(const char fill = ' '){

        cout << mbff;

        // preenche o buffer com espacos
        for (int i = 0; i < mbff_size; i++) mbff[i] = fill;

        return false;
    }

};

#endif // DISPLAY_H
