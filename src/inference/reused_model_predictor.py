"""A Predictor module to load model and get prediction reused model.

"""
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer
from src.inference.predictor import Predictor
from src.utility.utils import config
from src.utility import constants


class ReusedModelPredictor(Predictor):
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
            self.model = LsaSummarizer()
        return self.model

    def get_model_output(self, input_data):
        """A method to get model output from given text input
        Args:
            input_data (text):input text data

        Returns:
            output: model prediction
        """

        model = self.get_model()
        parser = PlaintextParser.from_string(
            input_data, Tokenizer(str(config.get(constants.LANGUAGE)))
        )
        model_summary = model(
            parser.document, int(config.get(constants.NUM_SENTENCES))
        )
        summary_output = ""
        for sentence in model_summary:
            summary_output += str(sentence)
        return summary_output
