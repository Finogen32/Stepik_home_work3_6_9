def test_button_name_for_different_languages(browser):
    button=browser.find_element_by_css_selector('button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button=="Добавить в корзину" or "Añadir al carrito" or "Ajouter au panier", "Ошибка названия кнопки"