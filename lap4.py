def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 9000, 10500, 12000)
    if so_nuoc <= 10 and so_nuoc >=0:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc

def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"đường":0.04,"đậu":0.07}
    banh_thap_cam = {"đường":0.06,"đậu":0}
    banh_deo = {"đường":0.05,"đậu":0.2}
    nguyen_lieu = {}
    