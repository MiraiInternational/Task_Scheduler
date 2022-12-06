from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.banner import MDBanner
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import FloatLayout
import SQL

BTN_SIZE = (.14, .1)


class New_Parameter(MDApp):

    def build(self):
        screen = FloatLayout()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Orange"
        screen.add_widget(FitImage(source='pic\\1618529499_62-funart_pro-p-oboi-fon-material-dizain-62.png'))
        pk_list = [el[0] for el in SQL.query(SQL.my_cursor, 'SELECT Type_ID from type_of_parameter')]
        def has_numbers(inputString):
            return any(char.isdigit() for char in inputString)

        def validate():

            But2.disabled = Field1.error

        def error_1(instance, value):
            Field1.error = False
            if Field1.text != "":
                try:
                    int(Field1.text)
                    if int(Field1.text) not in pk_list:
                        Field1.helper_text = 'Этот ID не используется'
                        Field1.error = True
                except ValueError:
                    Field1.error = True
                    Field1.helper_text = 'ID должен быть INT'
            else:
                Field1.error = True
            validate()


        Field1 = MDTextField(
            hint_text="Type_ID",
            pos_hint={"x": 0.05, "y": 0.7},
            size_hint={0.6, 0.05},
            multiline=False,
            helper_text_mode='on_error',
            max_text_length=64,
        )
        Field1.bind(focus=error_1)


        def new(instance):
            SQL.query(SQL.my_cursor, f'DELETE from type_of_parameter WHERE Type_ID = {Field1.text}')
            SQL.mydb.commit()
            MDApp.get_running_app().stop()


        But2 = MDRaisedButton (
            text='Удалить',
            size_hint=BTN_SIZE,
            pos_hint={"x": 0.81, "y": 0.05},
            on_release=new,
            disabled=True
        )

        screen.add_widget(Field1)
        screen.add_widget(But2)
        return screen


if __name__ == "__main__":
    New_Parameter().run()