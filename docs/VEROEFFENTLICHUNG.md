# Adler-Fraktal: Veröffentlichung vorbereiten

Stand der Dateierzeugung: 30. September 2026. Marcus Adler hat die öffentliche Ablage und die Lizenzen ausdrücklich gewählt. Das Paket wird als technischer Bericht v1.0.0 veröffentlicht; eine unabhängige Begutachtung wurde nicht durchgeführt. Der DOI `10.5281/zenodo.23057945` wurde im eigenen Zenodo-Konto tatsächlich reserviert. Seine Registrierung erfolgt mit der Veröffentlichung des Datensatzes. Das Erstellungsdatum allein belegt keine historische Priorität.

## Fertig vorbereitet

- Originalcode unverändert archiviert, Referenzgenerator v1.0.0 und 12 Tests;
- deutsche Definition und Literaturprüfung;
- englisches neunseitiges Manuskript mit Beweisen und erzeugten Abbildungen;
- Metadaten und Zitierdatei mit dem tatsächlich reservierten DOI;
- Prüfsummen und reproduzierbare Befehle.

## Inhalt und Lizenzen

Die bekannte IFS-Verwandtschaft und die fehlende Neuheitsbehauptung bleiben ausdrücklich erhalten. Für eine wissenschaftliche Einreichung ist eine unabhängige mathematische Durchsicht sinnvoll.

Der Autor hat MIT für die Software einschließlich seines Originalcodes und CC BY 4.0 für eigene Texte und Abbildungen gewählt. `LICENSE` und `LICENSE_DOCUMENTATION.md` nennen den jeweiligen Geltungsbereich. ORCID und institutionelle Zugehörigkeit werden nur eingetragen, wenn sie tatsächlich vorliegen.

## GitHub

Das öffentliche Repository [maadler/adler-fractal](https://github.com/maadler/adler-fractal) wurde tatsächlich im Konto `maadler` angelegt. Der geprüfte Quellcode, die Dokumentation und die Abbildungen bilden die Version 1.0.0. Für diese Version ist der Release-Tag `v1.0.0` vorgesehen. `CITATION.cff` enthält den reservierten Zenodo-DOI und die tatsächliche Repository-Adresse.

## Zenodo: konkreter Ablauf

Die folgenden Angaben beruhen auf der am 30. September 2026 geprüften [offiziellen Zenodo-Anleitung](https://help.zenodo.org/docs/deposit/create-new-upload/).

1. Bei [Zenodo](https://zenodo.org/) im eigenen Konto anmelden und **New upload** öffnen.
2. Manuskript-PDF und das vollständige ZIP-Paket hochladen. Der Upload ist bis zur Veröffentlichung ein Entwurf.
3. Titel, Autor und Beschreibung aus `PUBLIKATIONSMETADATEN.json` übernehmen. Für den gemischten Upload einen passenden Ressourcentyp wählen, beispielsweise **Publication / Report** für den Bericht mit beigefügtem Code. Bei separater Softwarearchivierung **Software** verwenden und später die beiden Datensätze verknüpfen.
4. Die tatsächliche Veröffentlichungssprache ist Englisch für das Manuskript; die beigefügte Dokumentation ist teilweise Deutsch. Stichworte sind unter anderem `recursive geometry`, `radial construction`, `iterated function system` und `polygon IFS`.
5. Die gewählte Lizenz in Zenodo korrekt setzen. Das Publikationsdatum ist der Tag der tatsächlichen öffentlichen Veröffentlichung.
6. Falls noch kein DOI existiert, die entsprechende Option wählen und **Get a DOI now!** benutzen. Das reserviert einen echten DOI, registriert ihn aber noch nicht.
7. Den tatsächlich reservierten DOI in Manuskript und Zitierdatei einsetzen, Dateien neu erzeugen, Prüfsummen und ZIP aktualisieren und die endgültigen Dateien hochladen.
8. **Save draft** und **Preview** benutzen. Titel, Autorenreihenfolge, Lizenz, Dateien und Beschreibung prüfen.
9. Mit **Publish** öffentlich machen. Erst dann wird der DOI registriert. Die Datensatz-URL und den registrierten DOI anschließend dokumentieren.

Laut der aktuellen Zenodo-Anleitung gehen reservierte DOI verloren, wenn der zugehörige Entwurf gelöscht wird. Die Metadaten sind nach Veröffentlichung öffentlich, auch bei eingeschränktem Dateizugriff. Neue Versionen erhalten die tatsächlichen Identifikatoren des Archivs; sie werden hier nicht vorweggenommen.

## Positionierung

Titel: **The Adler Fractal: A Recursive Radial Drawing and Its Polygon-IFS Limits**.

Die Veröffentlichung dokumentiert eine Konstruktion und ihren Code. Sie ist kein Beweis dafür, dass der Algorithmus neu ist, und keine amtliche Vergabe eines mathematischen Namens. Die bereits bekannten homogenen und inhomogenen IFS-Bezüge werden ausdrücklich genannt.

Eine arXiv-Einreichung ist ein optionaler späterer Schritt, falls eine unabhängige fachliche Prüfung und das wissenschaftliche Niveau eine passende Einreichung rechtfertigen. In diesem Paket wird weder eine Annahme bei arXiv noch ein Peer Review behauptet.
