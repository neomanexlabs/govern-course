# Errors and logging

- Log at INFO for business events: invoice sent, payment recorded.
- Log at WARNING for anything a shop owner might notice.
- Log at ERROR only for things someone must fix.
- Never log amounts together with customer names.
- Include the invoice id in every invoice log line.
