# Theorie Software Design: Antworten
## Frage 1
### Frage:
Sie beginnen als EntwicklerIn in einem neuen Unternehmen und bekommen die Verantwortung für ein Modul. 
Das Modul ist über eine lange Zeit hinweg gewachsen und besteht nur aus sehr wenigen Klassen. 
Die Methoden dieser Klassen sind meist sehr lange, oftmals einige hundert Zeilen oder länger, und 
sie sind auch eher spärlich dokumentiert. Was für Nachteile ergeben sich für Sie durch diesen Code? 
Welche grundlegenden Software Design Prinzipien werden evtl. nicht eingehalten?
### Antwort:
Aufgrund der fehlenden Dokumentation ist es sehr schwer die Funktionsweise des Moduls nachzuvollziehen. 
Um das Modul zu verstehen und die Abhängigkeiten der darin enthaltenen Klassen und Funktionen zu 
verstehen, muss der ganze Code zunächst gelesen werden. Beim Lesen des Codes könnte hierbei eine 
Dokumentation verfasst werden, was wiederum sehr viel Zeit in Anspruch nimmt.  

Bei der Entwicklung des Moduls wurde das KISS-Prinzip (Keep it simple and short) offensichtlich nicht
eingehalten, da die Methoden der Klassen alles andere als kurz gehalten wurden. Möglicherweise gingen 
die Entwickler davon aus, dass das YAGNI-Prinzip (You're not gonna need it) zur Anwendung kommen würde, 
weshalb sie alle weiteren Prinzipien außer Acht ließen.



## Frage 2
### Frage:
Für die vollständige Überarbeitung/Neuschreiben bleibt Ihnen keine Zeit, da sie ihr/e Vorgesetze/r 
schon mit der Umsetzung des nächsten Features beauftragt hat. Wie würden Sie bei der Umsetzung 
vorgehen?
### Antwort:
Als erstes sollten Prioritäten gesetzt werden. Wenn nicht genug Zeit für eine vollständige Überarbeitung
des Moduls gegeben wird, sollten zumindest die Funktionen dokumentiert werden. Zusätzlich sollten die 
Vorgesetzten darüber informiert werden, dass für die vollständige Bearbeitung des Moduls mehr Zeit 
benötigt wird, welche, entweder als großer Block oder verteilt über die folgenden Wochen, 
eingeplant werden sollte.