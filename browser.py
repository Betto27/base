from selenium import webdriver

class Browser(object):
    # Inicia o browser chrome, mas pode ser feito com outros como Firefox, Safari e IE
    driver = webdriver.Chrome()
    # Define o tempo máximo para carregamento da página
    driver.set_page_load_timeout(30)
    # Maximiza a janela do browser ao ser iniciado
    driver.maximize_window()

    #fecha o navegador
    def browser_quit(self):
        self.driver.quit()

    #Limpa o browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()

    def get(self, url):
        self.driver.get(url)

    def localizar(self, elemento):
        self.driver.find_element_by_css_selector(elemento).click()

    def localizador_text(self, elemento):
        return self.driver.find_element_by_css_selector(elemento).text
