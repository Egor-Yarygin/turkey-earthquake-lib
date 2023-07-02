import matplotlib.pyplot as plt
import numpy as np
from turkey_eq import plot_map
import os
from datetime import datetime

# Тестирование базового случая
def test_plot_map():
    plot_times = ['2023-07-01T00:00:00', '2023-07-02T00:00:00']
    data = {
        'ROTI': {
            '2023-07-01T00:00:00': np.array([(0, 0, 1.5), (1, 1, 2.5)]),
            '2023-07-02T00:00:00': np.array([(0, 0, 2.0), (1, 1, 3.0)])
        },
        'TEC': {
            '2023-07-01T00:00:00': np.array([(0, 0, 10.0), (1, 1, 15.0)]),
            '2023-07-02T00:00:00': np.array([(0, 0, 12.0), (1, 1, 18.0)])
        }
    }
    type_d = ['ROTI', 'TEC']
    
    # Проверка, что функция не вызывает ошибку
    try:
        plot_map(plot_times, data, type_d)
    except Exception as e:
        assert False, f"Функция вызвала ошибку: {e}"
    
    # Проверка, что график успешно создается
    assert plt.gcf() is not None, "График не создан"
    
    # Дополнительные проверки, например, можно проверить количество подграфиков и их заголовки
    
    # Закрытие графика
    plt.close()



# Тестирование базового случая
def test_retrieve_data():
    file_path = "test_data.h5"
    type_d = "ROTI"
    times = [
        datetime(2023, 7, 1, 0, 0, 0),
        datetime(2023, 7, 2, 0, 0, 0)
    ]
    # Создаем тестовый файл
    with h5py.File(file_path, 'w') as f_out:
        data = {
            "2023-07-01T00:00:00": np.array([(0, 0, 1.5), (1, 1, 2.5)]),
            "2023-07-02T00:00:00": np.array([(0, 0, 2.0), (1, 1, 3.0)])
        }
        for str_time, arr in data.items():
            f_out['data'][str_time] = arr
    
    # Проверка, что функция не вызывает ошибку
    try:
        retrieved_data = retrieve_data(file_path, type_d, times)
    except Exception as e:
        assert False, f"Функция вызвала ошибку: {e}"
    
    # Проверка, что данные успешно получены
    assert len(retrieved_data) == 2, "Неверное количество временных отметок"
    assert all(time in retrieved_data for time in times), "Не все временные отметки присутствуют в данных"
    
    # Проверка, что данные правильно считались из файла (можно добавить дополнительные проверки данных)
    assert np.array_equal(retrieved_data[datetime(2023, 7, 1, 0, 0, 0)], np.array([(0, 0, 1.5), (1, 1, 2.5)])), "Неверные данные для временной отметки 2023-07-01T00:00:00"
    assert np.array_equal(retrieved_data[datetime(2023, 7, 2, 0, 0, 0)], np.array([(0, 0, 2.0), (1, 1, 3.0)])), "Неверные данные для временной отметки 2023-07-02T00:00:00"
    
    # Удаление тестового файла
    os.remove(file_path)
