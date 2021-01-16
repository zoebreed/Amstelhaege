# Amstelhaege
#### Door Casper Smit, Shu Yan Ng en Zoë Breed

## De case
Na jarenlang getouwtrek is de knoop eindelijk doorgehakt: er komt een nieuwe woonwijk in de Duivendrechtse polder, net ten noorden van Ouderkerk aan de Amstel. De huisjes zijn bedoeld voor het midden- en bovensegment van de markt, met name expats en hoogopgeleide werknemers actief op de Amsterdamse Zuidas.

Omdat de Duivenderechtse polder ooit beschermd natuurgebied was, is de compromis dat er alleen lage vrijstaande woningen komen, om zo toch het landelijk karakter te behouden. Dit, gecombineerd met een aantal strenge restricties ten aanzien van woningaanbod en het oppervlaktewater, maakt het een planologisch uitdagende klus. De gemeente overweegt drie varianten: de 20-huizenvariant, de 40-huizenvariant en de 60-huizenvariant. Er wordt aangenomen dat een huis meer waard wordt naarmate de vrijstand toeneemt, de rekenpercentages zijn per huistype vastgesteld.

## restricties
1. De wijk komt te staan op een stuk land van 180x160 meter (breed x diep). 
2. De vrijstand van een woning is de kleinste afstand tot de dichtstbijzijnde andere woning in de wijk. Oftewel, voor een vrijstand van 6 meter moeten alle andere woningen in de wijk op minimaal 6 meter afstand staan. Deze afstand is bepaald als de kortste afstand tussen twee muren, dus niet vanuit het centrum van de woning.
3. De verplichte vrijstand voor iedere woning moet binnen de kaart vallen. Overige vrijstand mag buiten de kaart worden meegerekend.
4. In geval van percentuele waardevermeerdering per meter is de toename niet cumulatief. 
5. De wijk bestaat voor een deel uit oppervlaktewater. Huizen mogen niet op het water worden geplaatst, maar hun vrijstand mag daar wel op vallen (zowel de verplichte als die voor de waarde berekening).

| Huizen           | Groote          | Vrijstand             | Waarde        | Prijsverbetering |
|------------------|-----------------|-----------------------|---------------|------------------|
| Eengezinswoning  | 8 x 8 meter     | 2 meter               | € 285.000,-   | 3%               |
| Bungalow         | 11 x 7 meter    | 3 meter               | € 399.000,-   | 4%               |
| Mansion          | 12 x 10 meter   | 6 meter               | € 610.000,-   | 6%               |

## Aan de slag
Deze code is geschreven in [Python3](https://www.python.org/downloads/). De vereisten kunnen worden gevonden in requirements.txt of de packages kunnen geïnstalleerd worden door de onderstaande code in de terminal te kopiëren.

```
pip install -r requirements.txt
```

## Runnen
Om de code te runnen dient u in u terminal de volgende code in te voeren:
```
python main.py 
```
Er volgt dan een keuze menu waarbij je de volgende keuzes kan maken:
- Welke wijk (wijk1, wijk2, wijk3)
- Hoeveel huizen er worden geplaatst (20, 40, 60)
- Met welk algoritme de huizen worden geplaatst (random, random_greedy)
- Welk algoritme wil je gebruiken (hillclimber, hillclimber2)
- Hoeveel iteraties wil je maken

## Algoritme
#### Random
In het random algoritme worden de huizen doormiddel van random gegenereerde coordinaten geplaats.

#### Random + Greedy

#### Hillclimber

#### Hillclimber2

#### Aantal huizen
Voor de wijk is het mogelijk om een verschillend aantal maximum huizen te plaatsen. De opties hiervoor zijn: 20, 40 en 60.

#### Wijken
In de case is er keuzen uit drie wijken die onderling verschillen in de ligging van het water. Deze wijken zijn van links naar rechts: wijk1, wijk2 en wijk3.

<img src="/docs/wijk_1.png" width=30%> <img src="/docs/wijk_2.png" width=30%> <img src="/docs/wijk_3.png" width=30%>

#### Resultaten

