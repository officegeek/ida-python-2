# OOP i Python 
Introduktion til Object Oriented Programming i Python

## Hvad er OOP?
Objektorienteret programmering (*OOP*) er en måde at strukturere din kode på, så både datas karakteristika og adfærd kan samles i en enkelt struktur.

Denne enkelte struktur giver dig derefter mulighed for at bruge den klasse eller det objekt, du har oprettet igen og igen i hele din kode, efter princippet i **Don't Repeat Yourself** (*DRY*).

Dette er i modsætning til *proceduremæssig* programmering, hvor man koder en sekvens af trin for at udføre en opgave ved hjælp af funktioner og kodeblokke.

## Eksempel - Medarbejder
Som eksempel kan vi bruge medarbejdere i en virksomhed. Du ønsker at gemme oplysninger om disse medarbejdere

F.eks.
- Navn
- E-mail
- Fødselsdag
- Afdeling
- Løntrin
- Løn
- Ansættelse dato
- osv.

Vi vil gerne tilføje noget funktionalitet når en medarbejder gør noget, eller hvor der sker noget. For eksempel vil du måske give dem en lønforhøjelse, du vil måske betale dem en bonus.

Ved at oprette en **medarbejderklasse** kan du gemme alle disse data og udføre funktioner på hver medarbejder. Du kan genbruge den samme *funktionalitet* igen og igen.

Måden dette gøres på er ved at oprette klasser, der bruges som tegninger til objekter. Klassen beskrev overordnet hvad objektet vil men, men er adskilt fra selve objektet, som er en specifik instans.