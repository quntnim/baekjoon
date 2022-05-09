import base64
def base16_Incoding(s): 
    str_bytes = s.encode('utf-8') 
    str_base64 = base64.b16encode(str_bytes) 
    base16_str = str_base64.decode('utf-8') 
    return base16_str
print(base16_Incoding(input()))