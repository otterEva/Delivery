import logging
import structlog
from logging.config import dictConfig
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from structlog.typing import EventDict, Processor, WrappedLogger


def configure_logger(
    enable_json_logs: bool = False,
    enable_sql_logs: bool = False,
    level: int | str = logging.INFO,
) -> None:
    processors: list[Processor] = [
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.contextvars.merge_contextvars,
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
    ]

    structlog.configure(
        processors=processors
        + [structlog.stdlib.ProcessorFormatter.wrap_for_formatter],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    logs_render = cast(
        "Processor",
        (
            structlog.processors.JSONRenderer()
            if enable_json_logs
            else structlog.dev.ConsoleRenderer(
                colors=True, exception_formatter=structlog.dev.ConsoleRenderer()
            )
        ),
    )

    configure_default_logging_by_structlog(logs_render, level, enable_sql_logs)


def _remove_color_message(
    _: "WrappedLogger", __: str, event_dict: "EventDict"
) -> "EventDict":
    if "color_message" in event_dict:
        del event_dict["color_message"]
    return event_dict


def configure_default_logging_by_structlog(
    logs_render: "Processor", level: int | str, enable_sql_logs: bool
) -> None:
    pre_chain: list[Processor] = [
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.contextvars.merge_contextvars,
        structlog.processors.format_exc_info,
        structlog.stdlib.ExtraAdder(),
    ]

    processor = [
        structlog.stdlib.ProcessorFormatter.remove_processors_meta,
        _remove_color_message,
        logs_render,
    ]

    base_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processors": processor,
                "foreign_pre_chain": pre_chain,
            }
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "null": {
                "class": "logging.NullHandler",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": level,
        },
        "loggers": {
            **(
                {"sqlalchemy.engine.Engine": {"level": logging.INFO}}
                if enable_sql_logs
                else {}
            )
        },
    }
    dictConfig(base_config)
