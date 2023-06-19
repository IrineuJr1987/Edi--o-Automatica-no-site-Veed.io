from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
import random
import os
import shutil
import datetime
from webdriver_manager.chrome import ChromeDriverManager

#prepara o codigo para abrir com o perfil default do chrome
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=C:\\Users\\Bill\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
actions = ActionChains(driver)

for i in range(100):
     #abre a pagina do veed
     driver.get("https://www.veed.io")


     #Clique no botão "Create project":
     time.sleep(10)
     create_project_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div[2]/button[1]')
     create_project_button.click()

     time.sleep(10)
     fechar = driver.find_element(By.XPATH, "//Button[@class='UploadModalStyled__CloseModalButton-sc-1u30yst-0 dsahLz']")
     fechar.click()

     driver.find_element(By.XPATH, "//*[@id='dropWrapper-upload']/div/div/nav/nav/a[2]").click()
     #Faça o upload do vídeo na pasta "D:\videos\Videos Natureza":
     file_input = driver.find_element(By.XPATH, "//input[@accept='video/mp4,video/quicktime,video/x-msvideo,video/webm,video/x-ms-wmv,video/x-matroska,video/avi,video/mpeg,video/3gpp,video/*,image/gif,.mkv,.3gp,.flv,.veedio,audio/mp4,audio/mpeg,.aac,.wav,.m4a,audio/*,.jpg,.jpeg,.png,.webp,.gif']")

     # Lê todos os arquivos do diretório
     dir_path = "E:\\Conteudo\\videos\\Motivacional\\videos Natureza\\"
     files = os.listdir(dir_path)

     # Seleciona um arquivo aleatório
     selected_file = random.choice(files)

     # Atribui o caminho completo para o arquivo selecionado à variável file_path
     file_path = os.path.join(dir_path, selected_file)
     file_input.send_keys(file_path)

     #navegar até settings
     settings = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/nav/nav/a[1]')
     # settings.click()

     time.sleep(2)


     #Adicione o áudio "Epic new world":
     audio_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/nav/nav/a[3]")
     audio_button.click()
     time.sleep(5)
     #audio_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@accept='audio/mp4,audio/mpeg,.aac,.wav,.m4a,audio/*']")))
     
     try:
          audio_input = driver.find_element(By.XPATH, "//input[@accept='audio/mp4,audio/mpeg,.aac,.wav,.m4a,audio/*']")
          time.sleep(5)
          file_path = "E:\\Conteudo\\videos\\Motivacionalnewworld.mp3"
          time.sleep(5)
          audio_input.send_keys(file_path)
     except:
               time.sleep(5)
               audio_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/nav/nav/a[3]")
               audio_button.click()
               time.sleep(3)
               #audio_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@accept='audio/mp4,audio/mpeg,.aac,.wav,.m4a,audio/*']")))
               audio_input = driver.find_element(By.XPATH, "//input[@accept='audio/mp4,audio/mpeg,.aac,.wav,.m4a,audio/*']")
               time.sleep(5)
               file_path = "E:\\Conteudo\\videos\\Motivacional\\musicas\\newworld.mp3"
               time.sleep(5)
               audio_input.send_keys(file_path)
     #audio_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Epic new world')]")))

     #Clique no botão "Subtitles":
     subtitles_button = driver.find_element(By.XPATH, "//html/body/div[1]/main/div[2]/div/div/nav/nav/a[4]")
     subtitles_button.click()

     #Clique no botão "Manual subtitles":
     manual_subtitles_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/button[1]")
     manual_subtitles_button.click()

     addsub_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/button")
     addsub_button.click()

     divsub = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div")
     divsub.click()

     # Lê todos os arquivos do diretório
     dir_path = "E:\\Conteudo\\videos\\Motivacional\\Frases"
     files = os.listdir(dir_path)

     # Seleciona um arquivo aleatório
     selected_file = random.choice(files)

     # Lê o conteúdo do arquivo
     with open(os.path.join(dir_path, selected_file), "r") as f:
          content = f.read()

     pyperclip.copy(content)
     actions.key_down(Keys.CONTROL)
     actions.send_keys("v")
     actions.key_up(Keys.CONTROL)
     actions.perform()
     time.sleep(3)

   
     #altera o tempo da legenda
     duration = driver.find_element(By.XPATH, "//input[@value='00:03.0']")
     duration.click()
     duration.send_keys(Keys.DELETE+Keys.DELETE+Keys.DELETE+Keys.DELETE+Keys.DELETE+Keys.DELETE+"09"+Keys.ENTER)

     time.sleep(3)

     #altera os estilo do legenda
     styles = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/header/div[2]/nav/div[3]")
     styles.click()
     time.sleep(2)
     styles2 = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[1]/button")
     styles2.click()
     time.sleep(2)
     styles2.click()
     time.sleep(2)
     styles3 = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div/div[15]")
     styles3.click()
     time.sleep(2)
     styles4 = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]")
     styles4.click()
     styles5 = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div[1]/div[2]/input")
     styles5.send_keys("60"+Keys.ENTER)


     #Altere o tamanho para TikTok:
     settings = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/nav/nav/a[1]')
     settings.click()
     size_dropdown = driver.find_element(By.XPATH,  "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[1]/div")
     size_dropdown.click()
     time.sleep(2)
     actions.send_keys("tiktok"+Keys.ENTER)
     actions.perform()
     time.sleep(2)
     settings.click()
     time.sleep(2)
     duration_dropdown = driver.find_element(By.XPATH, "//input[@class='TimeInput__StyledInput-sc-1gb4ot9-1 dgKDrV']")
     duration_dropdown.click()
     duration_dropdown.send_keys(Keys.CONTROL, "a")
     duration_dropdown.send_keys("10" + Keys.ENTER)

     #Clique no botão "Export":
     export_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/button")
     export_button.click()

     #Clique no botão "Export video":
     export_video_button = driver.find_element(By.XPATH, "//button[@class='sc-fEXmlR sc-bjfHbI ekszMa gnLOBs sharedStyles__StyledExportButton-sc-1cr1m3o-19 hKbiac']")
     export_video_button.click()
     time.sleep(120)
     #Clique no botão "download":
     download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div/button")
     download.click()
     download2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/button[1]")
     download2.click()

     time.sleep(20)

     # Muda o caminho do arquivo para a pasta "D:\\videos\\Frases ja usadas"
     used_dir_path = "E:\\Conteudo\\videos\\Motivacional\\Frases ja usadas"
     shutil.move(os.path.join(dir_path, selected_file), os.path.join(used_dir_path, selected_file))


     # Obtém a data de modificação de cada arquivo da pasta "downloads"
     files = os.listdir("C:\\Users\\Bill\\downloads")
     files_with_modification_time = [(f, os.stat("C:\\Users\\Bill\\downloads\\" + f).st_mtime) for f in files]

     # Ordena a lista pelo atributo st_mtime (data de modificação)
     files_with_modification_time.sort(key=lambda x: x[1], reverse=True)

     # Move o arquivo com a data de modificação mais recente para a pasta "D:\arquivos"
     if files_with_modification_time:
          file_name, _ = files_with_modification_time[0]
     
     # Gera o novo nome do arquivo com a data e hora atual
     current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
     new_file_name = f"{current_time}.mp4"
     
     # Move o arquivo para a pasta "D:\arquivos" com o novo nome
     shutil.move("C:\\Users\\Bill\\downloads\\" + file_name, f"E:\\Conteudo\\videos\\Motivacional\\Prontos para envio\\{new_file_name}")



