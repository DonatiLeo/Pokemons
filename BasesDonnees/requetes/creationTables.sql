CREATE TABLE IF NOT EXISTS Compte(
	id INTEGER NOT NULL UNIQUE,
	pseudo TEXT NOT NULL,
	email TEXT NOT NULL,
	password TEXT NOT NULL,
	PRIMARY KEY(id AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS Pokemons_possessed(
	id INTEGER NOT NULL UNIQUE,
	compte_id INTEGER NOT NULL,
	pseudo TEXT NOT NULL,
	id_pokemon INTEGER NOT NULL,
	name_pokemon TEXT NOT NULL,
	pokemons_possessed_total REAL NOT NULL,
	PRIMARY KEY(id AUTOINCREMENT)
);

INSERT INTO Pokemons_possessed(id,compte_id,pseudo,id_pokemon,name_pokemon,pokemons_possessed_total) VALUES
(1,1,'Yuan',31,'Pikatchu',1);