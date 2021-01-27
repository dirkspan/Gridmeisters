# Gridmeisters

## Smartgrid case
Minor programmeren: Programmeertheorie. Opdracht: SmartGrid. Steeds meer mensen hebben zonnepanelen en produceren dus ook hun eigen energie. Hier komt echter wel bij dat er een overschot kan zijn. Het overschot wordt terugverkocht aan de leverancier. In deze case wordt het probleem van de grid managen worden opgelost. Er moeten batterijen zijn om de pieken in consumptie en produktie te te kunnen managen. In deze case moeten de huizen op een zo voordelige manier aan de batterijen verbonden worden, zonder dat de capaciteit wordt overschreden. Er moet betaald worden per stukje grid dat gelegd wordt. Hoe minder kabels er gelegd hoeven te worden hoe voordeliger de oplossing. 


### vereisten

python -m pip install -U matplotlib

#### Gebruik

Invoer: python3 main.py data/dist1_b.csv data/dist1_h.csv

Kies 1 voor het random algoritme
Kies 2 voor de hillcimber
Kies 3 voor Constraint relaxation
Kies 4 voor Multiple time
Please select an algorithm to run: 1 = Randomize, 2 = HillClimber and 3 = Constraint relaxation 4 = Multiple times algorithm 3 5 = Multiple times algorithm 4

### Random algoritme
Verbind de huizen random aan een batterij. Hierin wordt wel rekening gehouden met de capaciteit

### Hillclimber algoritme
Verbind huizen op de korste manier aan een batterij en zoekt hierin vervolgens verbeteringen. 

### Constraint relaxation algoritme
Lost het eerst simpel op, door de huizen aan de dichtsbijzijnde batterij te koppelen. Vervolgens wordt hier naar een voordeligere oplossing gezocht door de huizen op een voordelige mannier te verbinen. Hierin wordt optimaal gebruik gemaakt van het delen van de kabels.