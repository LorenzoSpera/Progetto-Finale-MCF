# Progetto-Finale-MCF

## Indice
1. [Contenuto](#contenuto)
2. [Esecuzione simulazione](#esecuzionesimulazione)
3. [Analisi dei risultati](#analisirisultati)
4. [Installazione pacchetti](#installazione)

### Contenuto

Repository contenente il progetto finale del corso di Metodi Computazionali per la Fisica (2023-2024) consistente nella simulazione
di uno sciame elettromagnetico partendo dal modello di Rossi. All'interno del repository sono presenti due script python: _sciame_def.py_
e _run_sciame.py_. Nel primo si trova la defizione delle varie classi usate per la realizzazione della simulazione; ovvero si hanno le 
classi che definiscono le particelle e una classe sciame in cui viene realizzata la simulazione secondo il modello richiesto. 

### Esecuzione simulazione 

Il risultato della simulazione e la presentazione dei risultati si trovano nel secondo file. Il primo script viene importato nel secondo
tramite la libreria _sys_. Una volta scaricati entrambi i file il primo viene importato nel secondo con il comando ```sys.path.append('path
del file sciame_def.py')```.Per eseguire la simulazione si può procedere come segue:
* si scelgono i parametri della simulazione, tipo della particella iniziale, 
    energia della particella, energia critica dei materiali, perdita di energia per ionizzazione, 
    passo di avanzamento  e lunghezza di radiazione del materiale.
* nella parte iniziale dello script sono già presenti due simulazioni: una per i due materiali (acqua e silicato di bismuto) con valori
ricavati dal particle data group e l'altra con dei valori diversi per effettuare un confronto.
* l'utente può liberamente cambiare tali parametri.
* una volta eseguita la simulazione viene stampata l'energia persa per ionizzazione dopo l'intero processo e 
    le grandezze richieste vengono riportate in una tabella. 
* tali grandezze vengono studiate anche graficamente con l'aggiunta di alcuni grafici per analizzare a pieno il
    fenomeno fisico. Viene specificato il contenuto di ogni grafico e viene chiesto all'utente se vuole visualizzarlo
    inserendo il rispettivo comando indicato.
### Analisi dei risultati
Nell'ultima parte è poi presente il confronto tra simulazioni con energie diverse per i materiali. Per velocizzare la visualizzazione
si consiglia di inserire 0 ogni volta che viene chiesto se si vogliono visualizzare i risultati eccetto quando viene esplicitamente
citato il confronto tra le simulazioni.
Nella repository è inoltre presente un file .pdf che mi è stato utile nella realizzazione della simulazione (per tenere conto
dei vari punti) e soprattutto nel confronto dei risultati ottenuti. Il file delinea la struttura della simulazione e descrive i
risultati ottenuti per varie simulazioni, concentrando la trattazione sulla sensibilità della simulazione rispetto alle grandezze 
e i parametri che possono essere variati. Dato che il codice è stato aggiornato, per effettuare un confronto con i nuovi risultati, 
è stata aggiunta una sezione al file .pdf rimuovendone due relative alla simulazione del codice non aggiornato che riporava
alcune inconsistenze.

### Installazione pacchetti

Per la visualizzazione delle grandezze richieste è stata utilizzata la libreria _rich_ di Python. Se tale libreria non dovesse già essere installata
ci si sposti nella cartella di lavoro e si proceda con l'installazione da terminale secondo il seguente comando:
```
pip install rich
```
Per l'installazione si richiede una versione di Python pari o superiore alla 3.7.