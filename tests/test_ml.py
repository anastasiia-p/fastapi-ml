import pytest

from ml.model import SentimentPrediction, load_model


@pytest.fixture(scope="function")
def model():
    # Load the model once for each test function
    return load_model()


@pytest.mark.parametrize(
    "text, expected_label",
    [
        ("очень плохо", "negative"),
        ("очень хорошо", "positive"),
        ("по-разному", "neutral"),
    ],
)
def test_sentiment(model, text: str, expected_label: str):
    model_pred = model(text)
    assert isinstance(model_pred, SentimentPrediction)
    assert model_pred.label == expected_label
