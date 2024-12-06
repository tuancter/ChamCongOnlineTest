# models/taikhoan.py
import sqlite3

class TaiKhoan:
    def __init__(self, id, email, matkhau, nhanvien_id):
        self.id = id
        self.email = email
        self.matkhau = matkhau
        self.nhanvien_id = nhanvien_id

    @staticmethod
    def get_taikhoan_by_email(email):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM taikhoan WHERE email = ?', (email,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return TaiKhoan(*row)
        return None

    @staticmethod
    def add_taikhoan(email, matkhau, nhanvien_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO taikhoan (email, matkhau, nhanvien_id)
            VALUES (?, ?, ?)
        ''', (email, matkhau, nhanvien_id))
        conn.commit()
        conn.close()

    @staticmethod
    def update_matkhau(email, matkhau):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE taikhoan
            SET matkhau = ?
            WHERE email = ?
        ''', (matkhau, email))
        conn.commit()
        conn.close()
