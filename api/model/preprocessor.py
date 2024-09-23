from sklearn.model_selection import train_test_split
import pickle
import numpy as np


class PreProcessor:

    def separate_test_training(self, dataset, test_percentual, seed: 7):
        X_train, X_test, Y_train, Y_test = self.__prepare_holdout(dataset, test_percentual, seed)
        return (X_train, X_test, Y_train, Y_test)

    def __prepare_holdout(self, dataset, test_percentual, seed):
        data = dataset.values
        X = data[:, 0:5]
        Y = data[:, 5]
        return train_test_split(X, Y, test_size=test_percentual, random_state=seed)

    def prepare_form(form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        X_input = np.array([
            form.gender,
            form.attendance_rate,
            form.study_hours_per_week,
            form.previous_grade,
            form.extracurricular_activities,
            form.parental_support
        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        return X_input

    @staticmethod
    def scaler(X_train):
        """ Normaliza os dados. """
        # normalização/padronização
        scaler = pickle.load(open('./MachineLearning/pipelines/best_student_performance_model.pkl', 'rb'))
        reescaled_X_train = scaler.transform(X_train)
        return reescaled_X_train
