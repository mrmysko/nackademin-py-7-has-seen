# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.
seen = set()


def has_seen(obj: str | int) -> bool:
    """Check if value is in seen."""

    global seen
    if obj in seen:
        return True

    seen.add(obj)
    return False


if __name__ == "__main__":
    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    #
    # Exempel:
    #
    # print(funktionsnamn("hejsan", 99))
    # print(funktionsnamn([19, 22, 31, 29, 1])
    print(has_seen(1))  # False
    print(has_seen("a"))  # False
    print(has_seen(1))  # True
    print(has_seen(2))  # False
    print(has_seen("a"))  # True
