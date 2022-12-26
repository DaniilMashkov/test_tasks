import re


class Operation:

    def __init__(self, pattern: dict) -> None:
        self._date = pattern.get('date')[:10].replace('-', '.')
        self._description = pattern.get('description')
        self._amount = pattern['operationAmount']['amount']
        self._currency = pattern['operationAmount']['currency']['name']
        self._from = self.parse_account(pattern.get('from')) if pattern.get('from') else ''
        self._to = self.parse_account(pattern.get('to')) if pattern.get('to') else ''

    def __str__(self) -> str:
        return f'{self._date} {self._description}\n{self._from} -> {self._to}\n{self._amount} {self._currency}\n'

    def __eq__(self, other) -> bool:
        return self._date == other

    def __lt__(self, other) -> bool:
        return self._date < other

    def __gt__(self, other) -> bool:
        return self._date > other

    @staticmethod
    def parse_account(account) -> str:
        if 'Счет' in account:
            return re.sub(r'(\d{16})(\d{4})', r'**\2', account)
        return re.sub(r"(\d{4})(\d{2})(\d{6})(\d{4})", r"\1 \2** **** \4", account)


class CollectInstances:

    def __init__(self, data) -> None:
        self.data = data
        self.lst = []
        self._collect()

    def _collect(self) -> list[Operation]:
        for item in self.data:
            instance = Operation(item)
            self.lst.append(instance)
        return self.lst

    def sort_data(self) -> None:
        self.lst.sort(reverse=True)
