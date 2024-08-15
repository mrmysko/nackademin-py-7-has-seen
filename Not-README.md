[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/fzml9kHJ)
# Uppgift 7 - Funktionen has_seen() håller reda på vad den "sett"

## <a name='Syfte'></a>Syfte

Syftet med denna uppgift är att öva på att använda Python's `Set`.

<!-- vscode-markdown-toc -->

- [Syfte](#Syfte)
- [Förberedelser](#Frberedelser)
- [Beskrivning](#Beskrivning)
  - [Detaljer](#Detaljer)
    - [Skapa en funktion](#Skapaenfunktion)
    - [Tips](#Tips)
    - [Exempel](#Exempel)
  - [Inlämningsinstruktioner](#Inlmningsinstruktioner)
- [Anteckningar](#Anteckningar)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Frberedelser'></a>Förberedelser

- Repetera grundläggande koncept kring Python-datatyper, med ett särskilt fokus
  på Set.
- Förstå hur funktioner definieras i Python, inklusive hanteringen av argument
  och returvärden.
- Bekanta dig med konceptet av variabler som definieras utanför funktioner för
  att bevara värden mellan funktionsanrop, vilket är relevant för denna uppgift.

## <a name='Beskrivning'></a>Beskrivning

Utveckla en funktion med namnet `has_seen` som används för att identifiera om ett
specifikt objekt, av datatypen heltal (`int`) eller sträng (`str`), har blivit
observerat tidigare av funktionen.

### <a name='Detaljer'></a>Detaljer

#### <a name='Skapaenfunktion'></a>Skapa en funktion

- **Funktionsignatur:** `def has_seen(obj: int | str) -> bool:`
- **Vad den ska göra:** Funktionen ska kontrollera om den anropats med obj
  tidigare.
- **Vad den ska skriva ut:** Inget!
- **Vad den ska returnera:** Funktionen ska returnera True om objektet obj har
  observerats tidigare, annars False.

#### <a name='Tips'></a>Tips

- Använd en Set för att lagra och snabbt kontrollera om ett objekt är unikt
  eller inte. Denna Set ska definieras utanför `has_seen`-funktionen, som en
  global variabel.

#### <a name='Exempel'></a>Exempel

Observera att dessa exempelanrop är **beroende av varandra** och måste göras i
angiven ordning för att de förväntade resultaten ska stämma. Varje anrop
påverkar resultatet av de efterföljande anropen genom att uppdatera den interna
`Set` som håller reda på observerade objekt.

1. **Anrop:** `has_seen(1)`

   - **Förväntad utskrift:** Inget!
   - **Förväntat returvärde:** `False`

2. **Anrop:** `has_seen("a")`

   - **Förväntad utskrift:** Inget!
   - **Förväntat returvärde:** `False`

3. **Anrop:** `has_seen(1)`

   - **Förväntad utskrift:** Inget!
   - **Förväntat returvärde:** `True`

4. **Anrop:** `has_seen(2)`

   - **Förväntad utskrift:** Inget!
   - **Förväntat returvärde:** `False`

5. **Anrop:** `has_seen("a")`
   - **Förväntad utskrift:** Inget!
   - **Förväntat returvärde:** `True`

### <a name='Inlmningsinstruktioner'></a>Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. **Använda Github Classroom:**

   - Du har troligen redan accepterat uppgiften via en länk som tillhandahålls
     av utbildaren och gjort en `git clone` av det tilldelade repositoriet då du
     läser denna text. Det är i detta repository du kommer att hitta `README.md`
     med ytterligare instruktioner.

2. **Modifiera `uppgift.py`:**

   - Din lösning på uppgiften ska skrivas i `uppgift.py`. Det finns specifika
     instruktioner i `uppgift.py` om var du ska placera din källkod.

3. **Lämna in med Git:**

   - När du är klar med din uppgift, använd kommandona `git add .`, `git commit`
     följt av `git push` för att skicka in dina ändringar till GitHub.

4. **Automatiska "smoke tests":**

   - Efter att du har pushat din kod kommer automatiska "smoke tests" att köras.
     Dessa tester indikeras med en grön bock om de passerar, eller ett rött
     kryss om de misslyckas. Om du får ett rött kryss, är det viktigt att du
     klickar dig fram i GitHub tills du kan se varför testerna inte passerade.

5. **Feedback och granskning från utbildaren:**

   - Om dina tester passerar med en grön bock, kan du invänta feedback från din
     utbildare. Utbildaren kan antingen sätta "Request Changes" om ytterligare
     förändringar behövs, eller "approve" om uppgiften är godkänd som den är.
     Det är viktigt att du inväntar någon av dessa innan du väljer Merge.
   - Vid "Request Changes" är det viktigt att noggrant granska feedbacken och
     göra de nödvändiga justeringarna baserat på utbildarens anvisningar för att
     säkerställa att din uppgift uppfyller alla krav.
   - Efter att utbildaren har gjort "Approve" på din inlämning, får du göra en
     "Merge" av din "Feedback"-pull request, men inte förrän ett godkännande har
     erhållits.

6. **Initiera diskussioner i "Feedback"-pull requesten:**

   - Som student är du uppmuntrad att aktivt delta i processen genom att
     initiera diskussioner i din "Feedback"-pull request. Detta är en viktig del
     av inlärningsprocessen, där du kan ställa frågor, begära förtydliganden
     eller diskutera lösningar och feedback med din utbildare. Att engagera sig
     i dessa diskussioner ger dig möjlighet att djupare förstå uppgiftens krav
     och förbättra din kod baserat på interaktionen.

## <a name='Anteckningar'></a>Anteckningar

Inga.
