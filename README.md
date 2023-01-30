# Kasvinhoitosovellus

Tässä sovelluksessa käyttäjä voi lisätä erilaisia kasveja ja niihin liittyvät hoito-ohjeet. Jokainen käyttäjä voi olla peruskäyttäjä tai ylläpitäjä.

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi etsiä tiettyä kasvia.
- Käyttäjä voi lisätä kasveja ja niihin liittyvät tiedot, kuten nimi, kuva, hoito-ohjeet tähtiasteikkona ja kommentteina. 
- Käyttäjä näkee sovelluksessa olevat kasvit ja kasvin valittaessa käyttäjä pääsee näkemään, kuinka paljon tämä kasvi tarvitsee aurinkoa ja vettä.
- Käyttäjä myös näkee kaikki kommentit ja voi itse kommentoida.
- Käyttäjä voi etsiä kaikki kasvit, joiden kuvauksessa on annettu sana.
- Ylläpitäjä voi lisätä ja poistaa kasveja.
- Ylläpitäjä voi uudelleen arvioida, kuinka paljon se tarvitsee aurinkoa ja vettä.
- Ylläpitäjä voi poistaa käyttäjien annettuja kommentteja.
- Ylläpitäjä voi luoda ryhmiä, joihin kasveja voi luokitella. Yksittäinen kasvi voi kuulua yhteen tai useampaan ryhmään.

## Testausohjeet

- Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

  - DATABASE_URL=postgresql:///user <br>
  - SECRET_KEY=salainen-avain
  
- Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:
  - python3 -m venv venv
  - source venv/bin/activate
  - pip install -r ./requirements.txt
  
- Määritä vielä tietokannan skeema komennolla:
  - psql < schema.sql
  
- Käynnistä sovelluksen komennolla:
  - flask run
