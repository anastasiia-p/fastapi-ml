import pytest
import requests


@pytest.mark.parametrize(
    "input_text, expected_label",
    [
        ("очень плохо", "negative"),
        ("очень хорошо", "positive"),
        ("по-разному", "neutral"),
    ],
)
def test_sentiment(input_text: str, expected_label: str):
    response = requests.get("http://0.0.0.0/predict/", params={"text": input_text})
    assert response.json()["text"] == input_text
    assert response.json()["sentiment_label"] == expected_label
