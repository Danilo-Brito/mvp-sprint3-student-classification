import pickle


class Pipeline:

    @staticmethod
    def load_pipeline(path):
        """Carregamos o pipeline construindo durante a fase de treinamento
        """
        try:
            with open(path, 'rb') as file:
                pipeline = pickle.load(file)
            return pipeline
        except FileNotFoundError:
            print(f"Error: File not found at {path}")
        except pickle.UnpicklingError:
            print("Error: The file could not be unpickled. It may be corrupted.")
        except Exception as e:
            print(f"An error occurred: {e}")