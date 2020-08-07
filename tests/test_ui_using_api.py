import requests
import pytest
from pylenium import Pylenium


def get_deal_by_id(deal_id: int) -> dict:
    response = requests.get(f'https://jane.com/proxy/catalog/storefront/{str(deal_id)}')
    if response.ok:
        return response.json()
    raise ConnectionError("Response was not ok", response.content)


def test_get_deal_by_id():
    """ Positive Test to check my function. """
    assert get_deal_by_id(1093193) is not None


def test_get_deal_with_invalid_id_raised_error():
    """ Negative Test to check that my function raises the error as expected. """
    with pytest.raises(ConnectionError):
        get_deal_by_id(0)


@pytest.mark.parameterize("deal_id", [1093715, 1093193])
def test_deal_in_the_UI_matches_deal_from_BE(py, deal_id):
    deal = get_deal_by_id(deal_id)
    deal_price = str(deal['price'])  # => '19.99'

    py.visit(f'https://jane.com/deal/{deal_id}')
    assert deal_price in py.get('[data-testid="dd-price"]').text()


def test_get_deal_ids():
    ENDPOINT = 'https://jane.com/proxy/catalog/storefront/deal-list-ids'
    body = {
        "dealStatus": [
            "Live"
        ],
        "feedCode": "tops-her",
        "isNewVisitor": False,
        "preHydrateCount": 40,
        "dealFields": [
            "averageShipTime",
            "campaigns",
            "discount",
            "isDeliveredElectronically",
            "isSoldOut",
            "likeCount",
            "mainImageUrl",
            "mainThumbnailUrl",
            "optionsLabel",
            "price",
            "productId",
            "relativeUrl",
            "retail",
            "segmentingAttributes",
            "sellerName",
            "shippingFirstItem",
            "shortUrl",
            "soldQuantity",
            "startDate",
            "storefrontDealType",
            "title"
        ]
    }
    response = requests.post(ENDPOINT, json=body)
    _json = response.json()

    deal_ids = _json['dealIds']
    total_count = _json['totalCount']
    assert len(deal_ids) == total_count
