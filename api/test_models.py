from model import *
from model.appraiser import Appraiser
from model.model import Model

charger = Charger()
model = Model()

url_data = "./MachineLearning/data/test_student_performance.csv"
column = ['name', 'gender', 'attendance_rate', 'study_hours_per_week', 'previous_grade', 'extracurricular_activities',
          'parental_support']

dataset = Charger.charge_data(url_data, column)
array = dataset.values
x = array[:, 0:-1]
y = array[:, -1]


def test_model_lr():
    lr_path = './MachineLearning/models/lr_model.pkl'
    model_lr = Model.load_model(lr_path)

    accuracy_lr = Appraiser.evaluate(model_lr, x, y)

    assert accuracy_lr >= 0.78


def test_model_knn():
    knn_path = './MachineLearning/models/knn_model.pkl'
    model_knn = Model.load_model(knn_path)

    accuracy_knn = Appraiser.evaluate(model_knn, x, y)

    assert accuracy_knn >= 0.78


def test_model_rf():
    rf_path = './MachineLearning/pipelines/rf_student_pipeline.pkl'
    model_rf = Pipeline.load_pipeline(rf_path)

    accuracy_rf = Appraiser.evaluate(model_rf, x, y)

    assert accuracy_rf >= 0.78
