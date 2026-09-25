import customtkinter as ctk

root = ctk.CTk()

root.geometry(f"1600x530+145+800")
root.resizable(False, False)

root.attributes("-alpha", 0.85)

import pyautogui


import pyautogui


def press_key(key_name):
    # Словарь сопоставления текста с кнопки с именами клавиш в pyautogui
    key_map = {
        "esc": "escape",
        "backspace": "backspace",
        "caps lock": "capslock",
        "enter": "enter",
        "ctrl": "ctrl",
        "win": "win",
        "alt": "alt",
        "space": "space",
        "shift": "shift",
        "tab": "tab",
        "super": "win",
        "''": "'",  # Для твоей кнопки с кавычками
    }

    # Если передали пустую строку (пробел), ставим 'space'
    clean_key = key_name.lower() if key_name else "space"

    # Получаем точное название клавиши для pyautogui
    target_key = key_map.get(clean_key, clean_key)

    try:
        pyautogui.press(target_key)
        print(f"Нажата клавиша: {target_key}")
    except Exception as e:
        print(f"Ошибка нажатия {target_key}: {e}")
    return

Button = ctk.CTkButton(root, text="Esc", font=("Arial",60, "bold"), width=80, height=80, fg_color="#0c34ab", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("escape"))
Button.place(x= 20, y= 20)

Button1 = ctk.CTkButton(root, text="1", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("1"))
Button1.place(x= 160, y= 20)

Button2 = ctk.CTkButton(root, text="2", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("2"))
Button2.place(x= 260, y= 20)

Button3 = ctk.CTkButton(root, text="3", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("3"))
Button3.place(x= 360, y= 20)

Button4 = ctk.CTkButton(root, text="4", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("4"))
Button4.place(x= 460, y= 20)

Button5 = ctk.CTkButton(root, text="5", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("5"))
Button5.place(x= 560, y= 20)

Button6 = ctk.CTkButton(root, text="6", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("6"))
Button6.place(x= 660, y= 20)

Button7 = ctk.CTkButton(root, text="7", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("7"))
Button7.place(x= 760, y= 20)

Button8 = ctk.CTkButton(root, text="8", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("8"))
Button8.place(x= 860, y= 20)

Button9 = ctk.CTkButton(root, text="9", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("9"))
Button9.place(x= 960, y= 20)

Button0 = ctk.CTkButton(root, text="0", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("0"))
Button0.place(x= 1060, y= 20)

Button10 = ctk.CTkButton(root, text="-", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("-"))
Button10.place(x= 1160, y= 20)

Button11 = ctk.CTkButton(root, text="=", font=("Arial",60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("="))
Button11.place(x= 1260, y= 20)

Button12 = ctk.CTkButton(root, text="Backspace", font=("Arial", 40, "bold"), width=60, height=80, fg_color="#0c34ab", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("backspace"))
Button12.place(x= 1360, y= 20)

Button13 = ctk.CTkButton(root, text="Tab", font=("Arial", 40, "bold"), width=150, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("tab"))
Button13.place(x= 20, y= 120)

Button14 = ctk.CTkButton(root, text="Q", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("Q"))
Button14.place(x= 190, y= 120)

Button15 = ctk.CTkButton(root, text="W", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("W"))
Button15.place(x= 290, y= 120)

Button16 = ctk.CTkButton(root, text="E", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("E"))
Button16.place(x= 390, y= 120)

Button17 = ctk.CTkButton(root, text="R", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("R"))
Button17.place(x= 490, y= 120)

Button18 = ctk.CTkButton(root, text="T", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("T"))
Button18.place(x= 590, y= 120)

Button19 = ctk.CTkButton(root, text="Y", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("Y"))
Button19.place(x= 690, y= 120)

Button20 = ctk.CTkButton(root, text="U", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("U"))
Button20.place(x= 790, y= 120)

Button21 = ctk.CTkButton(root, text="I", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("I"))
Button21.place(x= 890, y= 120)

Button22 = ctk.CTkButton(root, text="O", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("O"))
Button22.place(x= 990, y= 120)

Button23 = ctk.CTkButton(root, text="P", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("P"))
Button23.place(x= 1090, y= 120)

Button24 = ctk.CTkButton(root, text="[", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("["))
Button24.place(x= 1190, y= 120)

Button25 = ctk.CTkButton(root, text="]", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("]"))
Button25.place(x= 1290, y= 120)

Button25 = ctk.CTkButton(root, text="|", font=("Arial", 60, "bold"), width=190, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("|"))
Button25.place(x= 1390, y= 120)

Button26 = ctk.CTkButton(root, text="Caps Lock", font=("Arial", 40, "bold"), width=190, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("caps lock"))
Button26.place(x= 20, y= 220)

Button27 = ctk.CTkButton(root, text="A", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("caps lock"))
Button27.place(x= 250, y= 220)

Button28 = ctk.CTkButton(root, text="S", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("A"))
Button28.place(x= 350, y= 220)

Button29 = ctk.CTkButton(root, text="D", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("S"))
Button29.place(x= 450, y= 220)

Button30 = ctk.CTkButton(root, text="F", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("D"))
Button30.place(x= 550, y= 220)

Button31 = ctk.CTkButton(root, text="G", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("F"))
Button31.place(x= 650, y= 220)

Button32 = ctk.CTkButton(root, text="H", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("G"))
Button32.place(x= 750, y= 220)

Button33 = ctk.CTkButton(root, text="J", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("H"))
Button33.place(x= 850, y= 220)

Button34 = ctk.CTkButton(root, text="K", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("J"))
Button34.place(x= 950, y= 220)

Button35 = ctk.CTkButton(root, text="L", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("K"))
Button35.place(x= 1050, y= 220)

Button36 = ctk.CTkButton(root, text=":", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("L"))
Button36.place(x= 1150, y= 220)

Button37 = ctk.CTkButton(root, text="''", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key(":"))
Button37.place(x= 1250, y= 220)

Button38 = ctk.CTkButton(root, text="Enter", font=("Arial", 60, "bold"), width=230, height=80, fg_color="#0c34ab", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("''"))
Button38.place(x= 1350, y= 220)

Button39 = ctk.CTkButton(root, text="Shift", font=("Arial", 60, "bold"), width=270, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("enter"))
Button39.place(x= 20, y= 320)

Button40 = ctk.CTkButton(root, text="Z", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("shift"))
Button40.place(x= 310, y= 320)

Button41 = ctk.CTkButton(root, text="X", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("Z"))
Button41.place(x= 410, y= 320)

Button42 = ctk.CTkButton(root, text="C", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("X"))
Button42.place(x= 510, y= 320)

Button43 = ctk.CTkButton(root, text="V", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("C"))
Button43.place(x= 610, y= 320)

Button44 = ctk.CTkButton(root, text="B", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("V"))
Button44.place(x= 710, y= 320)

Button45 = ctk.CTkButton(root, text="N", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("B"))
Button45.place(x= 810, y= 320)

Button45 = ctk.CTkButton(root, text="M", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("N"))
Button45.place(x= 910, y= 320)

Button46 = ctk.CTkButton(root, text="<", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("M"))
Button46.place(x= 1010, y= 320)

Button47 = ctk.CTkButton(root, text=">", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("<"))
Button47.place(x= 1110, y= 320)

Button48 = ctk.CTkButton(root, text="?", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#047016", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key(">"))
Button48.place(x= 1210, y= 320)

Button49 = ctk.CTkButton(root, text="Shift", font=("Arial", 60, "bold"), width=270, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("shift"))
Button49.place(x= 1310, y= 320)

Button50 = ctk.CTkButton(root, text="Ctrl", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("ctrl"))
Button50.place(x= 20, y= 420)

Button51 = ctk.CTkButton(root, text="Win", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("win"))
Button51.place(x= 160, y= 420)

Button52 = ctk.CTkButton(root, text="Alt", font=("Arial", 60, "bold"), width=90, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("alt"))
Button52.place(x= 310, y= 420)

Button53 = ctk.CTkButton(root, text="", font=("Arial", 60, "bold"), width=620, height=80, fg_color="#0c34ab", text_color="#0c34ab",hover_color= "#00cc66", command= lambda: press_key("space"))
Button53.place(x= 420, y= 420)

Button54 = ctk.CTkButton(root, text="Alt", font=("Arial", 60, "bold"), width=90, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("alt"))
Button54.place(x= 1060, y= 420)

Button55 = ctk.CTkButton(root, text="Super", font=("Arial", 40, "bold"), width=90, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("|"))
Button55.place(x= 1175, y= 420)

Button50 = ctk.CTkButton(root, text="Ctrl", font=("Arial", 60, "bold"), width=80, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("ctrl"))
Button50.place(x= 1320, y= 420)

Button50 = ctk.CTkButton(root, text="Fn", font=("Arial", 60, "bold"), width=120, height=80, fg_color="#000000", text_color="#19254a",hover_color= "#00cc66", command= lambda: press_key("fn"))
Button50.place(x= 1460, y= 420)

root.title("Keyboard Presser")

root.mainloop()
