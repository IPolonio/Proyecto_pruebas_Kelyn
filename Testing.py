from selenium import webdriver
driver = webdriver.Edge()
import os 
import time 
from selenium.webdriver.common.by import By
from jinja2 import Environment, FileSystemLoader




if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

def getting_into_workspace():
     time.sleep(5)
     param_field = driver.find_element(By.ID,"courseLabel")
     param_field.click()



def login_try():
     
     username_field = driver.find_element(By.ID, "login-email")
     username_field.send_keys("polonio.isaac@gmail.com")

     passwordfield = driver.find_element(By.ID,"password")
     passwordfield.send_keys("Isaacalexander27@")
     time.sleep(5)
     driver.save_screenshot("screenshots/Captura_login.Png" )
        
     boton_sign_in = driver.find_element(By.CLASS_NAME,"btn-login")
     boton_sign_in.click();


def checking_course():
     driver.get("https://app.aluracursos.com/courses/mine")
     driver.save_screenshot("screenshots/courses.Png" )
driver.implicitly_wait(10)
        

def entering_course():
     driver.get("https://app.aluracursos.com/course/git-github-control-version")
     driver.save_screenshot("screenshots/course.png")
     driver.implicitly_wait(10)


def resume_course():
     driver.get("https://app.aluracursos.com/certificate/polonio-isaac/git-github-control-version")
     driver.save_screenshot("screenshots/gitcourse.png")
     driver.implicitly_wait(10)

driver.get("https://app.aluracursos.com/loginForm?logout")

login_try();

driver.implicitly_wait(15)


driver.get("https://app.aluracursos.com/dashboard")

getting_into_workspace()

driver.implicitly_wait(10)

driver.save_screenshot("screenshots/Captura_workspace.Png" )


driver.implicitly_wait(10)

checking_course()

driver.implicitly_wait(10)

entering_course()

driver.implicitly_wait(10)

resume_course()

driver.implicitly_wait(10)

driver.quit()


# Create the 'reports' folder if it doesn't exist
if not os.path.exists('reports'):
    os.makedirs('reports')

# Define the path for the report template
template_path = 'reports/report_template.html'

# Cargar la plantilla HTML
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(template_path)

# Definir los datos para el informe
data = {
    'login_try': 'screenshots/Captura_login.Png',
    'getting_into_workspace': 'screenshots/Captura_workspace.Png',
    'checking_course': 'screenshots/courses.Png',
    'entering_course': 'screenshots/course.png',
    'resume_course': 'screenshots/gitcourse.png'
}

# Renderizar la plantilla con los datos
report = template.render(data=data)

# Guardar el informe en un archivo HTML dentro de la 'reports' folder
report_path = 'reports/report.html'
with open(report_path, 'w') as f:
    f.write(report)