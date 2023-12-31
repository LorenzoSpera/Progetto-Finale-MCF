# Progetto-Finale-MCF
Repository contenente il codice relativo al progetto finale del corso di Metodi Computazionali 2023-2024 e relative istruzioni.
Nella repository sono presenti due script: sciame_def.py e run_sciame.py. All’interno del primo sono definite le varie classi e metodi che permettono la realizzazione della simulazione. Il secondo script viene invece usato per implementare la simulazione cambiando i vari parametri in entrata in accordo con la richiesta. Il primo viene importato nel secondo tramite l’utilizzo della libreria sys tramite il comando sys.path.append (‘percorso del file sciame_def.py’). In questo secondo script sono già state definite delle simulazioni per l’analisi delle grandezze da studiare (l’utente può in ogni caso modificare i parametri iniziali come desidera). La simulazione e la presentazione dei risultati procedono come segue:

	- l’utente seleziona i valori di partenza, scegliendo la particella che genera lo sciame, la sua energia, l’energia critica del materiale (per elettroni e positroni), la perdita di energia e il passo di avanzamento della simulazione.

	- il programma restituisce le grandezze richieste. Innanzitutto viene stampata l’energia totale persa per ionizzazione. Poi, in un apposita tabella vengono riportate le altre grandezze per ogni step (numero delle particelle, energia persa per ionizzazione).

	- le grandezze vengono analizzate anche graficamente; l’utente può decidere di visualizzare o meno i rispettivi grafici di cui viene sempre specificato il contenuto.


La prima simulazione viene fatta a partire da dei parametri che ottimizzano il processo. Le simulazioni successive sono volte allo studio dei due materiali indicati con la procedura illustrata.
Nella repository è poi presente un file PDF che mi è stato utile nell’analisi dei dati e nel tenere conto dello sviluppo della simulazione. Dato che i materiali vengono analizzati in simulazioni diverse, in questo file PDF viene sinteticamente riportato un confronto e una linea generale di discussione dei risultati per le simulazioni che si trovano nello script e che l’utente può consultare liberamente.
