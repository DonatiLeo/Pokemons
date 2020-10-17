CREATE TABLE IF NOT EXISTS Compte(
	id INTEGER NOT NULL UNIQUE,
	pseudo TEXT NOT NULL,
	email TEXT NOT NULL,
	password TEXT NOT NULL,
	PRIMARY KEY(id AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS Pokemons_possessed(
	compte_id INTEGER NOT NULL,
	id_pokemon INTEGER NOT NULL,
	FOREIGN KEY(compte_id) REFERENCES Compte(id),
	FOREIGN KEY(id_pokemon) REFERENCES Pokemons(id_pokemon),
	PRIMARY KEY(compte_id,id_pokemon)
);
