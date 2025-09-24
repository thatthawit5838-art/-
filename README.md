# RegisterBook (Django)

ระบบทะเบียนหนังสือส่งออนไลน์ (login + CRUD) พร้อมค้นหา/แบ่งหน้า/Export CSV

## วิธีเริ่มต้น
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# ตั้งค่าโครงสร้างฐานข้อมูล
python manage.py migrate

# สร้างผู้ดูแลระบบ (Admin)
python manage.py createsuperuser
# ตั้ง username/password แล้วเข้า /admin ได้

# รันเซิร์ฟเวอร์
python manage.py runserver
```

เปิดเว็บที่ http://127.0.0.1:8000/

## ฟีเจอร์
- ล็อกอินด้วยบัญชี Django
- เพิ่ม/แก้ไข/ลบ/ค้นหา ทะเบียนหนังสือส่ง
- Pagination 20 แถว/หน้า
- Export CSV ตามคอลัมน์ราชการ
- Admin site สำหรับดู/แก้ไขข้อมูลโดยผู้ดูแล

> ค่า reg_no (เลขทะเบียนส่ง) รันอัตโนมัติ เรียงตามวันที่และหมายเลขล่าสุด