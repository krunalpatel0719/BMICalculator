import pytest
from Main import bmi_class
def test_underweight_category():
    bmi = bmi_class()
    assert bmi.bmi_category(16) == "underweight"

def test_normalweight_category():
    bmi = bmi_class()
    assert bmi.bmi_category(20) == "of normal weight"
def test_overweight_category():
    bmi = bmi_class()
    assert bmi.bmi_category(27) == "overweight"
def test_obese_category():
    bmi = bmi_class()
    assert bmi.bmi_category(35) == "obese"
def test_invalid_weight(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 7\n' if 'height' in prompt else '0\n')
    bmi = bmi_class()
   
    with pytest.raises(ValueError) as exc_info:
        bmi.calculate_bmi()
    assert str(exc_info.value) == "Weight must be non-zero"
def test_invalid_feet(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '0 7\n' if 'height' in prompt else '150\n')
    bmi = bmi_class()
   
    with pytest.raises(ValueError) as exc_info:
        bmi.calculate_bmi()
    assert str(exc_info.value) == "Height must be non-zero"
def test_invalid_inches(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 12\n' if 'height' in prompt else '150\n')
    bmi = bmi_class()
   
    with pytest.raises(ValueError) as exc_info:
        bmi.calculate_bmi()
    assert str(exc_info.value) == "Height in inches must be less than 12"
def test_invalid_positive_height(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '-5 -7\n' if 'height' in prompt else '150\n')
    bmi = bmi_class()
   
    with pytest.raises(ValueError) as exc_info:
        bmi.calculate_bmi()
    assert str(exc_info.value) == "Height must be positive"
def test_invalid_positive_weight(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 7\n' if 'height' in prompt else '-150\n')
    bmi = bmi_class()
   
    with pytest.raises(ValueError) as exc_info:
        bmi.calculate_bmi()
    assert str(exc_info.value) == "Weight must be positive"
def test_calculate_bmi(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 7\n' if 'height' in prompt else '150\n')
    bmi = bmi_class()
    assert bmi.calculate_bmi() == "Your BMI is: 24.06 and you are of normal weight"
   
    # Test cases using EPC technique
def test_bmi_below_normal_lower(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 6\n' if 'height' in prompt else '111.28\n')
    bmi = bmi_class()
    assert bmi.calculate_bmi() == "Your BMI is: 18.39 and you are underweight"

def test_bmi_below_normal_upper(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 6\n' if 'height' in prompt else '111.29\n')
    bmi = bmi_class()
    assert bmi.calculate_bmi() == "Your BMI is: 18.40 and you are underweight"

# def test_bmi_above_normal_lower(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda prompt: '5 7\n' if 'height' in prompt else '130\n')
#     bmi = bmi_class()
#     assert bmi.calculate_bmi() == "Your BMI is: 25.24 and you are of normal weight"

# def test_bmi_above_normal_upper(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda prompt: '5 7\n' if 'height' in prompt else '250\n')
#     bmi = bmi_class()
#     assert bmi.calculate_bmi() == "Your BMI is: 24.90 and you are of normal weight"