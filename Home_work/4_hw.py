# Задача 1
class Rectangle:

    def __init__(self, width:int, height:int):
        self.width:int = width
        self.height:int = height


    def square(self) -> int:
        return self.width * self.height

    def perimetr(self) -> int:
        return (self.width + self.height) * 2

S1 = Rectangle(3,2)
S2 = Rectangle(5,3)
S3 = Rectangle(4,6)

print('Задача 1')
print(S1.square())
print(S2.square())
print(S3.square())

print(S1.perimetr())
print(S2.perimetr())
print(S3.perimetr())


# Задача 2
class Math:

    def __init__(self, a:int, b:int):
        self.a:int = a
        self.b:int = b

    def addition(self) -> int:
        return self.a + self.b

    def multiplication(self) -> int:
        return self.a * self.b

    def division(self) -> float:
        if self.b == 0:
            return 0
        else:
            return self.a / self.b

    def subtraction(self) -> int:
        return self.a - self.b

M1 = Math(4, 2)

print('Задача 2')
print(M1.addition())
print(M1.multiplication())
print(M1.division())
print(M1.subtraction())

# Задача 3
class Button:

    def __init__(self, label:str):
        self.label:str = label
        self.type:str = "Кнопка"
        self.location:str = ""

    def click(self) -> str:
        return 'Клик по кнопке ' + self.label

text_box_btn = Button('Text Box')
check_box_btn = Button('Check Box')
radio_button_btn = Button('Radio Button')
web_tables_btn = Button('Web Tables')
buttons_btn = Button('Buttons')
links_btn = Button('links')
broken_Links_images_btn = Button('Broken Links - Images')
upload_and_download_btn = Button('Upload And Download')
dynamic_properties = Button('Dynamic Properties')

print('Задача 3')
print(text_box_btn.label)
print(check_box_btn.label)
print(radio_button_btn.label)
print(web_tables_btn.label)
print(buttons_btn.label)
print(links_btn.label)
print(broken_Links_images_btn.label)
print(upload_and_download_btn.label)
print(dynamic_properties.label)

print(text_box_btn.click())
print(check_box_btn.click())
print(radio_button_btn.click())
print(web_tables_btn.click())
print(buttons_btn.click())
print(links_btn.click())
print(broken_Links_images_btn.click())
print(upload_and_download_btn.click())
print(dynamic_properties.click())