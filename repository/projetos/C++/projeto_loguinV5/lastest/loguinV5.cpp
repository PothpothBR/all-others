#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
#include "loguinV5.h"
using namespace std;

int main(){

int op;
ofstream o_l;



    cout << "deseja fazer loguin ou criar uma nova conta?";
    cout << "\n\n";
    cout << "     loguin[1] -- criar_nova[2]";

    cin >> op;
system("cls");

    if(op == 1){

    int ver5=0;
    int refaz;
	string nome,senha,ver1,ver2;

do{

system("cls");
	//reconhecimento do nome

	do{
	cout << "-------------------------------------------------\n";
	cout  <<"informe seu nome:\n\t";
	cin>>nome;

	///////////

	//reconhecimento da senha
    cout << "-------------------------------------------------\n";
	cout <<"informe sua senha:\n\t";
	cin>>senha;
	pessoa pes1(nome,senha);
	cout << "-------------------------------------------------\n";
	//////////
	do{
	cout << "dados inseridos corretamente?  - sim/nao\n\t";
	cin >> ver1;
	cout << "-------------------------------------------------\n";
    refaz=verificacao(ver1);
	}while (refaz==1);
if(refaz!=0){	ver5=pes1.validade(pes1.nome,pes1.senha);}

    }while (refaz==2);

		system("cls");


		verf5(ver5);
}while ((ver5==23) || (ver5== 13) || (ver5== 33));


    }

    else if(op == 2){

    string nomec,senhac;

    o_l.open("C:/Users/bd88/Desktop/projeto_loguinV5/recursos/cache/cache.txt");
    o_l << "";
    o_l.close();

    o_l.open("C:/Users/bd88/Desktop/projeto_loguinV5/recursos/cache/cache.txt",ios::app);

    cout << "informe seu nome de usuario:" << setw(1) << endl;
    cin >> nomec;

    cout << "informe sua senha:" << setw(1) << endl;
    cin >> senhac;

    o_l << nomec;
    o_l << "\n";
    o_l << senhac;

    o_l.close();
    }







return 0;
}
