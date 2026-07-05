# บันทึกการแก้โจทย์

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ2996 - [LEARNING LOG] สลับตัวอักษร
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
543001
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
โจทย์ ให้รับ input เป็นข้อความ 5 ตัวอักษรเเล้ว output ออกมาเป็นข้อความที่สลับย้อนกลับ จากที่เรา input ไป เเละทุกตัวอักษรต้องเป็น lower
Input :
ความยาวตัวอักษรภาษาอังกฤษ 5 ตัว

Output :
ตัวอักษรเเบบกลับด้านเเล้วเป็นตัวพิมพ์เล็กทุกตัว

Constraints:
ต้องเป็น 5 ตัวอักษรเท่านั้น เเละทุกตัวต้องเป็นพิมพ์เล็ก
```

---

## 3. แผนแรกของฉัน

```text
Step 1: รับ Input text จำนวน 5 ตัวอักษร
Step 2: ให้ทำการ print ข้อความออกมาโดยใช้ string slicing step = -1 ทำให้มันอ่านย้อนกลับมา เเละ ใช้ method lower เพื่อบังคับให้เป็นตัวพิมพ์เล็กเท่านั้น
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
ใช้เเบบเดียวกับเเผนเเรกเลย
เเต่พยายามหาวิธีลดรูปเพื่อประหยัดโค้ดให้สั้นเเละเร็วขึ้นกว่าเดิมโดยที่ไม่ต้องเขียนหลายบรรทัด
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
เป็นตัวพิมพ์ใหญ่ทั้งหมด เพื่อทดสอบว่า output เป็น lower มั้ย
```

Input:

```text
AAAAA
```

Expected output:

```text
aaaaa
```

Actual output:

```text
aaaaa
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
Palindrome test
```

Input:

```text
Civic
```

Expected output:

```text
civic
```

Actual output:

```text
civic
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ด้วยความที่โจทย์บอกว่า รับข้อความ 5 ตัวอักษร เเต่ไม่ได้ให้เทสเคสเเบบสำหรับถ้ามันเกิน 5 ตัวอักษร ก็เลยไมได้เขียนดัก Testcase เอาไว้
```

Input:

```text
ABCDEFG
```

Expected output:

```text
gfedcba
```

Actual output:

```text
gfedcba
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

```text
No
```

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ


```text
Yes
```

ได้ทำโจทย์ข้อนี้ร่วมกับเพื่อนใน Lab Week 01 ตอนทำ Pair Programming 
ถ้าใช่ ให้อธิบายสั้น ๆ ว่าได้รับความช่วยเหลือแบบใด

ใครช่วยคุณ

```text
คู่ Pair Programming
```

เขาช่วยอะไร

```text
ช่วยเเชร์ความคิดว่าใช้เทคนิคอะไรดีในการทำข้อนี้ 
```

คุณยังทำอะไรด้วยตนเอง

```text
เขียนโค้ด เเละทดสอบหลายๆ Testcase ด้วยตัวเอง
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
