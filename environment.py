from browser import Browser
from time import sleep

# Executa o comando antes de todos os testes iniciarem
def before_all(context):
    context.browser = Browser()

# Executa o comando depois de todos os testes terminarem
def after_all(context):
    context.browser.browser_quit()

# Executa os comandos entre cada cenário
def after_scenario(context, scenario):
    context.browser.browser_clear()