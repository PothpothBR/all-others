/*
  ----------------------------------------------------
  |              Biblioteca feita por                |
  |     [Bruno Dalagnol] [2018] [versao: sei la]     |
  |--------------------------------------------------|
  |                                                  |
  |			    /\         /\       ___              |
  |			   /--\_______/--\     / _|              |
  |			   |  Y       Y  |    / /                |
  |			   |    ==T==    |   / /                 |
  |			   \_____________/  / /                  |
  |				  |  _____   \ / /                   |
  |				  |           \ /                    |
  |				  |  |--|  |\  |                     |
  |				  |__||_|__||__|                     |
  ----------------------------------------------------
*/
#ifndef SHEET_H
#define SHEET_H
#include "position.h"

// classe para armazenar as propriedades de um bitmap MOB_SHEET
class MOB_SHEET {
public:
	int totalCells, *cellX, *cellY;

	float handleX[9], handleY[9];

	// o tamanho de uma celula
	MOB_DIMENSION cell_dimension;
	// a quantidade de celulas
	MOB_DIMENSION cell_count;
	
	MOB_SHEET(float width,float height,float cols,float rows) {


		float w = cell_dimension.width = width / cols;
		float h = cell_dimension.height = height / rows;
		cell_count.width = cols, cell_count.height = rows;
		totalCells = cols*rows;

		float hw = w / 2;
		float hh = h / 2;

		this->handleX[0] = 0;   this->handleY[0] = 0;
		this->handleX[1] = -hw; this->handleY[1] = 0;
		this->handleX[2] = -w;  this->handleY[2] = 0;
		this->handleX[3] = 0;   this->handleY[3] = -hh;
		this->handleX[4] = -hw; this->handleY[4] = -hh;
		this->handleX[5] = -w;  this->handleY[5] = -hh;
		this->handleX[6] = 0;   this->handleY[6] = -h;
		this->handleX[7] = -hw; this->handleY[7] = -h;
		this->handleX[8] = -w;  this->handleY[8] = -h;

		this->cellX = (int *) malloc(sizeof(int) * this->totalCells);
		this->cellY = (int *) malloc(sizeof(int) * this->totalCells);

		for (float index = 0; index < this->totalCells; index++) {
			cellX[(int)index] = (int)index % (int)cols * w;
			cellY[(int)index] = int(index / cols) * h;
		}
		
	}

	MOB_SHEET() {}

	~MOB_SHEET() {
		free(this->cellX);
		free(this->cellY);
        cellX = nullptr;
        cellY = nullptr;
	}

};
#endif
