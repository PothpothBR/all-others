#ifndef SFORMAT_H

// retorna o tamanho da string ate a primeira quebra de linha, ou ate uma caractere especifico   ***sem conta-lo***
int ssize(const char* str, char end = '\n'){
    int i = 1;
    for (char ch = str[0]; ch != '\n' && ch != '\0' && ch != end; ch = str[i], i++);
    return i-1;
}

// remove um certo caractere em todas as ocorrencias, se "size = 0" sera usado "ssize()" para descobrir o tamanho
char* srefine(char* str, char cut, int size = 0){

    /*
    se str for definido como "char* nome"
    ocorrera erro pois virara const char*
    se for "char nome[]" nao ocorrera;
    */

    /*
    dependente de uma string pre alocada a qual e referenciada a str
    */

    // se nao for definido size, descobre-o
    if(!size){
        size = ssize(str) + 1; // "+ 1" para o "\n"
    }
    //se size for = 0 informa erro e retorna
    if (size <= 0){
        perror("srefine", "null string");
        return nullptr;
    }

    // variavel para armazenar quantos caracteres a serem removidos
    int back_cut = 0;

    for (int i = 0; i <= size; i++){
        // se for o caractere de corte remove-o
        if (str[i] == cut){back_cut++; continue;}
        // se nao, insere
        str[i - back_cut] = str[i];
    }
    return str;
}

// faz o mesmo so que, retorna um ponteiro alocado na memoria ram, e aceita strings como argumento
char* srefine(const char* str, char cut, int size = 0){

    /*
    se str for definido como "char* nome"
    ocorrera erro pois virara const char*
    se for "char nome[]" nao ocorrera;
    */

    /*
    cria uma string internamente, sem tratamento de memoria e a retorna
    */

    // se nao for definido size, descobre-o
    if(!size){
        size = ssize(str) + 1; // "+ 1" para o "\n"
    }
    //se size for = 0 informa erro e retorna
    if (size <= 0){
        perror("srefine", "null string");
        return nullptr;
    }

    // variavel para armazenar quantos caracteres a serem removidos
    int back_cut = 0;

    // ponteiro para retorno
    char *tmp_str = (char*) calloc(size, sizeof(char));

    for (int i = 0; i <= size; i++){
        // se for o caractere de corte remove-o
        if (str[i] == cut){back_cut++; continue;}
        // se nao, insere
        tmp_str[i - back_cut] = str[i];
    }
    return tmp_str;
}

// retorna um vetor com a posicao de um certo caractere em todas as suas ocorrencias, valor inicial sendo tamanho
int* ssearch(const char* str, char sch, int size = 0){

    // se nao for definido size, descobre-o
    if(!size){
        size = ssize(str) + 1; // "+ 1" para o "\n"
    }
    //se size for = 0 informa erro e retorna
    if (size <= 0){
        perror("srefine", "null string");
        return nullptr;
    }

    // vetor para alocar as posicoes, valor inicial sendo tamanho
    int* counts = (int*) calloc(1, sizeof(int));
    counts[0] = 1;

    for (int i = 0; i <= size; i++){

        // se for igual a sch aumenta o tamanho e aloca a posicao
        if (str[i] == sch){
            // realoca o buffer
            counts = (int*) realloc(counts, ++counts[0] * sizeof(int));

            // insere no buffer a posicao
            counts[counts[0] - 1] = i;
        }
    }
    return counts;
}

// objeto para tratar o retorno de ssearch **futuramente mais complexo**
class sstring{
public:

    /****definicao de variaveis****/
    // string tratada
    char* string = nullptr;
    int string_size = 0;

    // valores tratados
    int* counts = nullptr;
    int counts_size = 0;
    

    /****construtores****/
    // construtor *indireto* para ssearch
    void spawn_sstring(int* counts){

        // insere o tamanho ** '-1' por que a posicao 0 e o tamanho **
        counts_size = counts[0] - 1;

        // trata os valores
        this->counts = (int*) calloc(counts_size, sizeof(int));

        for (int i = 1; i < counts_size + 1; i ++){
            this->counts[i - 1] = counts[i];
        }

        // e libera o buffer obsoleto
        free(counts);
    }

    // construtor *indireto* para srefine
    void spawn_sstring(char* str) {
        this->string = str;
        string_size = ssize(str);
    }

    // construtor para srefine
    sstring(char* str) {
        this->string = str;
        string_size = ssize(str);
    }

    // construtor para ssearch
    sstring(int* counts) {

        // insere o tamanho ** '-1' por que a posicao 0 e o tamanho **
        counts_size = counts[0] - 1;

        // trata os valores
        this->counts = (int*)calloc(counts_size, sizeof(int));

        for (int i = 1; i < counts_size + 1; i++) {
            this->counts[i - 1] = counts[i];
        }

        // e libera o buffer obsoleto
        free(counts);
    }

    // construtor de copia
    sstring(sstring* tmp) {
        if (tmp->string) string = tmp->string;
        if (tmp->string_size) string_size = tmp->string_size;
        if (tmp->counts) counts = tmp->counts;
        if (tmp->counts_size) counts_size = tmp->counts_size;

    }
    
    /****destrutor****/
    // libera o buffer
    ~sstring(){
        if(counts) free(counts);
        if(string) free(string);
    }
};

// recorta a string e a retorna, juntamente com a posicao da letra antes de cada letra cortada
sstring ssearchfine(const char* str, char cut, int size = 0){

    /*
    se str for definido como "char* nome"
    ocorrera erro pois virara const char*
    se for "char nome[]" nao ocorrera;
    */

    /*
    cria uma string internamente, sem tratamento de memoria e a retorna
    */

    // se nao for definido size, descobre-o
    if (!size) {
        size = ssize(str) + 1; // "+ 1" para o "\n"
    }
    //se size for = 0 informa erro e retorna
    if (size <= 0) {
        perror("srefine", "null string");
    }

    // variavel para armazenar quantos caracteres a serem removidos
    int back_cut = 0;
    // ponteiro para retorno
    char* tmp_str = (char*)calloc(size, sizeof(char));

    // vetor para alocar as posicoes
    int* counts = (int*)calloc(1, sizeof(int));
    // valor inicial sendo tamanho
    counts[0] = 1;

    for (int i = 0; i <= size; i++) {
        // se for igual a cut aumenta o tamanho e aloca a posicao
        if (str[i] == cut) {

            
            // realoca o buffer
            counts = (int*)realloc(counts, ++counts[0] * sizeof(int));
            // insere no buffer a posicao
            counts[counts[0] - 1] = i;
        }

        

        // se for o caractere de corte remove-o
        if (str[i] == cut) { back_cut++; continue; }
        // se nao, insere
        tmp_str[i - back_cut] = str[i];

        
    }

    // constroi a classe a ser retornada
    sstring* str_return = (sstring*)calloc(sizeof(sstring), 1);
    str_return->spawn_sstring(tmp_str);
    str_return->spawn_sstring(counts);


    return str_return;
}
#endif // SFORMAT_H
