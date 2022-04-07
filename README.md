# Datenmanagement NoSQL Documentstore

## Implementierung
### Couchbase installieren
Um Couchbase schnell zu installieren verwenden wir folgenden Docker-Befehl:
```
docker run -itd --name couchbase-server -p 8091-8094:8091-8094 -p 11210:11210 couchbase:community
```

Damit wird das Docker-Image für couchbase-server community edition gepullt und anschließend ausgeführt. Wenn der Download abgeschlossen ist und die Couchbase-Instanz läuft können wir zu der Implementierung erster CRUD-Befehle übergehen.
[1]


[1] "https://docs.couchbase.com/tutorials/getting-started-ce/install-manage/tutorial_en.html"
