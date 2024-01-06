from typing import List

import requests


def categories_list(is_list: bool = False) -> List[dict] | iter:
    url_name = "http://127.0.0.1:8000/api/v1/categories/"
    response = requests.get(url_name)
    result = []
    if response.status_code == 200:
        for line in response.json():
            result.append(line.get("name", "not found").strip())
        if is_list:
            return result
        else:
            return iter(result)
    else:
        raise requests.exceptions.ConnectionError()


def products_list():
    url_name = "http://127.0.0.1:8000/api/v1/products/"
    response = requests.get(url_name)
    result = []
    if response.status_code == 200:
        for line in response.json():
            result.append(
                {
                    "name": line.get("name").strip(),
                    "category": line.get("category").get("name").strip(),
                    "description": "Описание не заданно"
                    if line.get("description") == ""
                    else line.get("description").strip(),
                    "sell_price": f'Цена {float(line.get("sell_price"))}'
                    if float(line.get("sell_price")) == 0
                    else f'Цена со скидкой {float(line.get("sell_price"))}',
                    "quantity": float(line.get("quantity")),
                }
            )
        return result
