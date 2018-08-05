def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if part[0] == "0":
            return False
        try:
            int_part = int(part)
        except Exception:
            return False
        if int_part > 255 or int_part < 0:
            return False
    return True



print(is_valid_ip("192.168.01.1"))