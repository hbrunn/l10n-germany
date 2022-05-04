# Copyright 2022 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from datetime import datetime
from codecs import BOM_UTF8
from collections import OrderedDict
from csv import DictWriter, writer as csvwriter, QUOTE_NONNUMERIC
from io import StringIO


class DatevWriter(DictWriter):
    def __init__(
        self,
        data_type,
        data_name,
        data_version,
        consultant_id,
        client_id,
        fiscal_year_start,
        account_code_length,
        period_start,
        period_end,
        dataset_name,
        user_initials,
        currency,
        fields,
    ):
        self.buffer = StringIO()
        self.header = [
            "EXTF",  # constant for external programs
            700,  # header version
            data_type,  # type of data - 21=transactions
            data_name,  # name of type
            data_version,  # version of data
            datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3],
            None,
            "",
            "",
            "",
            consultant_id,
            client_id,
            fiscal_year_start,
            account_code_length,
            period_start,
            period_end,
            dataset_name,
            user_initials,
            1,  # 1 default, 2 end of year
            0,
            0,  # 0 not locked, 1 locked
            currency,
            None,
            "",
            None,
            None,
            "",
            "",
            None,
            "",
            "",
        ]
        self.fields = OrderedDict(fields)
        super().__init__(
            self.buffer,
            fieldnames=list(self.fields.keys()),
            delimiter=";",
            quoting=QUOTE_NONNUMERIC,
        )

    def writeheader(self):
        self.buffer.write(BOM_UTF8.decode("utf8"))
        csvwriter(self.buffer, delimiter=";", quoting=QUOTE_NONNUMERIC).writerow(
            self.header
        )
        return super().writeheader()

    def _coerce_value(self, key, value):
        if not value:
            return None
        length = self.fields.get(key)
        if length:
            return str(value)[:length]
        return value

    def writerow(self, row):
        return super().writerow(
            {key: self._coerce_value(key, value) for key, value in row.items()}
        )

    def writerows(self, rows):
        return super().writerows(
            {key: self._coerce_value(key, value) for key, value in row.items()}
            for row in rows
        )


class DatevTransactionWriter(DatevWriter):
    def __init__(
        self,
        consultant_id,
        client_id,
        fiscal_year_start,
        account_code_length,
        period_start,
        period_end,
        user_initials,
        currency,
    ):
        super().__init__(
            21,
            "Buchungsstapel",
            12,
            consultant_id,
            client_id,
            fiscal_year_start,
            account_code_length,
            period_start,
            period_end,
            "Buchungsstapel %s" % period_start,
            user_initials,
            currency,
            [
                ("Umsatz (ohne Soll/Haben-Kz)", None),
                ("Soll/Haben-Kennzeichen", None),
                ("WKZ Umsatz", None),
                ("Kurs", None),
                ("Basis-Umsatz", None),
                ("WKZ Basis-Umsatz", None),
                ("Konto", None),
                ("Gegenkonto (ohne BU-Schlüssel)", 9),
                ("BU-Schlüssel", 4),
                ("Belegdatum", 4),
                ("Belegfeld 1", 36),
                ("Belegfeld 2", 12),
                ("Skonto", None),
                ("Buchungstext", 60),
                ("Postensperre", None),
                ("Diverse Adressnummer", None),
                ("Geschäftspartnerbank", None),
                ("Sachverhalt", None),
                ("Zinssperre", None),
                ("Beleglink", None),
                ("Beleginfo - Art 1", None),
                ("Beleginfo - Inhalt 1", None),
                ("Beleginfo - Art 2", None),
                ("Beleginfo - Inhalt 2", None),
                ("Beleginfo - Art 3", None),
                ("Beleginfo - Inhalt 3", None),
                ("Beleginfo - Art 4", None),
                ("Beleginfo - Inhalt 4", None),
                ("Beleginfo - Art 5", None),
                ("Beleginfo - Inhalt 5", None),
                ("Beleginfo - Art 6", None),
                ("Beleginfo - Inhalt 6", None),
                ("Beleginfo - Art 7", None),
                ("Beleginfo - Inhalt 7", None),
                ("Beleginfo - Art 8", None),
                ("Beleginfo - Inhalt 8", None),
                ("KOST1 - Kostenstelle", 36),
                ("KOST2 - Kostenstelle", 36),
                ("Kost-Menge", None),
                ("EU-Land u. UStID (Bestimmung)", None),
                ("EU-Steuersatz (Bestimmung)", None),
                ("Abw. Versteuerungsart", None),
                ("Sachverhalt L+L", None),
                ("Funktionsergänzung L+L", None),
                ("BU 49 Hauptfunktionstyp", None),
                ("BU 49 Hauptfunktionsnummer", None),
                ("BU 49 Funktionsergänzung", None),
                ("Zusatzinformation - Art 1", None),
                ("Zusatzinformation- Inhalt 1", None),
                ("Zusatzinformation - Art 2", None),
                ("Zusatzinformation- Inhalt 2", None),
                ("Zusatzinformation - Art 3", None),
                ("Zusatzinformation- Inhalt 3", None),
                ("Zusatzinformation - Art 4", None),
                ("Zusatzinformation- Inhalt 4", None),
                ("Zusatzinformation - Art 5", None),
                ("Zusatzinformation- Inhalt 5", None),
                ("Zusatzinformation - Art 6", None),
                ("Zusatzinformation- Inhalt 6", None),
                ("Zusatzinformation - Art 7", None),
                ("Zusatzinformation- Inhalt 7", None),
                ("Zusatzinformation - Art 8", None),
                ("Zusatzinformation- Inhalt 8", None),
                ("Zusatzinformation - Art 9", None),
                ("Zusatzinformation- Inhalt 9", None),
                ("Zusatzinformation - Art 10", None),
                ("Zusatzinformation- Inhalt 10", None),
                ("Zusatzinformation - Art 11", None),
                ("Zusatzinformation- Inhalt 11", None),
                ("Zusatzinformation - Art 12", None),
                ("Zusatzinformation- Inhalt 12", None),
                ("Zusatzinformation - Art 13", None),
                ("Zusatzinformation- Inhalt 13", None),
                ("Zusatzinformation - Art 14", None),
                ("Zusatzinformation- Inhalt 14", None),
                ("Zusatzinformation - Art 15", None),
                ("Zusatzinformation- Inhalt 15", None),
                ("Zusatzinformation - Art 16", None),
                ("Zusatzinformation- Inhalt 16", None),
                ("Zusatzinformation - Art 17", None),
                ("Zusatzinformation- Inhalt 17", None),
                ("Zusatzinformation - Art 18", None),
                ("Zusatzinformation- Inhalt 18", None),
                ("Zusatzinformation - Art 19", None),
                ("Zusatzinformation- Inhalt 19", None),
                ("Zusatzinformation - Art 20", None),
                ("Zusatzinformation- Inhalt 20", None),
                ("Stück", None),
                ("Gewicht", None),
                ("Zahlweise", None),
                ("Forderungsart", None),
                ("Veranlagungsjahr", None),
                ("Zugeordnete Fälligkeit", None),
                ("Skontotyp", None),
                ("Auftragsnummer", None),
                ("Buchungstyp", None),
                ("USt-Schlüssel (Anzahlungen)", None),
                ("EU-Land (Anzahlungen)", None),
                ("Sachverhalt L+L (Anzahlungen)", None),
                ("EU-Steuersatz (Anzahlungen)", None),
                ("Erlöskonto (Anzahlungen)", None),
                ("Herkunft-Kz", None),
                ("Buchungs GUID", None),
                ("KOST-Datum", None),
                ("SEPA-Mandatsreferenz", None),
                ("Skontosperre", None),
                ("Gesellschaftername", None),
                ("Beteiligtennummer", None),
                ("Identifikationsnummer", None),
                ("Zeichnernummer", None),
                ("Postensperre bis", None),
                ("Bezeichnung SoBil-Sachverhalt", None),
                ("Kennzeichen SoBil-Buchung", None),
                ("Festschreibung", None),
                ("Leistungsdatum", None),
                ("Datum Zuord. Steuerperiode", None),
                ("Fälligkeit", None),
                ("Generalumkehr (GU)", None),
                ("Steuersatz", None),
                ("Land", None),
                ("Abrechnungsreferenz", None),
                ("BVV-Position", None),
                ("EU-Land u. UStID (Ursprung)", None),
                ("EU-Steuersatz (Ursprung)", None),
            ],
        )


class DatevPartnerWriter(DatevWriter):
    def __init__(
        self,
        consultant_id,
        client_id,
        fiscal_year_start,
        account_code_length,
        period_start,
        period_end,
        user_initials,
        currency,
    ):
        super().__init__(
            16,
            "Debitoren/Kreditoren",
            5,
            consultant_id,
            client_id,
            fiscal_year_start,
            account_code_length,
            period_start,
            period_end,
            "Debitoren/Kreditoren",
            user_initials,
            currency,
            [
                ("Konto", 9),
                ("Name (Adressattyp Unternehmen)", 50),
                ("Unternehmensgegenstand", 50),
                ("Name (Adressattyp natürl. Person)", 30),
                ("Vorname (Adressattyp natürl. Person)", 30),
                ("Name (Adressattyp keine Angabe)", 50),
                ("Adressattyp", 1),
                ("Kurzbezeichnung", 15),
                ("EU-Land", None),
                ("EU-UStID", 13),
                ("Anrede", None),
                ("Titel/Akad. Grad", None),
                ("Adelstitel", None),
                ("Namensvorsatz", None),
                ("Adressart", None),
                ("Straße", None),
                ("Postfach", None),
                ("Postleitzahl", None),
                ("Ort", None),
                ("Land", None),
                ("Versandzusatz", None),
                ("Adresszusatz", None),
                ("Abweichende Anrede", None),
                ("Abw. Zustellbezeichnung 1", None),
                ("Abw. Zustellbezeichnung 2", None),
                ("Kennz. Korrespondenzadresse", None),
                ("Adresse Gültig von", None),
                ("Adresse Gültig bis", None),
                ("Telefon", None),
                ("Bemerkung (Telefon)", None),
                ("Telefon GL", None),
                ("Bemerkung (Telefon GL)", None),
                ("E-Mail", None),
                ("Bemerkung (E-Mail)", None),
                ("Internet", None),
                ("Bemerkung (Internet)", None),
                ("Fax", None),
                ("Bemerkung (Fax)", None),
                ("Sonstige", None),
                ("Bemerkung (Sonstige)", None),
                ("Bankleitzahl 1", None),
                ("Bankbezeichnung 1", None),
                ("Bank-Kontonummer 1", None),
                ("Länderkennzeichen 1", None),
                ("IBAN-Nr. 1", None),
                ("Leerfeld1", None),
                ("SWIFT-Code 1", None),
                ("Abw. Kontoinhaber 1", None),
                ("Kennz. Hauptbankverb. 1", None),
                ("Bankverb 1 Gültig von", None),
                ("Bankverb 1 Gültig bis", None),
                ("Bankleitzahl 2", None),
                ("Bankbezeichnung 2", None),
                ("Bank-Kontonummer 2", None),
                ("Länderkennzeichen 2", None),
                ("IBAN-Nr. 2", None),
                ("Leerfeld2", None),
                ("SWIFT-Code 2", None),
                ("Abw. Kontoinhaber 2", None),
                ("Kennz. Hauptbankverb. 2", None),
                ("Bankverb 2 Gültig von", None),
                ("Bankverb 2 Gültig bis", None),
                ("Bankleitzahl 3", None),
                ("Bankbezeichnung 3", None),
                ("Bank-Kontonummer 3", None),
                ("Länderkennzeichen 3", None),
                ("IBAN-Nr. 3", None),
                ("Leerfeld3", None),
                ("SWIFT-Code 3", None),
                ("Abw. Kontoinhaber 3", None),
                ("Kennz. Hauptbankverb. 3", None),
                ("Bankverb 3 Gültig von", None),
                ("Bankverb 3 Gültig bis", None),
                ("Bankleitzahl 4", None),
                ("Bankbezeichnung 4", None),
                ("Bank-Kontonummer 4", None),
                ("Länderkennzeichen 4", None),
                ("IBAN-Nr. 4", None),
                ("Leerfeld4", None),
                ("SWIFT-Code 4", None),
                ("Abw. Kontoinhaber 4", None),
                ("Kennz. Hauptbankverb. 4", None),
                ("Bankverb 4 Gültig von", None),
                ("Bankverb 4 Gültig bis", None),
                ("Bankleitzahl 5", None),
                ("Bankbezeichnung 5", None),
                ("Bank-Kontonummer 5", None),
                ("Länderkennzeichen 5", None),
                ("IBAN-Nr. 5", None),
                ("Leerfeld5", None),
                ("SWIFT-Code 5", None),
                ("Abw. Kontoinhaber 5", None),
                ("Kennz. Hauptbankverb. 5", None),
                ("Bankverb 5 Gültig von", None),
                ("Bankverb 5 Gültig bis", None),
                ("Leerfeld6", None),
                ("Briefanrede", None),
                ("Grußformel", None),
                ("Kunden-/Lief.-Nr.", None),
                ("Steuernummer", None),
                ("Sprache", None),
                ("Ansprechpartner", None),
                ("Vertreter", None),
                ("Sachbearbeiter", None),
                ("Diverse-Konto", None),
                ("Ausgabeziel", None),
                ("Währungssteuerung", None),
                ("Kreditlimit (Debitor)", None),
                ("Zahlungsbedingung", None),
                ("Fälligkeit in Tagen (Debitor)", None),
                ("Skonto in Prozent (Debitor)", None),
                ("Kreditoren-Ziel 1 Tg.", None),
                ("Kreditoren-Skonto 1 %", None),
                ("Kreditoren-Ziel 2 Tg.", None),
                ("Kreditoren-Skonto 2 %", None),
                ("Kreditoren-Ziel 3 Brutto Tg.", None),
                ("Kreditoren-Ziel 4 Tg.", None),
                ("Kreditoren-Skonto 4 %", None),
                ("Kreditoren-Ziel 5 Tg.", None),
                ("Kreditoren-Skonto 5 %", None),
                ("Mahnung", None),
                ("Kontoauszug", None),
                ("Mahntext 1", None),
                ("Mahntext 2", None),
                ("Mahntext 3", None),
                ("Kontoauszugstext", None),
                ("Mahnlimit Betrag", None),
                ("Mahnlimit %", None),
                ("Zinsberechnung", None),
                ("Mahnzinssatz 1", None),
                ("Mahnzinssatz 2", None),
                ("Mahnzinssatz 3", None),
                ("Lastschrift", None),
                ("Leerfeld7", None),
                ("Mandantenbank", None),
                ("Zahlungsträger", None),
                ("Indiv. Feld 1", None),
                ("Indiv. Feld 2", None),
                ("Indiv. Feld 3", None),
                ("Indiv. Feld 4", None),
                ("Indiv. Feld 5", None),
                ("Indiv. Feld 6", None),
                ("Indiv. Feld 7", None),
                ("Indiv. Feld 8", None),
                ("Indiv. Feld 9", None),
                ("Indiv. Feld 10", None),
                ("Indiv. Feld 11", None),
                ("Indiv. Feld 12", None),
                ("Indiv. Feld 13", None),
                ("Indiv. Feld 14", None),
                ("Indiv. Feld 15", None),
                ("Abweichende Anrede (Rechnungsadresse)", None),
                ("Adressart (Rechnungsadresse)", None),
                ("Straße (Rechnungsadresse)", None),
                ("Postfach (Rechnungsadresse)", None),
                ("Postleitzahl (Rechnungsadresse)", None),
                ("Ort (Rechnungsadresse)", None),
                ("Land (Rechnungsadresse)", None),
                ("Versandzusatz (Rechnungsadresse)", None),
                ("Adresszusatz (Rechnungsadresse)", None),
                ("Abw. Zustellbezeichnung 1 (Rechnungsadresse)", None),
                ("Abw. Zustellbezeichnung 2 (Rechnungsadresse)", None),
                ("Adresse Gültig von (Rechnungsadresse)", None),
                ("Adresse Gültig bis (Rechnungsadresse)", None),
                ("Bankleitzahl 6", None),
                ("Bankbezeichnung 6", None),
                ("Bank-Kontonummer 6", None),
                ("Länderkennzeichen 6", None),
                ("IBAN-Nr. 6", None),
                ("Leerfeld8", None),
                ("SWIFT-Code 6", None),
                ("Abw. Kontoinhaber 6", None),
                ("Kennz. Hauptbankverb. 6", None),
                ("Bankverb 6 Gültig von", None),
                ("Bankverb 6 Gültig bis", None),
                ("Bankleitzahl 7", None),
                ("Bankbezeichnung 7", None),
                ("Bank-Kontonummer 7", None),
                ("Länderkennzeichen 7", None),
                ("IBAN-Nr. 7", None),
                ("Leerfeld9", None),
                ("SWIFT-Code 7", None),
                ("Abw. Kontoinhaber 7", None),
                ("Kennz. Hauptbankverb. 7", None),
                ("Bankverb 7 Gültig von", None),
                ("Bankverb 7 Gültig bis", None),
                ("Bankleitzahl 8", None),
                ("Bankbezeichnung 8", None),
                ("Bank-Kontonummer 8", None),
                ("Länderkennzeichen 8", None),
                ("IBAN-Nr. 8", None),
                ("Leerfeld10", None),
                ("SWIFT-Code 8", None),
                ("Abw. Kontoinhaber 8", None),
                ("Kennz. Hauptbankverb. 8", None),
                ("Bankverb 8 Gültig von", None),
                ("Bankverb 8 Gültig bis", None),
                ("Bankleitzahl 9", None),
                ("Bankbezeichnung 9", None),
                ("Bank-Kontonummer 9", None),
                ("Länderkennzeichen 9", None),
                ("IBAN-Nr. 9", None),
                ("Leerfeld11", None),
                ("SWIFT-Code 9", None),
                ("Abw. Kontoinhaber 9", None),
                ("Kennz. Hauptbankverb. 9", None),
                ("Bankverb 9 Gültig von", None),
                ("Bankverb 9 Gültig bis", None),
                ("Bankleitzahl 10", None),
                ("Bankbezeichnung 10", None),
                ("Bank-Kontonummer 10", None),
                ("Länderkennzeichen 10", None),
                ("IBAN-Nr. 10", None),
                ("Leerfeld12", None),
                ("SWIFT-Code 10", None),
                ("Abw. Kontoinhaber 10", None),
                ("Kennz. Hauptbankverb. 10", None),
                ("Bankverb 10 Gültig von", None),
                ("Bankverb 10 Gültig bis", None),
                ("Nummer Fremdsystem", None),
                ("Insolvent", None),
                ("SEPA-Mandatsreferenz 1", None),
                ("SEPA-Mandatsreferenz 2", None),
                ("SEPA-Mandatsreferenz 3", None),
                ("SEPA-Mandatsreferenz 4", None),
                ("SEPA-Mandatsreferenz 5", None),
                ("SEPA-Mandatsreferenz 6", None),
                ("SEPA-Mandatsreferenz 7", None),
                ("SEPA-Mandatsreferenz 8", None),
                ("SEPA-Mandatsreferenz 9", None),
                ("SEPA-Mandatsreferenz 10", None),
                ("Verknüpftes OPOS-Konto", None),
                ("Mahnsperre bis", None),
                ("Lastschriftsperre bis", None),
                ("Zahlungssperre bis", None),
                ("Gebührenberechnung", None),
                ("Mahngebühr 1", None),
                ("Mahngebühr 2", None),
                ("Mahngebühr 3", None),
                ("Pauschalenberechnung", None),
                ("Verzugspauschale 1", None),
                ("Verzugspauschale 2", None),
                ("Verzugspauschale 3", None),
                ("Alternativer Suchname", None),
                ("Status", None),
                ("Anschrift manuell geändert (Korrespondenzadresse)", None),
                ("Anschrift individuell (Korrespondenzadresse)", None),
                ("Anschrift manuell geändert (Rechnungsadresse)", None),
                ("Anschrift individuell (Rechnungsadresse)", None),
                ("Fristberechnung bei Debitor", None),
                ("Mahnfrist 1", None),
                ("Mahnfrist 2", None),
                ("Mahnfrist 3", None),
                ("Letzte Frist", None),
            ],
        )


class DatevAccountWriter(DatevWriter):
    def __init__(
        self,
        consultant_id,
        client_id,
        fiscal_year_start,
        account_code_length,
        period_start,
        period_end,
        user_initials,
        currency,
    ):
        super().__init__(
            20,
            "Kontenbeschriftungen",
            3,
            consultant_id,
            client_id,
            fiscal_year_start,
            account_code_length,
            period_start,
            period_end,
            "Kontenbeschriftungen",
            user_initials,
            currency,
            [
                ("Konto", 9),
                ("Kontobeschriftung", 40),
                ("SprachId", 5),
                ("Kontenbeschriftung lang", 300),
            ],
        )
