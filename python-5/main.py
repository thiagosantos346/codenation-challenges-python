import time

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def getDefaultTimeFormat():
    return "%a, %d %b %Y %H:%M:%S"


def epochToHumanDate(epocTime: int, timeFormat: str) -> str:

    humanDate = time.strftime(
        timeFormat,
        time.localtime(epocTime)
    )

    return humanDate


def getPeriodTime(
    epochToHumanDate: object,
    epocTime: str,
    firstPeriod: list,
) -> int:

    hour = int(epochToHumanDate(epocTime, '%H'))
    if hour >= firstPeriod[0] and hour < firstPeriod[1]:
        # Diurno
        return 0
    # Noturno
    return 1


def getDeltaTimeSeconds(start: int, end: int):
    return end - start


def feeConnecion(balance: float):
    return balance + 0.36


def feeOnDay(deltaTime: int) -> float:
    return (int(deltaTime/60) * 0.09)


def feeOnNigth(deltaTime: int) -> float:
    return (int(deltaTime/60) * 0)


def aplayFee(
    feeFuncion: object,
    deltaTime: int,
    balance: float
) -> float:

    return feeFuncion(deltaTime) + balance


def createBalance():
    return 0


def getTotalBalance(start: int, end: int) -> float:
    balance = createBalance()
    balance = feeConnecion(balance)

    period = getPeriodTime(
        epochToHumanDate,
        start,
        [6, 22]
    )

    deltaTime = getDeltaTimeSeconds(start, end)

    if period == 0:
        balance = aplayFee(feeOnDay, deltaTime, balance)
    elif period == 1:
        balance = aplayFee(feeOnNigth, deltaTime, balance)

    return balance


def group_by_phone_number(records: list) -> list:

    set_numbers = set()
    locaL_records = records

    for record in records:
        set_numbers.add(record['source'])

    balance_by_number = list()

    for number in set_numbers:
        parcial_balance = 0
        for record in locaL_records:
            if record['source'] == number:
                parcial_balance += record['total']

        balance_by_number.append({
            'source': number,
            'total': round(parcial_balance, 2)
        })

    return balance_by_number


def dict_list_order_by(key_order: str, values: list) -> list:

    def sortFuncion(dict: str) -> list:
        return dict[key_order]

    values.sort(key=sortFuncion, reverse=True)

    return values


def classify_by_phone_number(records: list) -> list:
    numbers_classifieds = list()

    for record in records:
        source = record['source']
        start = int(record['start'])
        end = int(record['end'])
        balance = getTotalBalance(start, end)
        number_classified = dict({
            'source': source, 'total': round(balance, 2)
        })
        numbers_classifieds.append(number_classified)

    numbers_classifieds = group_by_phone_number(numbers_classifieds)
    numbers_classifieds = dict_list_order_by('total', numbers_classifieds)

    return numbers_classifieds


def main():
    numbers = classify_by_phone_number(records)
    print(numbers)


if __name__ == "__main__":
    main()
