Aplicação que organiza e roda programas CAJOlang
==================
Projeto de recrutamento da Raccoon 2018.1 
Autor: Luiz Augusto Vieira Manoel	avm.luiz@gmail.com

###Intruções de compilação e execução

O programa é feito em _python3_.
Para compilar e executar o usuário deve ter o python3 instalado em sua máquina. 
Caso não tiver digite 'sudo apt-get install python3.5' no terminal do linux.
Se está usando windows, [clique aqui](https://www.python.org/).
Com o python instalado, basta acessar o dirétorio do arquivo pelo terminal e digitar `python3 Org_and_run_CAJOlang.py` (Linux) ou `python Org_and_run_CAJOlang.py` (Windows)

O programa espera como entrada programas CAJOlang (arquivos no formato .cl), que devem estar no mesmo diretório do arquivo .py

###Observação importante 
A primeira linha do programa CAJOlang diz o minuto X que ele roda a cada hora.
Dentro desse minuto, o programa vai rodar UMA VEZ a qualquer segundo (não necessariamente no minuto X e 0 segundos)