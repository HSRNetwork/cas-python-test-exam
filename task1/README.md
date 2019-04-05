# Task1
## Aufgabenstellung
Dein Kollege hat mit der Erstellung eines Konfigurationsgeneriungstools begonnen und ist nun leider erkrankt und nicht erreichbar.
Zum Glück hat er den Code auf Github versioniert und du hast Zugriff darauf. 
Du weisst von der letzten Mittagspause, dass im Programm noch nicht alles läuft und entsprechend kommentiert ist.

1. Löse die Probleme, welche im Programm vorhanden sind.
2. Erweitere das Programm sodass es die folgenden Voraussetzungen erfüllt:

    * Die Konfigurationen sollen als Files abgelegt werden. Als Filename soll das Format <hostname>.config gewählt werden.
    * Neu sollen auch die VRFs in der YAML-Konfiguration hinterlegt werden können. Und beim Generieren der Konfigurationsfiles einbezogen werden. 
    Wichtig: Es soll möglich sein mehrere VRF pro Gerät zu definieren. 
    Es sollen dabei folgenden Werte definiert werden können: name, description, rd, route_target_export, route_target_import
