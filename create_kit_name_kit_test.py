# Набор тестов для проверки параметра "name"
# при создании набора пользователя в Яндекс.Прилавок
# с помощью API Яндекс.Прилавок
import data
import sender_stand_request

def get_kit_body(name): # Функция меняет значения в параметре name
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name): # Функция для позитивной проверки
    kit_body = get_kit_body(name)
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Успешное создание набора. Параметр name состоит из 511 символов
def test_create_kit_511_symbol_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def negative_assert_no_name(kit_body): # Функция для негативной проверки
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400

# Тест 3. Ошибка. Параметр name состоит из пустой строки
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_no_name(kit_body)

def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400

# Тест 4. Ошибка. Количество символов больше допустимого. Параметр name состоит из 512 символов
def test_create_kit_512_symbol_in_name_get_error_response():
    negative_assert_symbol("Abcd" * 128)

# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_kit_eng_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_kit_rus_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора. Параметр name состоит из строки спецсимволов
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Тест 8. Успешное создание набора. Параметр name состоит из строки с пробелом
def test_create_kit_space_key_symbol_in_name_get_success_response():
    positive_assert("Человек и КО")

# Тест 9. Успешное создание набора. Параметр name состоит из строки с цифрами
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Ошибка. В запросе нет параметра name
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

# Тест 11. Ошибка. Передан другой тип параметра. Тип параметра name: число
def test_create_kit_type_number_in_name_get_error_response():
    negative_assert_symbol(123)