"""A factory module to get predictor class based on type"""
from src.inference.custom_model_predictor import (
    CustomModelPredictor,
)

from src.inference.reused_model_predictor import (
    ReusedModelPredictor,
)


def get_predictor(model_type):
    """A method to retun Predictor class object

    Args:
        model_type (str): Model type

    Returns:
        Predictor: A predictor class
    """

    if model_type == "Custom Model":
        return CustomModelPredictor()

    return ReusedModelPredictor()
