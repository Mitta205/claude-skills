---
name: auto-md-convert
description: Automatisch converteren van geüploade .docx en .pdf bestanden naar markdown (.md) voordat ze gelezen worden. Triggert wanneer de gebruiker een .docx of .pdf bestand upload in /mnt/user-data/uploads/. Bespaart tokens door eerst te converteren naar compactere markdown in plaats van het ruwe bestand in context te lezen. Gebruik dit ALTIJD als eerste stap bij het werken met geüploade .docx of .pdf bestanden, tenzij de gebruiker expliciet vraagt om de originele opmaak te behouden of om het bestand zelf te bewerken (bijv. find-and-replace in een .docx).
---

# Auto Markdown Convert

Deze skill converteert geüploade `.docx` en `.pdf` bestanden automatisch naar markdown om token-gebruik te beperken voordat de inhoud gelezen wordt.

## Wanneer toepassen

Pas deze skill toe wanneer:
- Er één of meer `.docx` of `.pdf` bestanden in `/mnt/user-data/uploads/` staan
- De gebruiker iets vraagt over de inhoud van die bestanden (lezen, samenvatten, analyseren, vragen beantwoorden)

Pas deze skill **NIET** toe wanneer:
- De gebruiker expliciet vraagt het originele bestand te bewerken (bijv. "voeg een tabel toe aan dit .docx", "vul dit PDF-formulier in") — gebruik dan de docx of pdf skill
- De gebruiker de exacte opmaak/styling nodig heeft
- Het een gescande PDF betreft zonder tekstlaag (OCR is niet meegenomen in dit script)

## Hoe te gebruiken

1. Inspecteer welke bestanden in `/mnt/user-data/uploads/` staan
2. Run het meegeleverde script voor elk `.docx` of `.pdf`:

```bash
cd /home/claude
python /mnt/skills/user/auto-md-convert/convert.py "/mnt/user-data/uploads/BESTANDSNAAM.docx"
```

Het script schrijft de output naar:
- `/home/claude/<naam>.md` — voor jou om te lezen
- `/mnt/user-data/outputs/<naam>.md` — zodat de gebruiker hem ook kan downloaden

3. Lees de gegenereerde `.md` met het `view` commando in plaats van het origineel
4. Vermeld kort aan de gebruiker dat je hebt geconverteerd, en deel het `.md` bestand via `present_files` als ze er waarschijnlijk wat aan hebben

## Bij problemen

- Als `pymupdf` of `python-docx` niet geïnstalleerd zijn, installeer ze met:
  `pip install --break-system-packages pymupdf python-docx`
- Als conversie faalt (bijv. corrupt bestand, beveiligde PDF), val terug op normaal lezen en informeer de gebruiker
- Voor zeer kleine bestanden (<10KB) is conversie vaak niet de moeite waard — je mag dan direct lezen

## Voorbeeld output melding

> Ik heb je document `rapport.docx` geconverteerd naar markdown om efficiënt te kunnen lezen. Hier is een samenvatting: ...
