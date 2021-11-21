
import format_strings

import interpreter

import data_manager

lines = 1 #contagem de linhas lidas

def cache(): #le e interpreta a folha de cache
   
   cache = open('dict.htdl','r') #abre o cache   
   
   def get_lines(): #funcao para ler a data
       return cache.readline() #retorna a linha do cache
   
   
   
cache()