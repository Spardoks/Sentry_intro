import sentry_sdk

sentry_sdk.init(
    dsn="https://****",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

sentry_sdk.capture_message("This is a custom message with alert", level="info")