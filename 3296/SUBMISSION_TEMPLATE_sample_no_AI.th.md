# บันทึกการแก้โจทย์

ไฟล์นี้เป็นตัวอย่าง ห้ามคัดลอกเนื้อหานี้ไปใช้เป็น submission ของตนเอง

ใช้ไฟล์นี้เพื่อดูระดับรายละเอียดที่คาดหวังเท่านั้น

ตัวอย่างนี้แสดงโจทย์ง่าย ๆ ที่ไม่ได้ใช้ AI

ตัวอย่างนี้ยังแสดงวิธีเปิดเผยความช่วยเหลือเล็กน้อยจากคนด้วย เนื่องจากไม่ได้ใช้ AI นักศึกษาไม่ต้องทำ `ai_reflection.md`

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3296 - [LEARNING LOGS] RGB Mixed
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
667417
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
0-15 minutes
```

วิธีนับเวลา:

- นับเฉพาะเวลาที่ตั้งใจทำโจทย์นี้ด้วยตนเองจริง ๆ
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก
- ไม่นับเวลาพัก กินข้าว เรียน นอน เวลาที่ทำโจทย์อื่น หรือเวลาที่ไม่ได้ทำโจทย์นี้

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
โจทย์ให้ Input ค่าของ RGB สองบรรทัด จากนั้นหาค่าเฉลี่ย ของเเต่ละสี R G B

Input:
RGB สองบรรทัดเช่น
0 0 0
20 20 20

Output:
ค่าเฉลี่ยของ RGB

Constraints:
ในการที่จะต้องให้เศษมันปัดเศษลงเสมอ
```

---

## 3. แผนแรกของฉัน

```text
Step 1: ให้ input rgb 1 กับ rgb 2 เข้าไป
Step 2: นำ rgb 1 กับ rgb 2 มาบวกกันในเเต่ละค่า r + r , g + g , b + b
Step 3: นำไปหาค่าเฉลี่ยคือ หาร 2 โดยค่าต้องปัดเศษลงเสมอเลยต้องใช้ floor division
Step 4: เเสดง output
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
วิธีเดียวกับวิธีเเรกเลย
```

---

## 5. การทดสอบของฉัน

เขียน test cases อย่างน้อย 3 กรณีที่ลองเองหรือออกแบบเอง

พยายามเลือก test cases ที่แตกต่างกัน

แต่ละ test case ให้อธิบายว่าทำไมเลือกกรณีนั้น

ถ้า input หรือ output มีหลายบรรทัด ให้เขียนไว้ใน text blocks

### Test Case 1

ทำไมเลือก case นี้:

```text
ตัวเลขปกติ ที่หารลงตัว
```

Input:

```text
100 200 50
200 100 150
```

Expected output:

```text
150 150 100
```

Actual output:

```text
150 150 100
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ค่าที่เป็น edge case
```

Input:

```text
0 0 0
255 255 255
```

Expected output:

```text
127 127 127
```

Actual output:

```text
127 127 127
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ตัวเลขที่หารเเล้วเป็นเศษ
```

Input:

```text
11 33 55
21 43 65
```

Expected output:

```text
16 38 60
```

Actual output:

```text
16 38 60
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

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

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
