import sqlite3

class Luong:
    def __init__(self, ma_luong, ma_nhan_vien, thang, nam, so_ngay_di_lam, so_ngay_di_muon, tong_luong):
        self.ma_luong = ma_luong
        self.ma_nhan_vien = ma_nhan_vien
        self.thang = thang
        self.nam = nam
        self.so_ngay_di_lam = so_ngay_di_lam
        self.so_ngay_di_muon = so_ngay_di_muon
        self.tong_luong = tong_luong

    @staticmethod
    def get_luong_by_nhanvien_id(ma_nhan_vien, thang, nam):
        """
        Lấy thông tin lương của nhân viên theo ma_nhan_vien, thang và nam.
        """
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM Luong 
            WHERE ma_nhan_vien = ? AND thang = ? AND nam = ?
        ''', (ma_nhan_vien, thang, nam))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Luong(*row)
        return None

    @staticmethod
    def add_luong(ma_nhan_vien, thang, nam, so_ngay_di_lam, so_ngay_di_muon, tong_luong):
        """
        Thêm thông tin lương cho nhân viên
        """
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Luong (ma_nhan_vien, thang, nam, so_ngay_di_lam, so_ngay_di_muon, tong_luong)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (ma_nhan_vien, thang, nam, so_ngay_di_lam, so_ngay_di_muon, tong_luong))
        conn.commit()
        conn.close()

    @staticmethod
    def update_luong(ma_luong, so_ngay_di_lam, so_ngay_di_muon, tong_luong):
        """
        Cập nhật thông tin lương cho nhân viên
        """
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Luong
            SET so_ngay_di_lam = ?, so_ngay_di_muon = ?, tong_luong = ?
            WHERE ma_luong = ?
        ''', (so_ngay_di_lam, so_ngay_di_muon, tong_luong, ma_luong))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_luong(ma_luong):
        """
        Xóa thông tin lương của nhân viên
        """
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Luong WHERE ma_luong = ?', (ma_luong,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_luong():
        """
        Lấy tất cả thông tin lương của tất cả nhân viên
        """
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Luong')
        rows = cursor.fetchall()
        conn.close()
        return [Luong(*row) for row in rows]
