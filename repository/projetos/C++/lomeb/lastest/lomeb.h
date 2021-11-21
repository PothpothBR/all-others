#ifndef LOMEB_H
#define LOMEB_H

#include <iostream>
#include "C:/Users/bd88/Google Drive/backup lomeo(old moblib)/lastest/timing.h"
#include "C:/Users/bd88/Google Drive/backup lomeo(old moblib)/lastest/colision.h"

class Writebox {
public:
	TICKS key_time;
	int size = 0;
	int digit_pos = 0;
	char *buffer = nullptr;
	char keyghost = ' ';
	int time = 0;
	float fps = 0.0;

	Writebox(int write_size, int time, float FPS = 0) {
		key_time.stettime(time, FPS);
		size = write_size;
		buffer = new char[size];
		this->time = time;
		this->fps = FPS;
		for (int i = 0; i < size;i++) {
			buffer[i] = ' ';
		}
	}

	// apaga o buffer
	~Writebox() {
		delete[] buffer;
	}

	// manipula o buffer
	void write(const char input, bool keyboard_state) {
		// se a tecla foi pressionada
		// apos a primeira tecla inserida espera um tempo ate comessar repetir
		key_time.wait();
		if (keyboard_state) {
			// insere a tecla e espera
			if (key_time.trigger() || input != keyghost) {
				if (input == '\b') {
					// se for o backspace remove
					if (digit_pos > 0) {
						buffer[--digit_pos] = ' ';
					}

				}
				else {
					//se for caractere o insere
					if (digit_pos < size) {
						buffer[digit_pos++] = input;
					}
				}
				// pega a tecla para verificar repeticao
				keyghost = input;
				// e ajusta o tempo para inserir tecla para aumentar a velocidade
				key_time.stettime(2);
			}

		}
		// se a tecla foiu soltada reseta o timer e o coloca para disparar
		if (!keyboard_state) {

			key_time.stettime(time, fps);
			key_time.charge();
		}
	}

}writebox(42, 20);

class Box {

public:

	// propriedades da caixa
	float _x = 0, _y = 0,
		_width = 0, _height = 0, // ideia genial, quando o valor for menor que 1, tipo 0.24 esse valor sera contado como porcentagem, sendo facil descontar da largura ou altura para pegar um valor variavel
		_padding[4] = { 0 },
		_margin[4] = { 0 },
		_border[4] = { 0 };

	// posicoes das propriedades
	/*
	 *     1
	 *   #####
	 * 0 ##### 3
	 *   #####
	 *     2
	 */
	static const int up = 1;
	static const int down = 2;
	static const int left = 0;
	static const int right = 3;

	// ponteiro para caixas filho
	Box **_nested = nullptr;
	int _nested_size = 0;

	// ponteiro para caixa pai
	Box *_inherit = nullptr;

	// ponteiro statico para alocacao global de caixas
	static Box **_global;
	static int _global_size;

	//funcoes de chamada para membro
	//margem
	void margin(float size) { for (int i = 0;i < 4;i++) _margin[i] = size; }
	void margin(int position, int size) { _margin[position] = size; }
	//espacamento interno
	void padding(float size) { for (int i = 0;i < 4;i++) _padding[i] = size; }
	void padding(int position, int size) { _padding[position] = size; }
	//borda
	void border(float size) { for (int i = 0;i < 4;i++) _border[i] = size; }
	void border(int position, int size) { _border[position] = size; }
	// retorna a posicao de desenho
	float x() { return _x + _margin[left] + _border[left]; }
	float y() { return _y + _margin[up] + _border[up]; }
	float width() { return  _width; }
	float height() { return _height; }
	// retorna a posicao real(cheia)
	float X() { return _x; }
	float Y() { return _y; }
	float WIDTH() { return  _margin[left] + _border[left] + _width + _border[right] + _margin[right]; }
	float HEIGHT() { return _margin[up] + _border[up] + _height + _border[down] + _margin[down]; }

	void inherit(Box *_inherit = nullptr) {

		// verifica se ha uma caixa pai para se adicionar, e se ja nao ja foi adicionado a uma caixa pai
		if (_inherit && !this->_inherit) {

			// atribui a posicao do pai e da os descontos de borda e espacamento interno
			_x = _inherit->x() + _inherit->_padding[left];
			_y = _inherit->y() + _inherit->_padding[up];

			// procura por outras caixas filas do mesmo pai que ja tenham sido criadas antes
			for (int i = 0; i < _inherit->_nested_size; i++) {

				Box *temp = _inherit->_nested[i];
				/*
				al_draw_line(10, _y, 10, _y + HEIGHT(), al_map_rgb(255, 0, 0), 4);
				al_draw_line(15, temp->Y(), 15, temp->Y() + temp->HEIGHT(), al_map_rgb(255, 0, 0), 4);
				al_flip_display();
				al_rest(3);*/

				// se nao estiver na mesma linha, pula para o proximo irmao
				if (colid_out_axis(_y, HEIGHT(), temp->Y(), temp->HEIGHT())) continue;

				// atribui a posicao da outra caixa e os descontos de borda e espacamento esterno
				_x += temp->WIDTH();

				// se a caixa sair fora do pai, joga-a para baixo da outra caixa e reseta a posicao _x
				if (colid_in_axis(_x, WIDTH(), _inherit->x(), _inherit->width() - _inherit->_padding[right] + 1)) { // nao é nessesario colidir a posicao y

					_y = temp->Y() + temp->HEIGHT();
					_x = _inherit->x() + _inherit->_padding[left];
				}
				else {
					// se a altura total da caixa for mair que suas antecessora, alinha-a a sua parte inferior
					if (_y + HEIGHT() > temp->Y() + temp->HEIGHT()) {
						temp->_y = _y + HEIGHT() - temp->HEIGHT();
					}
					// se nao for alinha a caixa a parte inferior de sua antecessora
					else if (_y + HEIGHT() < temp->Y() + temp->HEIGHT()) {
						_y = temp->Y() + temp->HEIGHT() - HEIGHT();
					}
				}
				/*
				al_draw_line(10, _y, 10, _y + HEIGHT(), al_map_rgb(0, 0, 255), 4);
				al_draw_line(15, temp->Y(), 15, temp->Y() + temp->HEIGHT(), al_map_rgb(0, 0, 255), 4);
				al_flip_display();
				al_rest(5);
				al_clear_to_color(al_map_rgb(0, 0, 0));*/
			}

			// adiciona a caixa pai ao lugar da mesma
			this->_inherit = _inherit;

			// adiciona a si propria aos iramos na caixa pai
			_inherit->_nested = (Box**)realloc(_inherit->_nested, ++_inherit->_nested_size * sizeof(Box*));
			_inherit->_nested[_inherit->_nested_size - 1] = this;

		}// se nao ouver caixa pai considera-se que o pai e o corpo da tela de desenho
		else {
			_x = 0;
			_y = 0;
		}

		//this->position = position;

	}

	Box() {

		_global = (Box**)realloc(_global, sizeof(Box*) * ++_global_size);
		_global[_global_size - 1] = this;

	}

	// inicia as pripriedades basicas
	Box(float _width, float _height) {

		this->_width = _width;
		this->_height = _height;
		_global = (Box**)realloc(_global, sizeof(Box*) * ++_global_size);
		_global[_global_size - 1] = this;
	}

}box;

Box** Box::_global = nullptr;
int Box::_global_size = 0;

#endif
