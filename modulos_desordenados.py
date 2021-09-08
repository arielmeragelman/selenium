from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



def definir_navegador():
    from webdriver_manager.chrome import ChromeDriverManager  #te permite mantener tu driver actualizado y sincronizado con tu version de chrome
    
    

    # ESTAS OPCIONES ME QUEDARON CARGADAS PORQUE MI SOFT DESCARGABA ARCHIVOS EN UNA UBICACION EN PARTICULAR
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
    "download.default_directory": r'C:\Users\', 
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    })
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)  # SETEAS EL DRIVER, LAS OPCIONES SE PUEDEN AMPLIAR O QUITAR, BASICAMENTE DEFINEN EL COMPORTAMIENTO DE CHROME, TAMBIEN PODES DEFINIR EL ZOOM INICIAL O EL TAMAÑO DE LA VENTANA
    
    return driver


def buscar_elemento(driver,delay,xpath_origen):
    '''DEVUELVE EL TEXTO QUE ENCUENTRA EN DETERMINADO XPATH QUE PASAMOS COMO ARGUMENTO, SE DEBE PASAR COMO ARGUMENTO EL DRIVER , UN TIEMPO DE DELAY, Y EL XPATH  '''    
    xpath= xpath_origen
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,xpath)))
        elemento_xpath = driver.find_element_by_xpath(xpath)
        texto_elemento_xpath=elemento_xpath.text
    except:                        #SI LUEGO DEL DELAY HACE TIMEOUT EN VEZ DE TIRAR ERROR ASIGNA COMO SALIDA UN STRING NULO  
        texto_elemento_xpath=""
        pass    
    return texto_elemento_xpath



def abrir_pagina(driver,web):    
''' REALIZA EL INTENTO DE ABRIR LA PAGINA, EN CASO DE QUE LA MISMA NO SE CARGUE POR EL MOTIVO QUE SEA DEVUELVE EL CODIGO DE ERROR  '''
    try:
        driver.get(web)
        estado_pagina="1"
    except:
        print("PAGINA NO ENCONTRADA - ERROR EN SISTEMA")
        estado_pagina="0"
        return estado_pagina
    return estado_pagina

def ingresar_nota(driver,delay,web,links_url,xpath_nota):
    texto_nota=[]
    for i in range(0,len(links_url)):
        estado_pagina=abrir_pagina(driver,links_url[i])
        if estado_pagina == "0":
            pass
        else:
            texto_nota.append(buscar_elemento(driver,delay,xpath_nota))
    return texto_nota
    

#EJEMPLO DE USO DE UN CLICK DE UN ELEMENTO, ESPERAMOS QUE EL DRIVER DETERMINE QUE SE PUEDE CLICKEAR, LUEGO llamamos la funcion retry para clickear, se puede obviar el primer webdriver igualmente
	        desplegar_mas = '/html/body/form/div[4]/div[4]div/div[1]/div/div/div/filter-form/div/div[2]/div/div/div/div/div/div/i'
			WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH,desplegar_mas)))
	        retryingFindClick_xpath(driver,desplegar_mas)
	
	        var_buscar= '/html/body/form/div[4]/div/div/div[1]/div/div/div/filter-form/div/div[2]/div/div/div/div[1]/div[1]/select/option[5]'
			WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH,var_buscar)))
	        select_ = driver.find_element_by_xpath(var_buscar)
	        select_.click()
	        texto_proveedor.send_keys(rs)
	 
	def click_link_texto(driver,titulo):
		'''toma el driver y el texto que tiene asociado el link y lo ejecuta, no esta aun cargado con try y except'''
		pagina_link = driver.find_element_by_link_text(titulo)
		pagina_link.click()
		return "1"
	
	    
	def retryingFindClick_id(driver,BY):
		'''TOMA COMO ARGUMENTO EL DRIVER Y EL ID DEL ELEMENTO A BUSCAR E INTENTA HACER CLICK, EN CASO DE FALLO ESPERA Y VUELVE A INTENTAR HASTA 3 VECES'''
	        result = False
	        attempts =0
	        while(result == False and attempts < 4) :
	            try :
	                time.sleep(3)
	                print("ESTOY EN ID CON BY:"+str(BY))
	                print(result)
	                boton_temporal=driver.find_element_by_id(BY)
	                driver.execute_script("arguments[0].click();", boton_temporal)
                    
	                
	                result = True
	                return result
	                
	            except :
	                print("NO ENCUENTRA VUELVE A PROBAR - "+str(attempts))
	                attempts= attempts +1
	        
	        return result
	
	    
	    
	def retryingFindClick_name(driver,BY) :
	    '''TOMA COMO ARGUMENTO EL DRIVER Y EL NAME DEL ELEMENTO A BUSCAR E INTENTA HACER CLICK, EN CASO DE FALLO ESPERA Y VUELVE A INTENTAR HASTA 3 VECES'''
			result = False
	        attempts =0
	        while(result == False and attempts <4) :
	            try :
	                print("ESTOY EN ID NAME BY:"+str(BY))
	                print(result,str(attempts))
                    
	
	                
	                
	                boton_temporal=driver.find_element_by_name(BY)
	                driver.execute_script("arguments[0].click();", boton_temporal)
	                result = True
	                return result
	                break
	            except :
	                print("NO ENCUENTRA VUELVE A PROBAR")
	                attempts= attempts +1
	        
	        return result
	
	
	
	def retryingFindClick_xpath(driver,BY) :
	    '''TOMA COMO ARGUMENTO EL DRIVER Y EL XPATH DEL ELEMENTO A BUSCAR E INTENTA HACER CLICK, EN CASO DE FALLO ESPERA Y VUELVE A INTENTAR HASTA 3 VECES'''
		    result = False
	        attempts =0
	        while(result == False or attempts > 3) :
	            try :
	                print("ESTOY EN XPATH CON BY:"+str(BY))
	                print(result)
	                
	                boton_temporal=driver.find_element_by_xpath(BY)
	                driver.execute_script("arguments[0].click();", boton_temporal)
	
	                
	                result = True
	                return result
	                break
	            except :
	                print("NO ENCUENTRA VUELVE A PROBAR")
	                print("NO ENCUENTRA VUELVE A PROBAR"+str(attempts))
	                attempts= attempts +1
	        
	        return result
