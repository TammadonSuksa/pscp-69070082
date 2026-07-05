# บันทึกการแก้โจทย์

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3011 - Colors
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
542982
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
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
ให้ตรวจสอบสี ถ้าผสมสีนี้เเล้วได้สีนี้ output ก็จะได้สีตามที่โจทย์กำหนด เเล้วก็ถ้าไม่ได้ใช้เเม่สีใส่ใน input จะให้เเสดงขึ้นว่า error เเต่ถ้าเเม่สีใช้สีเดียวกันให้ออกมาเป็นสีนั้น

Input:
2 บรรทัด คือสี

Output:
ตามเงื่อนไขของสีที่ผสมหรือ Error

Constraints:
การเขียน condition ที่จำกัด ทำให้ติด PEP-8 เลยต้องมีการลดรูปในการเขียน if else
```

---

## 3. แผนแรกของฉัน

```text
Step 1: input เเม่สีจำนวน 2 บรรทัด
Step 2: เช็คทั้งสองสีว่าอยู่ในเงื่อนไขของการผสมสีมั้ย 
Step 3: ถ้าอยู่ในเงื่อนไขก็จะผสมได้สีนั้นตามที่โจทย์กำหนดมา
Step 4: ถ้าเกิดไม่ได้ใช้เเม่สีก็จะขึ้น Error
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
logic เหมือนกับเเผนเเรกเลย
เป็นการใช้ if else เช็คทั้ง color บรรทัดที่ 1 เเละ บรรทัดที่ 2 เพราะเผื่อจะมีการสลับตำเเหน่ง เลยต้องเขียน if else เพื่อดักเอาไว้
(อาจจะมีวิธีที่ดีกว่านี้ในการเช็คค่าทีเดียวเลย โดยไม่ต้องเขียน if else เช็ค color บรรทัดที่ 1 เเละบรรทัดที่ 2 ซ้ำซ้อนไปมา อาจจะเเค่เช็ค For Example -> ถ้าเจอ Red เเละ บรรทัดต่อไป ถ้าเจอ Yellow ก็ผสมสีเลย ถึงเเม้ถ้า Input จะอยู่คนละที่ก็ตาม เพื่อลดโค้ดให้อ่านง่าย มีประสิทธิภาพ เเละ Scale ได้ดีขึ้นในอนาคต เเต่ logic)
```

---

## 5. การทดสอบของฉัน


### Test Case 1

ทำไมเลือก case นี้:

```text
เช็คว่า output จะออกมาเป็นเเม่สีมั้ย
```

Input:

```text
Red
Red
```

Expected output:

```text
Red
```

Actual output:

```text
Red
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
เช็คว่าจะขึ้น Error มั้ยถ้าไม่ใช่เเม่สี
```

Input:

```text
Red
White
```

Expected output:

```text
Error
```

Actual output:

```text
Error
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
เพื่อดูว่าสีผสมกันได้จริงๆตามที่โจทย์กำหนดใช่มั้ย เมื่อตำเเหน่งของสีต่างจากโจทย์กำหนด
```

Input:

```text
Yellow
Red
```

Expected output:

```text
Orange
```

Actual output:

```text
Orange
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
