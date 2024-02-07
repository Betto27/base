from behave import given, when, then
from nose.tools import assert_equal
from browser import Browser

browser = Browser()

@given(u'que acesso o site')
def step_impl(context):


    browser.get('https://www.tapeçariamythos.com')


@when(u'clico no botão Contato')
def step_impl(context):
    browser.localizar("#menu-item-139")


@then(u'acesso a pagina Contato')
def step_impl(context):
    assert_equal(browser.localizador_text(".uagb-ifb-title"), 'Solicite um orçamento')
