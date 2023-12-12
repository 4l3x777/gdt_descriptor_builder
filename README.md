# GDT Descriptor Builder. Генератор GDT дескриптора

## Задача - на основании

+ адреса расположения сегмента в физической памяти
+ размера - лимита сегмента
+ прав (чтение/запись/исполнение)
  
сформировать GDT дескриптор сегмента в виде hex дампа

## Используйте методы класса ```DescriptorBuilder```

+ ```generate_random``` для создания рандомного дескриптора
+ ```make``` для создания дескриптора по заднным параметрам
+ ```info``` для печати информации о дескрипторе

## Пример результата

```PYTHON
=== Descriptor===
Descriptor bin: 1101100110001010000111111101101110010100010010101011110100100101
Descriptor hex: d98a1fdb944abd25
=== Base address ===
Base address bin: 11011001110110111001010001001010
Base address hex: d9db944a
=== Segment limit ===
Segment limit bin: 10101011110100100101
Segment limit hex: abd25f
=== Access bits ===
╒═════╤═════╤═════╤═══════╕
│   G │   D │   L │   AVL │
╞═════╪═════╪═════╪═══════╡
│   1 │   0 │   0 │     0 │
╘═════╧═════╧═════╧═══════╛
=== Flags bits ===
╒═════╤═══════╤═════╤══════════╤═════════════════════╤═══════════════════════╤══════════════╕
│   P │   DPL │   S │   Access │   Accessibility(RX) │   Subtype(Conforming) │   Type(Code) │
╞═════╪═══════╪═════╪══════════╪═════════════════════╪═══════════════════════╪══════════════╡
│   0 │     0 │   1 │        1 │                   1 │                     1 │            1 │
│     │     0 │     │          │                     │                       │              │
╘═════╧═══════╧═════╧══════════╧═════════════════════╧═══════════════════════╧══════════════╛
```

## Ссылки

+ <https://www.codeproject.com/Articles/45788/The-Real-Protected-Long-mode-assembly-tutorial-for>
+ <https://wasm.in/blogs/category/zaschischennyj-rezhim.20/?page=2>
+ <http://sasm.narod.ru/docs/pm/pm_main.htm>
