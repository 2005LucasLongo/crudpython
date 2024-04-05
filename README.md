# crudpython
Comandos MySQL (jogue-os no MySQL Workbench e veja a mágica acontecer):

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

