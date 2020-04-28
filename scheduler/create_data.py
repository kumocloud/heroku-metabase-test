from datetime import date
from repository.prediction_result_repository import prediction_result_repository
from model.prediction_result import PredictionResult

if __name__ == '__main__':
    prediction_result_repository.create_table()
    prediction_results = [
        PredictionResult(date(2020, 4, 25), 'v1', 32, 18, 2680, 24, 3290, 4, 1650, 6, 1530, 15, 2070, 0, 0, 6, 2530),
        PredictionResult(date(2020, 4, 26), 'v1', 174, 84, 14610, 120, 15450, 33, 12410, 48, 12890, 85, 14520, 16, 19810, 36, 13930),
        PredictionResult(date(2020, 4, 27), 'v1', 173, 95, 14160, 115, 15020, 40, 16110, 48, 13810, 82, 15220, 12, 8710, 28, 10330),
        PredictionResult(date(2020, 4, 28), 'v1', 171, 107, 19960, 132, 17350, 41, 18170, 50, 14960, 85, 14170, 13, 12160, 31, 13780)
    ]
    prediction_result_repository.insert(prediction_results)
    print('completed!')
