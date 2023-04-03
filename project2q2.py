# Vera Mensah Aborah
# 10958719
# BMEN
import PySimpleGUI as sg
import qrcode as qrcode_lib
import os

def generate_qrcode(text):
    qrcode = qrcode_lib.QRCode(version=1, box_size=10, border=4)
    qrcode.add_data(text)
    qrcode.make(fit=True)
    qrcode_img = qrcode.make_image(fill_color="black", back_color="blue")
    return qrcode_img

def main():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Enter text to generate QR Code: ")],
        [sg.InputText(key="text_input")],
        [sg.Button("Generate"), sg.Exit()],
        [sg.Image(key="qrcode_output")]
    ]

    window = sg.Window("QR Code Generator", layout)

    while True:
        event, values = window.read()
        if event == "Generate":
            text = values["text_input"]
            try:
                qrcode_img = generate_qrcode(text)
                qrcode_filename = "qrcode.png"
                qrcode_img.save(qrcode_filename)
                window["qrcode_output"].update(filename=qrcode_filename)
                os.remove(qrcode_filename)
            except qrcode_lib.exceptions.DataOverflowError:
                sg.popup_error("Text too long to generate QR code.")
            except Exception as e:
                sg.popup_error(f"Error generating QR code: {e}")
        elif event == sg.WIN_CLOSED or event == "Exit":
            break

    window.close()

if __name__ == "__main__":
    main()
