# crudpython
WHY I AM STARTING THIS?!
Oh, yeah. Portifólio.

Vou fazer um CRUD simples com Python e MySQL, tendo como base o trabalho da A3 do primeirso semestre da minha faculdade, que foi em Java.

Comandos MySQL:

CREATE DATABASE CRUDPython;
USE CRUDPython;

CREATE TABLE IF NOT EXISTS clientes (
	ID INT8 AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
	ID INT8 AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DOUBLE DEFAULT 0,
    ID_cliente INT8 NOT NULL,
    FOREIGN KEY (ID_cliente) REFERENCES clientes (ID)
);

