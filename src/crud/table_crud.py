from abc import ABC
from collections import defaultdict
from typing import Optional, Type, TypeVar

from loguru import logger
from tortoise.models import Model

from src.models import SwordTierList, VanillaTierList, NetheriteTierList, User
from src.schemas import TierPlayer, TiersResponse, TierGroup

T = TypeVar('T', bound=Model)


class TierManagementService(ABC):
    @classmethod
    async def add_user_tier(cls, model: Type[T], user_id: int, tier: str) -> bool:
        try:
            user = await User.get(id=user_id)
            await model.create(tier=tier, user=user)
            logger.debug(f"Successfully added tier '{tier}' for user ID {user_id}.")
            return True
        except Exception as error:
            logger.error(f"Failed to add tier '{tier}' for user ID {user_id}: {error}")
            return False

    @classmethod
    async def fetch_all_tiers(cls, model: Type[T]) -> Optional[TiersResponse]:
        try:
            records = await model.all().prefetch_related("user")

            grouped_data = defaultdict(lambda: {"high": [], "low": []})

            for record in records:
                status = "low" if record.tier.startswith("lt") else "high"
                tier = int(record.tier[-1])
                grouped_data[tier][status].append({
                    "nickname": record.user.nickname,
                    "region": record.user.region
                })

            tiers = {
                tier: TierGroup(
                    high=[TierPlayer(**player) for player in group["high"]],
                    low=[TierPlayer(**player) for player in group["low"]]
                )
                for tier, group in grouped_data.items()
            }

            logger.debug("Successfully grouped and transformed tiers.")
            return TiersResponse(tiers=tiers)

        except Exception as error:
            logger.error(f"Failed to retrieve or transform tiers: {error}")
            return None


class SwordTierService:
    @classmethod
    async def add_tier(cls, user_id: int, tier: str) -> bool:
        return await TierManagementService.add_user_tier(SwordTierList, user_id, tier)

    @classmethod
    async def get_tiers(cls) -> Optional[TiersResponse]:
        return await TierManagementService.fetch_all_tiers(SwordTierList)


class VanillaTierService:
    @classmethod
    async def add_tier(cls, user_id: int, tier: str) -> bool:
        return await TierManagementService.add_user_tier(VanillaTierList, user_id, tier)

    @classmethod
    async def get_tiers(cls) -> Optional[TiersResponse]:
        return await TierManagementService.fetch_all_tiers(VanillaTierList)


class NetheriteTierService:
    @classmethod
    async def add_tier(cls, user_id: int, tier: str) -> bool:
        return await TierManagementService.add_user_tier(NetheriteTierList, user_id, tier)

    @classmethod
    async def get_tiers(cls) -> Optional[TiersResponse]:
        return await TierManagementService.fetch_all_tiers(NetheriteTierList)
