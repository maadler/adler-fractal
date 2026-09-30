# Adler-Fraktal: Literaturprüfung vom 30. September 2026

## Ergebnis

Die vorliegende Prüfung belegt **keine mathematische Neuheit**. Die kontraktive Endpunktfamilie ist genau ein reguläres Polygon-IFS in anderer Parametrisierung. Der kontraktive Linienabschluss ist ein inhomogener selbstähnlicher Attraktor mit einem Stern als Kondensationsmenge. Beide allgemeinen Klassen sind seit langem bekannt. Die eigene Benennung, Beschreibung und konkrete Implementierung können veröffentlicht werden, sofern bekannte Zusammenhänge transparent genannt werden.

Für die genaue endliche gleichlange Turtle-Zeichenvorschrift mit 72 Richtungen und zwei Generationen wurde in der durchgesehenen Literatur kein belastbarer Erstbeleg festgestellt. Das ist weder ein Beweis der Neuheit noch ein Nachweis, dass Marcus Adler diese Rekursion zuerst verwendet hat. Namenssuchen sind durch die zahlreichen anderen Forscher und Angebote mit dem Namen Adler besonders unscharf.

## Suchumfang und Vorgehen

Geprüft wurden am genannten Datum öffentliche Websuche, arXiv und die unten genannten Volltexte. Der Fokus lag auf der Rekursionsvorschrift und ihrer mathematischen Äquivalenz, nicht nur auf dem Namen. Suchbegriffe umfassten:

- `"Adler fractal" mathematics`, `"Adler-Fraktal"` und Varianten;
- `regular polygon iterated function system Sierpinski n-gon similarities fractal`;
- `recursive radial star fractal equal length spokes turtle`;
- `"recursive" "starburst" "fractal" turtle`;
- `"fractal" "spokes" "endpoints" recursion`;
- `inhomogeneous self similar sets condensation set Hausdorff dimension max Fraser paper`.

Nicht durchgeführt wurde eine vollständige systematische Suche in MathSciNet, zbMATH, historischen Büchern, allen Codearchiven oder nichtöffentlichen Quellen. Die Suchmaschinentreffer waren teilweise unspezifisch. Für die mathematische Einordnung wurde deshalb zusätzlich die konkrete Abbildungsvorschrift direkt mit den Primärquellen verglichen. Es wird keine absolute Aussage über die weltweite Verwendung des Namens getroffen.

## Entscheidende Primärquellen

| Quelle | Tatsächlich geprüft | Bezug zur Konstruktion |
| --- | --- | --- |
| Hutchinson (1981), *Fractals and Self-Similarity* | Volltext der auf der ANU-Autorseite bereitgestellten Fassung; insbesondere Einleitung, §§ 3 und 5 | Existenz und Eindeutigkeit kompakter IFS-Attraktoren; Dimensionsformel bei offener Mengenbedingung |
| Tzanov (2015), arXiv:1502.01384 | Abstract und Volltext; insbesondere §§ 1-3 sowie Diskussion in § 5 | Kontraktionen um reguläre Polygonvertices; polygonale und sternförmige Ausgangsfiguren; gleiche Attraktoren bei verschiedenen Anfangsfiguren |
| Fraser (2012; arXiv-Einreichung 2013), arXiv:1301.1881 | Abstract und Volltext; insbesondere § 1.1, Gleichungen (1.2)-(1.3) | Inhomogener Attraktor mit Kondensationsmenge; Zerlegung in homogenen Attraktor und Orbitalmenge; bekannte Hausdorff-Dimensionsregel |

Hutchinsons öffentlich bereitgestellte Fassung enthält kleinere Formatkorrekturen gegenüber dem Original. Bei Fraser wird die Zeitschriftenangabe 2012 von der arXiv-Einreichung 2013 unterschieden. Ein Titel oder Abstract allein wurde nicht als Beleg einer exakt gleichen endlichen Turtle-Rekursion behandelt.

## Direkter Äquivalenznachweis

Aus der vorgeschlagenen Skalierung entsteht für die Endpunkte

\[
f_j(x)=Lu_j+rx=rx+(1-r)v_j,\qquad v_j=\frac{L}{1-r}u_j.
\]

Dies ist die übliche Homothetie mit Faktor `r` um den Polygonvertex `vⱼ`. Die Namensänderung, andere Koordinateneinheiten und die Ergänzung einer zeichnerischen Wurzel machen daraus keine neue Endpunktfamilie. **Das ist eine mathematische Schlussfolgerung aus der eigenen Definition und den geprüften Polygon-IFS, keine Aussage, dass die komplette Originaldatei in einer Quelle gefunden wurde.**

Für den Stern `B = ⋃ⱼ[0,Luⱼ]` erfüllt der kontraktive Linienabschluss

\[
S=B\cup\bigcup_j f_j(S).
\]

Dies entspricht der bereits bekannten inhomogenen IFS-Gleichung mit Kondensationsmenge. Die Zusammenstellung im Manuskript erklärt diese Spezialisierung und die Besonderheiten des nichtkontraktiven Originals.

## Zulässige Positionierung des Entwurfs

Passend ist etwa:

> Marcus Adler dokumentiert unter dem vorgeschlagenen Namen Adler-Fraktal eine rekursive radiale Zeichenvorschrift und eine Referenzimplementierung. Der Entwurf analysiert ihre endlichen Spuren, den gleichlangen Grenzfall und ihre Beziehung zu bekannten Polygon-IFS.

Nicht durch die Prüfung gedeckt wären Aussagen wie „eine neue mathematische Fraktalfamilie“, „erstmals entdecktes Fraktal“, „amtlich registrierter Fraktalname“ oder „Priorität wissenschaftlich bewiesen“. Ein DOI liefert eine zitierfähige Veröffentlichung, keine Neuheitsprüfung.

## Quellenlinks

- [Hutchinson, Verlagsseite / DOI](https://doi.org/10.1512/iumj.1981.30.30055)
- [Hutchinson, frei zugänglicher Volltext vom Autor](https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf)
- [Tzanov, arXiv und Volltext](https://arxiv.org/abs/1502.01384)
- [Fraser, arXiv und Volltext](https://arxiv.org/abs/1301.1881)
- [Zenodo, aktuelle Anleitung zum neuen Datensatz](https://help.zenodo.org/docs/deposit/create-new-upload/)

Links und Einordnung wurden am 30. September 2026 geprüft. Es wurden keine ganzen fremden Artikel oder fremden Abbildungen in dieses Paket übernommen.
