import qrcode
from io import BytesIO
import base64


# Generate QR Code
 
def generateQR_Code(url: str, img_name: str = 'QRCode.png') -> any:
    code = qrcode.QRCode(
        version=1, 
        box_size=10,
        border=4
    )

    code.add_data(url)
    code.make(fit=True)

    img = code.make_image(fill_color='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    # qr_code = f"data:image/png;base64,{buffer.getvalue().decode()}"
    qr_code = f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"
    

    return qr_code