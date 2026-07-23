from typing import Literal
from pydantic import BaseModel, Field, field_validator


class SKURequest(BaseModel):
    brand: str = Field(
        ...,
        min_length=3,
        max_length=3,
        pattern=r"^[A-Z]{3}$",
        description="Brand code (3 uppercase letters, e.g. MNO)"
    )
    gender: Literal["M", "W", "U", "K"] = Field(
        ...,
        description="Gender code (M: Men, W: Women, U: Unisex, K: Kids)"
    )
    category: str = Field(
        ...,
        min_length=3,
        max_length=3,
        pattern=r"^[A-Z]{3}$",
        description="Category code (3 uppercase letters, e.g. TSH)"
    )
    color: str = Field(
        ...,
        min_length=3,
        max_length=3,
        pattern=r"^[A-Z]{3}$",
        description="Color code (3 uppercase letters, e.g. BLK)"
    )
    size: Literal["XS", "S", "M", "L", "XL", "XXL"] = Field(
        ...,
        description="Size code (XS, S, M, L, XL, XXL)"
    )
    season: str = Field(
        ...,
        pattern=r"^(FW|SS)\d{2}$",
        description="Season code (e.g. FW26, SS26)"
    )
    sequence: int = Field(
        ...,
        ge=1,
        le=999,
        description="Sequence number (1-999)"
    )

    @field_validator("brand", "category", "color", "gender", "size", "season", mode="before")
    @classmethod
    def convert_to_uppercase(cls, v: str) -> str:
        if isinstance(v, str):
            return v.upper()
        return v