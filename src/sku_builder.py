from src.models import SKURequest


def generate_sku(data: SKURequest) -> str:
    """
    Ghép các trường của SKURequest thành dạng SKU chuẩn:
    BRAND-GENDER-CAT-COL-SZ-SEA-SEQ
    Ví dụ: MNO-M-TSH-BLK-L-FW26-001
    """
    seq_str = f"{data.sequence:03d}"
    return f"{data.brand}-{data.gender}-{data.category}-{data.color}-{data.size}-{data.season}-{seq_str}"
# Cố tình viết code không an toàn
user_input = "1 + 1"
eval(user_input)
