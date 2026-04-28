import copy
import re
import tkinter as tk
from tkinter import Entry, ttk, messagebox, filedialog
import json, os
import random
from turtle import title
from PIL import Image, ImageTk
from tkinter import filedialog
from datetime import datetime
class User:
    def __init__(self,Ten='',SDT='',tk='',mk='',sotien=0.0,somay=0):
        self.TK=str(tk) 
        self.MK=str(mk) 
        self.SDT=str(SDT)
        self.Ten=Ten
        self.SoMay=somay
        self.SoTien=sotien
    def nhap(self,Ten='',SDT='',TK='',MK='',Somay=0,sotien=0.0):
        self.TK=str(TK) 
        self.MK=str(MK) 
        self.Ten=Ten
        self.SDT=str(SDT)
        self.SoMay=Somay
        self.SoTien=sotien
    def to_dict_data(self):
        return {
        "Ten": self.Ten,
        "SDT":self.SDT,
        "TenDN": self.TK,
        "MK": self.MK,
        "SoTien": self.SoTien,
        "SoMay":self.SoMay,
        
    }
    def __str__(self):
        return (f"Tên thiệt:{self.Ten},Số điện thoại:{self.SDT} TK:{self.TK}, MK:{self.MK}, SoMay:{self.SoMay}, So Tien:{self.SoTien}")
class DoAn:
    def __init__(self,Mamon='',TenMon='',Gia=0.0,MaKH='',Hinh='No_jpg.jpg',TrangThai='',SoLuong=0):
        self.Mamon=Mamon
        self.TenMon=TenMon 
        self.Gia=Gia
        self.Hinh=Hinh
        self.MaKH=MaKH
        self.TrangThai=TrangThai
        self.SoLuong=SoLuong
    def nhap(self,Mamon='',TenMon='',Gia=0.0,MaKH='',Hinh='No_jpg.jpg',TrangThai='',SoLuong=0):
        self.Mamon=Mamon
        self.TenMon=TenMon 
        self.Gia=Gia
        self.Hinh=Hinh
        self.MaKH=MaKH
        self.TrangThai=TrangThai
        self.SoLuong=SoLuong
    def to_dict_data(self):
        return {
        "Ma_Mon": self.Mamon,
        "Ten_Mon": self.TenMon,
        "Gia":self.Gia,
        "Hinh":self.Hinh,
        "MaKH": self.MaKH,
        "trangthai":self.TrangThai,
        "SoLuong":self.SoLuong
    }
    def __str__(self):
        return f"Mã món:{self.Mamon}, Tên món:{self.TenMon}, Giá:{self.Gia}, Hình:{self.Hinh}, Mã KH:{self.MaKH},Trạng Thái: {self.TrangThai}, còn lại {self.SoLuong}."
class NhanVien:
    def __init__(self, Ten='', MaNV='', MK='',SDT='', TongThu=0.0, Email=''):
        self.Ten = Ten
        self.MaNV = MaNV
        self.MK = MK
        self.SDT=SDT
        self.TongThu = TongThu
        self.Email = Email

    def nhap(self, Ten='', MaNV='', MK='', SDT='',TongThu=0.0, Email=''):
        self.Ten = Ten
        self.MaNV = MaNV
        self.MK = MK
        self.SDT=SDT
        self.TongThu = TongThu
        self.Email = Email

    def to_dict_data(self):
        return {
            "Ten": self.Ten,
            "MaNV": self.MaNV,
            "MK": self.MK,
            "TongThu": self.TongThu,
            "SDT":self.SDT,
            "Email": self.Email
        }

    def __str__(self):
        return f"Tên: {self.Ten}, Mã NV: {self.MaNV}, Mật khẩu: {self.MK},Số điện thoại:{self.SDT} Tổng thu: {self.TongThu}, Email: {self.Email}"

class YeuCau:
    def __init__(self, MaDH='', MaKH='', Ngay='', Gio='',SoMay=0, DanhSachMon=None):
        self.MaDH = MaDH
        self.MaKH = MaKH
        self.Ngay = Ngay
        self.Gio = Gio
        self.SoMay=SoMay
        self.DanhSachMon = DanhSachMon if DanhSachMon else []

    def to_dict_data(self):
        return {
            "MaDH": self.MaDH,
            "MaKH": self.MaKH,
            "Ngay": self.Ngay,
            "Gio": self.Gio,
            "SoMay":self.SoMay,
            "DanhSachMon": [
            mon.to_dict_data() if hasattr(mon, 'to_dict_data') else mon
            for mon in self.DanhSachMon
        ]
        }

    def __str__(self):
        mon_str = ', '.join([f"{m['MaMon']}({m['Gia']}đ)" for m in self.DanhSachMon])
        return f"Mã ĐH: {self.MaDH}, KH: {self.MaKH},Số máy: {self.SoMay} Ngày: {self.Ngay}, Giờ: {self.Gio}, Món: {mon_str}"

def Doc_File(name):
    with open(name, 'r',encoding='utf-8-sig')as file:
        data=json.load(file)
    return data

DSNV = []
DSND = []
DSOL = []
DSMAY = []
DSDA = []
DSDU = []
DSYC = []


def TaoUser(DSach):
    for i in data:
        x=User(i['Ten'],i['SDT'],i['TenDN'],i['MK'],i['SoTien'],i["SoMay"])
        DSach.append(x)  

def doc_dsmay_list(ten_file):
    with open(ten_file, "r", encoding="utf-8") as f:
        return [int(line.strip()) for line in f if line.strip().isdigit()]

def TaoYeuCau(DSach):
    for i in data:
        x = YeuCau(i['MaDH'],i['MaKH'],i['Ngay'],i['Gio'],i['SoMay'],i['DanhSachMon'])
        DSach.append(x)
        

def TaoDoAn(DSach):
    for i in data:
        x = DoAn(i['Ma_Mon'], i['Ten_Mon'], i['Gia'], i['MaKH'], i['Hinh'], i['trangthai'], i['SoLuong'])
        DSach.append(x)

def TaoNV(DSach):
    for i in data:
        x=NhanVien(i['Ten'],i['MaNV'],i['MK'],i['SDT'],i['TongThu'],i['Email'])
        DSach.append(x)  


data=Doc_File("YeuCau.json") 
TaoYeuCau(DSYC)

data=Doc_File("NhanVien.json")
TaoNV(DSNV)

data=Doc_File("QLTiemNet.json")
TaoUser(DSND)

data=Doc_File("DSonline.json")
TaoUser(DSOL)

data=Doc_File("DoAn.json")
TaoDoAn(DSDA)

data=Doc_File("DoUong.json")
TaoDoAn(DSDU)

DSMAY=[0]+doc_dsmay_list("DSMayDangOn.txt")

def luu_danh_sach(danh_sach, ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        for item in danh_sach:
            f.write(str(item) + "\n")

#print để tiện coppy nhớ xóa
for i in DSND:
    print(i)

def luu_vao_file(danh_sach, ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        data = [item.to_dict_data() for item in danh_sach]  # chuyển object -> dict
        json.dump(data, f, ensure_ascii=False, indent=2)



def ktr_Dang_Nhap(DSND,TK,MK):
    for i in DSND:
        if i.TK==TK:
            if i.MK==MK:
                return 1
            return 0
    return 0

def ktr_nhap_ten(Ten):
    # Kiểm tra có số không
    if re.search(r"\d", Ten):
        return False
    # Kiểm tra các ký tự hợp lệ cho tên (bao gồm tiếng Việt có dấu, dấu cách, dấu gạch nối, nháy đơn)
    p = r"^[a-zA-Z\s" \
        r"ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴ" \
        r"àáạảãâầấậẩẫăằắặẳẵ" \
        r"Đđ" \
        r"ÈÉẸẺẼÊỀẾỆỂỄ" \
        r"èéẹẻẽêềếệểễ" \
        r"ÌÍỊỈĨ" \
        r"ìíịỉĩ" \
        r"ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ" \
        r"òóọỏõôồốộổỗơờớợởỡ" \
        r"ÙÚỤỦŨƯỪỨỰỬỮ" \
        r"ùúụủũưừứựửữ" \
        r"ỲÝỴỶỸ" \
        r"ỳýỵỷỹ" \
        r"'-]+$"
    if not re.fullmatch(p, Ten):
        return False
    # Tên không được rỗng hoặc chỉ chứa khoảng trắng
    if not Ten.strip():
        return False
    return True

def ktr_SDT(SDT):
    if re.fullmatch(r"^0\d{9}$", SDT):
        return True
    return False
def ktr_SO(SO):
    if re.fullmatch(r"^-?\d*(\.\d+)?$|^-?\.\d+$",SO):
        return True
    return False

def ktr_EMAIL(email):
    # Mẫu cho email:
    p = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    if re.fullmatch(p, email):
        return True
    else:
        return False

def hien_bang_user(user,dsol,dsmay):
    win = tk.Toplevel()
    win.title("Người dùng")
    win.geometry("250x350")
    SoGio=float(user.SoTien)/10000
    time_label = tk.Label(win, text=f"Xin chào {user.Ten}\nBạn đang ngồi máy {user.SoMay}\nCòn lại {float(user.SoTien):.0f} và còn {SoGio:.2f} giờ", font=("Arial", 12))
    time_label.grid(row=0,column=0)
    after_id = None 
    def hien_cua_so_dat_do():
        dat_do_win = tk.Toplevel(win)
        dat_do_win.title("Đặt đồ ăn / đồ uống")
        dat_do_win.geometry("800x500")
        

        tabControl = ttk.Notebook(dat_do_win)
        tab_do_an = ttk.Frame(tabControl)
        tab_do_uong = ttk.Frame(tabControl)
        tabControl.add(tab_do_an, text='Đồ Ăn')
        tabControl.add(tab_do_uong, text='Đồ Uống')
        tabControl.pack(side="left", fill="both", expand=True)
        
        gio_hang = []
        #==Giỏ Hàng==
        khung_gio = tk.Frame(dat_do_win, width=200, bd=2, relief="sunken")
        khung_gio.pack(side="right", fill="y", padx=5)

        tk.Label(khung_gio, text="Giỏ hàng", font=("Arial", 12, "bold")).pack(pady=5)

        ds_gio = tk.Listbox(khung_gio, width=30, height=20)
        ds_gio.pack(padx=5, pady=5)

        tong_mon_label = tk.Label(khung_gio, text="Tổng món: 0")
        tong_mon_label.pack()

        tong_tien_label = tk.Label(khung_gio, text="Tổng tiền: 0đ")
        tong_tien_label.pack()
        
        def cap_nhat_gio():
            ds_gio.delete(0, tk.END)
            tong_mon = 0
            tong_tien = 0
            for mon in gio_hang:
                ds_gio.insert(tk.END, f"{mon.TenMon} - {mon.Gia}đ")
                tong_mon += 1
                tong_tien += int(mon.Gia)
            tong_mon_label.config(text=f"Tổng món: {tong_mon}")
            tong_tien_label.config(text=f"Tổng tiền: {tong_tien:,}đ")
            

        def them_vao_gio(item):
            gio_hang.append(item)
            cap_nhat_gio()
            
        def thanh_toan():
            def kiem_tra_so_luong_am(SoLuongTru):
                for mon in gio_hang:
                    danh_sach = DSDA if any(mon.Mamon == da.Mamon for da in DSDA) else DSDU
                    for item in danh_sach:
                        if mon.Mamon == item.Mamon:
                            if item.SoLuong < 0:
                                messagebox.showinfo("Thông báo", f"Món {item.TenMon} không đủ. Vui lòng chọn món khác.")
                                item.SoLuong +=SoLuongTru  # reset lại để tránh lưu dữ liệu sai
                                return False
                            break
                return True
            if not gio_hang:
                messagebox.showinfo("Thông báo", "Chưa có món nào trong giỏ.")
                reset()
                return
            tong_tien = sum(int(mon.Gia) for mon in gio_hang)
            if user.SoTien >= 10000 + tong_tien:
                 # Kiểm tra số lượng còn đủ không
                # Bước 1: Kiểm tra đủ hàng trước khi trừ
                for mon in gio_hang:
                    danh_sach = DSDA if any(mon.Mamon == da.Mamon for da in DSDA) else DSDU
                    for item in danh_sach:
                        if mon.Mamon == item.Mamon:
                            if item.SoLuong <= 0:
                                messagebox.showinfo("Thông báo", f"Món {item.TenMon} đã hết. Vui lòng chọn món khác.")
                                reset()
                                return
                            break

                # Bước 2: Trừ số lượng
                SoLuongTru=0
                for mon in gio_hang:
                    danh_sach = DSDA if any(mon.Mamon == da.Mamon for da in DSDA) else DSDU
                    for item in danh_sach:
                        if mon.Mamon == item.Mamon:
                            SoLuongTru+=1
                            item.SoLuong -= 1
                            break
                if not kiem_tra_so_luong_am(SoLuongTru):
                    reset()
                    return
                if messagebox.askyesno("Đơn hàng",f"Bạn đồng ý thanh toán {tong_tien}?"):
                    user.SoTien -= tong_tien
                    luu_vao_file(DSND, "QLTiemNet.json")
                    
                    # Tạo mã đơn hàng mới
                    ma_dh = f"HD{len(DSYC)+1:03d}"
                    
                    # Lấy ngày giờ hiện tại
                    now = datetime.now()
                    ngay = now.strftime("%Y-%m-%d")
                    gio = now.strftime("%H:%M:%S")

                    # Tạo đơn hàng
                    don_hang = YeuCau(
                        MaDH=ma_dh,
                        MaKH=user.TK,
                        Ngay=ngay,
                        SoMay=user.SoMay,
                        Gio=gio,
                        DanhSachMon=gio_hang.copy()  # copy để giữ nguyên dữ liệu
                    )

                    luu_vao_file(DSDA,"DoAn.json")
                    luu_vao_file(DSDU,"DoUong.json")
                    DSYC.append(don_hang)
                    luu_vao_file(DSYC, "YeuCau.json")

                    messagebox.showinfo("Thanh toán", f"Đã thanh toán {tong_tien:,}đ.\nCảm ơn bạn!")

                    gio_hang.clear()
                    
                    cap_nhat_gio()
                    time_label.config(text=f"Xin chào {user.Ten}\nBạn đang ngồi máy {user.SoMay}\nCòn lại {user.SoTien:.0f}")
                    reset()
            else:
                reset()
                messagebox.showerror("Lỗi", "Tài khoản phải còn lại 10000 sau thanh toán.")
                return
        def reset():
            for widget in tab_do_an.winfo_children():
                widget.destroy()
            for widget in tab_do_uong.winfo_children():
                widget.destroy()
            hien_thi_muc(tab_do_an, DSDA)
            hien_thi_muc(tab_do_uong, DSDU)
        def huy_gio():
            gio_hang.clear()
            cap_nhat_gio()
        def thoat():
            gio_hang.clear()
            cap_nhat_gio()
            dat_do_win.destroy()
        tk.Button(khung_gio, text="Thanh toán", command=thanh_toan).pack(pady=5)
        tk.Button(khung_gio, text="Hủy", command=huy_gio).pack()

        dat_do_win.protocol("WM_DELETE_WINDOW", thoat)
        def hien_thi_muc(tab, danh_sach):
            row = 0
            col = 0
            for item in danh_sach:
                try:
                    if item.SoLuong!=0:
                        if not item.Hinh or not os.path.exists(f"hinhanh/{item.Hinh}"):
                            img = Image.open(f"hinhanh/No_jpg.jpg")
                        else:
                            img = Image.open(f"hinhanh/{item.Hinh}")
                    else:
                        img = Image.open(f"hinhanh/Het_Hang.jpg")
                    img = img.resize((100, 100))
                    photo = ImageTk.PhotoImage(img)
                    
                    def tao_su_kien(item=item):
                        if item.SoLuong!=0:
                            return lambda e: them_vao_gio(item)
                        else:
                            return
                    panel = tk.Label(tab, image=photo)
                    panel.image = photo
                    panel.grid(row=row, column=col, padx=10, pady=10)
                    panel.bind("<Button-1>", tao_su_kien())
                    
                    ten = item.TenMon
                    gia = item.Gia
                    soluong=item.SoLuong
                    tk.Label(tab, text=f"{ten}\n{gia}đ.Còn:{soluong}").grid(row=row+1, column=col)

                    col += 1
                    if col >= 4:
                        col = 0
                        row += 2
                except Exception as e:
                    print("Lỗi hình ảnh:", e)

        hien_thi_muc(tab_do_an, DSDA)
        hien_thi_muc(tab_do_uong, DSDU)
        
        #==giỏ hàng==

    def hien_cua_so_doi_mk():
        doi_mk_win = tk.Toplevel(win)
        doi_mk_win.title("Đổi mật khẩu")
        
        tk.Label(doi_mk_win, text="Mật khẩu cũ:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_mkc = tk.Entry(doi_mk_win, show="*")
        entry_mkc.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(doi_mk_win, text="Mật khẩu mới:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_mkm = tk.Entry(doi_mk_win, show="*")
        entry_mkm.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(doi_mk_win, text="Xác nhận mật khẩu mới:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_XNMK = tk.Entry(doi_mk_win, show="*")
        entry_XNMK.grid(row=2, column=1, padx=10, pady=5)

        def doi_mk():
            mkc= entry_mkc.get()
            mkm = entry_mkm.get()
            XNMK = entry_XNMK.get()
            if user.MK!=mkc:
                messagebox.showerror("Thông báo","Mật khẩu cũ không đúng!")
                return
            if mkm and XNMK:
                if mkm == XNMK:
                    user.MK = mkm
                    messagebox.showinfo("Đổi mật khẩu", f"Đã đổi mật khẩu cho {user.TK}")
                    luu_vao_file(DSND,"QLTiemNet.json")
                    doi_mk_win.destroy()
                else:
                    messagebox.showerror("Lỗi", "Mật khẩu và xác nhận không giống nhau.")
            else:
                messagebox.showerror("Lỗi", "Chưa nhập đầy đủ.")

        tk.Button(doi_mk_win, text="Xác nhận", command=doi_mk).grid(row=3, column=0, columnspan=2, pady=10)
    def mo_game_ran():
        game_win = tk.Toplevel()
        game_win.title("Game Rắn săn mồi")
        game_win.geometry("420x460")
    
        canvas = tk.Canvas(game_win, width=400, height=400, bg="black")
        canvas.grid(pady=10)

        # ==== Cài đặt ====
        R, C, SIZE = 20, 20, 20
        ran = [(5, 5)]
        huong = (1, 0)
        moi = (10, 10)
        moi_dac_biet = None
        score = 0

        # Hiển thị điểm
        score_text = canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 12), text="Điểm: 0")

        def ve():
            #Xóa toàn bộ khung vẽ để vẽ lại mới từ đầu mỗi khung hình
            canvas.delete("all")
            # Rắn
            # phần thân rắn và vẽ hình chữ nhật màu xanh cho mỗi phần
            for x, y in ran:
                canvas.create_rectangle(x*SIZE, y*SIZE, (x+1)*SIZE, (y+1)*SIZE, fill="light green")
            # Mồi thường
            #Vẽ hình tròn (mồi) tại vị trí moi, màu đỏ.
            x, y = moi
            canvas.create_oval(x*SIZE, y*SIZE, (x+1)*SIZE, (y+1)*SIZE, fill="red")
            # Mồi đặc biệt
            if moi_dac_biet:
                x, y = moi_dac_biet
                canvas.create_oval(x*SIZE-5, y*SIZE-5, (x+1)*SIZE+5, (y+1)*SIZE+5, fill="gold")
            # Điểm
            canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 12), text=f"Điểm: {score}")

        def tao_moi():
            while True:
                m = (random.randint(0, C - 1), random.randint(0, R - 1))
                if m not in ran:
                    return m

        def di_chuyen():
            nonlocal moi, moi_dac_biet, score
            dx, dy = huong
            dau = ran[-1]
            moi_dau = (dau[0] + dx, dau[1] + dy)

            #Kiểm tra xem đầu rắn có đâm vào thân hay ra khỏi lưới không. Nếu có → Game Over.
            if moi_dau in ran or not (0 <= moi_dau[0] < C and 0 <= moi_dau[1] < R):
                messagebox.showinfo("Game Over", f"Rắn đã chết!\nTổng điểm: {score}")
                game_win.destroy()
                return
            #Thêm đầu mới vào rắn.
            ran.append(moi_dau)

            if moi_dau == moi:
                score += 1
                moi = tao_moi()
                # 20% xác suất tạo mồi đặc biệt
                if random.random() < 0.2:
                    moi_dac_biet = tao_moi()
            elif moi_dac_biet and moi_dau == moi_dac_biet:
                score += 3
                moi_dac_biet = None
            else:
                ran.pop(0)

            ve()
            game_win.after(150, di_chuyen)

        def doi_huong(event):
            nonlocal huong
            key = event.keysym
            if key == "Up" and huong != (0, 1): huong = (0, -1)
            elif key == "Down" and huong != (0, -1): huong = (0, 1)
            elif key == "Left" and huong != (1, 0): huong = (-1, 0)
            elif key == "Right" and huong != (-1, 0): huong = (1, 0)

        game_win.bind("<Key>", doi_huong)
        ve()
        di_chuyen()

    # ==== Nút nạp tiền và xử lý nạp tiền ====
    def nap_tien():
        dialog = tk.Toplevel()
        dialog.title("Nạp tiền")
   
        tk.Label(dialog, text="Nhập số tiền muốn nạp:").grid(padx=20, pady=5)
        entry = tk.Entry(dialog)
        entry.grid(padx=20, pady=5)
        
        def confirm():
            
            try:
                nhap = float(entry.get())
                if nhap >= 10000:
                    user.SoTien += nhap
                    messagebox.showinfo("Thành công", f"Đã thêm {nhap:.0f} đồng.")
                    time_label.config(text=f"Xin chào {user.Ten}\nBạn đang ngồi máy {user.SoMay}\nCòn lại {user.SoTien:.0f}")
                    luu_vao_file(DSND,"QLTiemNet.json")
                    dialog.destroy()
                else:
                    messagebox.showerror("Lỗi", "Số tiền phải lớn hơn 10000đ")
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")
   
        tk.Button(dialog, text="Xác nhận", command=confirm).grid(pady=10)
        tk.Button(dialog, text="Hủy", command=dialog.destroy).grid(pady=5)

    # ==== Nút đăng xuất ====
    def dang_xuat():
        global after_id
        if after_id is not None:
            win.after_cancel(after_id)
        dsol.remove(user)
        dsmay.remove(user.SoMay)
        user.SoMay = 0
        luu_vao_file(DSND,"QLTiemNet.json")
        luu_vao_file(dsol,"DSonline.json")
        luu_danh_sach(DSMAY,"DSMayDangOn.txt")
        win.destroy()
        messagebox.showinfo("Đăng xuất", f"{user.TK} đã đăng xuất.")
    win.protocol("WM_DELETE_WINDOW", dang_xuat)
    tk.Button(win, text="Đổi mật khẩu", command=hien_cua_so_doi_mk).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text="Nạp tiền", command=nap_tien).grid(row=1, column=0, sticky="e", padx=10, pady=5)
    tk.Button(win,text="Đặt đồ",command=hien_cua_so_dat_do).grid(row=2, column=0, sticky="e", padx=10, pady=5)
    tk.Button(win, text="Đăng xuất", command=dang_xuat).grid(row=2, column=0, sticky="w", padx=10, pady=5)
    # tk.Button(win, text="Chơi game rắn săn mồi", command=mo_game_ran).grid(row=3, column=0, pady=30)
    tk.Label(win,text="Chơi game rắn săn mồi").grid(row=4, column=0, pady=30)
    def tao_su_kien():
        return lambda e: mo_game_ran

    try:
       img = Image.open(f"hinh/RanSanMoi.png")
       img = img.resize((100, 100))
       photo = ImageTk.PhotoImage(img)
       panel = tk.Label(win, image=photo)
       panel.image = photo
       panel.grid(row=3, column=0, padx=10, pady=10)
       panel.bind("<Button-1>",lambda event: mo_game_ran())
    except:
          print("Lỗi hình ảnh:")
    # ==== Đồng hồ đếm ngược ====
    def cap_nhat_thoi_gian():
        global after_id
        if user.SoTien > 0:
            user.SoTien -= 2.77777777778  # Trừ giá tiền của 1s
            SoGio=user.SoTien/10000
        # Tính giờ, phút và giây từ số giờ thực
            tong_giay = int(SoGio * 3600)
            gio = tong_giay // 3600
            phut = (tong_giay % 3600) // 60
            giay = tong_giay % 60

        # Hiển thị theo định dạng 2 chữ số
            time_label.config(
                text=f"Xin chào {user.Ten}\nBạn đang ngồi máy {user.SoMay}\nCòn lại: {gio:02d}:{phut:02d}:{giay:02d}"
        )
            after_id=win.after(1000, cap_nhat_thoi_gian)
            luu_vao_file(DSND,"QLTiemNet.json")
        else:
            luu_vao_file(DSND,"QLTiemNet.json")
            messagebox.showinfo("Hết giờ", f"Tài khoản {user.TK} đã hết giờ và sẽ bị đăng xuất.")
            dang_xuat()
    if str(user.SoMay)=="0":
        win.destroy()
    cap_nhat_thoi_gian()
   
def mo_dang_nhap():
    login_win = tk.Tk()
    login_win.title("Đăng nhập")
    login_win.geometry("400x300")

    # Biến chọn vai trò
    vai_tro_var = tk.StringVar(value="Nguoi Dung")  # mặc định là người dùng

    tk.Label(login_win, text="Đăng nhập", font=("Arial", 14)).pack(pady=10)

    # Nhập tài khoản và mật khẩu
    tk.Label(login_win, text="Tài khoản").place(x=30, y=80)
    entry_user = tk.Entry(login_win)
    entry_user.place(x=120, y=80)

    tk.Label(login_win, text="Mật khẩu").place(x=30, y=120)
    entry_pass = tk.Entry(login_win, show="*")
    entry_pass.place(x=120, y=120)

    # Radiobutton chọn vai trò – CHUYỂN VỊ TRÍ XUỐNG DƯỚI
    frm_role = tk.Frame(login_win)
    frm_role.place(x=120, y=160)
    tk.Radiobutton(frm_role, text="Người dùng", variable=vai_tro_var, value="Nguoi Dung").pack(side="left", padx=10)
    tk.Radiobutton(frm_role, text="Quản lý", variable=vai_tro_var, value="Quan Ly Net").pack(side="left", padx=10)

    # Nút đăng nhập
    tk.Button(login_win, text="Đăng nhập", command=lambda: dang_nhap()).place(x=80, y=210)
    tk.Button(login_win, text="Quay lại", command=lambda: [login_win.destroy()]).place(x=200, y=210)

    def dang_nhap():
        username = entry_user.get()
        password = entry_pass.get()
        vai_tro = vai_tro_var.get()

        if vai_tro == "Quan Ly Net":
            if any(i.Email == username for i in DSNV):
                for i in DSNV:
                    if i.Email == username:
                        if i.MK == password:
                            
                            hien_thi_chuc_nang_quan_ly2(i.Email)
                            return
                messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng!")  
                return
            else:
                messagebox.showinfo("Thông báo", f"Không tìm thấy tài khoản {username}!")

        elif vai_tro == "Nguoi Dung":
            if not username or not password:
                messagebox.showinfo("Thông báo", f"Vui lòng nhập tài khoản và mật khẩu.")
                return
            for i in DSOL:
                if i.TK == username:
                    messagebox.showinfo("Thông báo", f"Tài khoản {username} đang đăng nhập ở máy {i.SoMay}.")
                    return
            for i in DSND:
                if i.TK == username:
                    if i.MK == password:
                        somay = random.randint(1, 40)
                        while somay in DSMAY:
                            somay = random.randint(1, 40)
                        if float(i.SoTien) <= 0:
                            messagebox.showinfo("Thông báo", f"Tài khoản {username} không còn tiền để đăng nhập.")
                            return
                        DSMAY.append(somay)
                        i.nhap(i.Ten, i.SDT, i.TK, i.MK, somay, i.SoTien)
                        DSOL.append(i)
                        luu_vao_file(DSOL, "DSonline.json")
                        luu_danh_sach(DSMAY, "DSMayDangOn.txt")
                        messagebox.showinfo("Thông báo", f"Tài khoản {username} đăng nhập thành công.")
                        
                        hien_bang_user(i, DSOL, DSMAY)
                        return
                    else:
                        messagebox.showinfo("Thông báo", f"Sai tài khoản hoặc mật khẩu.")
                        return
            messagebox.showinfo("Không tìm thấy", f"Tài khoản {username} không tồn tại.")
        else:
            messagebox.showerror("Lỗi", "Đăng nhập thất bại!")

    login_win.mainloop()
def hien_thi_chuc_nang_quan_ly2(ten_nguoi_dung):
    root = tk.Tk()
    t=''
    for i in DSNV:
        if i.Email==ten_nguoi_dung:
            t=i.Ten
            
    root.title(f"Quản lý người dùng {t}")
    root.geometry("750x550")

    notebook = ttk.Notebook(root)
    tab_chuc_nang = ttk.Frame(notebook)
    tab_yeu_cau = ttk.Frame(notebook)
    tab_do_an=ttk.Frame(notebook)
    
    notebook.add(tab_chuc_nang, text="Chức Năng")
    notebook.add(tab_yeu_cau, text="Yêu Cầu")
    notebook.add(tab_do_an,text="Đồ Ăn")
    notebook.pack(fill="both", expand=True)

    def hien_thi_chuc_nang():
        # ==== Cập nhật Treeview ====
        def cap_nhat_luoi():
            tree.delete(*tree.get_children())
            trang_thai = loc_trang_thai.get()
            for nd in DSND:
                if trang_thai == "Đang online" and (not nd.SoMay or nd.SoMay == 0):
                    continue
                if trang_thai == "Đã offline" and nd.SoMay and nd.SoMay != 0:
                    continue
                SoGio= float(nd.SoTien)/10000
                tong_phut = int(SoGio * 60)
                gio = tong_phut // 60
                phut = tong_phut % 60
                dinh_dang_gio = f"{gio:02d}:{phut:02d}"
                tree.insert("", tk.END, values=( nd.Ten, str(nd.SDT), str(nd.TK), str(nd.MK), dinh_dang_gio, nd.SoMay, nd.SoTien))
            lbl_tong_so.config(text=f"Tổng số tài khoản: {tree.get_children().__len__()}")

        # ==== Chọn dòng trên lưới ====
        def chon_dong(event):
            global tk_dang_chon
            chon = tree.selection()
            if chon:
                Ten,SDT,TK, MK, Sogio, Somay, Sotien= tree.item(chon[0])['values']
                tk_dang_chon=str(TK)
                selected = tree.focus()
                values = tree.item(selected, 'values')
                nhap_Ten.delete(0,tk.END)
                nhap_Ten.insert(0,Ten)
                SoTien=float(Sotien)
                SoTien=int(SoTien)
                SDT=str(values[1])
                nhap_SDT.delete(0,tk.END)
                nhap_SDT.insert(0, SDT)

                nhap_TK.delete(0,tk.END)
                nhap_TK.insert(0, TK)
                dinh_dang = "{:,}".format(SoTien).replace(",", ".")
                nhap_SoTien.delete(0,tk.END)
                nhap_SoTien.insert(0, dinh_dang)
            
                nhap_MK.delete(0,tk.END)    
                nhap_MK.insert(0, MK)
            
                chon_Somay.set(Somay)
    
        # ==== Thêm sinh viên ====
        def them():
            nhap_Ten.delete(0,tk.END)
            nhap_SDT.delete(0,tk.END)
            nhap_TK.delete(0, tk.END)
            nhap_TK.insert(0,"Tự động tạo theo tên và Số điện thoại")
            nhap_MK.delete(0,tk.END)
            nhap_SoTien.delete(0,tk.END)
            nhap_SoTien.insert(0,"0")
            chon_Somay.set("")

        # ==== Lưu người  mới ====
        def luu():
            Ten=nhap_Ten.get().strip()
            if ktr_nhap_ten(Ten)==False:
                messagebox.showerror("Lỗi tên","Tên không thể có số hoặc ký tự đặc biệt.")
                return       
            parts = Ten.split()
            SDT=nhap_SDT.get().strip()
            if ktr_SDT(SDT)==False:
                messagebox.showerror("Lỗi SĐT","Số điện thoại không hợp lệ.")
                return   
            viet_tat = ''.join(word[0] for word in parts[1:])  # lấy chữ cái đầu của tên đệm + tên chính
            TK = viet_tat + str(SDT)[1:]# Viết tắt của tên và số đt
            MK = nhap_MK.get().strip()
        
            Tien = nhap_SoTien.get().strip()
            
            Somay = chon_Somay.get()
            if not SDT or not MK or not Ten:
                messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập đầy đủ.")
                return
            if not Tien:
                messagebox.showwarning("Sai dữ liệu", "Vui lòng nhập số tiền hợp lệ.")
                return 
            try:
                if float(Tien)<0:
                    messagebox.showwarning("Sai dữ liệu", "Vui lòng nhập số tiền hợp lệ.")
                    return
            except:
                messagebox.showwarning("Sai dữ liệu", "Vui lòng nhập số tiền hợp lệ.")
                return
            if any(nd.TK == TK for nd in DSND):
                messagebox.showerror("Trùng mã", "tài khoản đã tồn tại.")
                return

            if messagebox.askyesno("Xác nhận", f"Thêm tài khoản {TK}?"):
                u=User(Ten,SDT,TK,MK, float(Tien),Somay)
                DSND.append(u)
                luu_vao_file(DSND,"QLTiemNet.json")
                cap_nhat_luoi()
                messagebox.showinfo("Thành công", "Đã thêm tài khoản.")

        def Doi_MK():
            global tk_dang_chon
            chon = tree.selection()
            if chon:
                MK_moi = nhap_MK.get().strip()
                if not MK_moi:
                    messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập đầy đủ.")
                    return
                if messagebox.askyesno("Xác nhận", f"Đổi mật khẩu tài khoản {tk_dang_chon}?"):
                    for nd in DSND:
                        if str(nd.TK) == str(tk_dang_chon):
                            nd.MK=MK_moi
                            break
                    luu_vao_file(DSND,"QLTiemNet.json")
                    cap_nhat_luoi()
                    messagebox.showinfo("Thành công", "Đã đổi mật khẩu thành công.")
            if not chon:
                messagebox.showwarning("Chưa chọn", "Vui lòng chọn tài khoản để đổi mật khẩu.")
                return
       
        def dangxuat():
            global tk_dang_chon
            chon=tree.selection()
            if not chon:
                messagebox.showwarning("Chưa chọn", "Chọn tài khoảng cần đăng xuất.")
                return
            TK=tree.item(chon[0])['values'][2]
            for i in DSND:
                if i.TK==TK:
                    for i in DSOL:
                        if i.TK==TK:
                                if messagebox.askyesno("Xác nhận", f"Đăng xuất tài khoản {TK}?"):   
                                    DSOL.remove(i)
                                    try:
                                        DSMAY.remove(i.SoMay)
                                    except:
                                        pass
                                    for j in DSND:
                                        if j.TK==i.TK:
                                            j.SoMay=0
                                    luu_vao_file(DSND,"QLTiemNet.json")
                                    luu_vao_file(DSOL,"DSonline.json")
                                    luu_danh_sach(DSMAY,"DSMayDangOn.txt")
                                
                                    cap_nhat_luoi()
                                    messagebox.showinfo("Đăng xuất", f"{i.TK} đã đăng xuất.")
                                return
                    else:
                         messagebox.showinfo("Thông báo",f"Tài khoản {TK} chưa đăng nhập.")
                         return 
             
            messagebox.showerror("Lỗi",f"Không tìm thấy tài khoản {TK}.")
            return
        def tim_nguoi_dung_theo_sdt():
            sdt_can_tim = nhap_SDT.get().strip()
            if not sdt_can_tim:
                messagebox.showinfo("Thông báo", "Vui lòng nhập số điện thoại.")
                return
            
            if ktr_SDT(sdt_can_tim)==False:
                messagebox.showerror("Thông báo","Vui lòng nhập số điện thoại hợp lệ.")
                return
            
            for i in tree.get_children():
                if tree.item(i, "values")[1] == sdt_can_tim:  # cột SĐT là cột thứ 1
                    tree.selection_set(i)
                    tree.focus(i)
                    tree.see(i)
                    chon_dong(None)  # gọi lại sự kiện hiển thị lên Entry
                    return
            messagebox.showinfo("Không tìm thấy", f"Không tìm thấy người dùng có SĐT: {sdt_can_tim}")

        def xoa():
            global tk_dang_chon
            chon = tree.selection()
            if not chon:
                messagebox.showwarning("Chưa chọn", "Chọn tài khoảng cần xóa.")
                return

            TK = tree.item(chon[0])['values'][2]

            if messagebox.askyesno("Xác nhận", f"Xóa tài khoản {TK}?"):
                # Lọc danh sách và cập nhật trực tiếp danh sách gốc
                ds_moi = [nd for nd in DSND if (str(nd.TK) != str(TK)) ]
                if len(ds_moi) < len(DSND):
                    DSND.clear()
                    DSND.extend(ds_moi)
                    luu_vao_file(DSND,"QLTiemNet.json")
                    cap_nhat_luoi()
                    tk_dang_chon = None
                    messagebox.showinfo("Thành công", f"Đã xóa tài khoản {TK}.")
                else:
                    messagebox.showerror("Lỗi", f"Không tìm thấy tài khoản {TK} để xóa.")

            
        def thoat():
            luu_vao_file(DSND,"QLTiemNet.json")
            luu_vao_file(DSOL,"DSonline.json")
            if root.winfo_exists():
                root.destroy()
            mo_dang_nhap()
        def xet_MK_Admin():
            win=tk.Toplevel(root)
            win.title("Quản lý nhân viên")
            win.geometry("300x100")
            frame_edit = tk.Frame(win)
            frame_edit.pack()
            tk.Label(frame_edit, text="Mật khẩu admin:").grid(row=2, column=0, padx=5, pady=2)
            entry_admin = tk.Entry(frame_edit, show="*", width=30)
            entry_admin.grid(row=2, column=1, padx=5, pady=2)
            def xet():
                if entry_admin.get() != "123":
                        messagebox.showerror("Lỗi", "Mật khẩu admin sai.")
                        return
                
                return thong_tin_nv()
            frame_btn = tk.Frame(win)
            frame_btn.pack(pady=10)
            tk.Button(frame_btn, text="Xác nhận", width=10, command=xet).pack(side="left", padx=10)
            tk.Button(frame_btn, text="Quay lại", width=10, command=win.destroy).pack(side="left", padx=10)
        def thong_tin_nv():
            win = tk.Toplevel(root)
            win.title("Quản lý nhân viên")
            win.geometry("700x400")

            # === Treeview ===
            tree_nv = ttk.Treeview(win, columns=("MaNV", "Ten", "SDT", "Email"), show="headings")
            for col in ("MaNV", "Ten", "SDT", "Email"):
                tree_nv.heading(col, text=col)
                tree_nv.column(col, width=150)
            tree_nv.pack(fill="both", expand=True, pady=10)

            def cap_nhat_tree():
                tree_nv.delete(*tree_nv.get_children())
                for nv in DSNV:
                    tree_nv.insert("", "end", values=(nv.MaNV, nv.Ten, nv.SDT, nv.Email))
            cap_nhat_tree()

            # === Entry để sửa ===
            frame_edit = tk.Frame(win)
            frame_edit.pack()

            tk.Label(frame_edit, text="Email mới:").grid(row=0, column=0, padx=5, pady=2)
            entry_email = tk.Entry(frame_edit, width=30)
            entry_email.grid(row=0, column=1, padx=5, pady=2)

            tk.Label(frame_edit, text="Mật khẩu mới:").grid(row=1, column=0, padx=5, pady=2)
            entry_mk = tk.Entry(frame_edit, width=30)
            entry_mk.grid(row=1, column=1, padx=5, pady=2)

            # === Hàm chọn dòng để sửa ===
            def chon_dong(event):
                chon = tree_nv.selection()
                if not chon: return
                ma_nv = tree_nv.item(chon[0])['values'][0]
                for nv in DSNV:
                    if nv.MaNV == ma_nv:
                        entry_email.delete(0, tk.END)
                        entry_email.insert(0, nv.Email)
                        entry_mk.delete(0, tk.END)
                        entry_mk.insert(0, nv.MK)
                        break
            tree_nv.bind("<<TreeviewSelect>>", chon_dong)

            # === Hàm cập nhật ===
            def sua_nv():
                chon = tree_nv.selection()
                if not chon:
                    messagebox.showwarning("Chọn dòng", "Chọn nhân viên cần sửa.")
                    return
                ma_nv = tree_nv.item(chon[0])['values'][0]
                for nv in DSNV:
                    if nv.MaNV == ma_nv:
                        nv.Email = entry_email.get().strip()
                        nv.MK = entry_mk.get().strip()
                        luu_vao_file(DSNV, "NhanVien.json")
                        messagebox.showinfo("Cập nhật", "Đã sửa thành công.")
                        cap_nhat_tree()
                        return

            # === Hàm xóa ===
            def xoa_nv():
                chon = tree_nv.selection()
                if not chon:
                    messagebox.showwarning("Chọn dòng", "Chọn nhân viên cần xóa.")
                    return
                ma_nv = tree_nv.item(chon[0])['values'][0]
                for nv in DSNV:
                    if nv.MaNV == ma_nv:
                        if messagebox.askyesno("Xác nhận", f"Bạn muốn xóa nhân viên {nv.Ten}?"):
                            DSNV.remove(nv)
                            luu_vao_file(DSNV, "NhanVien.json")
                            cap_nhat_tree()
                            messagebox.showinfo("Xóa", "Đã xóa thành công.")
                        return

            # === Nút thao tác ===
            frame_btn = tk.Frame(win)
            frame_btn.pack(pady=10)
            tk.Button(frame_btn, text="Sửa", width=10, command=sua_nv).pack(side="left", padx=10)
            tk.Button(frame_btn, text="Xóa", width=10, command=xoa_nv).pack(side="left", padx=10)
            

        def Tao_TK_AD():
            win=tk.Toplevel()
            win.title("Tạo tài khoản mới cho nhân viên")
            win.geometry("400x400")
            
            tk.Label(win,text="Họ Tên: ").grid(row=0, column=0, padx=10, pady=5, sticky="w")
            entry_Hoten=tk.Entry(win)
            entry_Hoten.grid(row=0, column=1, padx=10, pady=5)
            
            tk.Label(win,text="Số điện thoại: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")
            entry_SDT=tk.Entry(win)
            entry_SDT.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(win,text="Mật khẩu: ").grid(row=2, column=0, padx=10, pady=5, sticky="w")
            entry_MK=tk.Entry(win)
            entry_MK.grid(row=2, column=1, padx=10, pady=5)
            
            tk.Label(win,text="Email: ").grid(row=3, column=0, padx=10, pady=5, sticky="w")
            entry_Email=tk.Entry(win)
            entry_Email.grid(row=3, column=1, padx=10, pady=5)
            tk.Label(win,text="Mã NV sẽ tự động điền NV+SĐT ").grid(row=4, column=0, padx=10, pady=5, sticky="w")
            def Tao():
                Ten=entry_Hoten.get().strip()
                if ktr_nhap_ten(Ten)==False:
                    messagebox.showerror("Lỗi tên","Tên không thể có số hoặc kí tự đặt biệt!")
                    return
                SDT=entry_SDT.get().strip()
                if ktr_SDT(SDT)==False:
                    messagebox.showerror("Lỗi SĐT","Số điện thoại không hợp lệ.")
                    return
                MK=entry_MK.get()
                Email=entry_Email.get()
                if ktr_EMAIL(Email)==False:
                    messagebox.showerror("Lỗi Email","Email không hợp lệ.")
                    return
                
                Ma = "NV" + str(SDT)[1:]# Viết tắt của tên và số đt
                for nv in DSNV:
                    if nv.MaNV==Ma or nv.Email==Email:
                        messagebox.showinfo("Thông báo","Đã trùng mã hoặc Email") 
                        return
                x=NhanVien(Ten,Ma, MK,SDT,0,Email)
                DSNV.append(x)
                luu_vao_file(DSNV,"NhanVien.json")
                messagebox.showinfo("Thông báo","Đã tạo thành công")
                win.destroy()
            tk.Label(win, text="").grid(row=5, column=0, padx=10, pady=5)              
            tk.Button(win, text="Xác nhận", width=10, command=Tao).grid(row=5, column=1, pady=5,sticky="w")

        def NapTien():
            SoTien=nhap_tien.get().strip()
            global tk_dang_chon
            chon=tree.selection()
        
            if not chon:
                messagebox.showwarning("Chưa chọn", "Chọn tài khoảng cần nạp.")
                return
            tk=tree.item(chon[0])['values'][2]
            if float(SoTien)>=10000:
                    for nd in DSND:
                        if nd.TK==tk:
                            if messagebox.askyesno("Xác nhận", f"Nạp {SoTien} cho tài khoản {tk}?"):
                                nd.SoTien += float(SoTien)
                                luu_vao_file(DSND,"QLTiemNet.json")  
                                cap_nhat_luoi()
                                messagebox.showinfo("Thông báo",f"Đã nạp thành công {SoTien} cho {tk}.")
                                return
            else:
                messagebox.showwarning("Lỗi nạp","Phải nạp trên 10000 đ!")

        tk_dang_chon = None

        frame = tk.Frame(tab_chuc_nang)
        frame.pack(pady=10)
    
        tk.Label(frame,text="Số tiền nạp:").grid(row=0,column=2)    
        nhap_tien=tk.Entry(frame,width=25)
        nhap_tien.grid(row=0,column=3)
    
        tk.Label(frame, text="Họ Tên:").grid(row=0, column=0)
        nhap_Ten = tk.Entry(frame, width=25)
        nhap_Ten.grid(row=0, column=1)
    
    
        tk.Label(frame, text="Số tiền:").grid(row=1, column=0)
        nhap_SoTien = tk.Entry(frame, width=25)
        nhap_SoTien.grid(row=1, column=1)
    
        tk.Label(frame, text="Số điện thoại:").grid(row=2, column=0)
        nhap_SDT =tk.Entry(frame, width=25)
        nhap_SDT.grid(row=2, column=1)
    
        tk.Label(frame, text="Tài khoản:").grid(row=3, column=0)
        nhap_TK = tk.Entry(frame, width=25)
        nhap_TK.grid(row=3, column=1)
   
        tk.Label(frame, text="Mật khẩu:").grid(row=4, column=0)
        nhap_MK = tk.Entry(frame, width=25)
        nhap_MK.grid(row=4, column=1)
   
        tk.Label(frame, text="Số Máy:").grid(row=5, column=0)
        chon_Somay = ttk.Combobox(frame, width=22, state="readonly")
        chon_Somay.grid(row=5, column=1)
        
        tk.Label(frame, text="Lọc trạng thái:").grid(row=6, column=2)
        loc_trang_thai = ttk.Combobox(frame, values=["Tất cả", "Đang online", "Đã offline"], state="readonly", width=18)
        loc_trang_thai.set("Tất cả")
        loc_trang_thai.grid(row=6, column=3)
        
        tk.Button(frame, text="Tìm kiếm", command=tim_nguoi_dung_theo_sdt).grid(row=2, column=2)

        tk.Button(frame, text="Thêm nhân viên", command=Tao_TK_AD).grid(row=3, column=2)
        lbl_hinh = tk.Label(frame)
        lbl_hinh.grid(row=0, column=3, rowspan=4, padx=10)
        tk.Button(frame, text="Nạp", width=10, command=NapTien).grid(row=0, column=4, padx=5)
        # ==== Nút chức năng ====
        
        btns = tk.Frame(tab_chuc_nang)
        btns.pack(pady=5)
        
        tk.Button(btns, text="Thêm", width=10, command=them).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="Lưu", width=10, command=luu).grid(row=0, column=1, padx=5)
        tk.Button(btns, text="Đăng xuất", width=10, command=dangxuat).grid(row=0, column=2, padx=5)
        tk.Button(btns, text="Đổi mật khẩu", width=10, command=Doi_MK).grid(row=0, column=3, padx=5)
        tk.Button(btns, text="Xóa", width=10, command=xoa).grid(row=0, column=4, padx=5)
        tk.Button(btns, text="Reset", width=10, command=cap_nhat_luoi).grid(row=0, column=5, padx=5)
        tk.Button(btns, text="Thông tin NV", width=12, command=xet_MK_Admin).grid(row=0, column=6, padx=5)
        
        tk.Button(btns, text="Thoát", width=10, command=thoat).grid(row=0, column=7, padx=5)

        # ==== Treeview ====
        tree = ttk.Treeview(tab_chuc_nang, columns=("Tên","Số điện thoại","Tài khoản", "Mật khẩu", "Số giờ","Số máy"), show="headings", selectmode="browse")
        tree.heading("Tên", text="Tên")
        tree.heading("Số điện thoại", text="Số điện thoại")
        tree.heading("Tài khoản", text="Tài khoản")
        tree.heading("Mật khẩu", text="Mật khẩu")
        tree.heading("Số giờ", text="Số giờ")
        tree.heading("Số máy", text="Số máy")
    
        tree.column("Tên", width=200)
        tree.column("Số điện thoại", width=100)
        tree.column("Tài khoản", width=100)
        tree.column("Mật khẩu", width=100)
        tree.column("Số giờ", width=100)
        tree.column("Số máy", width=100)

        tree.bind("<<TreeviewSelect>>", chon_dong)
        tree.pack(fill='x', padx=20, pady=20)
        
        # Label thống kê (ở góc dưới bên phải)
        frame_thongke = tk.Frame(tab_chuc_nang)
        frame_thongke.pack(fill='x', padx=20, pady=(0, 10), anchor='e')

        lbl_tong_so = tk.Label(frame_thongke, text="Tổng số tài khoản: 0", anchor='e')
        lbl_tong_so.pack(anchor="e")
        # ==== Khởi chạy ====
        chon_Somay["values"]=DSMAY
        cap_nhat_luoi()

    def hien_thi_yeu_cau():

            def cap_nhat_luoi():
                global DSYC,data
                data = Doc_File("YeuCau.json")
                DSYC = []
                TaoYeuCau(DSYC)
                tree.delete(*tree.get_children())
                for yc in DSYC:
                    for mon in yc.DanhSachMon:
                        ten_mon = mon.get("Ten_Mon") or mon.get("MaMon", "")
                        tree.insert("", "end", values=(
                            yc.MaDH,
                            ten_mon,
                            yc.MaKH,
                            yc.SoMay,
                            yc.Ngay,
                            yc.Gio,
                            mon.get("trangthai", "Chưa xác nhận")
                        ))
                lbl_tk_yc.config(text=f"Tổng món đang đặt: {len(tree.get_children())}")

            # Bảng yêu cầu
            tree = ttk.Treeview(tab_yeu_cau, columns=("MaDH", "TenMon", "MaKH", "SoMay", "Ngay", "Gio", "TrangThai"), show="headings")
            tree.heading("MaDH", text="Mã ĐH")
            tree.heading("TenMon", text="Tên Món")
            tree.heading("MaKH", text="Mã KH")
            tree.heading("SoMay", text="Số Máy")
            tree.heading("Ngay", text="Ngày")
            tree.heading("Gio", text="Giờ")
            tree.heading("TrangThai", text="Trạng Thái")
            

            tree.column("MaDH", width=50)
            tree.column("TenMon", width=100)
            tree.column("MaKH", width=100)
            tree.column("SoMay", width=100)
            tree.column("Ngay", width=100)
            tree.column("Gio", width=100)
            tree.column("TrangThai", width=100)
            tree.pack(fill="both", expand=True)
            
            frame_tk_yc = tk.Frame(tab_yeu_cau)
            frame_tk_yc.pack(fill='x', padx=20, pady=(0,10), anchor='e')

            lbl_tk_yc = tk.Label(frame_tk_yc, text="Tổng món đang đặt: 0", anchor='e')
            lbl_tk_yc.pack(anchor='e')
            def loc_du_lieu():
                global DSYC
                tu_khoa = entry_ten_mon.get().lower().strip()
                trang_thai = cb_trang_thai.get().strip()

                tree.delete(*tree.get_children())
                for yc in DSYC:
                    for mon in yc.DanhSachMon:
                        ten_mon = mon.get("Ten_Mon", "").lower()
                        trangthai = mon.get("trangthai", "Chưa xác nhận")

                        if tu_khoa and tu_khoa not in ten_mon:
                            continue
                        if trang_thai and trangthai != trang_thai:
                            continue

                        tree.insert("", "end", values=(
                            yc.MaDH,
                            mon.get("Ten_Mon"),
                            yc.MaKH,
                            yc.SoMay,
                            yc.Ngay,
                            yc.Gio,
                            trangthai
                        ))
                lbl_tk_yc.config(text=f"Tổng món đang đặt: {len(tree.get_children())}")

            # ==== Giao diện lọc ====
            frame_loc = tk.Frame(tab_yeu_cau)
            frame_loc.pack(pady=5)

            tk.Label(frame_loc, text="Lọc theo món:").pack(side="left")
            ds_ten_mon = set()
            for yc in DSYC:
                for mon in yc.DanhSachMon:
                    ten_mon = mon.get("Ten_Mon") or mon.get("MaMon", "")
                    ds_ten_mon.add(ten_mon)
            ds_ten_mon = sorted(list(ds_ten_mon))            

            entry_ten_mon = ttk.Combobox(frame_loc, values=[""]+ds_ten_mon, state="readonly")
            entry_ten_mon.pack(side="left", padx=5)

            tk.Label(frame_loc, text="Trạng thái:").pack(side="left")
            cb_trang_thai = ttk.Combobox(frame_loc, values=["", "Chưa xác nhận", "Chờ làm"], state="readonly")
            cb_trang_thai.pack(side="left", padx=5)

            tk.Button(frame_loc, text="Lọc", command=loc_du_lieu).pack(side="left", padx=5)
            tk.Button(frame_loc, text="Đặt lại", command=cap_nhat_luoi).pack(side="left")

            def xac_nhan():
                global DSYC
                item = tree.focus()
                if not item:
                    messagebox.showinfo("Thông báo", "Chọn một đơn để xác nhận.")
                    return

                trang_thai = tree.set(item, "TrangThai")
                if trang_thai != "Chưa xác nhận":
                    messagebox.showinfo("Xác nhận", f"Đơn hàng đã ở trạng thái: {trang_thai}!")
                    return

                ma_dh = tree.set(item, "MaDH")
                ten_mon = tree.set(item, "TenMon")

                # Cập nhật trạng thái trong DSYC
                so_mon_xac_nhan = 0
                for yc in DSYC:
                    if yc.MaDH == ma_dh:
                        for mon in yc.DanhSachMon:
                            if (mon.get("Ten_Mon", "").strip().lower() == ten_mon.strip().lower() or mon.get("MaMon", "") == ten_mon):
                                if mon.get("trangthai", "") == "Chưa xác nhận":
                                    mon["trangthai"] = "Chờ làm"
                                    so_mon_xac_nhan += 1
                        break  # chỉ cần tìm đúng đơn hàng (MaDH), không cần duyệt tiếp

                if so_mon_xac_nhan > 0:
                    luu_vao_file(DSYC, "YeuCau.json")
                    messagebox.showinfo("Xác nhận", f"Đã xác nhận {so_mon_xac_nhan} món.")
                    cap_nhat_luoi()  # cập nhật lại lưới để phản ánh trạng thái mới
                else:
                    messagebox.showwarning("Không tìm thấy", f"Không có món nào phù hợp để xác nhận.")
            def hoan_thanh():
                global DSYC
                item = tree.focus()
                if not item:
                    messagebox.showinfo("Thông báo", "Chọn một món để hoàn thành.")
                    return

                trang_thai = tree.set(item, "TrangThai")
                if trang_thai != "Chờ làm":
                    messagebox.showwarning("Lỗi", "Chỉ hoàn thành món đã xác nhận.")
                    return

                ma_dh = tree.set(item, "MaDH")
                ten_mon = tree.set(item, "TenMon")
                gia_mon = 0

                # Tìm giá món
                for mon in DSDA + DSDU:
                    if mon.TenMon == ten_mon:
                        gia_mon = float(mon.Gia)
                        break

                if gia_mon == 0:
                    messagebox.showwarning("Lỗi", f"Không tìm thấy giá cho món '{ten_mon}'.")
                    return

                # Cộng tiền cho nhân viên
                for nv in DSNV:
                    if nv.Email == ten_nguoi_dung:
                        nv.TongThu += gia_mon
                        break
                luu_vao_file(DSNV, "NhanVien.json")

                # Xóa món khỏi đơn trong DSYC
                found_and_removed = False
                for yc in DSYC:
                    if yc.MaDH == ma_dh:
                        for mon in yc.DanhSachMon:
                            if (mon.get("Ten_Mon") == ten_mon or mon.get("MaMon") == ten_mon) and mon.get("trangthai") == "Chờ làm":
                                yc.DanhSachMon.remove(mon)
                                found_and_removed = True
                        break
                
                if found_and_removed:
                    # Xóa đơn rỗng
                    DSYC[:] = [yc for yc in DSYC if yc.DanhSachMon]
                    
                    luu_vao_file(DSYC, "YeuCau.json")
                    tree.delete(item)
                    messagebox.showinfo("Hoàn thành", f"Đã giao '{ten_mon}'. Cộng +{gia_mon:,} VNĐ vào tổng thu.")
                else:
                    messagebox.showwarning("Lỗi", "Không tìm thấy món cần hoàn thành trong dữ liệu hoặc trạng thái sai.")
                lbl_tk_yc.config(text=f"Tổng món đang đặt: {len(tree.get_children())}")
            btn_frame = tk.Frame(tab_yeu_cau)
            btn_frame.pack(pady=10)

            btn_xac_nhan = tk.Button(btn_frame, text="Xác nhận đơn", command=xac_nhan)
            btn_xac_nhan.pack(side="left", padx=10)

            btn_hoan_thanh = tk.Button(btn_frame, text="Hoàn thành", command=hoan_thanh)
            btn_hoan_thanh.pack(side="left", padx=10)
            
            btn_reset = tk.Button(btn_frame, text="Reset", command=cap_nhat_luoi)
            btn_reset.pack(side="left", padx=10)
            cap_nhat_luoi()
    def hien_thi_do_an():
        def ktr_nhap(ma):
            if not re.fullmatch(r"(DA|DU)\d{3}", ma):
                messagebox.showerror("Lỗi", "Mã món phải có dạng DA001 hoặc DU001.")
                return False
            return True
        def cap_nhat_luoi():
            tree.delete(*tree.get_children())
            loai = loai_loc.get()
            
            if loai == "Đồ ăn":
                danh_sach = DSDA
                
            elif loai == "Đồ uống":
                danh_sach = DSDU
            else:
                danh_sach = DSDA + DSDU

            for Food in danh_sach:
                tree.insert("", tk.END, values=(Food.Mamon, Food.TenMon, Food.Gia, Food.SoLuong))
            lbl_tk_da.config(text=f"Tổng món: {len(tree.get_children())}")
            
        
        def chon_dong(event):
            global mon_dang_chon, photo
            chon = tree.selection()
            if chon:
                Ma, Ten, Gia, SoLuong = tree.item(chon[0])['values']
                mon_dang_chon = str(Ma)

                nhap_ma.delete(0, tk.END)
                nhap_ma.insert(0, Ma)

                nhap_ten.delete(0, tk.END)
                nhap_ten.insert(0, Ten)

                dinh_dang = "{:,}".format(Gia).replace(",", ".")
                nhap_gia.delete(0, tk.END)
                nhap_gia.insert(0, dinh_dang)

                nhap_soluong.delete(0, tk.END)
                nhap_soluong.insert(0, SoLuong)

                danh_sach = DSDA +DSDU
                found = False
                for Food in danh_sach:
                    if Ma == Food.Mamon:
                        Hinh = Food.Hinh
                        found = True
                        break
                if not found or not os.path.exists(f"hinhanh/{Hinh}"):
                    Hinh = "No_jpg.jpg"

                nhap_hinh.delete(0, tk.END)
                nhap_hinh.insert(0, Hinh)
        def them():
            def chon_anh():
                filename = filedialog.askopenfilename(
                    title="Chọn ảnh",
                    filetypes=[("Ảnh", "*.jpg *.png")]
                )
                if filename:
                    tenfile = os.path.basename(filename)
                    nhap_hinh.delete(0, tk.END)
                    nhap_hinh.insert(0, tenfile)

            def xac_nhan_them():
                ma = nhap_ma.get()
                if ktr_nhap(ma)== False:
                    return
                ten = nhap_ten.get()
                if ktr_nhap_ten(ten)==False:
                    messagebox.showerror("Lỗi", "Tên không được có kí tự đặc biệt.")
                hinh = nhap_hinh.get()
                try:
                    gia = int(nhap_gia.get().replace(".", ""))
                    sl = int(nhap_soluong.get())
                except:
                    messagebox.showerror("Lỗi", "Giá và số lượng phải là số.")
                    return
                found=False
                if not ma or not ten:
                    messagebox.showerror("Lỗi", "Không được bỏ trống mã hoặc tên món.")
                    return

                if check_an.get() and check_uong.get():
                    messagebox.showerror("Lỗi", "Chỉ được chọn 1 loại: Thức ăn hoặc Thức uống.")
                    return
                elif check_an.get():
                    if ma[:2]=="DA":    
                        danh_sach = DSDA
                        found=True
                        tenfile="DoAn.json"
                    else:
                        messagebox.showerror("Lỗi", "Bạn chọn sai loại món hoặc nhập mã móm.")

                elif check_uong.get():
                    if ma[:2]=="DU":
                        danh_sach = DSDU
                        found=True
                        tenfile="DoUong.json"
                    else:
                        messagebox.showerror("Lỗi", "Bạn chọn sai loại món hoặc nhập mã móm.")
                else:
                    messagebox.showerror("Lỗi", "Bạn chưa chọn loại món.")
                    return
                if found:
                    for f in danh_sach:
                        if f.Mamon == ma:
                            messagebox.showerror("Lỗi", "Mã món đã tồn tại.")
                            return

                    danh_sach.append(DoAn(ma, ten, gia,"",hinh,"Chưa xác nhận" ,sl ))
                    luu_vao_file(danh_sach,tenfile)
                    messagebox.showinfo("Thành công", "Đã thêm món.")
                    top.destroy()
                    cap_nhat_luoi()

            top = tk.Toplevel()
            top.title("Thêm món mới")
            top.geometry("400x330")

            check_an = tk.BooleanVar(value=False)
            check_uong = tk.BooleanVar(value=False)

            tk.Label(top, text="Mã món").grid(row=0, column=0, sticky="e", padx=5, pady=5)
            nhap_ma = tk.Entry(top)
            nhap_ma.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(top, text="Tên món").grid(row=1, column=0, sticky="e", padx=5, pady=5)
            nhap_ten = tk.Entry(top)
            nhap_ten.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(top, text="Giá").grid(row=2, column=0, sticky="e", padx=5, pady=5)
            nhap_gia = tk.Entry(top)
            nhap_gia.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(top, text="Số lượng").grid(row=3, column=0, sticky="e", padx=5, pady=5)
            nhap_soluong = tk.Entry(top)
            nhap_soluong.grid(row=3, column=1, padx=5, pady=5)

            # Hình ảnh
            tk.Label(top, text="Tên hình").grid(row=4, column=0, sticky="e", padx=5, pady=5)
            nhap_hinh = tk.Entry(top)
            nhap_hinh.grid(row=4, column=1, padx=5, pady=5)

            tk.Button(top, text="Chọn ảnh", command=chon_anh).grid(row=4, column=2, padx=5)

            # Checkbutton
            tk.Label(top, text="Loại món:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
            tk.Checkbutton(top, text="Thức ăn", variable=check_an).grid(row=5, column=1, sticky="w", padx=5)
            tk.Checkbutton(top, text="Thức uống", variable=check_uong).grid(row=5, column=1,columnspan=2, sticky="e", padx=5)

            tk.Button(top, text="Xác nhận", command=xac_nhan_them).grid(row=6, column=0, columnspan=3, pady=15)

        def xoa():
            ma = nhap_ma.get()
            if ktr_nhap(ma)== False:
                return
            found=False
            for f in DSDA:
                if f.Mamon == ma:
                    found=True
                    if messagebox.askyesno("Thông báo",f"Xác nhận xóa món này?"):
                        DSDA.remove(f)
                        luu_vao_file(DSDA,"DoAn.json")    
                        messagebox.showinfo("Thông báo",f"Đã xóa thành công món {f.TenMon}")
                    break
            if not found:
                for f in DSDU:
                    if f.Mamon == ma:
                        found=True
                        if messagebox.askyesno("Thông báo",f"Xác nhận xóa món này?"):
                            DSDU.remove(f)
                            luu_vao_file(DSDU,"DoAn.json")

                            messagebox.showinfo("Thông báo",f"Đã xóa thành công món {f.TenMon}")
                        break
            if not found:
                messagebox.showerror("Thông báo",f"Không tìm thấy món có mã {ma}")
            cap_nhat_luoi()
    
        def sua():
            chon = tree.selection()
            if not chon:
                messagebox.showwarning("Chưa chọn", "Vui lòng chọn một món để sửa.")
                return

            ma_cu = tree.item(chon[0])['values'][0]  # Mã món cũ đang chọn
            ma_moi = nhap_ma.get().strip()
            ten_moi = nhap_ten.get().strip()
            try:
                gia_moi_raw = nhap_gia.get().strip().replace(",", "").replace(".", "")
                gia_moi = int(gia_moi_raw)
                sl_moi = int(nhap_soluong.get())
            except:
                messagebox.showerror("Lỗi", "Giá và Số lượng phải là số nguyên.")
                return

            if not re.fullmatch(r"(DA|DU)\d{3}", ma_moi):
                messagebox.showerror("Lỗi", "Mã món phải có dạng DA001 hoặc DU001.")
                return

            # Kiểm tra mã mới có trùng với món khác (trừ món đang sửa)
            for food in DSDA + DSDU:
                if food.Mamon == ma_moi and food.Mamon != ma_cu:
                    messagebox.showerror("Lỗi", f"Mã món '{ma_moi}' đã tồn tại.")
                    return

            # Tìm và cập nhật món đang chọn
            for ds in (DSDA, DSDU):
                for food in ds:
                    if food.Mamon == ma_cu:
                        food.Mamon = ma_moi
                        food.TenMon = ten_moi
                        food.Gia = gia_moi
                        food.SoLuong = sl_moi
                        luu_vao_file(DSDA, "DoAn.json")
                        luu_vao_file(DSDU, "DoUong.json")
                        cap_nhat_luoi()
                        messagebox.showinfo("Thành công", "Đã sửa món.")
                        return
        def thoat():
            luu_vao_file(DSND, "QLTiemNet.json")
            luu_vao_file(DSOL, "DSonline.json")
            if root.winfo_exists():
                root.destroy()
            
    
        # Giao diện nhập liệu
        mon_dang_chon = None
        frame = tk.Frame(tab_do_an)
        frame.pack(pady=10)
        btns = tk.Frame(tab_do_an)
        btns.pack(pady=5)
        
        tk.Label(frame, text="Mã món").grid(row=0, column=0)
        nhap_ma = tk.Entry(frame, width=25)
        nhap_ma.grid(row=0, column=1)
    
        tk.Label(frame, text="Tên món").grid(row=1, column=0)
        nhap_ten = tk.Entry(frame, width=25)
        nhap_ten.grid(row=1, column=1)
    
        tk.Label(frame, text="Giá").grid(row=2, column=0)
        nhap_gia = tk.Entry(frame, width=25)
        nhap_gia.grid(row=2, column=1)
    
        tk.Label(frame, text="Số lượng").grid(row=3, column=0)
        nhap_soluong = tk.Entry(frame, width=25)
        nhap_soluong.grid(row=3, column=1)
        
        tk.Label(frame, text="Tên hình").grid(row=4, column=0)
        nhap_hinh = tk.Entry(frame, width=25)
        nhap_hinh.grid(row=4, column=1)

        lbl_hinh = tk.Label(frame)
        lbl_hinh.grid(row=2, column=3, rowspan=2, padx=10)
        lbl_hinh._anh = None
        # Nút chức năng
        tk.Button(btns, text="Thêm", width=10, command=them).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="Xóa", width=10, command=xoa).grid(row=0, column=1, padx=5)
        tk.Button(btns, text="Sửa", width=10, command=sua).grid(row=0, column=2, padx=5)
        tk.Button(btns, text="Thoát", width=10, command=thoat).grid(row=0, column=3, padx=5)
        
        # Combobox lọc loại món
        tk.Label(btns, text="Lọc theo loại:").grid(row=1, column=0, pady=5)
        loai_loc = tk.StringVar(value="Tất cả")
        cb_loc = ttk.Combobox(btns, textvariable=loai_loc, values=["Tất cả", "Đồ ăn", "Đồ uống"], state="readonly", width=12)
        cb_loc.grid(row=1, column=1, padx=5)
        
       
        
        button = tk.Button(btns, text="Hiển thị tùy chọn", command=cap_nhat_luoi)
        button.grid(row=1, column=2, padx=5)
        # Bảng dữ liệu
        tree = ttk.Treeview(tab_do_an, columns=("Mã Món", "Tên Món", "Giá", "Số Lượng"), show="headings", selectmode="browse")
        tree.heading("Mã Món", text="Mã Món")
        tree.heading("Tên Món", text="Tên Món")
        tree.heading("Giá", text="Giá")
        tree.heading("Số Lượng", text="Số Lượng")
        
        tree.column("Mã Món", width=100)
        tree.column("Tên Món", width=200)
        tree.column("Giá", width=100)
        tree.column("Số Lượng", width=100)
        tree.bind("<<TreeviewSelect>>", chon_dong)
        tree.pack(fill='x', padx=20, pady=20)
        
        frame_tk_da = tk.Frame(tab_do_an)
        frame_tk_da.pack(fill='x', padx=20, pady=(0, 10), anchor='e')

        lbl_tk_da = tk.Label(frame_tk_da, text="Tổng món: 0", anchor='e')
        lbl_tk_da.pack(anchor='e')
        cap_nhat_luoi()

    # Gọi hàm để vẽ giao diện chức năng trong tab_chuc_nang
    hien_thi_chuc_nang()
    hien_thi_yeu_cau()
    hien_thi_do_an()
    tab_chuc_nang.mainloop()
    
mo_dang_nhap()
