## <Gra 1010!>

## Opis
Jest to gra inspirowana klasyczną grą **1010!**, zaimplementowana przy użyciu biblioteki **Pygame**. Gra polega na układaniu bloków na planszy o rozmiarze 8x8. Celem jest wypełnienie pełnych linii i kolumn, aby zdobywać punkty. Gra posiada również system zapisywania najlepszego wyniku.

## Wymagania
Aby uruchomić grę, musisz zainstalować **Pygame**. Możesz to zrobić za pomocą poniższego polecenia:

```
pip install pygame
```

## Uruchamianie gry
Po zainstalowaniu Pygame, uruchom grę za pomocą poniższego polecenia:

```
python game.py
```

Po uruchomieniu gry, zobaczysz planszę o rozmiarze 8x8, na której musisz umieszczać bloki. Gra umożliwia również restart, gdy naciśniesz przycisk **Restart** w górnej części ekranu.

## Sterowanie
- **Przeciągnij i upuść bloki**: Kliknij na blok, a następnie przeciągnij go na planszę, aby umieścić go w wybranym miejscu.
- **Kliknij przycisk Restart**: Aby rozpocząć nową grę, kliknij przycisk **Restart** znajdujący się w górnej części ekranu.

## Funkcje gry
- **Bloki**: Gra zawiera różne kształty bloków, takie jak kwadrat, linia pozioma, linia pionowa, litera "T", litera "Z" i inne.
- **Punkty**: Punkty zdobywa się za każdą wypełnioną linię lub kolumnę, a także za umieszczanie bloków na planszy.
- **Najlepszy wynik**: Gra zapisuje najlepszy wynik w pliku `best_score.txt`, który jest ładowany przy starcie gry i aktualizowany, gdy osiągniesz lepszy wynik.

## Plik konfiguracyjny
W grze wykorzystywane są następujące stałe:
- **WINDOW_SIZE**: Rozmiar okna gry (500 pikseli).
- **GRID_SIZE**: Rozmiar planszy (8x8).
- **CELL_SIZE**: Rozmiar pojedynczej komórki na planszy.
- **BLOCK_COLORS**: Kolory bloków, które mogą pojawić się w grze.

## Zasady
- Bloki, które będą przeciągane, muszą pasować do dostępnego miejsca na planszy.
- Wypełniona linia lub kolumna zostaje usunięta, a gracz zdobywa punkty.

![image](https://github.com/user-attachments/assets/9dafdee5-2e3e-48ec-96ba-d640c90f0239)
