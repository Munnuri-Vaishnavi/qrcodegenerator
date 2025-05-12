import qrcode
#1display text
qr=qrcode.make("hello iam vaishu!!")
qr.save("text_qr.png")
#2open a website (URL)
qr=qrcode.make("https://www.youtube.com")
qr.save("website_qr.png")
#3send an email
data="mailto:vanivaishu49@gmail.com?subject=hi &body =Hello"
qr=qrcode.make(data)
qr.save("email_qr.png")
#4send a text(sms)
sms_data="SMSTO:6303814387:Hello iam vaishu"
qr=qrcode.make(sms_data)
qr.save("sms_qr.png")
#5Make a call
call_data="tel:6303814387"
qr=qrcode.make(call_data)
qr.save("call_qr.png")
#6Trigger app action(eg.whatsapp)
whatsapp_data="https://wa.me/9032209351?text=oh ok"
qr=qrcode.make(whatsapp_data)
qr.save("Whatsapp_qr.png")
#7share location(not working)
location_data="https://www.google.com/maps/search/?api=1&query=12.9716,77.5946"#benguloor
qr=qrcode.make("location_data")
qr.save("location_qr.png")
#we can connect to wifi

