---
title: 02_XML
date: 2026-01-03
modified: 2026-01-03
tags:
  - master
origin: "[[BIBLIOTHEKSINFORMATIK]]"
sources:
  - "[[Marcel-Dominique Block]]"
  - "[[02_XML.html]]"
language: german
file-format: markdown (.md)
note-type: lecture
relations:
  - "[[Technische Hochschule Wildau]]"
---
# <u>2. XML</u>
## 2.1. XML
XML
- Standardisierte Beschreibungssprache (Auszeichnungssprache, Markup Language)
- Standard für Datenaustausch im Web!

XML kann...
- .. von Menschen verstanden werden
- .. von Maschinen interpretiert werden

Gründe für den Erfolg von XML
- Textbasiert
- Beschreibung der Daten statt der Darstellung
- Stylesheets: Definition der Präsentation
- Einfache Struktur

Geschichte
- Entwicklung von GML ( Generalized Markup Language) durch IBM Ende der 1960er
- SGML (Standard Generalized Markup Language)
	- ISO 8879
	- Wird zum Industriestandard in den 1980er
	- Mächtige Metasprache zur Definition von Auszeichnungssprachen
	- Elemente und Attribute können spezifiziert werden
	- Validierung durch Dokumenttypdefinitionen (DTD)
- Entwicklung von HTML (Hypertext Markup Language) 1989 am CERN
	- Ist ein Dokumenttype von SGML
	- Schwerpunkt: Darstellung und Layout, nicht die inhaltliche Struktur
	- Keine Erweiterungsmöglichkeiten
- Microsoft, IBM und weitere entwickeln XML
	- Standardisierung erfolgt durch das World-Wide-Web-Consortium (W3C)
### 2.1.1. Zusammenhänge
Zusammenhänge zwischen SGML, HTML und XML:

![[IMG DB/Unbenannt 1.png|500]]

- XML kombiniert die Vorteile von SGML und HTML
	- Flexibilität & Beschreibungsmöglichkeiten von Strukturen aus SGML
	- Einfachheit aus HTML
	- HTML-Features wie Stylesheets und Hyperlinks werden auf XML übertragen
### 2.1.2. Bereichsspezifische Beschreibungssprachen
- XML bietet Autoren die Möglichkeit ihre XML-Dokumente über Document-Type-Definitions (DTD) zu definieren
- Mit diesem Konzept erfolgt die Definition bereichspezifischer Beschreibungssprachen
	- MathML (Mathematical Markup Language)
	- CML (Chemical Markup Language)
	- SMIL (Synchronized Multimodel Integration Language)
- XML ist eher ein Werkzeug für Spezialisten während Endanwender mit XML über Anwendungen und XHTML als XML konformes HTML, mit XML in Verbindung kommen

Trennung von Inhalten und Darstellung:

![[Unbenannt 1 1.png]]
### 2.1.3. Eigenschaften von XML-Dokumenten
- Ein XML-Dokument ist wohlgeformt (well-formed), wenn es die Syntaxregeln der W3C erfüllt. z.B.:
	- Jedes Element ist entweder leer (`<tag ../>`) oder wird durch ein schließendes Tag (`</tag>`) beendet
	- Der Aufbau muss streng hierarchisch sein
- Ein XML-Dokument ist gültig (valid), wenn es eine vorgegebene Spezifikation erfüllt:
	- DTD
	- XSD
### 2.1.4. Namenräume in XML
Beispiel: XML mit Informationen über einen Tisch
```xml
<table>
	<name>African Coffee Table</name>
	<width>80</width>
	<length>120<length/>
</table>
```

Beispiel: XML mit HTML-Tabelle
```xml
<table>
	<tr>
		<td>Apples</td>
		<td>Bananas</td>
	</tr>
<table/>
```

Um die konfliktfreie Wiederverwendbarkeit von Elementbezeichnern zu unterstützen können Namenräume (name space) zugeordnet werden

```xml
<root
xmlns:h="http://www.w3.org/TR/html4/"
xmlns:f="http://www.w3schools.com/furniture"
	<h:table>
		<h:tr>
		<h:td>Apples</h:td>
		<h:td>Bananas</h:td>
		</h:tr>
	</h:table>
	
	<f:table>
		<f:name>Adrican Coffee Table</f:name>
		<f:width>80</f:width>
		<f:length>120</f:lenght>
	</f:table>
</root>
```
## 2.2. DTD - Document Type Definition
- Möglichkeit, die Struktur von XML-Dokumenten zu beschreiben
- Quellen für Selbststudium:
	- [http://de.selfhtml.org/xml/dtd/](http://de.selfhtml.org/xml/dtd/)
	- [http://de.selfhtml.org/xml/regeln/dokumenttypdeklaration.htm](http://de.selfhtml.org/xml/regeln/dokumenttypdeklaration.htm)
- Es gibt 3 Arten eine DTD einzubinden

Variante 1: Intern
```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<!DOCTYPE memo [
	DTD-Anweisungen
]>
<memo>
...
</memo>
```
Beispiel:
```xml
<?xml version="1.0"?>
<!DOCTYPE Gruss [
	<!ELEMENT Gruss (#PCDATA)>
]>
<Gruss>Hallo Jupiter!</Gruss>
```

Variante 2: Extern
```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<!DOCTYPE memo SYSTEM "memo.dtd">
<memo>
...
</memo>
```
Beispiele:
```xml
<?cml version="1.0"?>
<!DOCTYPE EMail SYSTEM "../src/email.dtd">
```

```xml
<?xml version="1.0"?>
<!DOCTYPE EMail SYSTEM "http://www.example.org/xmlvorlagen/email.dtd">
```

Variante 3: Extern
```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<!DOCTYPE memo PUBLIC "Identifikator" "DTD-URL">
<memo>
...
</memo>
```
Beispiel:
``` xml
<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
```
### 2.2.1. XML Syntax
```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<!DOCTYPE memo SYSTEM memo.dtd>
<!-- Ein Kommentar -->
<memo>
	<von>
		<Name>Ernst Mayer</Name>
		<email>e.mayer@zzz.de</email>
	</von>
	<an>
		<Name>Fritz Peter</Name>
		<email>f.peter@yyy.de</email>
	</an>
	<thema id="1">ein Memo-Beispiel</thema>
	<bod>
		<paragraph>Ich muss an einem Beispiel XML erklären.</paragraph>
		<paragraph>Sag mal Deine Meinung!</paragraph>
	</body>
</memo>
```

```dtd
<!-- DTD memo -->
<!ELEMENT memo (von, an, thema, body)>

<!ELEMENT von (Name, email)>
<!ELEMENT an (Name, email)>

<!ELEMENT Name (#PCDATA)>
<!ELEMENT email (#PCDATA)>

<!ELEMENT thema (#PCDATA)>
<!ATTLIST thema id CDATA #REQUIRED>

<!ELEMENT body (paragraph+)>
<!ELEMENT paragraph (#PCDATA)>
```

Definition von Attributen
```dtd
<!ELEMENT square EMPTY>
<!ATTLIST square width CDATA "0">
```
Beispiel in XML:
```xml
<square width="100" />
```

XML DTD Validierungstools:
- Altova XML Spy: IDE für XML Dokumente - Lizenzkostenpflichtig
- XMLStarlet: [https://xmlstar.sourceforge.net/download.php](https://xmlstar.sourceforge.net/download.php) - Frei verfügbar
XML Online Validierer:
- W3C Markup Validation Service: [https://validator.w3.org](https://validator.w3.org)

XML-DTDs sind von SGML übernommen und haben eine Reihe von Einschränkungen
- DTDs sind keine XML-Dokumente
- DTDs beschreiben nur die Syntax, können z.B. keine Wertebereiche festlegen
- keine Unterstützung von Namensräumen
- begrenzte Möglichkeit zur Definition von Datentypen
## 2.3. XSD
- XML Schema Definition (XSD)
	- Alternativ zu DTD
	- Empfehlung des W3C
- Besonderheiten
	- Vordefinierte Datentypen
		- xs:string
		- xs:decimal
		- xs:integer
		- xs:boolean
		- xs:date
		- xs:time

Einfaches Beispiel für Elemente:
```xsd
<xs:element name="lastname" type="xs:string"/>
<xs:element name="age" type="xs:integer"/>
<xs:element name ="dateborn" type="xs:date"/>
```
Beispiel in XML:
```xml
<lastname>Refsnes</lastname>
<age>36</age>
<dateborn>1970-03-27</dateborn>
```
### 2.3.1. Besonderheiten
- Definition eigener Datentypen (Archetypen)
- Typkonstruktoren
	- sequence
	- all
	- choice

Beispiel für Typkonstruktoren:
```xml
<xs:element name="employee" type="fullpersoninfo"/>

<xs:complexType name="personinfo">
	<xs:sequence>
		<xs:element name="firstname" type="xs:string"/>
		<xs:element name="lastname" type="xs:string"/>
	</xs:sequence>
</xs:complexType>

<xs:complexType name="fullpersoninfo">
	<xs:complexContent>
		<xs:extension base="personinfo">
			<xs:sequence>
				<xs:element name="address" type="xs:string"/>
				<xs:element name="city" type="xs:string">
				<xs:element name="country" type="xs:string"/> 
			</xs:sequence>
		<xs:extension>
	<xs:complexContent>
<xs:complexType>
```

Attribute
```xml
<xs:attribute name="lang" type="xs:string" default="EN"/>
```
Beispiel in XML:
```xml
<lastname lang="EN">Smith</lastname>
```

Definition semantischer Constraints für Werte (sog. Facets)
```xml
<xs:element name="age">
	<xs:simpleType>
		<xs:restriction base="xs:string">
			<xs:minInclusive value="0"/>
			<xs:minInclusive value="120"/>
		</xs:restriction>
	</xs:simpleType>
</xs:element>
```
Weiteres Beispiel für Constrains:
```xml
<xs:element name="gender">
	<xs:simpleType>#
		<xs:restriction base="xs:string">
			<xs:pattern value="m|w|d">
		</xs:restriction>
	</xs:simpleType>
</xs:element>
```
Weiteres Beispiel für Constrains:
```xml
<xs:element name="car" type="carType"/>

<xs:simpleType name="carType">
	<xs:restriction base="xs:string">
		<xs:enumeration value="Audi"/>
		<xs:enumeration value="Fiat"/>
		<xs:enumeration value="VW"/>
		<xs:enumeration value="BMW"/>
	</xs:restriction>
</xs:simpleType>
```

Vollständiges Beispiel: note
```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:element name="note">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="to" type="xs:string"/>
				<xs:element name="from" type="xs:string"/>
				<xs:element name="heading" type="xs:string"/>
				<xs:element name="body" type="xs:string">
			</xs:sequence>
		</xs:complexType>
	</xs:element>
<xs:schema>
```
Beispiel note als DTD
```xml
<?xml version="1.0"?>
<!DOCTYPE note [
	<!ELEMENT note (to,from,heading,body)>
	<!ELEMENT to (#PCDATA)>
	<!ELEMENT from (#PCDATA)>
	<!ELEMNET heading (#PCDATA)>
	<!ELEMENT body (#PCDATA)>
]>

<note>
	<to>Tove</to>
	<from>Jani</from>
	<heading>Reminder</heading>
	<body>Don't forget me this weekend</body>
</note>
```
Referenzierung DTD
```xml
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">

<note>
	<to>Tove</to>
	<from>Jani</from>
	<heading>Reminder</heading>
	<body>Don't forget me this weekend!</body>
</note>
```
Referenzierung XSD
```xml
<?xml version="1.0"?>

<note xmlns="http://www.w3schools.com"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.w3schools.com note.xsd">
	<to>Tove</to>
	<from>Jani</from>
	<heading>Reminder</heading>
	<body>Don't forget me this weekend!</body>
</note>
```
## 2.4. Transformation von XML-Dokumenten
- Die eXtensible Stylesheet Language (XLS) ermöglicht die Darstellung (Publishing) und Umwandlung von XML-Dokumenten, um sie für eine Vielzahl von Anwendungen nutzbar zu machen
- Möglich sind:
	- Strukturelle Transformationen
	- Erzeugung dynamischer Dokumente
	- Darstellungstransformationen

![[Unbenannt 2.png]]
### 2.4.1. XSL
XSL baut auf zwei Quellen auf:
- Cascading Style Sheets (CSS) erlauben die einheitliche Formatierung von HTML-Tags. CSS ist standardisiert und aktuell in Version 3 verfügbar. Der Standard wird vollständig von allen aktuellen Browsern unterstützt.
- Document Style Semantics and Specification Language (DSSSL) aus der Definition von SGML

XSL besteht aus drei separaten Sprachen:
- den XSL Transformations (XSLT), welche Regeln für die Umwandlung eines XML-Dokuments spezifiziert
- XPath zur Einführung von Informationen in ein XML-Dokument und zum Navigieren indem Dokument
- XSL-FO (formatting objects) zur Umwandlung eines XML-Dokuments in andere Formate wie PDF, LaTex oder PS
### 2.4.2. XSL & XPath
- XPath ist eine Abfragesprache (Data Query Language - DQL), um durch die Menge der Elemente und Attribute eines XML-Dokuments navigieren und zugreifen zu können
- XPath ist eine XML-Sprache (W3C Standard)
- XPath ist Grundlage für andere XML-Sprachen:
	- XPointer
	- XLink
	- XQuery

![[Unbenannt 3.png]]
### 2.4.3. XSL & XSLT
XSLT steht für XSL Transformations und wird genutzt um ein XML-Dokument in ein anderen XML Dokument zu transformieren

![[Unbenannt 4.png]]

Beispiel: Unterschiedliche XSL Transformationen auf die gleiche XML-Datei angewandt
![[Unbenannt 5.png]]

- XSL arbeitet auf dem abstrakten Strukturbaum des XML-Dokuments (XPath)
- Mit Hilfe von XSLT werden im XSL-Stylesheet die Transformationsregeln beschrieben (Templates)
- Strukturbaum wird durchlaufen, für jeden Knoten wird ein passendes Template aus dem XSL-Stylesheet gesucht und angewendet

![[Unbenannt 6.png]]

Beispiel: Umwandlung des folgenden XMLs
```xml
<?xml version="1.0" encoding="iso-8859-1"?>

<catalog>
	<cd>
		<title>Empire Burlesque</title>
		<artist>Bob Dylan</artist>
		<country>USA</country>
		<company>Columbia</company>
		<price>10.90</price>
		<year>1985</year>
	</cd>
...
</catalog>
```
Dafür definieren wir das XSL Style Sheet
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlsns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output methode="html"/>
	<xsl:template match="/">
		<html>
			<body>
				<h2>My CD Collection</h2>
				<table border="1">
					<tr bgcolor="#9acd32">
						<th align="left">Title</th>
						<th align="left">Artist</th>
					</tr>
				<xsl:for-each select="/catalog/cd">
					<tr>
						<td><xsl:value-of select="title"/></td>
						<td><xsl:value-of select="artist"/></td>
					</tr>
				</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>
```
Nun müssen wir das XML-Dokument noch um die Stylesheet-Referenz ergänzen.
```xml
<?xml version="1.0" encoding="iso-8859-1"?>
<?xml-stylesheet type="text/xsl" href="cdcatalog.xsl"?>
<catalog>
	<cd>
		<title>Empire Burlesque</title>
		<artist>Bob Dylan</artist>
		<country>USA</country>
		<company>Columbia</company>
		<price>10.90</price>
		<year>1985</year>
	</cd>
...
</catalog>
```

- Das Ergebnis im Browser
- Steht ein XML/XSLT-fähiger Browser zur Verfügung, kann das XML-Dokument direkt angezeigt werden
	- Voraussetzung: XML-Datei muss Processing-Instruction enthalten, die auf XSL-Datei verweist, z.B.:

```xml
<?xml-stylesheet type="text/xsl" href="cdcatalog.xsl"?>
```

![[Unbenannt 7.png]]
### 2.4.4. Fazit: Präsentation von XML-Dokumenten
- XML Dokumente können mit Hilfe von XSL in verschiedenen Medien dargestellt werden zentrale Veraltung der Inhalte
	- Darstellung abhängig vom Anzeigegerät
	- Content Management
