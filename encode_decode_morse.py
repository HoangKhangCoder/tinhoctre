# Từ điển Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Đảo ngược từ điển để giải mã
REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """Chuyển đổi văn bản thành mã Morse"""
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(' ')  # Giữ nguyên ký tự không xác định
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    """Chuyển đổi mã Morse thành văn bản"""
    text = []
    for code in morse_code.split(' '):
        if code in REVERSE_MORSE_DICT:
            text.append(REVERSE_MORSE_DICT[code])
        elif code == '':
            text.append(' ')  # Xử lý nhiều khoảng trắng
        else:
            text.append('?')  # Ký tự Morse không xác định
    return ''.join(text)

# Giao diện chương trình
def main():
    print("CHƯƠNG TRÌNH MÃ HÓA/GIẢI MÃ MORSE")
    print("1. Mã hóa văn bản thành Morse")
    print("2. Giải mã Morse thành văn bản")
    
    choice = input("Chọn chức năng (1/2): ")
    
    if choice == '1':
        text = input("Nhập văn bản cần mã hóa: ")
        result = text_to_morse(text)
        print("Mã Morse:", result)
    elif choice == '2':
        morse = input("Nhập mã Morse cần giải mã (các ký tự cách nhau bằng khoảng trắng): ")
        result = morse_to_text(morse)
        print("Văn bản giải mã:", result)
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()