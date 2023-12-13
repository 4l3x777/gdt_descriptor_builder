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
+ ```make_descriptor_protected_mode``` для создания дескриптора для работы в protected mode

## Пример результата

```PYTHON
=== Descriptor===
Descriptor bin (big-endian): 0000000001000000100111110000000001111110000000000000001000000000
Descriptor hex (big-endian): 00409f007e000200
Descriptor bin (little-endian): 0000000001000000000000000111111000000000111110010000001000000000
Descriptor hex (little-endian): 0002007e009f4000
Descriptor FASM assembler (little-endian): "db 0x00, 0x02, 0x00, 0x7e, 0x00, 0x9f, 0x40, 0x00"
=== Base address ===
Base address bin (big-endian): 00000000000000000111111000000000
Base address hex (big-endian): 00007e00
=== Segment limit ===
Segment limit bin (big-endian): 000000000000001000000000
Segment limit hex (big-endian): 000200
=== Access bits ===
╒═════╤═════╤═════╤═══════╕
│   G │   D │   L │   AVL │
╞═════╪═════╪═════╪═══════╡
│   0 │   1 │   0 │     0 │
╘═════╧═════╧═════╧═══════╛
=== Flags bits ===
╒═════╤═══════╤═════╤══════════╤═════════════════════╤═══════════════════════╤══════════════╕
│   P │   DPL │   S │   Access │   Accessibility(RX) │   Subtype(Conforming) │   Type(Code) │
╞═════╪═══════╪═════╪══════════╪═════════════════════╪═══════════════════════╪══════════════╡
│   1 │     0 │   1 │        1 │                   1 │                     1 │            1 │
│     │     0 │     │          │                     │                       │              │
╘═════╧═══════╧═════╧══════════╧═════════════════════╧═══════════════════════╧══════════════╛
```

## Ссылки

+ <https://www.codeproject.com/Articles/45788/The-Real-Protected-Long-mode-assembly-tutorial-for>
+ <https://wasm.in/blogs/category/zaschischennyj-rezhim.20/?page=2>
+ <http://sasm.narod.ru/docs/pm/pm_main.htm>
+ <https://www.cs.bham.ac.uk/~exr/lectures/opsys/10_11/lectures/os-dev.pdf>
