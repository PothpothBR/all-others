#ifndef LOGUINV3_H_INCLUDED
#define LOGUINV3_H_INCLUDED
#include <stdio.h>
#include <fstream>
using namespace std;
int verificacao(string ver);
void verf5(int verinfinito);

class pessoa{
	public:
	string nome,senha;
    int validade(string no,string se);
    //construtor
    pessoa(string nom,string sen);
};


//valida os dados
int pessoa::validade(string no,string se){
string cache_nome,cache_senha;
int ver3;
int ver4;
ifstream i_l;
    i_l.open("C:/Users/bd88/Desktop/projeto_loguinV5/recursos/cache/cache.txt");

    getline(i_l,cache_nome);
    getline(i_l,cache_senha);
cout <<"0"<< cache_nome<<"0" << cache_senha<<"0";
//cout << no<<se;
system("pause");
    i_l.close();
if(no==cache_nome){
    ver3=1;
}else{
    ver3=11;
}

if(se==cache_senha){
    ver4=2;
}else{
    ver4=22;
}
ver3+=ver4;
cout << ver3;
system("pause");
return ver3;
}

//construtor
pessoa::pessoa(string nom,string sen){
nome=nom;
senha=sen;
}


int verificacao(string ver){
    int refaz1;
    string ver2;
	if (ver=="sim"){
		cout << "-------------------------------------------------\n";
		if(ver2=="sim"){
            refaz1=0;}
		else if(ver2=="nao"){
            refaz1=0;}
	}else if (ver=="nao"){
		cout <<"deseja re-inserir os dados? -sim/nao\n\t";
		cin >> ver2;
		cout << "-------------------------------------------------\n";

		if(ver2=="sim"){
            refaz1=2;
            system("cls");

            }
		else if(ver2=="nao"){
            refaz1=0;

		}

	}else{
        cout <<"dado incorreto tente sim ou nao\n";
        cout << "-------------------------------------------------\n";
        refaz1=1;
	}
return refaz1;
}
void verf5(int verinfinito){
	int ver5=verinfinito;
		switch(ver5){
		case 3:
		cout << "-------------------------------------------------\n" << "-------------------------------------------------\n"  << "-------------------------------------------------\n";
		cout << "\tdados coretos - login concluido!!\n";
		cout << "-------------------------------------------------\n" << "-------------------------------------------------\n"  << "-------------------------------------------------\n";
			break;
		case 23:		cout << "-------------------------------------------------\n" << "-------------------------------------------------\n"  << "-------------------------------------------------\n";
			cout << "\tsenha incorreta\n\a";
					cout << "-------------------------------------------------\n" << "-------------------------------------------------\n"  << "-------------------------------------------------\n";
			break;
		case 13:		cout << "-------------------------------------------------\n" << "-------------------------------------------------\n"  << "-------------------------------------------------\n";
			cout << "\tnome incorreto\n\a";		cout << "-------------------------------------------------\n" << "-------------------------------------------------\n"  << "-------------------------------------------------\n";
			break;
		case 33:		cout << "-------------------------------------------------\n" << "-------------------------------------------------\n"  << "-------------------------------------------------\n";
		cout <<"\tnome e senha incorretos\n\a" ;
		cout << "-------------------------------------------------\n" << "-------------------------------------------------\n"  << "-------------------------------------------------\n";

		break;
	}
system("pause");

	}
#endif //LOGUINV3_H_INCLUDED
