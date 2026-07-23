import pytest
from pydantic import ValidationError
from typing import Any, cast
from src.models import SKURequest
from src.sku_builder import generate_sku


def test_generate_sku_valid():
    request_data = SKURequest(
        brand="MNO",
        gender="M",
        category="TSH",
        color="BLK",
        size="L",
        season="FW26",
        sequence=1,
    )
    assert generate_sku(request_data) == "MNO-M-TSH-BLK-L-FW26-001"


def test_generate_sku_auto_uppercase_and_padding():
    request_data = SKURequest(
        brand="abc",
        gender="W",
        category="pant",  # 4 letters should fail validation
    ) if False else SKURequest(
        brand="abc",
        gender="W",
        category="pnt",
        color="red",
        size="S",
        season="ss26",
        sequence=42,
    )
    assert generate_sku(request_data) == "ABC-W-PNT-RED-S-SS26-042"


def test_invalid_brand_length():
    with pytest.raises(ValidationError):
        SKURequest(
            brand="ABCD",  # 4 letters
            gender="M",
            category="TSH",
            color="BLK",
            size="L",
            season="FW26",
            sequence=1,
        )


def test_invalid_gender():
    with pytest.raises(ValidationError):
        SKURequest(
            brand="ABC",
            gender=cast(Any, "X"),  # Invalid gender
            category="TSH",
            color="BLK",
            size="L",
            season="FW26",
            sequence=1,
        )


def test_invalid_sequence():
    with pytest.raises(ValidationError):
        SKURequest(
            brand="ABC",
            gender="M",
            category="TSH",
            color="BLK",
            size="L",
            season="FW26",
            sequence=1000,  # > 999
        )
