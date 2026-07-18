# บันทึกการแก้โจทย์

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3042 - [LEARNING LOGS] หาร 10
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
558258
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
โจทย์ให้ตัวเลขมา เเล้วหาว่ามีเลขตัวไหนบางที่หาร 10 ลงตัว โดยเเสดงผลออกเป็นบรรทัดเดียว

Input:
จำนวนเต็มบวก N

Output:
ตั้งเเต่ N ถึง 0 ที่หารด้วย 10 ลงตัว

Constraints:
ต้องเเสดงผลออกเป็นบรรทัดเดียวกันเลยต้องใช้เรื่องของ argument print มาช่วย
```

---

## 3. แผนแรกของฉัน

```text
Step 1: รับตัวเลข N เข้ามา
Step 2: หา จำนวนรอบที่วน i โดยการ เอาไปหาร // 10
Step 3: สร้าง for loop ให้เดินถอยหลัง ก็คือ -1
Step 4: เเสดงผลตัวเลขตามจำนวนรอบ i โดยให้ i * 10 ก็จะได้ตาม output 
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
เเบบเดียวกับที่คิดในเเผนเเรกของฉันเลย
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
ทดสอบตัวเลขที่น้อยกว่า 0 ว่ามันจะคำนวณมั้ย ถ้าคำนวณเเสดงว่าผิด
```

Input:

```text
-20
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

### Test Case 2

ทำไมเลือก case นี้:

```text
ทดสอบตัวเลขที่เป็นทศนิยม เเน่นอนว่าจะต้อง Error เพราะรับข้อมูลเป็น interger
```

Input:

```text
1.5
```

Expected output:

```text
Error : ValueError
```

Actual output:

```text
Error : ValueError
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ทดสอบเลข 0 ว่ามันจะคำนวณมั้ย ตามปกติเเล้วมันควรจะคำนวณ ถ้า output เป็น 0 เเสดงว่าถูก
```

Input:

```text
0
```

Expected output:

```text
0
```

Actual output:

```text
0
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
