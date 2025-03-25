# Algoritmi-Genetici

`Tema.py` implementează un algoritm genetic pentru determinarea maximului unei funcții pozitive pe un domeniu dat. Funcția este un polinom de gradul 2, cu coeficienți dați. Algoritmul cuprinde etapele de selecție, încrucișare (crossover) și mutație.

## Precizări
Se folosește metoda de codificare discutată la cursul de Algoritmi Avansați din cadrul Facultății de Matematică și Informatică și încrucișarea cu un singur punct de tăietură/de rupere. Se ține cont și de selecția de tip elitist (individul cu fitness-ul cel mai mare va trece automat în generația următoare).

## Date de intrare
- Dimensiunea populației (numărul de cromozomi)
- Domeniul de definiție al funcției (capetele unui interval închis)
- Parametrii pentru funcția de maximizat (coeficienții polinomului de grad 2)
- Precizia cu care se lucrează (cu care se discretizează intervalul)
- Probabilitatea de recombinare (crossover, încrucișare)
- Probabilitatea de mutație
- Numărul de etape al algoritmului

## Date de ieșire
Un fișier text sugestiv care prezintă detaliat operațiile efectuate în prima etapă a algoritmului, iar apoi un rezumat al evoluției populației pentru celelalte etape.
Un exemplu este fișierul [Evolutie.txt](https://drive.google.com/file/d/18nmiIlpkGTz3QGxRV5HPSal0wWKK0onj/view), care a fost obținut pentru funcția $−x^2 + x + 2$, domeniul [−1, 2], dimensiunea populației 20, precizia 6, probabilitatea de recombinare 25%, probabilitatea de mutație 1% și 50 de etape.