##########################################################
# Lorenzo Spera (lorenzo.spera@studenti.unipg.it)        #
#                                                        #
# Universià degli Studi di Perugia                       #
# Corso di Metodi Computazionali per la Fisica           # 
#---------------------------------------------------     #
# Progetto finale: Simulazione di uno sciame em          #
#                                                        #
# Script che implementa la simulazione realizzata        #
# nello script sciame_def.py. L'utente può selezionare   #
# i diversi parametri specificati nella simulazione e    #
# confrontare i risultati graficamente. La simulazione   #
# restituisce le grandezze richieste in una tabella e    #
# l'utente può decidere o meno se visualizzare i risulta #
# ti dal punto di vista grafico. Nello script è presente #
# una simulazione per il materiale acqua e per il silica #
# to di bismuto e una con dei valori diversi. L'utente   #
# può cambiare liberamente i valori ed eseguire varie    #
# simulazioni. Nella parte finale si trova il confronto  #
# per lo sviluppo dello sciame a partire da diversi      #
# valori dell'energia iniziale.                          #
##########################################################
import numpy as np 
import sys, os 

sys.path.append('//Users/lorenzospera/Desktop/Terzo_anno/MCF/github/Progetto-Finale-MCF/sciame_def.py')  # inserire il path del file sciame_def.py

# importare il modulo
import sciame_def
from sciame_def import sciame_elettromagnetico


"""
Valori di partenza scelti dall'utente:
    - energia iniziale 
    - energia critica del materiale
    - lunghezza di radiazione del materiale
    - passo di avanzamento (compreso tra 0 e 1)

    N.B = per ottimizzare la simulazione si consiglia di utilizzare dei valori per l'energia iniziale sufficientemente alti,
    ovvero dalle centinaia o migliaglia di MeV. Si tenga poi conto del fatto che la perdita di energia è proporzionale al passo di avanzamento s
    ; scegliendo s grande (sempre tra 0 e 1 ) aumenta la probabilità di produzione di coppia e di emissione (e quindi il numero di 
    particelle), ma, essendo la perdita di energia proporzionale ad s, questa sarà altrettanto grande e la simulazione potrebbe
    arrestarsi più velocemente.
"""

tipo_particella_iniziale  = 'Elettrone'       # selezionare il tipo di particella iniziale: 'Elettrone', 'Positrone', 'Fotone'
energia_utente = 600000                       # energia iniziale scelta dall'utente in MeV
passo_utente = 0.33                           # passo di avanzamento scelto dall'utente
lunghezza_radiazione_h2O = 36.08              # in cm 
lunghezza_radiazione_bso = 7.81               # in cm (1.097)

perdita_per_ionizzazione_h2O = energia_utente/(np.e*lunghezza_radiazione_h2O)     # in MeV/cm
perdita_per_ionizzazione_bso = energia_utente/(np.e*lunghezza_radiazione_bso)     # in Mev/cm

energia_critica_elettroni_h2O = 78.33   # in MeV
energia_critica_positroni_h2O = 76.24   # in MeV

energia_critica_elettroni_bso = 10.68   # in MeV
energia_critica_positroni_bso = 10.32   # in Mev 


# simulazione di una particella (tipo_particella) con energia E0 che genera lo sciame con parametri scelti dall'utente e quelli dei due materiali 

"""
Per la simulazione sciame utente, si è scelto un valore della perdita di energia molto più basso rispetto a quello dei materiali per 
effettuare un confronto con questi.
"""
sciame_utente = sciame_elettromagnetico(tipo_particella = tipo_particella_iniziale, E0 = energia_utente, Ec_elettroni=energia_critica_elettroni_bso
                                        ,Ec_positroni=energia_critica_positroni_bso
                                        ,dEx0 = energia_utente/4000, s = passo_utente, X0 = lunghezza_radiazione_h2O)

sciame1_bso  = sciame_elettromagnetico(tipo_particella = tipo_particella_iniziale, E0 = energia_utente, Ec_elettroni=energia_critica_elettroni_bso
                                        ,Ec_positroni=energia_critica_positroni_bso
                                        ,dEx0 = perdita_per_ionizzazione_bso, s = passo_utente, X0 = lunghezza_radiazione_bso)

sciame1_h2O = sciame_elettromagnetico(tipo_particella = tipo_particella_iniziale,E0 = energia_utente, Ec_elettroni=energia_critica_elettroni_h2O
                                      ,Ec_positroni=energia_critica_positroni_h2O
                                      ,dEx0 = perdita_per_ionizzazione_h2O, s = passo_utente, X0 = lunghezza_radiazione_h2O )

print("Simulazione per valori arbitrari scelti dall'utente. La simulazione potrebbe richiedere un pò di tempo: ")

sciame_utente.simulazione_sciame()

print('------------------------------------------------------------------------')
print("Simulazione per valori scelti dall'utente usando valori critici di H_2O. La simulazione potrebbe richiedere un pò di tempo: ")

sciame1_h2O.simulazione_sciame()

print('------------------------------------------------------------------------')
print("Simulazione per valori scelti dall'utente usando valori critici di BSO. la simulazione potrebbe richiedere un pò di tempo: ")

sciame1_bso.simulazione_sciame()


#------------------------------------------------------------------------------------#

"""
L'utente può poi confrontare l'andamento dello sviluppo longitudinale (in questo caso energia persa per 
ionizzazione ad ogni step e numero di particelle per step) per i due materiali partendo da 3 energie 
diverse tra di loro. Viene utilizzato il metodo confronta_sciame i cui parametri sono identici a quelli 
di simula sciame, ma devono essere aggiunte inizialmente le 3 energie iniziali e gli specifici valori per i 
materiali. Come esempio viene implementata la seguente simulazione con alcuni valori specifici.
L'utente può cambiare liberamente i valori e vedere come variano i risultati.
"""

energia_0 = 600000
energia_1 = 700000              # queste sono le 3 energie iniziali che l'utente può scegliere
energia_2 = 800000
passo_utente_2 = 0.55           # passo della simulazione scelto dall'utente

tipo_particella_2 = 'Elettrone' # selezionare il tipo di particella iniziale: 'Elettrone', 'Positrone', 'Fotone'

print('-------------------------------------------------------------------------------------------')
confronto_sciame = int(input("1 se si vuole effettuare il confronto a partire da energie diverse. 0 altrimenti: "))
if (confronto_sciame==1):

    """
    viene richiamato il metodo confronta sciame che mette a confronto tra di loro le simulazioni i cui parametri vengono
    specificati all'interno di quest'ultimo metodo. L'utente può sempre cambiare suddetti parametri.
    """
                                            
    sciame_elettromagnetico.confronta_sciame(tipo_particella = tipo_particella_2, E00 = energia_0, E01 = energia_1, E02 = energia_2,
                                            Ec_elettroni_h20 = energia_critica_elettroni_h2O, Ec_positroni_h20 = energia_critica_positroni_h2O,
                                            Ec_elettroni_bso = energia_critica_elettroni_bso, Ec_positroni_bso = energia_critica_positroni_bso,
                                            dEx0_h20 = perdita_per_ionizzazione_h2O, dEx0_bso = perdita_per_ionizzazione_bso,
                                            s = passo_utente_2, X0_h20 = lunghezza_radiazione_h2O, X0_bso = lunghezza_radiazione_bso)
else:
    print("Simulazione terminata.")

















