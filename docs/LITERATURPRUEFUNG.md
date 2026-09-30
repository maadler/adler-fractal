# Adler-Fraktal: Literaturprüfung vom 30. September 2026

Diese Notiz hält fest, wonach gesucht wurde, was dabei herauskam und was ich daraus schließe. Suche und Quellenvergleich liefen mit KI-Unterstützung. Für Version 1.0.1 wurden Fraser und Tzanov noch einmal am Volltext gegengeprüft, bei Hutchinson die bibliografischen Angaben.

## Ergebnis

Die Prüfung belegt **keine mathematische Neuheit**. Die kontraktive Endpunktfamilie ist genau ein reguläres Polygon-IFS in anderer Parametrisierung. Der kontraktive Linienabschluss ist ein inhomogener selbstähnlicher Attraktor mit einem Stern als Kondensationsmenge. Beide allgemeinen Klassen sind seit langem bekannt.

Für die genaue endliche gleich lange Turtle-Zeichenvorschrift mit 72 Richtungen und zwei Generationen wurde in der durchgesehenen Literatur kein belastbarer früherer Beleg gefunden. Das ist weder ein Beweis der Neuheit noch ein Nachweis, dass ich diese Rekursion als Erster verwendet habe. Namenssuchen sind durch die vielen anderen Forscher und Angebote mit dem Namen Adler besonders unscharf.

## Suchumfang und Vorgehen

Geprüft wurden am genannten Datum öffentliche Websuche, arXiv und die unten genannten Volltexte. Der Fokus lag auf der Rekursionsvorschrift und ihrer mathematischen Äquivalenz, nicht nur auf dem Namen. Suchbegriffe umfassten:

- `"Adler fractal" mathematics`, `"Adler-Fraktal"` und Varianten;
- `regular polygon iterated function system Sierpinski n-gon similarities fractal`;
- `recursive radial star fractal equal length spokes turtle`;
- `"recursive" "starburst" "fractal" turtle`;
- `"fractal" "spokes" "endpoints" recursion`;
- `inhomogeneous self similar sets condensation set Hausdorff dimension max Fraser paper`.

Nicht durchgeführt wurde eine vollständige systematische Suche in MathSciNet, zbMATH, historischen Büchern, allen Codearchiven oder nichtöffentlichen Quellen. Die Suchmaschinentreffer waren teilweise unspezifisch. Für die mathematische Einordnung wurde deshalb zusätzlich die konkrete Abbildungsvorschrift direkt mit den Primärquellen verglichen. Eine Aussage über die weltweite Verwendung des Namens ist damit nicht möglich.

## Entscheidende Primärquellen

| Quelle | Geprüft | Bezug zur Konstruktion |
| --- | --- | --- |
| Hutchinson (1981), *Fractals and Self-Similarity* | Volltext der auf der ANU-Autorseite bereitgestellten Fassung; insbesondere Einleitung, §§ 3 und 5 | Existenz und Eindeutigkeit kompakter IFS-Attraktoren; Dimensionsformel bei offener Mengenbedingung |
| Tzanov (2015), arXiv:1502.01384 | Abstract und Volltext; insbesondere §§ 1-3 sowie § 5 | Kontraktionen um die Ecken regulärer Polygone; polygonale und sternförmige Ausgangsfiguren, in § 5 auch der Strahlenstern vom Mittelpunkt zu den Ecken; gleiche Attraktoren bei verschiedenen Ausgangsfiguren |
| Fraser (2012; arXiv-Einreichung 2013), arXiv:1301.1881 | Abstract und Volltext; insbesondere § 1.1, Gleichungen (1.2)-(1.3) | Inhomogener Attraktor mit Kondensationsmenge; Zerlegung in homogenen Attraktor und Orbitalmenge; bekannte Hausdorff-Dimensionsregel |

Hutchinsons öffentlich bereitgestellte Fassung enthält kleinere Formatkorrekturen gegenüber dem Original. Bei Fraser wird die Zeitschriftenangabe 2012 von der arXiv-Einreichung 2013 unterschieden. Ein Titel oder Abstract allein wurde nicht als Beleg einer exakt gleichen endlichen Turtle-Rekursion behandelt.

## Direkter Äquivalenznachweis

Aus der Skalierung entsteht für die Endpunkte

```math
f_j(x)=Lu_j+rx=rx+(1-r)v_j,\qquad v_j=\frac{L}{1-r}u_j.
```

Dies ist die übliche Homothetie mit Faktor `r` um die Polygonecke `vⱼ`. Ein anderer Name, andere Koordinateneinheiten und die Ergänzung einer zeichnerischen Wurzel machen daraus keine neue Endpunktfamilie. **Das ist eine mathematische Schlussfolgerung aus der eigenen Definition und den geprüften Polygon-IFS, keine Aussage, dass das vollständige Originalskript in einer Quelle gefunden wurde.**

Für den Stern `B = ⋃ⱼ[0,Luⱼ]` erfüllt der kontraktive Linienabschluss

```math
S=B\cup\bigcup_j f_j(S).
```

Dies entspricht der bekannten inhomogenen IFS-Gleichung mit Kondensationsmenge. Der Bericht erklärt diese Spezialisierung und die Besonderheiten des nichtkontraktiven Originals.

## Was daraus folgt

Ich beschreibe das Adler-Fraktal deshalb so:

> Unter dem Namen Adler-Fraktal dokumentiere ich eine rekursive radiale Zeichenvorschrift und eine Referenzimplementierung. Der Bericht analysiert ihre endlichen Spuren, den gleich langen Grenzfall und ihre Beziehung zu bekannten Polygon-IFS.

Nicht gedeckt wären Aussagen wie „eine neue mathematische Fraktalfamilie“, „erstmals entdecktes Fraktal“, „amtlich registrierter Fraktalname“ oder „Priorität wissenschaftlich bewiesen“. Ein DOI liefert eine zitierfähige Veröffentlichung, keine Neuheitsprüfung.

## Quellenlinks

- [Hutchinson, Verlagsseite / DOI](https://doi.org/10.1512/iumj.1981.30.30055)
- [Hutchinson, frei zugänglicher Volltext vom Autor](https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf)
- [Tzanov, arXiv und Volltext](https://arxiv.org/abs/1502.01384)
- [Fraser, arXiv und Volltext](https://arxiv.org/abs/1301.1881)

Links und Einordnung wurden am 30. September 2026 geprüft. Es wurden keine ganzen fremden Artikel oder fremden Abbildungen in dieses Paket übernommen.
