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
6. De wijk moet voor 20% uit oppervlaktewater bestaan, opgedeeld in niet meer dan vier lichamen. Om de wijk aantrekkelijk te houden, moeten de lichamen een hoogte-breedteverhoudingen tussen de 1 en de 4 liggen.

| Huizen           | Groote          | Vrijstand             | Waarde        | Prijsverbetering |
|------------------|-----------------|-----------------------|---------------|------------------|
| Eengezinswoning  | 8 x 8 meter     | 2 meter               | € 285.000,-   | 3%               |
| Bungalow         | 11 x 7 meter    | 3 meter               | € 399.000,-   | 4%               |
| Maison           | 12 x 10 meter   | 6 meter               | € 610.000,-   | 6%               |

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
- Welke wijk (wijk1, wijk2, wijk3, random water, greedy water)
- Hoeveel huizen er worden geplaatst (20, 40, 60)
- Met welk algoritme de huizen worden geplaatst (random, greedy, random greedy, genetic)
- Welk algoritme wil je gebruiken (None, hillclimber random, hillclimber step, hillclimber swap,  simulated annealing)
- Hoeveel iteraties wil je maken

## Algoritme
#### Random
In het random algoritme worden de huizen doormiddel van random gegenereerde coordinaten geplaats op de kaart zodra deze voldoen aan de restricties. Na een aantal iteraties te hebben uitgevoerd wordt de wijk met de hoogste score opgeslagen. 

#### Greedy
Het greedy algoritme plaats de huizen naar afnemende waarde: maison, bungalow, ééngezinswoning. Er wordt voor elk huis naar alle beschikbare x,y-coordinaten gekeken en het huis wordt geplaats op de positie die de hoogste wijk prijs oplevert. 

#### Random + Greedy
Het random greedy algoritme plaats huizen één voor één op een random locatie waarna het huis verplaatst wordt naar 400 verschillende locaties en het het huis uiteindelijk geplaatst wordt op de locatie die de hoogste waarde oplevert. De huizen worden verder geplaatst van meest waardevol naar minst waardevol (maison, bungalow en eengezinswoning).

#### Hillclimber random
Bij het hillclimber algoritme worden eerst alle huizen geplaatst (er kan worden gekozen volgens welk algoritme dit gebeurt), dan wordt er een random huis naar een random loctie verplaats. Als deze verplaatsing de totale prijs verhoogt wordt het huis daar neergezet. Echter als deze verplaatsing de totale prijs verlaagt wordt het huis weer teruggeplaatst naar de orginele locatie.

#### Hillclimber step
In deze versie van het hillclimber algoritme worden de huizen opnieuw allemaal geplaats volgens het gekozen algoritme. Een random huis wordt dan in een elke mogelijke richting verplaatst met stappen van 1 meter. Als door deze verplaatsing de  waarde van de wijk toeneemt blijven we het huis in die richting verplaatsen totdat het de wijkwaarde verlaagt.

#### Hillclimber swap
In de laatste hillclimber versie 


#### Simulated annealing
Het zwaktepunt van vele algoritmes, waaronder greedy en hillclimber, is dat er een lokaal optimum in plaats van een globaal optimum gevonden wordt. Om toch een globaal optimaal te kunnen vinden wordt bij simulated annealing soms ook een negatieve zet geaccepteerd. De kans waarmee een negatieve zet wordt geaccepteerd, wordt kleiner naarmate de tijd verstrijkt. Verder wordt de kans groter als het prijsverschil groter is om te zorgen dat er echt een grote stap genomen wordt in plaats van een klein zijstapje.  

#### Genetic


### Aantal huizen
Voor de wijk is het mogelijk om een verschillend aantal maximum huizen te plaatsen. De opties hiervoor zijn: 20, 40 en 60.

### Wijken
In de case is er keuzen uit drie wijken die onderling verschillen in de ligging van het water. Deze wijken zijn op de afbeelding te zien van links naar rechts: wijk1, wijk2 en wijk3. Verder is het ook mogelijk om een unieke wijk te creeëren. Dit kan doormiddel van bij de wijken te kiezen uit random_water of greedy_water. random_water plaats een random aantal waterlichamen (tussen de 1 en 4) op een random locactie. Bij greedy_water

<img src="/docs/images/wijk_1.png" width=30%> <img src="/docs/images/wijk_2.png" width=30%> <img src="/docs/images/wijk_3.png" width=30%>

## Resultaten
De resultaten de berekening zijn te vinden in het mapje results die een output.csv bevat met alle coordinaten van de objecten. Verder wordt er ook een kaart gemaakt die opgeslagen is al "prijs van de wijk".png, hierop is de indeling van de wijk te zien.

