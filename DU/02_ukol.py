import requests
import json

dotaz = input("Chcete hledat podle názvu (n) nebo IČO (i)?: ").strip().lower()

if dotaz == "n":
    nazev = input("Zadejte název subjektu: ").strip()
    
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {"obchodniJmeno": nazev}
    
    res = requests.post(
        "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat",
        headers=headers,
        json=data
    )
    
    if res.status_code == 200:
        vysledky = res.json()
        subjekty = vysledky.get("ekonomickeSubjekty", [])
        pocet = vysledky.get("pocetCelkem", 0)

        print(f"\nPočet nalezených subjektů: {pocet}")
        for subjekt in subjekty:
            jmeno = subjekt.get("obchodniJmeno", "Neznámé jméno")
            ico = subjekt.get("ico", "Neznámé IČO")
            print(f"{jmeno}, {ico}")
        
        # Možnost zobrazit detail po výběru IČO
        vybrane_ico = input("\nZadejte IČO pro více informací: ").replace(" ", "")
        if vybrane_ico:
            url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{vybrane_ico}"
            detail_response = requests.get(url)

            if detail_response.status_code == 200:
                data = detail_response.json()
                obchodni_jmeno = data.get("obchodniJmeno", "Neznámé jméno")
                adresa = data.get("sidlo", {}).get("textovaAdresa", "Neznámá adresa")
                print(f"\n{obchodni_jmeno}\n{adresa}")
            else:
                print("Nepodařilo se získat další informace o subjektu.")
    else:
        print("Chyba při vyhledávání podle názvu.")

elif dotaz == "i":
    dotaz = ''.join(input("Zadejte IČO subjektu: ").split())
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{dotaz}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        obchodni_jmeno = data.get("obchodniJmeno", "Neznámé jméno")
        adresa = data.get("sidlo", {}).get("textovaAdresa", "Neznámá adresa")
        print(obchodni_jmeno)
        print(adresa)
    else:
        print("Nepodařilo se získat informace o subjektu. Zkontrolujte IČO a zkuste to znovu.")
else:
    print("Neplatná odpověď. Zadejte 'n' pro název nebo 'i' pro IČO.")