# API definition

## umgangssprachlich

API ist zu einem inflationaerem schlagwort geworden dass fuer alles und nichts angewandt wird.

## theoretisch

fast jeder request an einen server ist theoretisch eine API nutzung.

## praktisch

wenn es eine **maschine zu maschine** kommunikation ist. z.b. wenn js-auf dem frontend etwas aus der db anfordert
und das vom backend z.b. via fastapi in fomr einer jsons zuruckgegeben wir und dann auf BE oder FE gerendert wird.

| kriterium      | str HTTP request              | API request                                                                   |
| :------------- | :---------------------------- | :---------------------------------------------------------------------------- |
| zweck          | kommukikation mit mensch      | maschine 2 maschine                                                           |
| ziel           | browser endnutzer             | andere programme/entwickler, \nscriptts, apps                                 |
| policy         | API offen, veraenderlich      | in der regel gibt es seine fixe policy                                        |
| HTTP-methoden  | meist nur GET, POST           | in der Regel alle: GET, POST, PUT, PATCH, DELETE                              |
| datenformat    | meist HTML                    | fst immer json.                                                               |
| errormessage   | 404                           | deatilierter                                                                  |
| zustaendigkeit | Template liefern (strd httpf) | userdaten um die leeren felder im template zu fuellen (api via http mit json) |

**in der regel ist folgendes damit gemeint:**

| JSON + HTTP + strukturierte Endpoints + Doku + für Code |
| ------------------------------------------------------- |

## openweathermap.org als beispiel

mein api-key: 231b2783ca83e098259411736fca2c4b
