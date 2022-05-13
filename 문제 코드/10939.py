import base64
def base32_decoding(s): 
    str_bytes = s.encode('utf-8') 
    str_base32 = base64.b32decode(str_bytes) 
    base32_str = str_base32.decode('utf-8') 
    return base32_str
print(base32_decoding(input()))