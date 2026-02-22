---
dcterms:title: 03_HTML
dcterms:contributor:
  - "[[Marcel-Dominique Block]]"
dcterms:created: 2026-02-01
dcterms:modified: 2026-02-01
dcterms:subjects:
  - "[[Web Development]]"
  - "[[HTML]]"
dcterms:isPartOf:
  - "[[Internetprogramming-Lecture-BIM25]]"
dcterms:references:
schem:language: german
rdf:type: schema:Course
schema:educationalProgramName: "[[Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
# 3. HTML
- HTML ist die HyperText Markup Language
- Es handelt sich um eine Auszeichnungssprache, die die logischen Bestandteile eines Dokuments beschreibt
- Das Beschreibungsschema ist hierarchisch gegliedert
- Eine Vernetzung von Dokumenten ist durch Verweise (Hyperlinks) möglich
- Es handelt sich um eine plattformunabhängige Beschreibung in Klartext
- HTML ist zur Beschreibung von Dokumenten universell einsetzbar
- Mit HTML können Überschriften, Texte, Listen und Tabellen erzeugt werden, Verweise auf andere Webseiten oder Datenquellen im Internet gemacht werden. Weiterhin besteht de Möglichkeit, Grafiken und multimediale Inhalte als Referenz einzubinden.
- Cascading Style Sheets (CSS): legen die Gestaltung von HTML-Elementen fest
- JavaScript: Programmiersprache für dynamische HTML-Seiten
- Common Gateway Interface (CGI): Schnittstelle zu Software und Datenbanken
## Plugins
- Plattformunabhängige Anwendung
- Plug-Ins kommunizieren mit dem Web-Browser und sind in eine Web-Seite integrierbar
- Sie ermöglichen es, Dateiformate und verarbeiten, die die Browser nicht verstehen oder eigenständige Anwendungen in einem  in den Browser integrierten Fenster ablaufen zu lassen
## Elemente und Tags
- HTML-Dateien bestehen auf Text. Zur Vorhebung der Textauszeichnung gibt es bestimmte Zeichen bzw. Kombinationen von Zeichen aus dem normalen Zeichenwort, die eine besondere Bedeutung erhalten (Tags).
- Der Inhalt von HTML-Dateien steht in HTML-Elementen
- HTML-Elemente werden durch Tags markiert
- Fast alle Elemente haben ein einleitendes und ein abschließendes Tag. Dazwischen liegt der Gültigkeitsbereich des entsprechenden Elements.
## HTML Dokument
### Aufbau eines HTML-Dokuments
- Eine HTML Datei besteht gewöhnlich aus drei Teilen:
	- der Dokumenttyp-Angabe (verwendete HTML-Version)
	- dem Header (Kopfdaten, z.B. Angabe des Titels)
	- dem Body (Körper, der eigentliche Inhalte des Dokuments)
- Jeder HTML-Befehl (HTML-Tag) ist in spitze Klammer eingeschlossen
#### Header:
```html
<head><title>Seitentitel</title></head>
```
#### Body:
```html
<body>Seitenrumpf</body>
```
#### Das Grundgerüst einer HTML-Datei hat folgende Form:
```html
<html>
	<head>
		<title>Titelseite des Dokuments</title>
	</head>
	<body>
		Eigentlicher Inhalt des Dokuments, der verschiedenen Formatierungsanweisungen enthgalten kann
	</body>
</html>
```
## Dokumenttyp
- Der Dokumententyp wird gemäß SGML (Standardized Generalizes Markup Language) angegeben
- Der Dokumententyp steht im Dokument noch vor dem `<html>`-Tag
- Er ist abhängig von HTML-Version und art des Dokuments
#### Beispiele: Standard HTML 4
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.1//EN">
```
#### Standard HTML 5
```html
<!DOCTYPE html>
```
## HTML-Tags
- Es gibt keine Unterschiede zwischen Groß- und Kleinschreibung innerhalb der Tags
- Tags können verschachtelt werden, z.B.
	```html
	<h4><i>HTML</i> - die Sprache des WWW</h4>
	```
- Einleitende Tags und Standalone-Tags können zusätzliche Angaben (Attribute) enthalten, z.B.
	```html
	<h4 align="center">HTML - die Sprache des WWW</h4>
	```

#### Überschriften (Headings) - Es gibt sechs Größen der Headings, die aufsteigend kleiner werden
```html
<h1>Überschriftebene 1</h1>
...
<h6>Überschriftebene 6</h6>
```
### Abschnitte (Paragraphs)
-  Es wird am Ende eine Leerzeile eingefügt
- Zeilenumbrüche innerhalb des Abschnitts haben keine Wirkung
```html
<p>Abschnitt</p>
```
### Hervorhebung (formatting)
```html
<b>Fetter Text (bold)</b>
<i>Kursiver Text (italic)</i>
<u>Unterstrichener Text (underline)</u>
```
#### Horizontale Linie (horizontal rule)
```html
<hr>
```
#### Zeilenumbruch (break)
```html
<br>
```
- `<hr>` und `<br>` gehören zu den Standalone-Tags, d.h. sie werden nicht durch ein End-Tag beendet
### Listen
#### Aufzählungen
```html
<ul>
	<li>Listenelement</li>
	<li>Listenelement</li>
</ul>
```
#### Numerische Listen
```html
<ol>
	<li>Listenelement</li>
	<li>Listenelement</li>
</ol>
```
### Sonderzeichen
- Das Zeichen `ß` wird durch die Zeichenfolge `&szlig;` ersetzt (Maskierung)
- Das Zeichen `ä` wird durch die Zeichenfolge `&auml;` ersetzt (andere Umlaute analog)
- Seit HTML 4.0 kann statt der Maskierung ein entsprechender Zeichensatz geladen werden
```html
<head>
	<title>Titel der Datei</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
```
### Zeichenmaskierung
- Das Zeichen `<` wird durch die Zeichenfolge `&lt;` ersetzt
- Das Zeichen `>` wird durch die Zeichenfolge `&gt;` ersetzt
- Das Zeichen `&` wird durch die Zeichenfolge `&amp;` ersetzt
- Das Zeichen `"` wird durch die Zeichenfolge `&quot;` ersetzt
### Kommentare
- Kommentare können einzeilig oder mehrzeilig sein
- Kommentare beginnen mit `<!--`
- Einzeilige Kommentare enden mit `-->`
- Beispiel 1:
	```html
	<!-- Dieser Text ist ein Kommentar -->
	```
- Beispiel 2:
	```html
	<!-- Erste Zeile eines mehrzeiligen Kommentars
		Letzte Zeile des Kommentars -->
	```
## Verweise - Hyperlinks
- Verweise (Hyperlinks) erlauben des Sprung zu einem anderen Dokument im WWW per Mausklick
- Syntax: `<a href="[Verweisziel]">Verweistext</a>`
- Verweistext bezeichnet im Klartext, wohin die Verbindung geht, und wird im Browser angezeigt
- Verweistext kann auch eine Grafik enthalten
- Das Verweisziel bezeichnet die Adresse (in der Regel URL) des Dokumentes, auf das verwiesen wird
- Das Verweisziel muss in Anführungszeichen stehen --> Es ist ein Attribut des a-Tags
- Das Verweisziel kann u.a. sein:
	- andere HTML-Datei auf gleicher Website
	- WWW-Adressen
	- FTP- oder Newsgroup-Adresse
	- Email-Adresse
#### Beispiel für Hyperlinks
```html
<a href="verzeichnis\datei.html">Verweistext</a>
<a href="http://www.tfh-wildau.de/akaflieg/"> Fliegergruppe</a>
<a href="http://www.w3schools.com"><img src="smiley.gif"></a>
<a href="mailto:mblock@th-wildau.de">Mail an den Dozent</a>
<a href ="file://localhost/c:/html/homepage.html">Lokale Homepage</a>
```

```html
<!-- Relative Pfade -->
<a href="../datei.html">Hier finden Sie alles</a>
<a href=“/tmp/datei.html>">Hier finden Sie alles</a>

<!-- Beispiele für absolute Pfade -->
<a href="http://beispiel.de/datei.html">Eine Datei</a>
```
## Farben
- Farbangabe durch Namen
- 16 Grundfarben können durch Angabe des Farbnamens ausgewählt werden, z.B.:
	- yellow
	- red
	- white
	- black

```html
<!-- schwarzer Hintergrund des Dokumentes -->
<body bgcolor="black">
  <font color="yellow">gelber Text</font>

  <!-- hellblauer Tabellenhintergrund -->
  <table bgcolor="aqua">
    <tr><th>Tabellenkopf</th></tr>
  </table>

  <!-- rote Trennlinie -->
  <hr color="red">
</body>
```

- Farbangabe durch RGB-Werte
- Die Farbe wird aus den Grundfarben Rot, Grün und Blau zusammengesetzt
	- Helligkeitswerte zwischen 0 und 255
	- Darstellung erfolgt hexadezimal
#### Beispiel:
```html
<!-- dunkelgrauer Dateihintergrund -->
<body bgcolor="#808080">
  <font color="#990000">roter Text</font>
  <!-- blaugrüner Tabellenhintergrund -->
  <table bgcolor="#00C0C0">
    <tr><th>Tabellenkopf</th></tr>
  <!-- violette Trennlinie -->
  <hr color="#CC00CC">
</body>
```
## Tabellen
```html
<table border="1">
  <tr>
    <th>Name</th>
    <th>Vorname</th>
    <th>Wohnort</th>
  </tr>
  <tr>
    <td>Müller</td>
    <td>Petra</td>
    <td>Berlin</td>
  </tr>
  <tr>
    <td>Pallberg</td>
    <td>Siegfried</td>
    <td>Kassel</td>
  </tr>
</table>
```

- Das Attribut `border` wird von HTML 5 nicht unterstützt
- Best Practice: Formatierungseigenschaften in CSS definieren

- Die Tabelle soll Daten strukturell und informativ aufbereiten und zur Informationsvermittlung einsetzen (Kalender, Fahrpläne, Statistik, usw.)
- Einer Tabelle kann ein Titel zugeordnet werden
	```html
	<table title="Fahrplan der U-Bahn Berlin">
	```
- Einige Attribute wie z.B. summary sind seit HTML 5 nicht länger Teil des Standards
- Das Caption-Tag fügt eine Überschrift als Teil der Tabelle ein
	```html
	<table><caption>U-Bahnfahrplan Winter</caption></table>
	```
- Bei komplexen Tabellen können auch Spaltenüberschriften und eine Zuordnung von Zellen zu diesen Spalten vergeben werden
	```html
	<table title="Mitarbeiter der Entwicklung">
	  <tr>
	    <th id="name">Name</th>
	    <th id="vorname">Vorname</th>
	    <th id="wohnort">Wohnort</th>
	  </tr>
	  <tr>
	    <td headers="name">Müller</td>
	    <td headers="vorname">Petra</td>
	    <td headers="wohnort">Berlin</td>
	  </tr>
	  <tr>
	    <td headers="name">Pallberg</td>
	    <td headers="vorname">Siegfried</td>
	    <td headers="wohnort">Kassel</td>
	  </tr>
	</table>
	```
## Tabellen - Barrierefreiheit
- Für blinde und sehbehinderte Menschen stellen Tabellen oft Barrieren dar, da die Bewegung mit der Tab-Taste durchgeführt wird und der text einer Tabelle Zeile als Braillezeile umgesetzt wird
- Obwohl Tabellen nicht für das Layout einer Seite gedacht sind, werden dafür oft rahmenlose Tabellen verwendet
- Ein Screenreader bewegt sich in der Tabelle von Zeile zu Zeile. Voneinander abhängige Inhalte, die über mehrere Zeilen verteilt sind, werden dabei auseinander gerissen
- Layouttabellen sind daher im Sinner der Barrierefreiheit vermieden werden!
## Grafiken
- Grafik ausrichten, horizontaler und vertikaler Abstand
	- Seit HTML 5 nicht mehr Teil des Standards
	- Wird vollständig durch CSS realisiert
- Grafik-Formate: GIF, PNG, JPG
#### Die Syntax für das Einbinden von Grafiken lokale Grafiken
```html
<img src="datei.gif">
<img src="datei.jpg">
```
#### Lokale Grafiken in anderen Verzeichnissen
```html
<img src="verzeichnis\datei.jpg">
<img src="..\datei.gif">
```
#### Grafiken auf anderen WWW-Servern
```html
<img src="http://www.datan.de/Pic/logo.gif">
```
#### Grafiken mit alternativem Text
```html
<img src="datei.gif" alt="Kurzbeschreibung des Bildes">
```
#### Breite und Höhe einer Grafik angeben
```html
<img src="datei.gif" width="300" height="200">
```
## Grafiken - Barrierefreiheit
- Bilder und Grafiken sollten nur eingesetzt werden, wenn sie einen konkreten Bezug zu den Inhalten der Web-Seite haben
- Laut einer Studie der NN Group trifft das lediglich auf 35% aller auf Web-Seiten verwendeten Bilder zu. Alle anderen dienen lediglich gestalterischen Zwecken und führen bei visuell und kognitiv beeinträchtigten Menschen eher zu Desorientierung.
- Es sollte bei jedem Bild das alt-Attribut verwendet werden, das dieser bei Systemen dargestellt wird, die das Bild nicht anzeigen können und außerdem von Screenreader gelesen werden

- Gestalterische Elemente, die durch Grafiken realisiert wurden können häufig vollständig durch CSS ab Version 3 des Standards umgesetzt werden
- Bilder, die eine rein gestalterische Funktion haben, sollten mit einem leeren alt-Attribut gekennzeichnet werden
- Über das title-Attribut können ergänzende Beschreibungen zu einem Bild gegeben werden
## Formulare
- Formulare dienen der Eingabe von Daten durch den Anwender
- Formulare werden z.B. benutzt um
	- Eingabefelder auszufüllen
	- Buttons anzuklicken
	- Listeneinträge auszuwählen
- Ein Formular hat folgenden Aufbau:
	```html
	<form action="...URL..." ggf. weitere Attribute..>
	    ... Formularelemente wie Eingabefelder,
	    Auswahllisten,
	    Buttons ...
	</form>
	```
### Formularelemente
#### Einzeiliges Eingabefeld
```html
<input type="text" name="Name" size="40" maxlength="80">
```
#### Mehrzeiliges Eingabefeld
```html
<textarea cols="60" rows="5" name="FreiText"></textarea>
```
#### Auswahlliste
```html
<select name="derBrowser">
    <option value="BrowserDerFreiheit">Netscape</option>
    <option value="IE">Legacy Explorer</option>
    <option value="FF">Firefox</option>
    <option value="CH">Chromium</option>
</select>
```
#### Checkbox (Auswahlknopf)
```html
<input type="checkbox" name="check1" value="Kaffee">
```
#### Radiobutton (eindeutiger Auswahlknopf)
```html
<input type="radio" name="Rentner" value="ja">Ja
<input type="radio" name="Rentner" value="nein">Nein
```
#### Klick-Button (herkömmlich)
```html
<input type="button" value="Zurück" onClick="alert('Hallo Welt');">
```
#### Buttons zum Absenden oder Zurücksetzen
```html
<input type="submit" value="Versenden">
<input type="reset">
```
#### Form Beispiel
![[form_example.png]]
```html
<!doctype html>
<html>
 <head>
  <title>Feedbackformular</title>
  <meta charset="UTF-8">
 </head>
 <body>
  <form action="mailto:mblock@th-wildau.de?subject=Feedback"
        enctype="text/plain" method="POST">
   <p>
    <label for="input_name">Name</label>
    <input name="name" id="input_name" type="text" required="required">
   </p>

   <p>
    <label for="select_veranstaltung">Veranstaltung</label>
    <select name="veranstaltung" id="select_veranstaltung">
     <option value="IPR" >Internetprogrammierung</option>
     <option value="DB" selected>Datenbanken</option>
    </select>
   </p>

   <fieldset>
    <legend>Gesamturteil</legend>

    <input name="urteil" id="input_urteil_1" value="eher gut" type="radio">
    <label for="input_urteil_1">eher gut</label><br>
    <input name="urteil" id="input_urteil_2" value="mittel" type="radio">
    <label for="input_urteil_2">mittel</label><br>
    <input name="urteil" id="input_urteil_3" value="eher schlecht" type="radio">
    <label for="input_urteil_3">eher schlecht</label>
   </fieldset>

   <fieldset>
    <legend>Optimierungsbedarf</legend>

    <input name="bedarf_1" id="bedarf_check_1" value="Theorie" type="checkbox">
    <label for="bedarf_check_1">Theorie / Vorlesung</label><br>
    <input name="bedarf_2" id="bedarf_check_2" value="Labor&uuml;bungen" type="checkbox">
    <label for="bedarf_check_2">Labor&uuml;bungen</label><br>
    <input name="bedarf_3" id="bedarf_check_3" value="Stoffauswahl" type="checkbox">
    <label for="bedarf_check_3">Stoffauswahl</label>
   </fieldset>

   <p>
    Welche Verbesserungsvorschl&auml;ge haben Sie?<br>
    <textarea name="kommentar" cols="60" rows="5"></textarea>
   </p>
   <p>
    <input type="submit" value="Senden">
    <input type="reset">
   </p>

  </form>
 </body>
</html>
```
#### Beispiel: Inhalt der versandten E-Mail
```text
name=Norbert Nörgler
veranstaltung=IPR
urteil=eher schlecht
bedarf_1=Theorie
bedarf_2=Laborübungen
bedarf_3=Stoffauswahl
kommentar=- weniger Stress
- Dozent auswechseln
```
## Formulare - Barrierefreiheit
- Visuell beeinträchtigte Menschen haben oft das Problem, dass die Zuordnung zwischen einem Formularfeld und dessen Überschrift nicht eindeutig ist
- Formularfeldern sollte daher stets eine Beschriftung (label-Tag) zugeordnet werden
- In den Formularfeldern sind alle relevanten Informationen als Text vorzugeben (Attribut: value)
- Dies ist sowohl für visuell als auch für motorisch beeinträchtigte Menschen hilfreich (Sonderzeichen, die durch Tastenkombinationen geschrieben werden)
## Mime-Typen
- Mime-Typen sind multipurpose internet multimedia extensions
- Fast immer, wenn entfernte Einheiten (z.B. Web-Server und -Browser) kommunizieren, geht es auch um die Art der zu übertragenden Daten
- Dabei hat sich im Internet das Schema der Mime-Typen durchgesetzt
- Verschiedene HTML-Elemente haben Attribute, die als Wertzuweisung Mime-Typen erwarten
- Einer Datei wird eine Kategorie und ein Untertyp zugeordnet
- Beispiel: Ein Bild hat den MIME-typ image und Untertypen wie z.B. gif und jpeg
- Beide Angaben werden durch Schrägstrich voneinander getrennt: image/gif
- Es gibt z.B. folgende Medienkategorien: text für Textdateien; image für Grafikdateien; video für Videodateien; audio für Sounddateien; application für Dateien, die an ein bestimmtes Programm gebunden sind
- Detaillierte Liste aller Medienkategorien: https://wiki.selfhtml.org/wiki/Referenz:MIME-Typen
