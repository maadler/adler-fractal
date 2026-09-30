# Adler-Fraktal: mathematische Spezifikation v1.0.0

Autor des bereitgestellten Originalcodes und vorgeschlagenen Namens: **Marcus Adler**. Erstellt am **30. September 2026**. Status: technischer Bericht zur öffentlichen Ablage; nicht unabhängig begutachtet; keine Prioritätsbehauptung. Softwareversion: **1.0.0**. Die Benennung bezeichnet die nachfolgende Konstruktion, nicht einen amtlich registrierten mathematischen Namen.

## 1. Parameter und Begriffe

Wir identifizieren die euklidische Ebene mit den komplexen Zahlen. Sei `m ≥ 3` eine ganze Zahl, `n ≥ 0` die ganzzahlige Rekursionstiefe, `L > 0` die Anfangslänge, `0 < r ≤ 1` der Skalierungsfaktor und `θ` eine feste globale Anfangsrichtung. Der Startpunkt ist `z₀`.

\[
u_j=\exp\bigl(i(\theta+2\pi j/m)\bigr),\qquad j=0,\ldots,m-1.
\]

Alle Generationen verwenden dieselben **absoluten** Richtungen. Es gibt keine Rotation relativ zum ankommenden Ast. Der Winkelabstand ist `α = 360° / m`; `m` ist der primäre Parameter. Für das Original gilt

\[
(m,n,L,r,\theta,z_0)=(72,2,200,1,0,0).
\]

Das Original verwendet `range(0, 360, ang)`. Für einen positiven ganzzahligen Nichtteiler von 360 ist die Lücke am Kreisende anders als die übrigen Lücken. Diese nichtregulären Richtungssets gehören nicht zur vorliegenden v1.0.0-Familie. Der Generator weist sie beim Winkelimport ausdrücklich ab.

## 2. Endpunkte und endliche Linienmenge

Für ein Wort `w = (j₁, …, jₖ)` ist der Punkt

\[
p_w=z_0+L\sum_{t=1}^{k}r^{t-1}u_{j_t},\qquad p_{\emptyset}=z_0.
\]

Die Endpunktmenge einer einzelnen Generation ist

\[
E_k=\{p_w:\lvert w\rvert=k\}.
\]

Sie hat `mᵏ` **Adressen**, nicht zwingend `mᵏ` verschiedene Punkte. Die endliche Adler-Linienmenge ist

\[
A_n=\bigcup_{k=1}^n\ \bigcup_{\lvert w\rvert=k}[p_{w^-},p_w],\qquad A_0=\emptyset.
\]

`w⁻` bezeichnet das Wort ohne sein letztes Zeichen. `[a,b]` ist das geschlossene gerade Liniensegment. Wiederholte Segmente sind in dieser Mengendefinition nur einmal enthalten, werden bei der zeichnerischen Ausführung aber jedes Mal gezeichnet.

In den folgenden Identitäten wird zur Vereinfachung `z₀ = 0` gesetzt. Für einen anderen Startpunkt wird die gesamte Figur übersetzt. Mit

\[
B=\bigcup_j[0,Lu_j],\quad f_j(x)=Lu_j+rx
\]

gilt `Aₙ = B ∪ ⋃ⱼ fⱼ(Aₙ₋₁)`.

## 3. Zeichenreihenfolge

An jedem Knoten werden zunächst alle `m` Strahlen in aufsteigender Winkelreihenfolge gezeichnet. Erst danach werden die Kinder rekursiv, ebenfalls in dieser Reihenfolge, besucht. Zwischen einem Segmentende und dem nächsten Startpunkt ist der Stift angehoben. Dies erhält die Ausführungsreihenfolge des Originals. Die neue Implementierung benutzt einen expliziten Stapel und kein globales Turtle-Objekt.

## 4. Endliche Eigenschaften

Die Anzahl der Zeichenbefehle lautet

\[
N_n=\sum_{k=1}^n m^k=\frac{m(m^n-1)}{m-1}.
\]

| Tiefe n, m = 72 | Zeichenbefehle |
| --- | ---: |
| 0 | 0 |
| 1 | 72 |
| 2 | 5.256 |
| 3 | 378.504 |
| 4 | 27.252.360 |

Für `m = 18` (Winkelabstand 20°, Default des ursprünglichen Funktionskopfs) ergibt Tiefe 4 dagegen `18 + 324 + 5.832 + 104.976 = 111.150` Befehle. Dies stimmt mit der nachgereichten App-Anzeige überein, falls die App dieselbe Befehlszählung verwendet. Der Screenshot allein legt die konkrete App-Rekursion und den Skalierungsfaktor nicht fest.

Die summierte Länge mit Zeichenmultiplikität ist `L m ∑ₖ₌₀ⁿ⁻¹ (m r)ᵏ`. Für das Original mit Tiefe 2 beträgt sie 1.051.200 Längeneinheiten. Dies ist nicht die Länge der Vereinigungsmenge ohne Überzeichnung.

Der scharfe äußere Radius um `z₀` lautet

\[
R_n=\begin{cases}nL,&r=1,\\L(1-r^n)/(1-r),&0<r<1.\end{cases}
\]

Die obere Schranke folgt aus der Dreiecksungleichung; ein Wort mit stets derselben Richtung erreicht sie. Jede Figur ist unter den Rotationen und Spiegelungen des regulären `m`-Ecks um den Startpunkt invariant. Bei `n ≥ 1` ist `Aₙ` zusammenhängend und eine endliche Vereinigung nichtdegenerierter Segmente, daher `dim_H Aₙ = 1`.

Für `r = 1`, `n = 2` gilt

\[
\lvert p_{(a,b)}-z_0\rvert=2L\left|\cos\frac{\pi(a-b)}m\right|.
\]

Das erklärt die konzentrischen diskreten Endpunktradien. Bei geradem `m` ist `|E₂| = m²/2 + 1`. Beweis: Ein von null verschiedener Mittelpunkt einer Sehne eines Kreises bestimmt deren ungeordnetes Endpunktpaar eindeutig. Von `m(m+1)/2` ungeordneten Paaren bilden die `m/2` antipodalen Paare alle den gleichen Mittelpunkt null. Beim Original ergeben sich **2.593 verschiedene Endpunkte**; null hat 72 geordnete Adressen. Die Kreisradien beschreiben Endpunkte, nicht ausgefüllte Kreislinien.

## 5. Gleich lange Linien: der unendliche Originalfall

Für das Original `m = 72`, `r = 1` ist die Vereinigung aller Endpunkte eine additive Gruppe: Zu jeder Richtung gehört auch ihre Gegenrichtung, daher lassen sich alle ganzzahligen Linearkombinationen als endliche Wörter realisieren.

Unter den Richtungen liegen insbesondere 0°, 30°, 60° und 90°. Mit `θ = 0` gilt

\[
2u_{30^\circ}-u_{90^\circ}=(\sqrt3,0),\qquad
2u_{60^\circ}-u_{0^\circ}=(0,\sqrt3).
\]

Außerdem sind `(1,0)` und `(0,1)` enthalten. Somit enthält die Endpunktgruppe

\[
L(\mathbb Z+\sqrt3\mathbb Z)\times L(\mathbb Z+\sqrt3\mathbb Z).
\]

`ℤ + √3 ℤ` ist dicht in der reellen Achse: Nach dem Schubfachprinzip gibt es beliebig kleine positive Zahlen dieser Form; ihre ganzzahligen Vielfachen approximieren jeden reellen Wert. Das kartesische Produkt ist daher dicht in der Ebene. Es folgt

\[
\overline{\bigcup_{n\ge1}A_n}=\mathbb R^2.
\]

Dabei hat die nicht abgeschlossene Linienvereinigung weiterhin Hausdorff-Dimension 1. Die Endpunktvereinigung ist abzählbar und hat Dimension 0, ihr Abschluss Dimension 2. Es gibt keinen beschränkten kompakten Grenzattraktor für `r = 1`. Die Aussage über die ganze Ebene betrifft alle Rekursionstiefen gemeinsam, nicht die endliche Originalabbildung.

## 6. Kontraktive Endpunktmenge

Für `0 < r < 1` definiert sich die kompakte Endpunktgrenzmenge durch

\[
K=\left\{L\sum_{t=1}^{\infty}r^{t-1}u_{j_t}:j_t\in\{0,\ldots,m-1\}\right\}.
\]

Sie ist der eindeutige nichtleere kompakte Attraktor des Polygon-IFS `fⱼ(x) = L uⱼ + r x`. Mit `vⱼ = L uⱼ / (1-r)` lässt sich dieselbe Abbildung als `fⱼ(x) = r x + (1-r) vⱼ` schreiben: Kontraktion um die Ecken eines regulären Polygons. Diese Klasse ist bekannt und wird hier nicht als neue Fraktalfamilie beansprucht.

Die Endpunktmengen konvergieren im Hausdorff-Abstand mit

\[
d_H(E_n,K)\le\frac{Lr^n}{1-r}.
\]

Das folgt durch Abschneiden beziehungsweise Fortsetzen der Adressreihe und Abschätzen des Restes. Die konvexe Hülle ist das reguläre Polygon mit Eckradius `L/(1-r)`.

## 7. Linienabschluss und Dimension

Setze `O = ⋃ₙ₌₁^∞ Aₙ` und `S = closure(O)`. Dann gilt

\[
S=O\cup K=B\cup\bigcup_j f_j(S),\qquad
\dim_H S=\max\{1,\dim_H K\}.
\]

Die Konstruktion ist damit ein inhomogenes selbstähnliches System mit dem Stern `B` als Kondensationsmenge. Diese Einordnung und die Dimensionsregel gehören zur bestehenden Theorie. Spezialisiert auf den vorliegenden Fall: Grenzpunkte von Segmenten aus beschränkten Generationen bleiben in deren abgeschlossener endlicher Vereinigung; Grenzpunkte aus unbeschränkt hohen Generationen liegen wegen des verschwindenden Restes in `K`. Umgekehrt werden Punkte in `K` durch ihre endlichen Präfixe approximiert. Da `O` eine abzählbare Vereinigung von Segmenten ist, folgt die Dimensionsformel aus der abzählbaren Stabilität der Hausdorff-Dimension. Für `n ≥ 1` gilt auch `d_H(Aₙ,S) ≤ L rⁿ/(1-r)`.

Die Ähnlichkeitsdimension `s = log(m)/log(1/r)` ist nur bei nachgewiesenen geeigneten Trennungsbedingungen die Hausdorff-Dimension von `K`. Allgemein gilt lediglich `dim_H K ≤ min(2,s)`. Ein hinreichendes, nicht notwendiges Kriterium für starke Trennung lautet

\[
r<\frac{\sin(\pi/m)}{1+\sin(\pi/m)}.
\]

Beweis: `fⱼ(K)` liegt in der Kreisscheibe um `L uⱼ` mit Radius `rL/(1-r)`. Die minimalen Mittelpunktabstände sind `2L sin(π/m)`. Das Kriterium macht die Scheiben disjunkt. Daraus folgen die offene Mengenbedingung und die übliche Dimensionsformel.

| m | r | dim_H K | dim_H S | Begründung |
| ---: | ---: | ---: | ---: | --- |
| 3 | 0,5 | 1,584963 | 1,584963 | Klassisches Sierpinski-Dreieck; offene Dreiecksinnenräume sind disjunkt |
| 4 | 0,5 | 2 | 2 | Vier halbgroße Eckquadrate überdecken das ganze Quadrat |
| 8 | 0,25 | 1,5 | 1,5 | Hinreichendes Trennungskriterium erfüllt |
| 8 | 0,1 | 0,903090 | 1 | Hinreichendes Trennungskriterium erfüllt |
| 72 | 0,03 | 1,219619 | 1,219619 | `0,03 < 0,04179626…` |
| 72 | 0,5 | Hier nicht bestimmt | Hier nicht bestimmt | Überlappungen; `s = 6,169925…` ist keine mögliche ebene Hausdorff-Dimension |

## 8. Versions- und Veröffentlichungspolitik

Die Version 1.0.0 fixiert Definition, Standardparameter und Exportsemantik. Fehlerkorrekturen ohne Änderung der definierten Mengen erhöhen die Patch-Version. Zusätzliche ausdrücklich benannte Konstruktionen erhöhen die Minor-Version. Änderungen an den geometrischen Regeln oder der Bedeutung bestehender Parameter erfordern eine Major-Version.

Der Name und das Erstellungsdatum sind kein Beweis mathematischer Priorität. Die Veröffentlichung dokumentiert eine Beschreibung samt Referenzimplementierung. Marcus Adler hat die öffentliche Ablage und die Lizenzwahl MIT für Code sowie CC BY 4.0 für eigene Texte und Abbildungen ausdrücklich gewählt. Eine unabhängige fachliche Prüfung wurde nicht durchgeführt. Der DOI `10.5281/zenodo.23057945` wurde vor der Ablage tatsächlich reserviert; seine Registrierung erfolgt mit der Veröffentlichung.

## 9. Primärquellen

1. J. E. Hutchinson, *Fractals and Self-Similarity*, Indiana University Mathematics Journal 30 (1981), 713-747. DOI: [10.1512/iumj.1981.30.30055](https://doi.org/10.1512/iumj.1981.30.30055).
2. V. Tzanov, *Strictly self-similar fractals composed of star-polygons that are attractors of Iterated Function Systems* (2015), [arXiv:1502.01384](https://arxiv.org/abs/1502.01384). Reguläre Polygon-IFS und sternförmige Anfangsmengen sind dort bereits beschrieben.
3. J. M. Fraser, *Inhomogeneous self-similar sets and box dimensions*, Studia Mathematica 213 (2012), 133-156; [arXiv:1301.1881](https://arxiv.org/abs/1301.1881), insbesondere Einleitung 1.1, Gleichungen (1.2)-(1.3) und die Hausdorff-Dimensionsregel.

Die hergeleiteten Aussagen über die konkrete endliche Rekursion und den dichten gleichlangen Originalfall sind hier mit eigenen direkten Beweisen dokumentiert; auch für diese Aussagen wird keine Erstentdeckung beansprucht.
