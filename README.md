# Gridmeisters

## Smartgrid case
Minor programmeren theorie. opdracht: SmartGrid.

### vereisten

python -m pip install -U matplotlib

## Gebruik

Invoer: python3 main.py data/dist1_b.csv data/dist1_h.csv

Kies 1 voor het random algoritme
Kies 2 voor de hillcimber
Kies 3 voor Constraint relaxation
Kies 4 voor Multiple time
Please select an algorithm to run: 1 = Randomize, 2 = HillClimber and 3 = Constraint relaxation 4 = Multiple times algorithm 3 5 = Multiple times algorithm 4

### Random algoritme
Verbind de huizen random aan een batterij. Hierin wordt wel rekening gehouden met de capaciteit

### Hillclimber algoritme
Verbind huizen op de korste mannier aan een batterij en zoekt hierin vervolgens verbeteringen. 

### Constraint relaxation algoritme
Lost het eerst simpel op, door de huizen aan de dichtsbijzijnde batterij te koppelen. Vervolgens wordt hier naar een voordeligere oplossing gezocht door de huizen op een voordelige mannier te verbinen. Hierin wordt optimaal gebruik gemaakt van het delen van de kabels.