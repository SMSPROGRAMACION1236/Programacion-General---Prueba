from src.model.languagamodel import LanguageModel


def test_get_language_not_none():
  languages = LanguageModel.get_language()
  assert languages != None # Esperamos que sea diferente a none
def test_get_language_has_elements():
  languages = LanguageModel.get_language()
  assert len(languages) >0 # Esperamos que la longitud de languages sea mayor que cero, es decir si es mayor que cero, es por que hay elementos
def test_get_language_check_elements_length():
  languages = LanguageModel.get_language()
  for language in languages:
    assert len(language) >0 # esperamos que la longitud de cada lenguaje sea mayor que 0