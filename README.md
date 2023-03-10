# Kasvinhoitosovellus

Tässä sovelluksessa käyttäjä voi lisätä erilaisia kasveja ja niihin liittyvät hoito-ohjeet. Jokainen käyttäjä voi olla peruskäyttäjä tai ylläpitäjä.

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi lisätä kasveja ja niihin liittyvät tiedot, kuten nimi, kuva, hoito-ohjeet ja kommentit.
- Käyttäjä näkee sovelluksessa olevat kasvit ja kasvin valittaessa käyttäjä pääsee näkemään, kuinka paljon tämä kasvi tarvitsee aurinkoa ja vettä.
- Käyttäjä myös näkee kaikki kommentit ja voi itse kommentoida.
- Käyttäjä voi etsiä kaikki kasvit, joiden kuvauksessa on annettu sana.
- Ylläpitäjä voi poistaa kasveja.
- Ylläpitäjä voi luoda ryhmiä, joihin kasveja voi luokitella. Yksittäinen kasvi voi kuulua yhteen tai useampaan ryhmään.
- Ylläpitäjä voi poistaa luotuja ryhmiä.

## Kesken jääneet ominaisuudet:

- Ylläpitäjä voi uudelleen arvioida, kuinka paljon se tarvitsee aurinkoa ja vettä.
- Ylläpitäjä voi poistaa käyttäjien annettuja kommentteja.

## Testausohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

```bash
DATABASE_URL=postgresql:///<tietokannan nimi>
SECRET_KEY=<salainen avain>
```

Oman salaisen avaimen voi luoda vaikkapa Python-tulkin avulla:
```bash
>>> python3
>>> import secrets
>>> secrets.token_hex(16)
```
  
Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```

Määritä vielä tietokannan skeema komennolla:
```bash
$ psql < schema.sql
```
  
Käynnistä sovelluksen komennolla:
```bash
$ flask run
```
