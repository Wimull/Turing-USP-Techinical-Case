# Turing.USP Technical Case
My solutions for the test cases for Turing USP admission. Covers Intermediate Logic tests and Data Analysis Level 1 tests
# Logic Tests
## Q1 _Vaca Magras no Turing_
### Q1A
You're given an array with a list of emails, each to be compared with the previous and removed the same initial letters if any, then your function, called _conta_economia()_ needs to return the letters removed by this method. Every email is the same length and shares the _@usp.br_ at the end.

```
conta_economia(["aninha123@usp.br","aninhazinha000@usp.br","aninhazinhainha@usp.br","jerson331@usp.br","jersaopika@usp.br","aninhaeudnv@usp.br"]
returns 21
```

### Q1B
You're given an list of scrabbled emails with some corruped ones and your function, _corrige_emails()_, needs do return an array with the original emails or _ERRO_ if it was corrupted. Every email has it order reversed and starting index randomized. Also, each original email ends with _@usp.br_. 
```
corrige_emails( [ "aninha@usp.br", "ibol.alimacrb.psu@ocna", "t.alalalimacrb.repsu@ppo", ".orbmem_ovonrb.psu@gnirut"])
returns ['aninha@usp.br', 'camila.lobianco@usp.br', 'ERRO', 'novo_membro.turing@usp.br']
```
## Q2 _Estacionamento do Nelnelson_
### Q2A
You are working with a 1-dimentional parking-lot and are given its size as well as an array cotaining the order of entry and exit of a car noted by a int, positive number for the car _n_ entering, negative for the car exiting. Your job is to validate this set of instruction, that is, that the car in the parking lot doesn't exceed its size and that no car may pass through one another to exit. Your fuction, _estacionamento_ok()_ should return _sim_ if no incongruence has been found, and _não_ if it has found any.
```
estacionamento_ok(3,[1,2,-2,3,-3,-1])      
returns "sim"
```
### Q2B
That 1-D parking lot now has a new exit on its back and now every _T_ moment a car is in there it moves a step closer to the exit, exiting when it has to move away from the parking lot. Your job is, given its size, an matrix with the id of each car and the moment entry, and a given moment, your function, _estado_atual()_, needs to return an array with the state of the parking lot at the given moment, using the id of a car to represent its position, and _0_ if empty. Assume no car enters at the same time.
```
estado_atual(4, [1,4,6,2], 7)              
returns [0, 3, 0, 2]
```
## _Desafio Amizades do Turing_
You're tasked with finding each unique group in a list of people, each with its unique list of relationship. Your input is an int tha represents how many people there are to be checked, and a matrix, representing a relationship, wich is made up of the id of a pearson and the id of another pearson. Your function, _micro_grupos()_ should then return an int representing how many groups, that is each relationship circle, there are in that list.
```
micro_grupos(7, [[1,2],[2,3],[3,1],[3,4],[6,5],[5,7]]))
returns 2
```
# Data Analysis
You're tasked with making a simple analysis, in portuguese, of the _adult.csv_ dataset with the values:<br>
    1. **age** <br>
    2. **workclass**<br>
    3. **fnlwgt** _final weight_<br>
    4. **education** <br>
    5. **educational-num** <br>
    6. **marital-status** <br>
    7. **occupation**<br>
    8. **relationship** <br>
    9. **race**<br>
    10. **gender** <br>
    11. **capital-gain** <br>
    12. **capital-loss**<br>
    13. **hours-per-week**<br>
    14. **native-country** <br>
    15. **income** <br>
and find the correlations between data to the target _income_.

