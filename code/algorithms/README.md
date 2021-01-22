In dit wordt elk algoritme verder uitgelegd en worden de gekozen parameters toegelicht.

## Random

## Random + Greedy

## Greedy

## Random Water

## Greedy Water

## Hillclimber 1
De eerste versie van hillclimber maakt gebruik van random plaatsing. Een random huis wordt geselecteerd en op een random valide plek gezet. Als deze plek de totale prijs hoger maakt, blijft het huis staan. Als de totale prijs lager wordt, wordt het huis teruggezet. Dit principe wordt herhaald voor 20000 iteraties. Na ongeveer 20000 iteraties convergeert de prijs zoals ook te zien is in de grafiek. Minimale winst kan nog gehaald worden door het aantal iteraties te verhogen, maar deze tijd kan veel beter gebruikt worden om het algoritme meerdere keren te herhalen. In de grafiek is namelijk ook te zien dat de prijs per iteratie erg varieert, wat aantoont dat de uiteindelijke prijs sterk afhankelijk is van de initiele plaatsing van de huizen.

<img src="../../docs/images/hillclimber1.png" width=60%> 

## Hillclimber 2

## Hillclimber 3

## Simulated annealing
Het simulated annealing algoritme kan uitgevoerd worden met hillclimber1, hillclimber2 en hillclimber3. Het algoritme wordt normaal uitgevoerd, maar in plaats van alleen bij een hogere prijs de verandering te accepteren, wordt een negatieve verandering ook geaccepteerd met een bepaalde kans.


Deze kans wordt gegeven door de volgende formule:<br><br>
<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\large&space;P&space;=&space;e^{\frac{-dE}{T}}" title="\large P = e^{\frac{-dE}{T}}" />,

waar dE het prijsverschil is (new_price - old_price), en T de huidige temperatuur. 


## Genetic
