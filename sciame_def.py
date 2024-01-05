#########################################################
# Lorenzo Spera (lorenzo.spera@studenti.unipg.it)       #
#                                                       #
# Universià degli Studi di Perugia                      #
# Corso di Metodi Computazionali per la Fisica          #
#---------------------------------------------------    #
# Progetto finale: Simulazione di uno sciame em         #
#                                                       #
# Script contenente la definizione delle classi che     #
# vengono create all'interno dello sciame: elettroni,   #
# fotoni e positroni specificando l'energia della       #
# particella. Lo script contiene anche la classe        #                 
# sciame_elettromagnetico con il metodo init che        #
# prende  in input i vari parametri e il metodo         #
# simula_sciame che simula lo sciame elettromagneti     #
# co restituendo le grandezze richieste. E' inoltre     #      
# presente il metodo confronta sciame che, a partire    #
# dal metodo return array, esegue il confronto tra      #  
# simulazionoi partendo da 3 energie diverse impostate  #
# dall'utente.                                          # 
#########################################################

import numpy as np 
from scipy import constants
from rich.console import Console
from rich.table import Table
import matplotlib.pyplot as plt
import scipy 
from scipy import optimize


m_e = constants.m_e                    # massa dell'elettrone
                 
c = constants.c * 1e02                 # velocità della luce nel vuoto in cm


class Fotone:

    """
    classe che definisce una particella di tipo fotone
    specificandone l'energia 

    """

    def __init__(self, energia):
        self.energia = energia

class Elettrone:

    """
    classe che definisce una particella di tipo elettrone
    specificandone l'energia
    
    """

    def __init__(self, energia):
        self.energia = energia

class Positrone:

    """
    classe che definisce una particella di tipo positrone
    specificandone l'energia
    
    """
    def __init__(self, energia):
        self.energia = energia


class sciame_elettromagnetico:

    """
    classe che definisce lo sciame_elettromagnetico(E0, Ec, dEx0, s)
    
    Parametri input:
        E0 : energia iniziale della particella 
        Ec : energia critica del materiale (sia per elettroni che positroni dato che possono variare ) 
        dEx0 : perdita per ionizzazione in una lunghezza di radiazione
        s: passo di avanzamento, espresso in frazioni di X_0 con 0<= s <= 1

    Attributi:
    _E0
    _Ec_elettroni
    _Ec_positroni
    _dEx0
    _s
    _tipo_particella : specifica il tipo di particella scelto dall'utente
    particelle : inserisce la particella iniziale specificandone l'energia
    energia_persa_per_step e numero_particelle_per_step servono per il conteggio delle particelle
    e dell'energia 
    """

    def __init__(self,tipo_particella, E0, Ec_elettroni, Ec_positroni, dEx0, s, X0):

        self._tipo_particella = tipo_particella
        self._E0 = E0
        self._Ec_elettroni = Ec_elettroni
        self._Ec_positroni = Ec_positroni
        self._dEx0 = dEx0
        self._s = s
        self._X0 = X0
        self.particelle = [{'tipo': self._tipo_particella, 'energia': E0}]
        self.energie_persa_per_step = []
        self.numero_particelle_per_step = [] 
        self.array_passi = []
        
        
    
    def simulazione_sciame(self):
        """

        Metodo della classe che implementa la simulazione dello sciame secondo il modello richiesto
        tenendo conto del numero di step, energia persa ad ogni step, numero di particelle e calcolo
        dell'energia totale persa per ionizzazione.

        """

        energia_ionizzazione_totale = 0             # energia persa per ionizzazione dopo l'intero processo 
        step = 0
        energia_particella = self._E0
        somma = 0

        check = 0                                    # condizione per l'arresto dello sciame 
        energie = self.energie_persa_per_step        # array contente le energie perse per step
        n_elettroni_totali = []                      # array contenente il numero di elettroni per step
        n_positroni_totali = []                      # array contenente il numero di positroni per step
        n_fotoni_totali = []                         # array contenente il numero di fotoni per step
        somma_particelle = []                        # array contenente il numero di particelle totali per step
        array_passi =  self.array_passi              # array contenente il numero di step
        array_distanze = []                          # array contenente le profondità relativa ad ogni step
        energia_corrente = self._E0 
        array_energia_corrente = []                  # array contenente le energie correntiì
        
        

        while energia_particella > 0:

            step += 1                                # lo step viene incrementato di 1 
            distanza= step*self._s                   # calcolo della distanza percorsa
            array_passi.append(step)
            array_distanze.append(distanza)
            nuove_particelle = []                    # lista che viene aggiornata ad ogni iterazione
            
            n_elettroni = 0 
            n_fotoni = 0 
            n_positroni = 0 
            energia_persa_per_step = 0
            
            
            for particella in self.particelle:
                
                
                tipo_particella = particella['tipo']
                energia_particella = particella['energia']
            
                
                if tipo_particella == 'Elettrone':
                    if energia_particella > (self._dEx0*self._s):

                        perdita_energia = self._dEx0*self._s
                        energia_persa_per_step += perdita_energia
                        nuova_energia = energia_particella - perdita_energia
                        n_elettroni += 1

                        """ 
                        in questo caso si controlla la seconda condizione sull'energia
                        dell'elettrone, ovvero sulla possibilità di emissione di un fotone

                        """
                        
                        
                        if nuova_energia > self._Ec_elettroni:

                            probabilità = 1-np.exp(-self._s) #-self._s
                            
                            if (np.random.uniform() < probabilità):
                                nuove_particelle.append({'tipo': 'Fotone', 'energia': nuova_energia/2})
                                nuove_particelle.append({'tipo': 'Elettrone', 'energia': nuova_energia/2})
                                somma += 2 
                                n_fotoni +=1 
                            else:
                                nuove_particelle.append({'tipo': 'Elettrone', 'energia': nuova_energia})
                                somma +=1
                                
                        else:
                            check = 1
                                        
                    else:

                        """
                        l'elettrone deve depositare per ionizzazione un valore 
                        casuale all'interno dell'intervallo [0,E]
                        """

                        energia_depositata = np.random.uniform(low = 0, high= energia_particella)
                        energia_persa_per_step += energia_depositata
                        check = 1
                         
                        
                       
                
                elif tipo_particella == 'Fotone':
                    if energia_particella > 2* m_e*c**2:

                        n_fotoni +=1 
                        probabilità_gamma = 1 - np.exp(-(7/9)*self._s)  #-self._s
                        
                        if (np.random.uniform() < probabilità_gamma):

                            """
                            in questo caso si ha la produzione di una coppia 
                            elettrone positrone
                            """

                            nuove_particelle.append({'tipo': 'Elettrone', 'energia': energia_particella/2})
                            nuove_particelle.append({'tipo': 'Positrone', 'energia': energia_particella/2})
                            somma += 2
                            n_elettroni += 1
                            n_positroni += 1
                            n_fotoni -= 1 
                        else:
                            nuove_particelle.append({'tipo': 'Fotone', 'energia': energia_particella})
                            somma +=1 
                    
                    else:

                        """ 
                        il fotone deposita per ionizzazione un valore casuale 
                        all'interno dell'intervallo [0,E]
                        """
                        energia_depositata_gamma = np.random.uniform(low = 0, high=energia_particella)
                        energia_persa_per_step += energia_depositata_gamma
                        
                        check = 1
                         

                else: #tipo_particella == 'Positrone':
                    if energia_particella > self._dEx0*self._s:
                        
                        perdita_energia_positrone = self._dEx0*self._s
                        energia_persa_per_step += perdita_energia_positrone
                        nuova_energia = energia_particella - perdita_energia_positrone
                       
                        """ 
                        in questo caso si controlla la seconda condizione sull'energia
                        del positrone, ovvero sulla possibilità di emissione di un fotone
                        """
                        
                        if nuova_energia > self._Ec_positroni:

                            n_positroni += 1 
                            probabilità = 1-np.exp(-self._s)  #-self._s

                            if (np.random.uniform() < probabilità):
                                nuove_particelle.append({'tipo': 'Fotone', 'energia': nuova_energia/2})
                                nuove_particelle.append({'tipo': 'Positrone', 'energia': nuova_energia/2})
                                somma += 2
                                n_fotoni +=1 
                            else:
                                nuove_particelle.append({'tipo': 'Positrone', 'energia': nuova_energia})
                                somma += 1 
                        else:
                            check = 1

                    else:

                        """
                        il positrone deve depositare per ionizzazione un valore 
                        casuale all'interno dell'intervallo [0,E]
                        """
                        
                        energia_depositata_positrone = np.random.uniform(low = 0, high = energia_particella)
                        energia_persa_per_step += energia_depositata_positrone   
                        check = 1
                        
                if check == 1:
                    break
                
                        
                
            if check == 1:
                break 
                      
            
            """
                - la lista di particelle deve essere aggiornata ad ogni step
                - si deve tenere conto dell'energia persa ad ogni step 
                - si deve tenere conto del numero di particelle ad ogni step
                - si deve tenere conto dell'energia totale persa

            """
            energia_corrente -= energia_persa_per_step
            self.particelle = nuove_particelle   
            self.numero_particelle_per_step.append(len(self.particelle))
            energie.append(energia_persa_per_step)
            n_elettroni_totali.append(n_elettroni)
            n_fotoni_totali.append(n_fotoni)
            n_positroni_totali.append(n_positroni)
            somma_particelle.append(n_elettroni+n_fotoni+n_positroni)
            array_energia_corrente.append(energia_corrente)
            
            


            
        energia_ionizzazione_totale = np.sum(energie)
        
            
        print('------------------------------------------------')
        print("L'energia totale persa per ionizzazione dopo l'intero processo è : ",energia_ionizzazione_totale, " MeV")
        print('------------------------------------------------')
        print('------------------------------------------------')
        print("L'energia residua alla fine del processo è : ", self._E0-energia_ionizzazione_totale, " MeV")
        print('------------------------------------------------')
        



        console = Console()

        # Dati delle colonne
        colonna1 = [ str(i) for i in range(step) ]
        colonna2 = [ str(i) for i in n_elettroni_totali]
        colonna3 = [ str(i) for i in n_fotoni_totali]
        colonna4 = [ str(i) for i in n_positroni_totali]
        colonna5 = [ str(i) for i in somma_particelle]
        colonna6 = [ str(i) for i in energie]

        

        # Creazione della tabella
        table = Table(title= "Grandezze nel corso dello sciame ")

        # Aggiunta delle colonne
        table.add_column("Step", justify="center", style="cyan", no_wrap=True)
        table.add_column(" # elettroni", justify="center", style="magenta", no_wrap=True)
        table.add_column("# fotoni", justify="center", style="yellow", no_wrap=True)
        table.add_column("# positroni", justify="center", style="red", no_wrap=True)
        table.add_column("# particelle totali", justify="center", style="green", no_wrap=True)
        table.add_column("Energia persa (MeV)", justify="center", style="purple", no_wrap=True)
        

        # Aggiunta dei dati alla tabella
        for i in range(len(n_elettroni_totali)):
            table.add_row(colonna1[i], colonna2[i], colonna3[i], colonna4[i], colonna5[i], colonna6[i])

        # Stampa della tabella
        console.print(table)

        """
        Di seguito si riportano i grafici che mostrano l'andamento:
            - dell'energia persa per ionizzazione ad ongi step
            - del numero di fotoni, elettroni, positroni e particelle totali ad ogni step

        Poi si eseguono le simulazioni per i due diversi materiali variando i possibili parametri, 
        in particolare studiando l'andamento in funzione dell'energia
        """
        grafici = int(input("1 per visualizzare i risultati graficamente. 0 altrimenti: "))
        if grafici == 1:
            #grafico dell'energia persa per step
            grafico_energia_per_step = int(input("1 per visualizzare l'andamento dell'energia persa per step. 0 altrimenti: "))
            if (grafico_energia_per_step == 1):
                plt.figure(figsize = [10,8])
                plt.title("Energia persa con $E_0$ = {:.0f} MeV, s = {:.3f}, $E_c(e^-)$ = {:.2f} MeV, $E_c(e^+)$={:.2f} MeV e $dEx_0$ = {:.2f} (MeV/m)".format(self._E0, self._s, self._Ec_elettroni,self._Ec_positroni, self._dEx0), c='darkred', fontsize = 10)  
                plt.plot(array_passi[:-1], energie, "+", c='red' , label='Energia persa per step')
                plt.plot(array_passi[:-1], energie, "--", c='blue' )
                plt.xlabel('Numero di step')
                plt.ylabel('Energia depositata per ionizzazione (MeV)')
                plt.legend(loc='upper right')
                
                plt.show()

            # grafico del numero di particelle per step
                
            grafico_particelle_per_step = int(input("1 per visualizzare l'andamento del numero di particelle per step. 0 altrimenti: "))
            if grafico_particelle_per_step == 1:
                fig , ax  = plt.subplots(2, 2, figsize = [10,8]) 
                fig.suptitle("Numero delle particelle con $E_0$ = {:.0f} MeV, s = {:.3f}, $E_c(e^-)$ = {:.2f} MeV, $E_c(e^+)$={:.2f} MeV e $dEx_0$ = {:.2f} (MeV/m)".format(self._E0, self._s, self._Ec_elettroni,self._Ec_positroni, self._dEx0), c='darkred', fontsize = 10)            
                ax[0][0].plot(array_passi[:-1], n_elettroni_totali, "+",label ='# elettroni per step', c='blue')
                ax[0][0].plot(array_passi[:-1], n_elettroni_totali, "--", c ='red')
                ax[0][1].plot(array_passi[:-1], n_fotoni_totali,"+", label ='# fotoni per step', c='orangered')
                ax[0][1].plot(array_passi[:-1], n_fotoni_totali,"--", c='steelblue')
                ax[1][0].plot(array_passi[:-1], n_positroni_totali, "+", label ='# positroni per step', c='mediumblue')
                ax[1][0].plot(array_passi[:-1], n_positroni_totali, "--",  c='gray')
                ax[1][1].plot(array_passi[:-1], somma_particelle,"+", label ='# particelle per step', c='chocolate')
                ax[1][1].plot(array_passi[:-1], somma_particelle,"--", c='forestgreen')
                ax[0][0].set_ylabel('Numero di elettroni')
                ax[1][0].set_ylabel('Numero di positroni')
                ax[0][1].set_ylabel('Numero di fotoni')
                ax[1][1].set_ylabel('Numero di particelle totali')
                for i in range(0,2):
                    for j in range(0,2):
                        ax[i][j].legend(loc='upper left')
                        ax[i][j].set_xlabel('Numero di step')
                
                plt.show()
            
        
            def test_function(x,X_0):
                """
                Funzion di fit per il numero di particelle ad ogni step:
                    - x è l'array contenenti i passi (distanze percorse)
                    - X_0 è la lunghezza di radiazione caratteristica del materiale
                """
                return 2**(x/X_0)
            

            # fit con gli array completi
            params1, params_covariance1 = optimize.curve_fit(test_function, xdata=array_passi[:-1], ydata=somma_particelle)
            fit_del_numero_di_particelle_completo= int(input("1 per visualizzare il fit del numero delle particelle per step. 0 altrimenti: "))
            if (fit_del_numero_di_particelle_completo == 1):
                plt.figure(figsize=[10,8])
                plt.title("Fit numero particelle con $E_0$ = {:.0f} MeV, s = {:.3f}, $E_c(e^-)$ = {:.2f} MeV, $E_c(e^+)$={:.2f} MeV e $dEx_0$ = {:.2f} (MeV/m)".format(self._E0, self._s, self._Ec_elettroni,self._Ec_positroni, self._dEx0), c='darkred', fontsize = 10)  
                plt.plot(array_passi[:-1], somma_particelle, "+", c='darkred', label = 'Data')
                plt.plot(array_passi[:-1], test_function(array_passi[:-1], params1[0]), c='blue', label='Fit')
                plt.legend(loc = 'upper left')
                plt.xlabel('Numero di step')
                plt.ylabel('Numero di particelle')
                
                plt.show()

            # grafico fit con rapporti
            # Valore funzione fit ottimizzata in corrispondneza degli step
                
            yfit = test_function(array_passi[:-1], params1[0])
            """
                Dato che il numero di particelle è il risultato di un conteggio, l'errore associato 
                al risultato è dato dalla radice quadrata del numero di conteggi
            """
            
            yerr = []
            for numero in somma_particelle:
                yerr.append(np.sqrt(numero))
            grafico_fit_con_scarti = int(input("1 per visualizzare il grafico del fit con l'aggiunta dei rapporti. 0 altrimenti:")) 
            if grafico_fit_con_scarti == 1:

                # Grafico con due subplot

                fig, ax = plt.subplots(2,1, figsize=[10,8], gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
                fig.subplots_adjust(hspace=0)

                # Grafico subplot 0 (dati e funzione di fit)
                ax[0].set_title('Fit Esponenziale $2^t$', fontsize=10, color='darkred')
                ax[0].errorbar(array_passi[:-1],  somma_particelle,  yerr=yerr, color='darkred',fmt='o', 
                            label='Data',capsize=5, ecolor ='gray', elinewidth = 1, capthick = 0.5 )
                ax[0].plot(    array_passi[:-1], yfit,            color='blue' ,        label='Fit  $\sigma_y$')
                ax[0].set_ylabel('Numero di particelle', fontsize=14)
                ax[0].tick_params(axis="y", labelsize=14) 
                ax[0].legend(fontsize=14, loc='upper left')
                

                # Grafico subplot 1 (rapporto dati / funzione di fit)
                ax[1].errorbar(array_passi[:-1],  somma_particelle/yfit, yerr=yerr/yfit, fmt='o', color='darkred',
                            capsize=5, ecolor ='gray', elinewidth = 1, capthick = 0.5 )
                ax[1].axhline(1, color='blue') 
                ax[1].set_xlabel('Numero di step', fontsize =14)
                ax[1].set_ylabel('Dati/Fit',  fontsize =14)
                ax[1].tick_params(axis="x",   labelsize=14) 
                ax[1].tick_params(axis="y",   labelsize=14) 
                #ax[1].set_ylim(0.5,1.5)       
                #ax[1].set_yticks(np.arange(0.5, 1.51, 0.25))
                ax[1].grid(True, axis='y')
                
                plt.show()

            # grafico dell'energia residua ad ogni step 
            
            grafico_energia_residua_step = int(input("1 per visualizzare l'energia residua per step. 0 altrimenti: "))
            if (grafico_energia_residua_step == 1):
                plt.figure(figsize=[10,8])
                plt.title("Energia residua con $E_0$ = {:.0f} MeV, s = {:.3f}, $E_c(e^-)$ = {:.2f} MeV, $E_c(e^+)$={:.2f} MeV e $dEx_0$ = {:.2f} (MeV/m)".format(self._E0, self._s, self._Ec_elettroni,self._Ec_positroni, self._dEx0), c='darkred', fontsize = 10)
                plt.plot(array_passi[:-1], array_energia_corrente, "+", c='red', label='Energia ad ogni step')
                plt.plot(array_passi[:-1], array_energia_corrente, "--", c='blue')
                plt.xlabel('Numero di step')
                plt.ylabel('Energia(MeV)')
                plt.legend(loc = 'upper right')
                
                plt.show()

            # grafico dell'energia residua in scala logaritmica
            grafico_energia_residua_step_log = int(input("1 per visualizzare l'energia residua per step in scala logaritmica. 0 altrimenti: "))
            if (grafico_energia_residua_step_log == 1):
                plt.figure(figsize=[10,8])
                plt.title("Energia residua con $E_0$ = {:.0f} MeV, s = {:.3f}, $E_c(e^-)$ = {:.2f} MeV, $E_c(e^+)$={:.2f} MeV e $dEx_0$ = {:.2f} (MeV/m)".format(self._E0, self._s, self._Ec_elettroni,self._Ec_positroni, self._dEx0), c='darkred', fontsize = 10)
                plt.plot(array_passi[:-1], array_energia_corrente, "+", c='red', label='Energia ad ogni step')
                plt.plot(array_passi[:-1], array_energia_corrente, "--", c='blue')
                plt.xlabel('Numero di step')
                plt.ylabel('log(Energia(MeV))')
                plt.yscale('log')
                plt.legend(loc = 'upper right')
                
                plt.show()

        
            # distribuzione dell'energia depositata per ionizzazione
            distribuzione_energia_depositata = int(input("1 per visualizzare la distribuzione dell'energia depositata. 0 altrimenti: "))
            if distribuzione_energia_depositata == 1:
                plt.figure(figsize=[10,8])
                plt.title("Energia depositata durante il processo con $E_0$ = {:.0f} MeV, s = {:.3f}, $E_c(e^-)$ = {:.2f} MeV, $E_c(e^+)$={:.2f} MeV e $dEx_0$ = {:.2f} (MeV/m)".format(self._E0, self._s, self._Ec_elettroni,self._Ec_positroni, self._dEx0), c='darkred', fontsize = 10)
                n , bins, p = plt.hist(energie, bins = int(np.sqrt(len(energie))), color='blue', label ='Energia depositata')
                plt.xlabel('Energia depositata (MeV)')
                plt.ylabel('Eventi/bins')
                plt.legend(loc = 'upper right')
                
                plt.show() 

        else:
            print("Simulazione terminata.")


    def return_array(self):

        """
        Metodo che restituisce l'array contenente gli step percorsi, il numero di particelle ad ogni step
        e l'energia persa per ionizzazione ad ogni step.
        """

        return self.array_passi, self.numero_particelle_per_step, self.energie_persa_per_step 
    
    def confronta_sciame(tipo_particella, E00, E01, E02, Ec_elettroni_h20, Ec_positroni_h20,
                        Ec_elettroni_bso, Ec_positroni_bso, dEx0_h20, dEx0_bso, s, X0_h20, X0_bso):
        
        """
        Metodo che esegue il confronto grafico per 6 simulazioni partendo da energie iniziali diverse.
        3 simulazioni per il materiale acqua  e 3 simulazioni per il silicato di bismuto.
        Viene richiamato il metodo return array e veien riportato graficamente lo sviluppo dello sciame, ovvero:
            - numero di particelle ad ogni step
            - energia persa per ionizzazione ad ogni step
        """
        sciame1 = sciame_elettromagnetico(tipo_particella=tipo_particella, E0= E00,
                                          Ec_elettroni = Ec_elettroni_h20, Ec_positroni= Ec_positroni_h20,
                                          dEx0 = dEx0_h20, s = s, X0 = X0_h20)
        sciame2 = sciame_elettromagnetico(tipo_particella=tipo_particella, E0= E01,
                                          Ec_elettroni = Ec_elettroni_h20, Ec_positroni= Ec_positroni_h20,
                                          dEx0 = dEx0_h20, s = s, X0 = X0_h20)
        sciame3 = sciame_elettromagnetico(tipo_particella=tipo_particella, E0= E02,
                                          Ec_elettroni = Ec_elettroni_h20, Ec_positroni= Ec_positroni_h20,
                                          dEx0 = dEx0_h20, s = s, X0 = X0_h20)
        sciame4 = sciame_elettromagnetico(tipo_particella=tipo_particella, E0= E00,
                                          Ec_elettroni = Ec_elettroni_bso, Ec_positroni= Ec_positroni_bso,
                                          dEx0 = dEx0_bso, s = s, X0 = X0_bso)
        sciame5 = sciame_elettromagnetico(tipo_particella=tipo_particella, E0= E01,
                                          Ec_elettroni = Ec_elettroni_bso, Ec_positroni= Ec_positroni_bso,
                                          dEx0 = dEx0_bso, s = s, X0 = X0_bso)
        sciame6 = sciame_elettromagnetico(tipo_particella=tipo_particella, E0= E02,
                                          Ec_elettroni = Ec_elettroni_bso, Ec_positroni= Ec_positroni_bso,
                                          dEx0 = dEx0_bso, s = s, X0 = X0_bso)
        sciame1.simulazione_sciame()
        sciame2.simulazione_sciame()
        sciame3.simulazione_sciame()
        sciame4.simulazione_sciame()
        sciame5.simulazione_sciame()
        sciame6.simulazione_sciame()

        step1 , num1, energia1 = sciame1.return_array()
        step2 , num2, energia2 = sciame2.return_array()
        step3 , num3, energia3 = sciame3.return_array()
        step4 , num4, energia4 = sciame4.return_array()
        step5 , num5, energia5 = sciame5.return_array()
        step6 , num6, energia6 = sciame6.return_array()

        confronto_grafico = int(input("1 per visualizzare il confronto dello sviluppo longitudinale per energie diverse. 0 altrimenti: "))
        if confronto_grafico == 1:
            fig, ax = plt.subplots(2 , 2, figsize = [12,8])
            fig.suptitle(" Confronto sviluppo longitudinale per diverse energie", c='darkred', fontsize = 10)
            # simulazione 1 per acqua 
            ax[0][0].plot(step1[:-1], num1, "--", c='blue')
            ax[0][0].plot(step1[:-1], num1, "+", c='red',label='$E_0$ = {:.2f} MeV'.format(E00))
            

            #simulazione 2 per acqua
            ax[0][0].plot(step2[:-1], num2, "--", c='steelblue')
            ax[0][0].plot(step2[:-1], num2, "+", c='orange',label='$E_0$ = {:.2f} MeV'.format(E01))

            # simulazione 3 per acqua
            ax[0][0].plot(step3[:-1], num3, "--", c='limegreen')
            ax[0][0].plot(step3[:-1], num3, "+", c='magenta',label='$E_0$ = {:.2f} MeV'.format(E02))

            
            ax[0][0].set_xlabel('Numero di step')
            ax[0][0].set_ylabel('Numero di particelle per H2O')
            ax[0][0].legend(loc = 'upper left')
            ax[0][0].grid(True)

            # simulazione 1 per acqua
            ax[0][1].plot(step1[:-1], energia1, "--", c='blue')
            ax[0][1].plot(step1[:-1], energia1, "+", c='red',label='$E_0$ = {:.2f} MeV'.format(E00))

            #simulazione 2 per acqua
            ax[0][1].plot(step2[:-1], energia2, "--", c='steelblue')
            ax[0][1].plot(step2[:-1], energia2, "+", c='orange',label='$E_0$ = {:.2f} MeV'.format(E01))

            # simulazione 3 per acqua
            ax[0][1].plot(step3[:-1], energia3, "--", c='limegreen')
            ax[0][1].plot(step3[:-1], energia3, "+", c='magenta',label='$E_0$ = {:.2f} MeV'.format(E02))

            
            ax[0][1].set_xlabel('Numero di step')
            ax[0][1].set_ylabel('Energia depositata(MeV) per H2O')
            ax[0][1].legend(loc = 'upper left')
            ax[0][1].grid(True)

            #--------------------------------------------------------------#

            # simulazione 1 per silicato di bismuto 
            ax[1][0].plot(step4[:-1], num4, "--", c='blue')
            ax[1][0].plot(step4[:-1], num4, "+", c='red',label='$E_0$ = {:.2f} MeV'.format(E00))

            #simulazione 2 per silicato di bismuto 
            ax[1][0].plot(step5[:-1], num5, "--", c='steelblue')
            ax[1][0].plot(step5[:-1], num5, "+", c='orange',label='$E_0$ = {:.2f} MeV'.format(E01))

            # simulazione 3 per silicato di bismuto 
            ax[1][0].plot(step6[:-1], num6, "--", c='limegreen')
            ax[1][0].plot(step6[:-1], num6, "+", c='magenta',label='$E_0$ = {:.2f} MeV'.format(E02))

            
            ax[1][0].set_xlabel('Numero di step')
            ax[1][0].set_ylabel('Numero di particelle per BSO')
            ax[1][0].legend(loc = 'upper left')
            ax[1][0].grid(True)

            # simulazione 1 per silicato di bismuto 
            ax[1][1].plot(step4[:-1], energia4, "--", c='blue')
            ax[1][1].plot(step4[:-1], energia4, "+", c='red',label='$E_0$ = {:.2f} MeV'.format(E00))

            #simulazione 2 per silicato di bismuto 
            ax[1][1].plot(step5[:-1], energia5, "--", c='steelblue')
            ax[1][1].plot(step5[:-1], energia5, "+", c='orange',label='$E_0$ = {:.2f} MeV'.format(E01))

            # simulazione 3 per silicato di bismuto 
            ax[1][1].plot(step6[:-1], energia6, "--", c='limegreen')
            ax[1][1].plot(step6[:-1], energia6, "+", c='magenta',label='$E_0$ = {:.2f} MeV'.format(E02))

            #ax[1][1].set_title("Andamento dell'energia depositata per diverse energie iniziali")
            ax[1][1].set_xlabel('Numero di step')
            ax[1][1].set_ylabel('Energia depositata(MeV) per BSO')
            ax[1][1].legend(loc = 'upper left')
            ax[1][1].grid(True)
        
            plt.show()





        


             









