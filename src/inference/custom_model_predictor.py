"""A Predictor module to load model and get prediction from custom  model.

"""

import pytextrank
import spacy


from src.inference.predictor import Predictor


class CustomModelPredictor(Predictor):
    """A child class to load model and get output

    Args:
        Predictor (Predictor): Parent class

    """

    model = None

    def get_model(self):
        """A method to load model

        Returns:
            model: trained model
        """

        if self.model is None:
            self.model = spacy.load("en_core_web_sm")
            self.model.add_pipe("textrank")
        return self.model

    def get_model_output(self, input_data):
        """A method to get model output from given text input
        Args:
            input_data (text):input text data

        Returns:
            output: model prediction
        """

        model = self.get_model()
        doc = model(input_data)
        text_ranker = doc._.textrank
        model_summary = text_ranker.summary(limit_phrases=15, limit_sentences=5)
        summary_output = ""
        for sentence in model_summary:
            summary_output += str(sentence)
        return summary_output
