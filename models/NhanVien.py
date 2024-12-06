import sqlite3
from database import tao_co_so_du_lieu

class NhanVien:
    def __init__(self, id=None, hoten=None, ngaysinh=None, diachi=None, sdt=None, email=None, vitri=None, luong=None):
        self.id = id
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.diachi = diachi
        self.sdt = sdt
        self.email = email
        self.vitri = vitri
        self.luong = luong

    @staticmethod
    def get_all_nhanvien():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM nhanvien')
        rows = cursor.fetchall()
        conn.close()
        return [NhanVien(*row) for row in rows]

    @staticmethod
    def get_nhanvien_by_id(nhanvien_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM nhanvien WHERE id = ?', (nhanvien_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return NhanVien(*row)
        return None

    @staticmethod
    def add_nhanvien(hoten, ngaysinh, diachi, sdt, email, vitri, luong):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO nhanvien (hoten, ngaysinh, diachi, sdt, email, vitri, luong)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (hoten, ngaysinh, diachi, sdt, email, vitri, luong))
        conn.commit()
        conn.close()

    @staticmethod
    def update_nhanvien(id, hoten, ngaysinh, diachi, sdt, email, vitri, luong):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE nhanvien
            SET hoten = ?, ngaysinh = ?, diachi = ?, sdt = ?, email = ?, vitri = ?, luong = ?
            WHERE id = ?
        ''', (hoten, ngaysinh, diachi, sdt, email, vitri, luong, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_nhanvien(id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM nhanvien WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    @staticmethod
    # def add_Nhanvien(nv):
    #     conn = sqlite3.connect('database.db')
    #     cursor = conn.cursor()
    #     cursor.execute('''
    #         INSERT INTO NhanVien (hoten, ngaysinh, diachi, sdt, email, vitri, luong)
    #         VALUES (?, ?, ?, ?, ?, ?, ?)
    #     ''', (nv.hoten, nv.ngaysinh, nv.diachi, nv.sdt, nv.email, nv.vitri, nv.luong))
    #     conn.commit()
    #     conn.close()
    #     return True


    def add_Nhanvien(nv):
        try:
            # Sử dụng context manager để tự động đóng kết nối
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()

                # Thực thi câu lệnh SQL để thêm nhân viên vào cơ sở dữ liệu
                cursor.execute('''
                    INSERT INTO NhanVien (hoten, ngaysinh, diachi, sdt, email, vitri, luong)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (nv.hoten, nv.ngaysinh, nv.diachi, nv.sdt, nv.email, nv.vitri, nv.luong))

                # Commit transaction
                conn.commit()

            return True  # Trả về True nếu thêm thành công
        except sqlite3.Error as e:
            # Xử lý lỗi nếu có khi thực thi SQL
            print(f"Lỗi khi thêm nhân viên: {e}")
            return False  # Trả về False nếu có lỗi
