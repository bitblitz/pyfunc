import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    valstr = req.params.get('val')
    if valstr:
        values = valstr.split(',')
        product = 1
        for v in values:
            product = product * int(v)

        return func.HttpResponse(f"result {product}!")
    else:
        return func.HttpResponse(
             "Please pass values on the query string.",
             status_code=400
        )
