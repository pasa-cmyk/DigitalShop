from collections.abc import Sequence
from decimal import Decimal
from typing import ClassVar, override

from app.domain.common.exchange_rate import (
    CurrencyPair,
    ExchangeRate,
    ExchangeRateGateway,
    ExchangeRateNotFoundError,
)
from app.domain.common.money import Currency
from app.domain.common.port import Clock


class StaticExchangeRateGateway(ExchangeRateGateway):
    BASE_RATES: ClassVar[dict[Currency, Decimal]] = {
        Currency.USD: Decimal(1),
        Currency.RUB: Decimal(80),
        Currency.UAH: Decimal(41),
        Currency.KZT: Decimal(540),
    }

    def __init__(self, clock: Clock):
        self._clock = clock

    @override
    async def get(self, pair: CurrencyPair) -> ExchangeRate:
        rates = await self.get_many(pairs=[pair])
        return rates[0]

    @override
    async def get_many(
        self,
        pairs: Sequence[CurrencyPair],
    ) -> tuple[ExchangeRate, ...]:
        now = self._clock.now()
        return tuple(self._build_rate(pair=pair, timestamp=now) for pair in pairs)

    def _build_rate(self, pair: CurrencyPair, timestamp) -> ExchangeRate:
        source_rate = self.BASE_RATES.get(pair.source)
        target_rate = self.BASE_RATES.get(pair.target)
        if source_rate is None or target_rate is None:
            raise ExchangeRateNotFoundError

        return ExchangeRate(
            pair=pair,
            rate=target_rate / source_rate,
            timestamp=timestamp,
        )
