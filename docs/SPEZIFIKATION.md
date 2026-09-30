# Adler-Fraktal: mathematische Spezifikation v1.0.1

**Marcus Adler** · Stand 30. September 2026 · technischer Bericht, nicht unabhängig begutachtet

Diese Spezifikation legt fest, was ich unter dem Adler-Fraktal verstehe: die Zeichenvorschrift aus meinem Turtle-Skript `original/eagle_fractal.py`, ihre Parameter und die Mengen, die daraus entstehen. Der Name ist mein Vorschlag für diese Konstruktion, kein etablierter mathematischer Begriff, und ich beanspruche weder Neuheit noch Priorität. Dieselben Aussagen stehen englisch im [Bericht](Adler_Fractal_Manuscript.pdf).

## 1. Parameter und Begriffe

Wir identifizieren die euklidische Ebene mit den komplexen Zahlen. Sei `m ≥ 3` eine ganze Zahl, `n ≥ 0` die ganzzahlige Rekursionstiefe, `L > 0` die Anfangslänge, `0 < r ≤ 1` der Skalierungsfaktor und `θ` eine feste globale Anfangsrichtung. Der Startpunkt ist `z₀`.

```math
u_j=\exp\bigl(i(\theta+2\pi j/m)\bigr),\qquad j=0,\ldots,m-1.
```

Alle Generationen verwenden dieselben **absoluten** Richtungen. Es gibt keine Rotation relativ zum ankommenden Ast. Der Winkelabstand ist `α = 360° / m`; `m` ist der primäre Parameter. Für das Original gilt

```math
(m,n,L,r,\theta,z_0)=(72,2,200,1,0,0).
```

Das Original verwendet `range(0, 360, ang)`. Ist die Schrittweite kleiner als 360 und kein Teiler davon, dann ist die Lücke am Kreisende anders als die übrigen Lücken. Solche nichtregulären Richtungssätze gehören nicht zu dieser Familie. Der Generator weist sie beim Winkelimport ab, ebenso die Schrittweiten 180 und 360, die weniger als drei Richtungen übrig lassen.

## 2. Endpunkte und endliche Linienmenge

Für ein Wort `w = (j₁, …, jₖ)` ist der Punkt

```math
p_w=z_0+L\sum_{t=1}^{k}r^{t-1}u_{j_t},\qquad p_{\emptyset}=z_0.
```

Die Endpunktmenge einer einzelnen Generation ist

```math
E_k=\{p_w:\lvert w\rvert=k\}.
```

Sie hat `mᵏ` **Adressen**, nicht zwingend `mᵏ` verschiedene Punkte. Die endliche Adler-Linienmenge ist

```math
A_n=\bigcup_{k=1}^n\ \bigcup_{\lvert w\rvert=k}[p_{w^-},p_w],\qquad A_0=\emptyset.
```

`w⁻` bezeichnet das Wort ohne sein letztes Zeichen. `[a,b]` ist das geschlossene gerade Liniensegment. Wiederholte Segmente sind in dieser Mengendefinition nur einmal enthalten, werden bei der zeichnerischen Ausführung aber jedes Mal gezeichnet.

In den folgenden Identitäten wird zur Vereinfachung `z₀ = 0` gesetzt. Für einen anderen Startpunkt wird die gesamte Figur verschoben. Mit

```math
B=\bigcup_j[0,Lu_j],\quad f_j(x)=Lu_j+rx
```

gilt für `n ≥ 1`: `Aₙ = B ∪ ⋃ⱼ fⱼ(Aₙ₋₁)`.

## 3. Zeichenreihenfolge

An jedem Knoten werden zunächst alle `m` Strahlen in aufsteigender Winkelreihenfolge gezeichnet. Erst danach werden die Kinder rekursiv, ebenfalls in dieser Reihenfolge, besucht. Zwischen einem Segmentende und dem nächsten Startpunkt ist der Stift angehoben. Das ist die Ausführungsreihenfolge des Originals; der Referenzgenerator bildet sie mit einem expliziten Stapel nach.

## 4. Endliche Eigenschaften

Die Anzahl der Zeichenbefehle lautet

```math
N_n=\sum_{k=1}^n m^k=\frac{m(m^n-1)}{m-1}.
```

| Tiefe n, m = 72 | Zeichenbefehle |
| --- | ---: |
| 0 | 0 |
| 1 | 72 |
| 2 | 5.256 |
| 3 | 378.504 |
| 4 | 27.252.360 |

Für `m = 18` (Winkelabstand 20°, der Vorgabewert im Funktionskopf des Originals) ergibt Tiefe 4 dagegen `18 + 324 + 5.832 + 104.976 = 111.150` Befehle.

Die summierte Länge mit Zeichenmultiplizität ist `L m ∑ₖ₌₀ⁿ⁻¹ (m r)ᵏ`. Für das Original mit Tiefe 2 beträgt sie 1.051.200 Längeneinheiten. Dies ist nicht die Länge der Vereinigungsmenge ohne Überzeichnung.

Der scharfe äußere Radius um `z₀` lautet

```math
R_n=\begin{cases}nL,&r=1,\\L(1-r^n)/(1-r),&0<r<1.\end{cases}
```

Die obere Schranke folgt aus der Dreiecksungleichung; ein Wort mit stets derselben Richtung erreicht sie. Jede Figur ist unter den Rotationen und Spiegelungen des regulären `m`-Ecks um den Startpunkt invariant. Bei `n ≥ 1` ist `Aₙ` zusammenhängend und eine endliche Vereinigung nichtdegenerierter Segmente, daher `dim_H Aₙ = 1`.

Für `r = 1`, `n = 2` gilt

```math
\lvert p_{(a,b)}-z_0\rvert=2L\left|\cos\frac{\pi(a-b)}m\right|.
```

Das erklärt die konzentrischen diskreten Endpunktradien. Weiterhin mit `r = 1` ist bei geradem `m` die Anzahl verschiedener Endpunkte `|E₂| = m²/2 + 1`. Beweis: `p_(a,b)/2` ist der Mittelpunkt der Sehne von `L u_a` nach `L u_b` (für `a = b` ein einzelner Punkt des Kreises), und ein von null verschiedener Mittelpunkt bestimmt das ungeordnete Paar eindeutig. Von `m(m+1)/2` ungeordneten Paaren bilden die `m/2` antipodalen Paare alle den gleichen Mittelpunkt null. Beim Original ergeben sich **2.593 verschiedene Endpunkte**; null hat 72 geordnete Adressen. Die Kreisradien beschreiben Endpunkte, nicht ausgefüllte Kreislinien.

## 5. Gleich lange Linien: der unendliche Originalfall

Für das Original `m = 72`, `r = 1` ist die Vereinigung aller Endpunkte eine additive Gruppe: Zu jeder Richtung gehört auch ihre Gegenrichtung, daher lassen sich alle ganzzahligen Linearkombinationen als endliche Wörter realisieren.

Unter den Richtungen liegen insbesondere 0°, 30°, 60° und 90°, also `u₀`, `u₆`, `u₁₂` und `u₁₈`. Mit `θ = 0` gilt

```math
2u_{6}-u_{18}=(\sqrt3,0),\qquad
2u_{12}-u_{0}=(0,\sqrt3).
```

Außerdem sind `u₀ = (1,0)` und `u₁₈ = (0,1)` enthalten. Somit enthält die Endpunktgruppe

```math
L(\mathbb Z+\sqrt3\mathbb Z)\times L(\mathbb Z+\sqrt3\mathbb Z).
```

`ℤ + √3 ℤ` ist dicht in der reellen Achse: Nach dem Schubfachprinzip gibt es beliebig kleine positive Zahlen dieser Form; ihre ganzzahligen Vielfachen approximieren jeden reellen Wert. Das kartesische Produkt ist daher dicht in der Ebene. Es folgt

```math
\overline{\bigcup_{n\ge1}A_n}=\mathbb R^2.
```

Dabei hat die nicht abgeschlossene Linienvereinigung weiterhin Hausdorff-Dimension 1. Die Endpunktvereinigung ist abzählbar und hat Dimension 0, ihr Abschluss Dimension 2. Es gibt keinen beschränkten kompakten Grenzattraktor für `r = 1`. Die Aussage über die ganze Ebene betrifft alle Rekursionstiefen gemeinsam, nicht die endliche Originalabbildung.

## 6. Kontraktive Endpunktmenge

Für `0 < r < 1` definiert sich die kompakte Endpunktgrenzmenge durch

```math
K=\left\{L\sum_{t=1}^{\infty}r^{t-1}u_{j_t}:j_t\in\{0,\ldots,m-1\}\right\}.
```

Sie ist der eindeutige nichtleere kompakte Attraktor des Polygon-IFS `fⱼ(x) = L uⱼ + r x`. Mit `vⱼ = L uⱼ / (1-r)` lässt sich dieselbe Abbildung als `fⱼ(x) = r x + (1-r) vⱼ` schreiben: Kontraktion um die Ecken eines regulären Polygons. Diese Klasse ist bekannt und wird hier nicht als neue Fraktalfamilie beansprucht.

Die Endpunktmengen konvergieren im Hausdorff-Abstand `d_H` (zwischen nichtleeren kompakten Mengen) mit

```math
d_H(E_n,K)\le\frac{Lr^n}{1-r}.
```

Das folgt durch Abschneiden beziehungsweise Fortsetzen der Adressreihe und Abschätzen des Restes. Die konvexe Hülle ist das reguläre Polygon mit Eckradius `L/(1-r)`.

### Gerades m bei r = 1/2: das gefüllte Vieleck

In diesem Fall ist `K` das ganze gefüllte reguläre `m`-Eck `P` mit den Ecken `vⱼ = 2L uⱼ`. Jedes `fⱼ(x) = (x + vⱼ)/2` bildet `P` in sich ab; es genügt also, dass die Bilder `P` überdecken. Schreibe `x ∈ P` als `α vⱼ + β vⱼ₊₁` mit `α, β ≥ 0`, `α + β ≤ 1` und, nach Symmetrie, `α ≥ β`. Dann ist `x = fⱼ(y)` für

```math
y=(2\alpha-1)\,v_j+2\beta\,v_{j+1}=(1-2\alpha)\,v_{j+m/2}+2\beta\,v_{j+1},
```

denn bei geradem `m` ist `−v_j = v_(j+m/2)` selbst eine Ecke. Für `α ≥ 1/2` liegt `y` nach der ersten Darstellung im Dreieck `0, vⱼ, vⱼ₊₁`. Sonst sind in der zweiten Darstellung beide Koeffizienten nichtnegativ mit Summe höchstens eins, `y` ist also eine Konvexkombination zweier Ecken und des Mittelpunkts. In beiden Fällen liegt `y` in `P`, also `P = ⋃ⱼ fⱼ(P)`, und aus der Eindeutigkeit des Attraktors folgt `K = P`.

Für `m = 72`, `r = 1/2` ist `K` damit das gefüllte 72-Eck mit Dimension 2, obwohl sich die Bilder überlappen. Die helle Mitte in einer Chaos-Spiel-Stichprobe ist eine Stichprobenwirkung: Punkte nahe dem Mittelpunkt verlangen lange Folgen derselben Richtung und werden selten gezogen. Bei ungeradem `m` liegt `−vⱼ` außerhalb von `P`, und der Mittelpunkt wird nicht überdeckt.

## 7. Linienabschluss und Dimension

Setze `O = ⋃ₙ₌₁^∞ Aₙ` und `S = closure(O)`. Dann gilt

```math
S=O\cup K=B\cup\bigcup_j f_j(S),\qquad
\dim_H S=\max\{1,\dim_H K\}.
```

Die Konstruktion ist damit ein inhomogenes selbstähnliches System mit dem Stern `B` als Kondensationsmenge. Diese Einordnung und die Dimensionsregel gehören zur bestehenden Theorie. Spezialisiert auf den vorliegenden Fall: Grenzpunkte von Segmenten aus beschränkten Generationen bleiben in deren abgeschlossener endlicher Vereinigung; Grenzpunkte aus unbeschränkt hohen Generationen liegen wegen des verschwindenden Restes in `K`. Umgekehrt werden Punkte in `K` durch ihre endlichen Präfixe approximiert. Da `O` eine abzählbare Vereinigung von Segmenten ist, folgt die Dimensionsformel aus der abzählbaren Stabilität der Hausdorff-Dimension. Für `n ≥ 1` gilt auch `d_H(Aₙ,S) ≤ L rⁿ/(1-r)`.

Linienabschluss und Endpunktmenge fallen genau dann zusammen, wenn der Anfangsstern schon in `K` liegt: `S = K ⇔ B ⊂ K`, denn dann liegt jedes Bild von `B` unter Verkettungen der `fⱼ` in `K`. Für `m = 3`, `r = 1/2` gilt das nicht (der Mittelpunkt gehört nicht zum Sierpinski-Dreieck), ebenso wenig, wenn `K` total unzusammenhängend ist. Für gerades `m` bei `r = 1/2` gilt es, weil `K` das gefüllte Vieleck ist.

Die Ähnlichkeitsdimension `s = log(m)/log(1/r)` ist nur bei nachgewiesenen geeigneten Trennungsbedingungen die Hausdorff-Dimension von `K`. Allgemein gilt lediglich `dim_H K ≤ min(2,s)`. Ein hinreichendes, nicht notwendiges Kriterium für starke Trennung lautet

```math
r<\frac{\sin(\pi/m)}{1+\sin(\pi/m)}.
```

Beweis: `fⱼ(K)` liegt in der Kreisscheibe um `L uⱼ` mit Radius `rL/(1-r)`. Die minimalen Mittelpunktabstände sind `2L sin(π/m)`. Das Kriterium macht die Scheiben disjunkt. Daraus folgen die offene Mengenbedingung und die übliche Dimensionsformel.

| m | r | dim_H K | dim_H S | Begründung |
| ---: | ---: | ---: | ---: | --- |
| 3 | 0,5 | 1,584963 | 1,584963 | Klassisches Sierpinski-Dreieck; offene Dreiecksinnenräume sind disjunkt |
| 4 | 0,5 | 2 | 2 | Vier halbgroße Eckquadrate überdecken das ganze Quadrat |
| 8 | 0,25 | 1,5 | 1,5 | Hinreichendes Trennungskriterium erfüllt |
| 8 | 0,1 | 0,903090 | 1 | Hinreichendes Trennungskriterium erfüllt |
| 72 | 0,03 | 1,219619 | 1,219619 | `0,03 < 0,04179626…` |
| 72 | 0,5 | 2 | 2 | Gefülltes 72-Eck (gerades `m`, Abschnitt 6); `s = 6,169925…` ist keine mögliche ebene Hausdorff-Dimension |

## 8. Versionen und Veröffentlichung

Version 1.0.0 hat Definition, Standardparameter und Exportsemantik festgelegt. Fehlerkorrekturen ohne Änderung der definierten Mengen erhöhen die Patch-Version. Zusätzliche ausdrücklich benannte Konstruktionen erhöhen die Minor-Version. Änderungen an den geometrischen Regeln oder der Bedeutung bestehender Parameter erfordern eine Major-Version.

Version 1.0.1 ist eine solche Korrektur. Das Originalskript zeichnet jetzt mit dem übergebenen Turtle-Objekt statt mit einem globalen; die Zeichnung bleibt Strich für Strich gleich. Der Bericht behauptet in Abschnitt 5 nicht mehr, dass sich Linienabschluss und Endpunktmenge immer unterscheiden, und der Fall `m = 72`, `r = 1/2` ist geklärt (hier Abschnitte 6 und 7). Die definierten Mengen sind unverändert. Die Einzelheiten stehen im [Änderungsprotokoll](../CHANGELOG.md).

Der Bericht ist auf Zenodo archiviert: DOI [10.5281/zenodo.23057944](https://doi.org/10.5281/zenodo.23057944) (alle Versionen), Version 1.0.1 unter [10.5281/zenodo.23063185](https://doi.org/10.5281/zenodo.23063185). Die Software steht unter MIT, Texte und Abbildungen unter CC BY 4.0. Ein DOI und ein Datum belegen keine mathematische Priorität. Formalisierung, Text und Referenzimplementierung sind mit KI-Unterstützung entstanden (OpenAI ChatGPT, Überarbeitung mit Anthropic Claude); eine unabhängige fachliche Prüfung gab es nicht.

## 9. Primärquellen

1. J. E. Hutchinson, *Fractals and Self-Similarity*, Indiana University Mathematics Journal 30 (1981), 713-747. DOI: [10.1512/iumj.1981.30.30055](https://doi.org/10.1512/iumj.1981.30.30055).
2. V. Tzanov, *Strictly self-similar fractals composed of star-polygons that are attractors of Iterated Function Systems* (2015), [arXiv:1502.01384](https://arxiv.org/abs/1502.01384). Reguläre Polygon-IFS und sternförmige Anfangsmengen sind dort bereits beschrieben, in Abschnitt 5 auch der Strahlenstern vom Mittelpunkt zu den Ecken.
3. J. M. Fraser, *Inhomogeneous self-similar sets and box dimensions*, Studia Mathematica 213 (2012), 133-156; [arXiv:1301.1881](https://arxiv.org/abs/1301.1881), insbesondere Einleitung 1.1, Gleichungen (1.2)-(1.3) und die Hausdorff-Dimensionsregel.

Die Aussagen über die konkrete endliche Rekursion, den dichten gleich langen Originalfall und das gefüllte Vieleck sind hier mit eigenen direkten Beweisen dokumentiert; auch dafür beanspruche ich keine Erstentdeckung.
