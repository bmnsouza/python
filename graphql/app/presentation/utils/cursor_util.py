import base64
import logging

from app.core.exceptions import CustomException

logger = logging.getLogger(__name__)


class Cursor:

    @staticmethod
    def encode(rn: int) -> str:
        return base64.b64encode(str(rn).encode()).decode()

    @staticmethod
    def decode(after: str) -> int:
        try:
            if not after:
                return 0

            return int(base64.b64decode(after).decode())
        except Exception as e:
            logger.exception("Erro ao decodificar cursor: %s", e)
            raise CustomException("Cursor inválido")
