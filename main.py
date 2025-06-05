
import uvicorn
from app import app
from config import (
    DEBUG,
    UVICORN_HOST,
    UVICORN_PORT,
    UVICORN_UDS,
    UVICORN_SSL_CERTFILE,
    UVICORN_SSL_KEYFILE,
    MOREBOT_SECRET,
    MOREBOT_LICENSE,
)
import logging

if __name__ == "__main__":
    # Do NOT change workers count for now
    # multi-workers support isn't implemented yet for APScheduler and XRay module
    try:
        if not all([MOREBOT_SECRET, MOREBOT_LICENSE]):
            raise RuntimeError("MOREBOT_SECRET/MOREBOT_LICENSE is not configured")
        uvicorn.run(
            "main:app",
            host=('0.0.0.0' if DEBUG else UVICORN_HOST),
            port=UVICORN_PORT,
            uds=(None if DEBUG else UVICORN_UDS),
            ssl_certfile=UVICORN_SSL_CERTFILE,
            ssl_keyfile=UVICORN_SSL_KEYFILE,
            workers=1,
            reload=DEBUG,
            log_level=logging.DEBUG if DEBUG else logging.INFO
        )
    except FileNotFoundError:  # to prevent error on removing unix sock
        pass
