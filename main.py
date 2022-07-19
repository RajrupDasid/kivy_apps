from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pandas as pd
# popup function
class PopupWindow(Widget):
    def btn(self):
        popFun()
# GUI pop up window
class P(FloatLayout):
    pass
#displaying content
def popFun():
    show=P()
    window=Popup(title="window",content=show, size_hint=(None,None),size=(300,300))
    window.open()

#validation class with user info
class loginWindow(Screen):
    email=ObjectProperty(None)
    passw=ObjectProperty(None)
    def validate(self):

        # email validation
        if self.email.text not in users["Email"].unique():
            popFun()
        else:
            # current window switch  for dispalying validation results
            sm.current= 'logdata'

            # reset Text input
            self.email.text = ""
            self.passw.text= ""
# accept user registration
class signupWindow(Screen):
    name2=ObjectProperty(None)
    email=ObjectProperty(None)
    passw=ObjectProperty(None)
    def signupbtn(self):

        # creating dataframe of the info
        user = pd.DataFrame ([[self.name2.text,self.email.text,self.pwd.text]], columns = ['Name','Email','Password'])

        if self.email.text !="":
            if self.email.text not in users['Email'].unique():
                #if the email not exists then append to csv file
                user.to_csv('login.csv',mode='a', header= False, index=False)
                sm.current='login'
                self.name2.text = ""
                self.email.text = ""
                self.passw.text = ""
        else:
            popFun()

#log data screen class
class logDataWindow(Screen):
    pass

# your application window manager
class windowManager(ScreenManager):
    pass

# important configuration part 
kv = Builder.load_file('login.kv')
sm = windowManager()
users = pd.read_csv('login.csv')

#main widget systems
sm.add_widget(loginWindow(name='login'))
sm.add_widget(signupWindow(name='signup'))
sm.add_widget(logDataWindow(name='logdata'))

#main class
class loginMain(App):
    def build(self):
        return sm

# diver code

if __name__=="__main__":
    loginMain().run()
