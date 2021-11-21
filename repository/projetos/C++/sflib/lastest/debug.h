#ifndef DEBUG_H

# ifndef NOT_DEBUG
#include <cstdlib>

// saida de erro formatada
template <class T = int> inline void perror(const char* ierarchy, T value, const char* complement){
    cout << " === [error] <" << ierarchy << "> \"" << value << "\" " << complement << " ===" << endl;
    exit(EXIT_FAILURE);
}
// saida de erro formatada, sem variavel
template <class T = int> inline void perror(const char* ierarchy, const char* complement){
    cout << " === [error] <" << ierarchy << "> " << complement << " ===" << endl;
    exit(EXIT_FAILURE);
}

#else
// sem saida de erro se a macro NOT_DEBUG estiver definida
template <class T> inline void perror(const char* ierarchy, T value, const char* complement){}
template <class T> inline void perror(const char* ierarchy, const char* complement){}
#endif

#endif // DEBUG_H
