from csv import reader
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8", newline="") as csv_file:
                infile = reader(csv_file)
                for row in infile:
                    nuovo_strumento=Strumento(row[0], row[1], row[2], row[3], row[4])
                    self.strumenti.append(nuovo_strumento)
                print("File caricato con successo")
        except FileNotFoundError:
            print("Errore: file non trovato")
            raise

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if not self.strumenti:
            nuovo_id="S1"
        else:
            ultimo_strumento=self.strumenti[-1]
            ultimo_id_num=int(ultimo_strumento.codice[1:])
            nuovo_id=f"S{ultimo_id_num+1}"

        nuovo_strumento=Strumento(nuovo_id, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovo_strumento)
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        strumento_esistente = False
        for strumento in self.strumenti:
            if strumento.codice == id_strumento:
                strumento_esistente = True
                break
        if not strumento_esistente:
            raise Exception("Errore: Lo strumento non esiste nel deposito.")
        for prestito in self.prestiti:
            if prestito.id_strumento == id_strumento:
                raise Exception("Errore: Lo strumento è già in prestito.")
        if not self.prestiti:
            id_prestito="P1"
        else:
            ultimo_prestito=self.strumenti[-1]
            ultimo_pr_num=int(ultimo_prestito.codice[1:])
            id_prestito=f"P{ultimo_pr_num+1}"

        nuovo_prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.strumenti.append(nuovo_prestito)
        return nuovo_prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        trovato=False
        for prestito in self.prestiti:
            if prestito.id_prestito == id_prestito:
                self.prestiti.remove(prestito)
                trovato=True
                break
        if not trovato:
            raise Exception("prestito non trovato")
        return None

class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"{self.codice}, {self.tipo}, {self.marca}, {self.anno_acquisto}, {self.valore}"

class Prestito:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.id_prestito = id_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.id_prestito}, {self.data}, {self.id_strumento}, {self.cognome_allievo}"