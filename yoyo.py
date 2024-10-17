# Шаг-1: Установка необходимых библиотек
# pip install numpy scikit-learn

# Шаг-2: Импорт библиотек
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Данные из условия задачи
true_positive = 20  # Важные сообщения, правильно классифицированные
true_negative = 10  # Неважные сообщения, правильно классифицированные
false_positive = 2  # Неважные сообщения, неправильно классифицированные как важные
false_negative = 3  # Важные сообщения, неправильно классифицированные как неважные

# Всего сообщений
total_messages = true_positive + true_negative + false_positive + false_negative

# Шаг-7: Расчет метрик

# 1. Точность (Accuracy)
accuracy = (true_positive + true_negative) / total_messages

# 2. Точность Предсказания (Precision) для класса Важные
precision = true_positive / (true_positive + false_positive)

# 3. Полнота (Recall) для класса Важные
recall = true_positive / (true_positive + false_negative)

# 4. F1-Мера для класса Важные
f1 = 2 * (precision * recall) / (precision + recall)

# Шаг-8: Вывод результатов
print(f"Точность (Accuracy): {accuracy:.2f}")
print(f"Точность Предсказания (Precision): {precision:.2f}")
print(f"Полнота (Recall): {recall:.2f}")
print(f"F1-Мера: {f1:.2f}")
