# บันทึกการแก้โจทย์

ไฟล์นี้เป็นตัวอย่าง ห้ามคัดลอกเนื้อหานี้ไปใช้เป็น submission ของตนเอง

ใช้ไฟล์นี้เพื่อดูระดับรายละเอียดที่คาดหวังเท่านั้น

ตัวอย่างนี้แสดงโจทย์ง่าย ๆ ที่ไม่ได้ใช้ AI

ตัวอย่างนี้ยังแสดงวิธีเปิดเผยความช่วยเหลือเล็กน้อยจากคนด้วย เนื่องจากไม่ได้ใช้ AI นักศึกษาไม่ต้องทำ `ai_reflection.md`

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3072 - [LEARNING LOGS] A-E-I-O-U
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
606949
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
15-30 minutes
```

วิธีนับเวลา:

- นับเฉพาะเวลาที่ตั้งใจทำโจทย์นี้ด้วยตนเองจริง ๆ
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
โจทย์ให้ทำการรับค่า input เข้าไปเเล้ว เราต้องเขียนโปรเเกรม นับ a e i o u ในประโยคข้อความ จากนั้นให้เเสดง output ว่ามี a e i o u กี่ตัว ทั้งพิมพ์เล็กพิมพ์ใหญ่

Input:
รับค่า ตัวอักษร text ออกมาเป็น string

Output:
ให้เเสดงสระ a e i o u ที่นับได้ออกมา

Constraints:
output ต้องออกมาเเค่ตัวตัวสระ a e i o u ที่นับได้เท่านั้น
```

---

## 3. แผนแรกของฉัน

```text
Step 1: รับค่า input ข้อความมาเป็น string
Step 2: ให้ลูปนับจำนวน a e i o u ใน text มาก่อนเเล้วจับใส่ใน list
Step 3: ให้ลูปอีกรอบนึงโดยลูปเเค่ ตัวอักษร a e i o u
Step 4: ใช้ method count ที่ลูป a e i o u ใน step ที่ 3 เพื่อ count ตัวอักษรเเต่ละตัวใน List ที่ได้สร้างขึ้น
Step 5: ใส่เงื่อนไขไป ถ้า count เเต่ละตัวมัน > 0 ให้ทำการ output ตัวนั้นออกมา
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
วิธีสุดท้ายใช้เเบบเดียวกันเเบบวิธีเเรกเลย เป็นวิธีโดยการ จับสระเข้า list เเล้วรูป count ทีละตัวอักษระ ถ้าตัวไหนที่มัน count ได้มากกว่า 0 ให้ทำการเเสดงผลออกมา
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
เช็คตัวอักษรว่าเเสดงผลออกมา 5 ตัวมั้ย
```

Input:

```text
Hello My name is Bank. Bank really loves pscp all the time. and he always love you.
```

Expected output:

```text
a : 8
e : 8
i : 2
o : 4
u : 1
```

Actual output:

```text
a : 8
e : 8
i : 2
o : 4
u : 1
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ถ้าไม่มีสระเลย มันยังจะขึ้นอยู่มั้ย
```

Input:

```text
GG XD LL
```

Expected output:

```text

```

Actual output:

```text

```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
เช็คว่าถ้ามีสระเเค่นี้มันจะออกมาเเค่นี้มั้ยหรือ output มันจะออกมาทุกสระ
```

Input:

```text
Hello
```

Expected output:

```text
e : 1
o : 1
```

Actual output:

```text
e : 1
o : 1
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
No
```

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```
        
คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
