# Progetto-Finale-MCF
Repository contente il progetto finale del corso di Metodi Computazionali per la Fisica (2023-2024) consistente nella simulazione
di uno sciame elettromagnetico partendo dal modello di Rossi. All'interno del repository sono presenti due script python: sciame_def.py
e run_sciame.py. Nel primo si trova la defizione delle varie classi usate per la realizzazione della simulazione; ovvero si hanno le 
classi che definiscono le particelle e una classe sciame in cui viene realizzata la simulazione secondo il modello richiesto. 
Il risultato della simulazione e la presentazione dei risultati si trovano nel secondo file. Il primo script viene importato nel secondo
tramite la libreria sys. Una volta scaricati entrambi i file il primo viene importato nel secondo con il comando sys.path.append('path
del file sciame_def.py'). Per eseguire la simulazione si può procedere come segue:
    - si scelgono i parametri della simulazione, tipo della particella, energia della particella,
    energia critica dei materiali, perdita di energia per ionizzazione, passo di avanzamento 
    e lunghezza di radiazione del materiale.
    - nello scirpt è già presente una simulazione per entrambi i materiali (acqua e silicato di bismuto) con i rispettivi valori 
    indicati nella richiesta e ricavati dal particle data group.
    - l'utente può liberamente cambiare tali parametri.
    - una volta eseguita la simulazione viene stampata l'energia persa per ionizzazione dopo l'intero processo e 
    le grandezze richieste vengono riportate in una tabella. 
    - tali grandezze vengono studiate anche graficamente con l'aggiunta di alcuni grafici per analizzare a pieno il
    fenomeno fisico. Viene specificato il contenuto di ogni grafico e viene chiesto all'utente se vuole visualizzarlo
    inserendo il rispettivo comando indicato.

Nella repository è inoltre presente un file .pdf che mi è stato utile nella realizzazione della simulazione (per tenere conto
dei vari punti) e soprattutto nel confronto dei risultati ottenuti. Il file delinea la struttura della simulazione e descrive i
risultati ottenuti per varie simulazioni, concentrando la trattazione sulla sensibilità della simulazione rispetto alle grandezze 
e i parametri che possono essere variati.
