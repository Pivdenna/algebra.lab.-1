# algebra.lab.-1
## Висновки
1. В випадку з обертанням, на нього на пряму впливає знак
біля аргументів матриці. Особливо добре це видно на прикладі з трикутником. 
Знак впливає на напрямок обертення фігури(за годинниковою, проти годинникової стрілки)
2. В наступному прикладі я множила на матрицю яка збільшує або навпаки зменшує розмір
фігури. Якщо аргументи менші 1, то фігура зменшується, якщо більше то відповідно 
збільшується. 
3. Відзеркалювання фігури відбувається відносно осі Х у моєму випадку. Множення на 2 
потрібно тому що ми в  принципі двіччі трансформуємо матрицю, коли перевертаємо вектор,
а потім повертаємо його на місце. Власне - відповідає за саме перевернення.
4. Розтягування відбувається по осі Х, зиінюючи при цьому координати з У.
За це в моєму коді відповідав shear_factor. 
5. Результат змінюється в залежності від порядку операцій. Досліджена в 2 етапі з зображенням
## Теоретичні питання
- Лінійні трансформації - це такі зміни які відбувається з векторними об'єктами в просторі
- В цій лабораторній роботі ми застосовували їх для редагування зображень, та змін фігур, 
які можуть бути використані в дуже багатьох сферах (3D моделювання, наприклад)
- Матриця трансормації - це така матриця яка описує зміни які ми застосовуємо до тих чи інших 
об'єктів в векторному просторі. Я б її інтерпретувала як математичний вигляд перетворень
- Матриця обертання є ортогональною. Вона завжди матиме квадратний вигляд. Не змінює положення 
об'єкто відносно координат
