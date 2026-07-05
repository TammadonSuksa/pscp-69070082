# บันทึกการแก้โจทย์

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3017 - [LEARNING LOGS] Bill
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
542995
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
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก

---

## 2. ความเข้าใจโจทย์ของฉัน

```text
โจทย์ให้ Input จำนวนเต็มราคาอาหารเเละเครื่องดื่มที่ลูกค้าสั่งไป เเละจะมี ServiceCharge 10% ของราคาอาหารที่สั่งไป
ขั้นต่ำ 50 เเต่ไม่เกิน 1000 ต่อไปคิด Vat 7% โดยคำนวณจาก ราคาอาหารรวมกับค่า servicecharge output ออกมาต้องเป็นทศนิยม 2 ตำเเหน่ง

Input:
ราคาอาหารจำนวนเต็ม

Output:
Total รวม = ราคาอาหาร + servicecharge + vat

Constraints:
ค่าบริการ ที่มันต้องขั้นต่ำ 50 กับ ไม่เกิน 1000 เลยต้องมีการเขียน if else เพื่อดักในส่วนนี้ไว้
```

---

## 3. แผนแรกของฉัน

```text
Step 1: ราคาอาหารที่ลูกค้าสั่งไป เป็นจำนวนเต็ม
Step 2: คำนวณ ServiceCharge เเล้วเอามาบวกกับ ราคาที่ลูกค้าสั่ง ถ้า servicecharge ต่ำกว่า 50 ให้เป็น 50 อัตโนมัติ เเละถ้ามากกว่า 1000 ก็ให้เป็น 1000 เท่านั้น
Step 3: คำนวณ Vat 7 % ของจำนวนรวมก่อนหน้า 
Step 4: ให้ print จำนวนราคาทั้งหมดออกมาเป็นทศนิยม 2 ตำเเหน่ง
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
วิธีสุดท้ายก็เป็นเเบบเดียวกับเเผนเเรกที่คิดไว้เลย เพราะสามารถเขียนออกมาได้เเบบนั้นเเล้วผ่านจริง
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
ทดสอบ servicecharge ขั้นต่ำ 50 บาทจริงมั้ย
```

Input:

```text
80
```

Expected output:

```text
139.10
```

Actual output:

```text
139.10
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ทดสอบว่า ค่าบริการมันเกิน 1000 มั้ย
```

Input:

```text
99999
```

Expected output:

```text
108068.93
```

Actual output:

```text
108068.93
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ทดสอบว่าค่าบริการคิดเป็น 10% ของราคาอาหารเเละเครื่องดื่มจริงมั้ย
```

Input:

```text
800
```

Expected output:

```text
941.60
```

Actual output:

```text
941.60
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
