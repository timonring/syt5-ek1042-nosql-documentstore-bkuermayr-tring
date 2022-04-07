# Recherche

## Funktionsweise von Couchbase

Couchbase ist eine dokumentenorientierte nicht-relationale Datenbank  (NoSQL-Datenbank). Sie speichert Informationen in Form von JSON-Dokumenten [1].

Die primäre Datenspeichereinheit in Couchbase Server ist also ein JSON-Dokument, das es ermöglicht Anwendungen ohne fest definierte relationale Datenbanktabellen zu erstellen. Da Anwendungsobjekte als Dokumente modelliert werden, müssen keine Schemamigrationen durchgeführt werden.

Die Binärdaten können auch in Dokumenten gespeichert werden, aber die Verwendung der JSON-Struktur ermöglicht die Indizierung und Abfrage der Daten mithilfe von Views. Couchbase Server bietet eine JavaScript-basierte Abfrage-Engine, um Datensätze basierend auf Field-Values zu finden [2].

Couchbase Server ist noch dazu eine persistente Datenbank, die eine integrierte RAM-Caching-Schicht nutzt, wodurch sehr schnelle Erstellungs-, Speicher-, Aktualisierungs- und Abrufvorgänge unterstützt werden. Couchbase basiert auf drei Kernprinzipien [4]:

1. **Einfach**

   Couchbase Server baut auf der grundlegenden Key/Value- oder Dokumentenspeicherstruktur von Memcached auf. Dies macht es sehr einfach, Daten zu speichern und abzurufen. Es müssen keine Datenstruktur definiert werden, bevor mit dem Speichern begonnen werden kann, und es sind keine komplizierten Abfragen oder Abfragesprachen erforderlich, um die Daten wieder abzurufen.

2. **Schnell**

   Da Couchbase Server versucht, jederzeit möglichst viele der aktiv genutzten Daten im Speicher zu halten, ist die Geschwindigkeit des Zugriffs auf die in der Datenbank gespeicherten Daten im Allgemeinen nur durch die Netzwerkgeschwindigkeit begrenzt, die für den Zugriff auf den Speicherwert erforderlich ist. 

3. **Flexibel**

   Das System ist aufgrund einer „Shared-Nothing“-Architektur linear skalierbar. Die Gesamtleistung des Clusters kann verbessert werden, indem weitere Knoten hinzufügt werden. Der Cluster (oder die Clients und Anwendungen, die ihn verwenden) muss während dieses Prozesses nicht herunterfahren werden, um diesen Vorgang auszuführen. Der gesamte Cluster läuft während des Vorgangs weiter.

## Cluster-Funktionalität

Die Cluster-Komponente verteilt Daten auf mehrere Server, um die Daten- und I/O-Last zu teilen, während sie intelligente Server- und Client-Zugriffsbibliotheken integriert, die es Clients ermöglichen, schnell auf den richtigen Knoten innerhalb des Clusters zuzugreifen. Durch diese intelligente Verteilung bietet Couchbase Server eine hervorragende Skalierbarkeit, die einfach erweitert werden kann, indem weitere Server hinzufügt werden, wenn Last oder Anwendungsanforderungen steigen [4].

Jeder Couchbase-Knoten besteht aus einem Index-Service, einem Daten-Service, einem Abfrage-Service und einer Cluster-Manager-Komponente. Die Services lassen sich bei Bedarf auf unterschiedlichen Knoten eines Clusters betreiben. Der Cluster Manager ist für die Konfiguration und die Überwachung aller Services in einem Couchbase-Cluster verantwortlich. Er managt beispielsweise die Replikations-Streams und verteilt Aufgaben [1]. 

![What is Couchbase ? – Can Sayın](https://www.cansayin.com/wp-content/uploads/2020/01/cb1-1.png)

​												Abb. 1, Couchbase Cluster mit mehreren Nodes [5]

Wenn Couchbase Server auf einem Knoten konfiguriert wird, kann er entweder als sein eigener, neuer Cluster oder als Teilnehmer in einem bestehenden Cluster angegeben werden. Sobald also ein Cluster existiert, können ihm aufeinanderfolgende Knoten hinzugefügt werden; jeder Knoten, auf dem Couchbase Server läuft. Wenn ein Cluster mehrere Knoten hat, läuft der Couchbase Cluster Manager auf jedem Knoten: Dieser verwaltet die Kommunikation zwischen den Knoten und stellt sicher, dass alle Knoten fehlerfrei sind. Der Cluster-Manager stellt der Benutzeroberfläche der Couchbase-Webkonsole Informationen über den Cluster bereit [3].

### Buckets

Couchbase Server bietet Buckets als Datenverwaltungsdienst. Diese Buckets sind isolierte virtuelle Container für Daten. Ein Bucket ist eine logische Gruppierung physischer Ressourcen innerhalb eines Clusters von Couchbase-Servern. Sie können von mehreren Clientanwendungen in einem Cluster verwendet werden. Buckets bieten einen sicheren Mechanismus zum Organisieren, Verwalten und Analysieren von Datenspeicherressourcen [4]. 

## Quellen

[1] "Was ist Couchbase? " [online](https://www.bigdata-insider.de/was-ist-couchbase-a-934651/)

[2] "Introduction to Couchbase" [online](https://www.todaysoftmag.com/article/1506/introduction-to-couchbase-nosql-document-database)

[3] "Clusters and Availability" [online](https://docs.couchbase.com/server/current/learn/clusters-and-availability/clusters-and-availability.html)

[4] "Chapter 1. Introduction to Couchbase Server" [online](https://www.oreilly.com/library/view/getting-started-with/9781449331054/ch01.html)

[5] "What is Couchbase?" [online](https://www.cansayin.com/what-is-couchbase/)